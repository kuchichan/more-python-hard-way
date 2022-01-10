from ..binary_search import binary_search, binary_search_on_list
from exc_13_double_linked_list.double_linked_list.dl_list import DoubleLinkedList
from exc_13_double_linked_list.double_linked_list.dl_node import DoubleLinkedListNode


def test_binary_search():
    list_ = [i for i in range(10)]

    assert binary_search(list_, 7) == list_.index(7)
    assert binary_search(list_, 3) == list_.index(3)
    assert binary_search(list_, 9) == list_.index(9)
    assert binary_search(list_, 0) == list_.index(0)
    assert binary_search(list_, 11) == None


def test_binary_search_duplicate_elements():
    list_ = [1, 1, 2, 2, 3, 3, 5, 5, 5, 10, 20, 21]

    assert binary_search(list_, 5) == list_.index(5)
    assert binary_search(list_, 1) == list_.index(1)
    assert binary_search(list_, 10) == list_.index(10)
    assert binary_search(list_, 21) == list_.index(21)
    assert binary_search(list_, 0) == None


def test_binary_seach_double_linked_list():
    d_list = DoubleLinkedList()
    d_list.push(1)
    d_list.push(2)
    d_list.push(3)
    d_list.push(4)
    d_list.push(5)

    assert binary_search_on_list(d_list, 3) == 2
    assert binary_search_on_list(d_list, 1) == 0
    assert binary_search_on_list(d_list, 5) == 4
