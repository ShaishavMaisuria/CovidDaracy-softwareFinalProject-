#!C:\Users\maisu\PycharmProjects\Test\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'dash-component-system==0.0.1rc1','console_scripts','build-dash-components'
__requires__ = 'dash-component-system==0.0.1rc1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('dash-component-system==0.0.1rc1', 'console_scripts', 'build-dash-components')()
    )
