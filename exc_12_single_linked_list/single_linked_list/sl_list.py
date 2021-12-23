from dataclasses import dataclass
from typing import Optional

from .sl_node import SingleLinkedNode


@dataclass
class SingleLinkedList:
    begin: Optional[SingleLinkedNode] = None
    end: Optional[SingleLinkedNode] = None

    def push(self, obj):
        node = SingleLinkedNode(obj)
        if self.begin is None:
            self.begin = node
            self.end = self.begin
        else:
            end = self.end
            end.next_ = node
            self.end = node

    def pop(self):
        if self.begin is None:
            return None
        elif self.begin is self.end:
            val = self.begin.value
            self.begin = None
            self.end = None
        else:
            node = self.begin
            prev = None
            while node.next_ is not None:
                prev = node
                node = node.next_
            val = node.value
            prev.next_ = None
            self.end = prev
        return val

    def shift(self, obj):
        node = SingleLinkedNode(obj)
        if self.begin is None:
            self.begin = node
            self.end = self.begin
        else:
            begin = self.begin
            node.next_ = begin
            self.begin = node

    def unshift(self):
        begin = self.begin
        if begin is None:
            return None
        else:
            val = begin.value
            self.begin = begin.next_
            begin = None
            return val

    def remove(self, obj):
        index = 0
        node = self.begin
        prev = None
        while node != None and node.value != obj:
            index += 1
            prev = node
            node = node.next_
        if node is None:
            return None
        else:
            if prev is None:
                self.begin = node.next_ if node.next_ is not None else None
            else:
                prev.next_ = node.next_ if node.next_ is not None else None
            node = None
            return index

    def first(self):
        return self.begin.value

    def last(self):
        return self.end.value

    def count(self):
        counter = 0
        if self.begin is None:
            return counter
        elem = self.begin
        while elem is not None:
            elem = elem.next_
            counter += 1
        return counter

    def get(self, index):
        counter = 0
        node = self.begin
        if node is None:
            return None
        while counter < index and node is not None:
            node = node.next_
            counter += 1

        return node.value if node is not None else None

    def dump(self, mark):
        print(mark + ":\n")
        node = self.begin
        while node != None:
            print(node)
            node = node.next_
