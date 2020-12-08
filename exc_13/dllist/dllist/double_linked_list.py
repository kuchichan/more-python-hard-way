from dataclasses import dataclass
from .double_linked_list_node import DoubleLinkedListNode
from typing import Optional


@dataclass
class DoubleLinkedList:
    begin: Optional[DoubleLinkedListNode] = None
    end: Optional[DoubleLinkedListNode] = None

    def push(self, obj: str) -> None:
        node = DoubleLinkedListNode(obj)
        if self.begin is None:
            self.begin = node
            self.end = self.begin
        else:
            self.end.next_ = node
            node.prev = self.end
            self.end = node

    def count(self) -> int:
        counter = 0

        if self.begin is None:
            return counter
        node = self.begin

        while node != None:
            node = node.next_
            counter += 1

        return counter

    def _invariant(self):
        if self.count() == 0:
            assert self.begin is None and self.end is None
        elif self.count() == 1:
            self.begin is self.end and self.begin is not None
        if self.count() != 0:
            self.begin.prev is None and self.end.next_ is None
        
