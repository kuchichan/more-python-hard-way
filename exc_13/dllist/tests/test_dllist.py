import pytest

from dllist import __version__
from dllist.double_linked_list import DoubleLinkedList
from dllist.double_linked_list_node import DoubleLinkedListNode


@pytest.fixture
def stuffed_dlist():
    d_list = DoubleLinkedList()
    d_list.push("Hello")
    d_list.push("Bonjour")
    d_list.push("Holla")
    return d_list


def test_version():
    assert __version__ == "0.1.0"


def test_push():
    d_list = DoubleLinkedList()
    d_list._invariant()
    d_list.push("Hello")
    assert d_list.count() == 1
    d_list._invariant()
    d_list.push("Bonjour")
    assert d_list.count() == 2

    d_list.push("Hola")
    assert d_list.count() == 3
    d_list._invariant()


def test_detach_middle_node(stuffed_dlist):
    bonjour_node = stuffed_dlist.begin.next_

    stuffed_dlist.detach(bonjour_node)
    stuffed_dlist._invariant()

    assert stuffed_dlist.count() == 2

    node = stuffed_dlist.begin
    while node is not None:
        assert node is not bonjour_node
        node = node.next_

    stuffed_dlist._invariant()


def test_detach_first_node(stuffed_dlist):
    bonjour_node = stuffed_dlist.begin

    stuffed_dlist.detach(bonjour_node)
    stuffed_dlist._invariant()

    assert stuffed_dlist.count() == 2

    node = stuffed_dlist.begin
    while node is not None:
        assert node is not bonjour_node
        node = node.next_

    stuffed_dlist._invariant()


def test_detach_last_node(stuffed_dlist):
    bonjour_node = stuffed_dlist.end

    stuffed_dlist.detach(bonjour_node)
    stuffed_dlist._invariant()

    assert stuffed_dlist.count() == 2

    node = stuffed_dlist.begin
    while node is not None:
        assert node is not bonjour_node
        node = node.next_

    stuffed_dlist._invariant()


def test_detach_one_element_list():
    list_ = DoubleLinkedList()
    list_.push("Hello")

    list_._invariant()

    node = list_.begin
    list_.detach(node)

    assert list_.count() == 0
    list_._invariant()


def test_shift(stuffed_dlist):
    stuffed_dlist.shift("Czesc")

    assert stuffed_dlist.begin.value == "Czesc"
    assert stuffed_dlist.count() == 4
    stuffed_dlist._invariant()


def test_shift_empty_list():
    list_ = DoubleLinkedList()
    list_.shift("Hello")

    assert list_.count() == 1
    assert list_.begin == list_.end
    assert list_.begin.value == "Hello"


def test_pop_on_empty_list():
    list_ = DoubleLinkedList()
    assert list_.pop() is None


def test_pop(stuffed_dlist):
    value = stuffed_dlist.pop()
    assert value == "Holla"
    assert stuffed_dlist.count() == 2


def test_unshift_on_empty_list():
    list_ = DoubleLinkedList()
    assert list_.unshift() is None


def test_unshift(stuffed_dlist):
    value = stuffed_dlist.unshift()
    assert value == "Hello"
    assert stuffed_dlist.count() == 2


def test_remove_on_empty_list():
    list_ = DoubleLinkedList()
    list_.remove("heheh")

    assert list_.begin is None
    assert list_.end is None


def test_remove_element_that_does_not_exist(stuffed_dlist):
    stuffed_dlist.remove("Do widzenia")

    assert stuffed_dlist.count() == 3


def test_remove_element(stuffed_dlist):
    stuffed_dlist.remove("Holla")

    assert stuffed_dlist.count() == 2
    stuffed_dlist._invariant()

    node = stuffed_dlist.begin

    while node is not None:
        assert node.value != "Holla"
        node = node.next_


def test_remove_element_from_empty_list():
    list_ = DoubleLinkedList()
    list_.remove("hi")

    assert list_.begin == list_.end
    assert list_.begin is None


def test_get_element_for_too_much_index():
    list_ = DoubleLinkedList()
    assert list_.get(10) is None


def test_get_element(stuffed_dlist):
    assert stuffed_dlist.get(0) == "Hello"
    assert stuffed_dlist.get(1) == "Bonjour"
    assert stuffed_dlist.get(2) == "Holla"


def test_first(stuffed_dlist):
    assert stuffed_dlist.first() == "Hello"


def test_last(stuffed_dlist):
    assert stuffed_dlist.last() == "Holla"


def test_dump(capsys, stuffed_dlist):
    stuffed_dlist.dump("No co tam")
    captured = capsys.readouterr()
    assert "Holla" in captured.out
    assert "Bonjour" in captured.out
    assert "Hello" in captured.out
    assert "No co tam" in captured.out
