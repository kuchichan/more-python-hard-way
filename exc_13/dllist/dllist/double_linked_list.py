from dataclasses import dataclass
from .double_linked_list_node import DoubleLinkedListNode
from typing import Optional


@dataclass
class DoubleLinkedList:
    begin: Optional[DoubleLinkedListNode] = None
    end: Optional[DoubleLinkedListNode] = None

    def push(self, obj: str) -> None:
        node = DoubleLinkedListNode(obj)
        if self.end is None:
            self.end = node
            self.begin = self.end
        else:
            self.end.next_ = node
            node.prev_ = self.end
            self.end = node

    def shift(self, obj: str) -> None:
        node = DoubleLinkedListNode(obj)
        if self.begin is None:
            self.begin = node
            self.end = self.begin
        else:
            self.begin.prev_ = node
            node.next_ = self.begin
            self.begin = node

    def pop(self) -> str:
        if self.end is None:
            return
        value = self.end.value
        self.detach(self.end)
        return value

    def unshift(self) -> str:
        if self.begin is None:
            return
        value = self.begin.value
        self.detach(self.begin)
        return value

    def remove(self, obj: str):
        node = self.begin
        while node is not None:
            if node.value == obj:
                self.detach(node)
                return
            node = node.next_

    def get(self, index: int) -> str:
        counter = 0
        node = self.begin
        while counter < index and node is not None:
            counter += 1
            node = node.next_

        return node.value if node is not None else None

    def first(self) -> str:
        return self.begin.value

    def last(self):
        return self.end.value

    def dump(self, text):
        print(text, "\n")
        node = self.begin
        while node is not None:
            print(node.value)
            node = node.next_
    
    def count(self) -> int:
        counter = 0
        node = self.begin
        while node is not None:
            node = node.next_
            counter += 1
        return counter

    def _invariant(self) -> None:
        if self.begin is None:
            assert self.end is None, "Self end is not None"
        else:
            self.begin.prev_ is None, "begin previous element is not None"
            self.end.next_ is None, "end next element is not None"

    def detach(self, node: DoubleLinkedListNode) -> None:
        if node.next_ is None and node.prev_ is None:
            self.begin = None
            self.end = None
        elif node.prev_ is None:
            node.next_.prev_ = node.prev_
            self.begin = node.next_
        elif node.next_ is None:
            node.prev_.next_ = None
            self.end = node.prev_
        else:
            node.next_.prev_ = node.prev_
            node.prev_.next_ = node.next_

    
