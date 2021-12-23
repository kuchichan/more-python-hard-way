from dataclasses import dataclass
from typing import Any


@dataclass
class StackNode:
    value: Any = None
    next_: "StackNode" = None


@dataclass
class QueueNode:
    value: Any = None
    next_: "QueueNode" = None
    prev_: "QueueNode" = None


class Queue:
    def __init__(self):
        self.sentinel = QueueNode(value=None)
        self.sentinel.next_ = self.sentinel
        self.sentinel.prev_ = self.sentinel

    def shift(self, value: Any) -> None:
        node = QueueNode(value=value, next_=self.sentinel.next_)
        self.sentinel.next_.prev_ = node
        self.sentinel.next_ = node
        node.prev_ = self.sentinel

    def pop(self) -> Any:
        val = self.sentinel.prev_.value
        self.sentinel.prev_.prev_.next_ = self.sentinel.prev_.next_
        self.sentinel.prev_ = self.sentinel.prev_.prev_
        return val

    def count(self) -> int:
        counter = 0
        node = self.sentinel.next_
        while node.value is not None:
            node = node.next_
            counter += 1

        return counter

    def dump(self, mark="===="):
        node = self.sentinel.next_
        while node.value is not None:
            print(mark)
            print("value: ", node.value)
            node = node.next_


class Stack:
    def __init__(self):
        self.guard = StackNode(value=None)
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
