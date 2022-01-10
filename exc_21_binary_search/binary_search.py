from typing import Any, TypeVar, List, Optional
from typing_extensions import Protocol
from abc import abstractmethod

from exc_13_double_linked_list.double_linked_list.dl_list import DoubleLinkedList
from exc_13_double_linked_list.double_linked_list.dl_node import DoubleLinkedListNode

T = TypeVar("T", "Comparable", int)


class Comparable(Protocol):
    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        pass

    @abstractmethod
    def __lt__(self: T, other: T) -> bool:
        pass

    def __gt__(self: T, other: T) -> bool:
        return (not self < other) and self != other

    def __le__(self: T, other: T) -> bool:
        return self < other or self == other

    def __ge__(self: T, other: T) -> bool:
        return not self < other


def binary_search(sorted_list: List[T], target: T) -> Optional[int]:
    m = len(sorted_list) // 2
    r = len(sorted_list) - 1
    l = 0

    while l <= r:
        if target > sorted_list[m]:
            l = m + 1
            m = (r + l) // 2
        elif target < sorted_list[m]:
            r = m - 1
            m = (r - l) // 2
        else:
            return m

    return None


def binary_search_on_list(sorted_list: DoubleLinkedList, target: int) -> Optional[int]:
    m = sorted_list.count() // 2
    r = sorted_list.count() - 1
    l = 0

    while l <= r:
        if target > sorted_list.get(m):
            l = m + 1
            m = (r + l) // 2
        elif target < sorted_list.get(m):
            r = m - 1
            m = (r - l) // 2
        else:
            return m
    return None
