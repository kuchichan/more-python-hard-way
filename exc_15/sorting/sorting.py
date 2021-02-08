from exc_13.dllist.dllist.double_linked_list import DoubleLinkedList
from exc_13.dllist.dllist.double_linked_list_node import DoubleLinkedListNode


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
    merged_rigt = merge_node(mid_node)

    return merge(merged_left, merged_rigt)


def merge_sort(numbers: DoubleLinkedList) -> None:
    numbers.begin = merge_node(numbers.begin)

    node = numbers.begin
    while node.next_ is not None:
        node = node.next_

    numbers.end = node 
