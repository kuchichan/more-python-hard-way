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
            node.prev_ = self.end
            self.end = node
            
    def shift(self, obj: str) ->  None:
        node = DoubleLinkedListNode(obj)
        if self.count() == 0:
            self.begin = node
            self.end = self.begin
        else:
            self.begin.prev_ = node
            node.next_ = self.begin
            self.begin = node

    def pop(self) -> str:
        if self.count() == 0:
            return
        else:
            value = self.end.value
            self.detach(self.end)
        return value

    def unshift(self) -> str:
        if self.count() == 0:
            return 
        else:
            value = self.begin.value
            self.detach(self.begin)
        return value
    
    def remove(self, obj: str):
        node = self.begin
        if node is None:
            return 
        
        while node is not None:
            if node.value == obj:
                break
            node = node.next_
    
        self.detach(node) if node is not None else None

    def get(self, index: int) -> str:
        node = self.begin
        if node is None:
            return
        count = 0
        while node is not None:
            if index == count:
                return node.value
            node = node.next_
            count += 1

        return None

    def first(self):
        return self.begin

    def last(self):
        return self.end

    def dump(self, text):
        print(text, "\n")
        node = self.begin
        while node is not None:
            print(node.value)
            node =node.next_
        
    
    def count(self) -> int:
        counter = 0

        if self.begin is None:
            return counter
        node = self.begin

        while node != None:
            node = node.next_
            counter += 1

        return counter
    

    def _invariant(self) -> None:
        if self.count() == 0:
            assert self.begin is None and self.end is None
        elif self.count() == 1:
            self.begin is self.end and self.begin is not None
        if self.count() != 0:
            self.begin.prev_ is None and self.end.next_ is None


    def detach(self, node: DoubleLinkedListNode) -> None:
        if node.next_ is None and node.prev_ is None:
            self.begin = None
            self.end = None
        elif node.next_ is None:
            node.prev_.next_ = None
            self.end = node.prev_
        elif node.prev_ is None:
            node.next_.prev_ = None
            self.begin = node.next_
        else:
            node.prev_.next_ = node.next_
            node.next_.prev_ = node.prev_
        del node

        
        


        
