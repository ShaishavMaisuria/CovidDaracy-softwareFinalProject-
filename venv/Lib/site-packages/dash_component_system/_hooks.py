import typing
import collections

from ._undefined import UNDEFINED


# noinspection PyClassHasNoInit, PyProtectedMember
class ComponentHooks:  # pylint: disable=no-init,too-few-public-methods
    """Hooks on a component level"""
    # noinspection PyTypeChecker
    _default_props_handlers = collections.defaultdict(
        lambda: collections.defaultdict(dict)
    )
    registry = set()

    @classmethod
    def register_default_prop(cls, namespace, typename, prop_name, default_prop):
        # type: (str, str, str, typing.Union[typing.Callable[[typing.Any], typing.Any], typing.Any]) -> None # noqa: E501
        cls._default_props_handlers[namespace][typename][prop_name] = default_prop

    @classmethod
    def get_default_prop(cls, component, prop_name):
        default_prop = cls._default_props_handlers[component._namespace][
            component._typename
        ].get(prop_name, UNDEFINED)
        if callable(default_prop):
            return default_prop(component, prop_name)
        return default_prop
