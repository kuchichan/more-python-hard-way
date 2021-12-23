from exc_13_double_linked_list.double_linked_list.dl_list import DoubleLinkedList 
from exc_13_double_linked_list.double_linked_list.dl_node import DoubleLinkedListNode


def bubble_sort(numbers: DoubleLinkedList):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        node = numbers.begin.next_
        while node:
            if node.prev_.value > node.value:
                node.prev_.value, node.value = node.value, node.prev_.value
                is_sorted = False
            node = node.next_


def merge(
    left: DoubleLinkedListNode, right: DoubleLinkedListNode
) -> DoubleLinkedListNode:
    result = None
    if left is None:
        return right
    if right is None:
        return left

    if left.value > right.value:
        result = right
        right.next_ = merge(left, right.next_)

    else:
        result = left
        left.next_ = merge(left.next_, right)

    result.next_.prev_ = result
    return result


def count(node: DoubleLinkedListNode) -> int:
    count = 0

    while node:
        node = node.next_
        count += 1

    return count


def merge_node(start: DoubleLinkedListNode) -> DoubleLinkedListNode:
    if start.next_ is None:
        return start

    mid = count(start) // 2

    cursor = start
    for _ in range(0, mid - 1):
        cursor = cursor.next_

    mid_node = cursor.next_
    cursor.next_ = None
    mid_node.prev_ = None

    merged_left = merge_node(start)
    merged_right = merge_node(mid_node)

    return merge(merged_left, merged_right)


def merge_sort(numbers: DoubleLinkedList) -> None:
    numbers.begin = merge_node(numbers.begin)

    node = numbers.begin
    while node.next_ is not None:
        node = node.next_

    numbers.end = node


def length(node1: DoubleLinkedListNode, node2: DoubleLinkedListNode) -> int:
    count = 1
    if node1 is node2:
        return count
    start = node1
    while start is not None:
        start = start.next_
        count += 1
        if start is node2:
            return count
    return 1


def partition(
    start: DoubleLinkedListNode, end: DoubleLinkedListNode
) -> DoubleLinkedListNode:
    mid = length(start, end) // 2
    mid_node = start
    for _ in range(mid):
        mid_node = mid_node.next_
    pivot_value = mid_node.value
    mid_node.value, end.value = end.value, mid_node.value

    node = start
    current_position = start
    for _ in range(0, length(start, end) - 1):
        if node.value < pivot_value:
            node.value, current_position.value = current_position.value, node.value
            current_position = current_position.next_
        node = node.next_

    end.value, current_position.value = current_position.value, end.value

    return current_position


def quick_sort_node(begin: DoubleLinkedListNode, end: DoubleLinkedListNode) -> None:
    if length(begin, end) <= 1:
        return
    pivot = partition(begin, end)
    if pivot.prev_:
        quick_sort_node(begin, pivot.prev_)
    if pivot.next_:
        quick_sort_node(pivot.next_, end)


def quick_sort(dlist) -> None:
    quick_sort_node(dlist.begin, dlist.end)
