import pytest
from random import randint

from exc_15_sorting_algos.sorting.sorting import (
    bubble_sort,
    merge_sort,
    partition,
    quick_sort_node,
    quick_sort,
)
from exc_13_double_linked_list.double_linked_list.dl_list import DoubleLinkedList

MAX_NUMBERS = 30


def random_list(count):
    numbers = DoubleLinkedList()
    for i in range(count, 0, -1):
        numbers.shift(randint(0, 10000))

    return numbers


@pytest.fixture(params=[[1, 1, 2, 3, 7, 1, 18], [1], [2, 1], [1, 2, 1]])
def simple_list(request):
    numbers = DoubleLinkedList()
    values = request.param

    for num in values:
        numbers.push(num)
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


@pytest.mark.parametrize(
    "simple_list",
    [
        [1, 1, 2, 3, 7, 1, 18],
    ],
    indirect=True,
)
def test_partition(simple_list):
    partitioned_node = partition(simple_list.begin, simple_list.end)

    # [4, 5, 2, 1, 3]
    # [2, 5, 4, 1, 3]
    # [2, 1, 3, 5, 4]

    assert partitioned_node.value == 3


def test_quick_sort_node(simple_list):
    quick_sort_node(simple_list.begin, simple_list.end)
    assert is_sorted(simple_list)


def test_quick_sort_node_serious():
    numbers = random_list(MAX_NUMBERS)
    quick_sort_node(numbers.begin, numbers.end)
    assert is_sorted(numbers)


def test_quick_sort():
    numbers = random_list(MAX_NUMBERS)
    quick_sort(numbers)
    assert is_sorted(numbers)
