from random import randint

from exc_15.sorting.sorting import bubble_sort, merge_sort
from exc_13.dllist.dllist.double_linked_list import DoubleLinkedList

MAX_NUMBERS = 30


def random_list(count):
    numbers = DoubleLinkedList()
    for i in range(count, 0, -1):
        numbers.shift(randint(0, 10000))

    return numbers


def is_sorted(numbers: DoubleLinkedList):
    node = numbers.begin
    while node and node.next_:
        if node.value > node.next_.value:
            return False
        else:
            node = node.next_
    return True


def test_bubble_sort():
    numbers = random_list(MAX_NUMBERS)

    bubble_sort(numbers)
    assert is_sorted(numbers)


def test_merge_sort():
    numbers = random_list(MAX_NUMBERS)

    merge_sort(numbers)
    assert is_sorted(numbers)
