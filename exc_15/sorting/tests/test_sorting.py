import pytest 
from random import randint

from exc_15.sorting.sorting import bubble_sort, merge_sort, partition, quick_sort
from exc_13.dllist.dllist.double_linked_list import DoubleLinkedList

MAX_NUMBERS = 30


def random_list(count):
    numbers = DoubleLinkedList()
    for i in range(count, 0, -1):
        numbers.shift(randint(0, 10000))

    return numbers

@pytest.fixture
def simple_list():
    numbers = DoubleLinkedList()
    values = [4,5,3,1,2 ] 
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

def test_partition(simple_list):
    partitioned_node = partition(simple_list.begin)
    
    # [4, 5, 2, 1, 3]
    # [2, 5, 4, 1, 3]
    # [2, 1, 3, 5, 4]
    
    assert partitioned_node.value == 3
    print(partitioned_node, "\n\n\n")

def test_quick_sort(simple_list):
    quick_sort(simple_list.begin)
    print(simple_list)
    
     
