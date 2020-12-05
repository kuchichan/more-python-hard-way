from dataclasses import dataclass
from typing import Optional

from .single_linked_node import SingleLinkedNode


@dataclass
class SingleLinkedList:
    begin: Optional[SingleLinkedNode] = None
    end: Optional[SingleLinkedNode] = None

    def push(self, obj):
        ...

    def pop(self):
        ...

    def shift(self, obj):
        ...

    def unshift(self):
        ...

    def remove(self, obj):
        ...

    def first(self):
        ...

    def last(self):
        ...

    def count(self):
        ...

    def get(self, index):
        ...

    def dump(self, mark):
        ...
