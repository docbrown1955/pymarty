from __future__ import annotations

import sys

sys.path.append("/home/gregoire/Bureau/pymarty/build/src/marty_pybinding/")
import pymartyc


class Index:
    def __init__(self, index: pymartyc.Index) -> None:
        self._index = index

    @property
    def name(self) -> str:
        return self._index.name

    @name.setter
    def name(self, name_: str) -> None:
        self._index.name = name_

    @staticmethod
    def from_marty(index: pymartyc.Index) -> Index:
        return Index(index)


def minkowski_index(name: str) -> Index:
    return Index.from_marty(pymartyc.minkowski_index(name))


index = minkowski_index("some_name")
index.name = "some_other_name"
print(index.name)
