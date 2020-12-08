from dllist import __version__
from dllist.double_linked_list import DoubleLinkedList
from dllist.double_linked_list_node import DoubleLinkedListNode


def test_version():
    assert __version__ == "0.1.0"


def test_push():
    d_list = DoubleLinkedList()
    d_list._invariant()
    d_list.push("Hello")
    assert d_list.count() == 1

    d_list.push("Bonjour")
    assert d_list.count() == 2

    d_list.push("Hola")
    assert d_list.count() == 3
    d_list._invariant()
