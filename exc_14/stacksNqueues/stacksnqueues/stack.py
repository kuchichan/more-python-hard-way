from dataclasses import dataclass
from typing import Any


@dataclass
class StackNode:
    value: Any = None
    next_: "StackNode" = None


class Stack:
    def __init__(self):
        self.guard = StackNode(
            value=None
        )
        self.guard.next_ = self.guard
        self.top: StackNode = self.guard

    def push(self, value: Any) -> None:
        node = StackNode(value=value, next_=self.top)
        self.top = node

    def pop(self) -> Any:
        value = self.top.value
        self.top = self.top.next_
        return value

    def count(self) -> int:
        counter = 0
        node = self.top
        while node.value is not None:
            node = node.next_
            counter += 1

        return counter

    def top(self) -> Any:
        return self.top.value

    def dump(self, mark="==="):
        node = self.top
        while node.value is not None:
            print("value: ", node.value)
            node = node.next_
        
        
