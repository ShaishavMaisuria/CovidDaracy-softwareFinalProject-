import collections

import six


if six.PY2:
    MutableSet = getattr(collections, 'MutableSet')
else:
    MutableSet = collections.abc.MutableSet


class OrderedSet(MutableSet):
    """
    Slow set to keep the order of unique elements in a list.
    """
    def __init__(self, *args):
        self._data = []
        for i in args:
            self.add(i)

    def add(self, x):
        if x not in self._data:
            self._data.append(x)

    def discard(self, x):
        self._data.remove(x)

    def __contains__(self, x):
        return x in self._data

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        for i in self._data:
            yield i
