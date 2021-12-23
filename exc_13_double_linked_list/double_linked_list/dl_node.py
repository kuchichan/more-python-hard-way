from dataclasses import dataclass
from typing import Optional

@dataclass
class DoubleLinkedListNode:
    value: str  # just for clarity
    prev_ : Optional["DoubleLinkedListNode"] = None
    next_ : Optional["DoubleLinkedListNode"] = None
