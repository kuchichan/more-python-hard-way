from dataclasses import dataclass
from typing import Optional

from .single_linked_node import SingleLinkedNode


@dataclass
class SingleLinkedList:
    begin: Optional[SingleLinkedNode] = None
    end: Optional[SingleLinkedNode] = None

    def push(self, obj):
        if self.begin is None:
            self.begin = SingleLinkedNode(obj)
            self.end = self.begin
        else:
            new_end = SingleLinkedNode(obj)
            self.end.next_ = new_end
            self.end = self.end.next_

    def pop(self):
        if self.end is None:
            return None
        elif self.end == self.begin:
            value = self.end.value
            self.end = None
            self.begin = None
            return value

        else:
            elem = self.begin
            while elem.next_ != self.end:
                elem = elem.next_

            self.end = elem
            val = elem.next_.value
            self.end.next_ = None
            return val

    def shift(self, obj):
        new_begin = SingleLinkedNode(obj)
        if self.begin is None:
            self.begin = new_begin
            self.end = self.begin
        else:
            new_begin.next_ = self.begin
            self.begin = new_begin

    def unshift(self):
        if self.begin is None:
            return None
        val = self.begin.value
        self.begin = self.begin.next_
        return val

    def remove(self, obj):
        elem = self.begin
        prev = None
        index = 0
        if elem is None:
            return None
        while elem.value != obj and elem != None:
            prev = elem
            elem = elem.next_
            index += 1
        if prev is None:
            self.begin = elem.next_
        else:
            prev.next_ = elem.next_

        return index

    def first(self):
        return self.begin.value if self.begin is not None else None

    def last(self):
        return self.end.value if self.end is not None else None

    def count(self):
        count = 0
        begin = self.begin
        while begin is not None:
            begin = begin.next_
            count += 1
        return count

    def get(self, index):
        elem = self.begin
        counter = 0
        if elem is None:
            return None
        while index != counter and elem is not None:
            elem = elem.next_
            counter += 1

        return elem.value if elem is not None else None

    def dump(self, mark):
        print(mark, ":\n ")
        elem = self.begin
        while elem is not None:
            print(elem.value)
            elem = elem.next_
