from dataclasses import dataclass
from typing import Optional

@dataclass
class DoubleLinkedListNode:
    value: str  # just for clarity
    prev : Optional["DoubleLinkedListNode"] = None
    next_ : Optional["DoubleLinkedListNode"] = None
