from __future__ import print_function
from collections import OrderedDict

import collections
import json
import sys
import subprocess
import shlex
import os
import argparse
import shutil
import functools
import pkg_resources

import stringcase

from ._r_components_generation import write_class_file
from ._r_components_generation import generate_exports
from ._component import generate_component


class _CombinedFormatter(argparse.ArgumentDefaultsHelpFormatter,
                         argparse.RawDescriptionHelpFormatter):
    pass


def generate_classes_files(project_shortname, metadata, *component_generators):
    components = []
    for component_path, component_data in metadata.items():
        component_name = component_path.split('/')[-1].split('.')[0]
        components.append(component_name)

        for generator in component_generators:
            generator(
                component_name,
                component_data['props'],
                component_data['description'],
                project_shortname
            )

    return components


def generate_imports(project_shortname, components):
    with open(os.path.join(project_shortname, '_imports_.py'), 'w') as f:
        imports_string = '{}\n\n{}'.format(
            '\n'.join(
                'from ._{} import {}'.format(stringcase.snakecase(x), x)
                for x in components
            ),
            '__all__ = [\n{}\n]'.format(
                ',\n'.join('    "{}"'.format(x) for x in components))
        )
        imports_string += '\n'

        f.write(imports_string)


# pylint: disable=too-many-locals
def generate_components(
        components_source, project_shortname,
        package_info_filename='package.json',
        ignore='^_',
        rprefix=None,
        clean=False,
):

    project_shortname = project_shortname.replace('-', '_').rstrip('/\\')

    if clean:
        for f in os.listdir(project_shortname):
            if f.endswith('.py') and f != '__init__.py':
                path = '{}/{}'.format(project_shortname, f)
                os.remove(path)
                print('Removed {}'.format(path))

    if rprefix:
        prefix = rprefix

    is_windows = sys.platform == 'win32'

    extract_path = pkg_resources.resource_filename(
        'dash_component_system', 'extract-meta.js'
    )

    cmd = shlex.split(
        'node {} {} {}'.format(extract_path, ignore, components_source),
        posix=not is_windows
    )

    shutil.copyfile('package.json',
                    os.path.join(project_shortname, package_info_filename))

    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=is_windows)
    out, err = proc.communicate()
    status = proc.poll()

    if err:
        print(err.decode(), file=sys.stderr)

    if not out:
        print(
            'Error generating metadata in {} (status={})'.format(
                project_shortname, status),
            file=sys.stderr)
        sys.exit(1)

    jsondata_unicode = json.loads(out.decode(), object_pairs_hook=OrderedDict)

    if sys.version_info[0] >= 3:
        metadata = jsondata_unicode
    else:
        metadata = byteify(jsondata_unicode)

    generator_methods = [generate_component]

    if rprefix:
        if not os.path.exists('man'):
            os.makedirs('man')
        if not os.path.exists('R'):
            os.makedirs('R')
        generator_methods.append(
            functools.partial(write_class_file, prefix=prefix))
    metadata = json.loads(out.decode(),
                          object_pairs_hook=collections.OrderedDict)

    components = generate_classes_files(
        project_shortname,
        metadata,
        *generator_methods
    )

    with open(os.path.join(project_shortname, 'metadata.json'), 'w') as f:
        json.dump(metadata, f, indent=2)

    generate_imports(project_shortname, components)

    if rprefix:
        with open('package.json', 'r') as f:
            jsondata_unicode = json.load(f, object_pairs_hook=OrderedDict)
            if sys.version_info[0] >= 3:
                pkg_data = jsondata_unicode
            else:
                pkg_data = byteify(jsondata_unicode)

        generate_exports(
            project_shortname, components, metadata, pkg_data, prefix
        )


def cli():
    parser = argparse.ArgumentParser(
        prog='dash-generate-components',
        formatter_class=_CombinedFormatter,
        description='Generate dash components by extracting the metadata '
        'using react-docgen. Then map the metadata to python classes.'
    )
    parser.add_argument('components_source',
                        help='React components source directory.')
    parser.add_argument(
        'project_shortname',
        help='Name of the project to export the classes files.'
    )
    parser.add_argument(
        '-p', '--package-info-filename',
        default='package.json',
        help='The filename of the copied `package.json` to `project_shortname`'
    )
    parser.add_argument(
        '-i', '--ignore',
        default='^_',
        help='Files/directories matching the pattern will be ignored'
    )
    parser.add_argument(
        '--r-prefix',
        help='Experimental: specify a prefix for DashR component names, write'
             'DashR components to R dir, create R package.'
    )
    parser.add_argument(
        '-c', '--clean',
        help='Remove all `.py` files inside `project_shortname`'
             'except `__init__.py`',
        action='store_true'
    )

    args = parser.parse_args()
    generate_components(
        args.components_source, args.project_shortname,
        package_info_filename=args.package_info_filename,
        ignore=args.ignore,
        rprefix=args.r_prefix,
        clean=args.clean
    )


# pylint: disable=undefined-variable
def byteify(input_object):
    # noinspection PyUnresolvedReferences
    if isinstance(input_object, dict):
        return OrderedDict([
            (byteify(key), byteify(value))
            for key, value in input_object.iteritems()
        ])
    elif isinstance(input_object, list):
        return [byteify(element) for element in input_object]
    elif isinstance(input_object, unicode):  # noqa:F821
        return input_object.encode('utf-8')
    return input_object


if __name__ == '__main__':
    cli()
