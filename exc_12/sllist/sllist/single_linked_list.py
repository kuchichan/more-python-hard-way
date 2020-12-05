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
            return elem.next_.value

    def shift(self, obj):
        self.push(self, obj)

    def unshift(self):
        ...

    def remove(self, obj):
        ...

    def first(self):
        ...

    def last(self):
        ...

    def count(self):
        count = 0
        begin = self.begin
        while begin is not None:
            begin = begin.next_
            count += 1
        return count

    def get(self, index):
        ...

    def dump(self, mark):
        ...
