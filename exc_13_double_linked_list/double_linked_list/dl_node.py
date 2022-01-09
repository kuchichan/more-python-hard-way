from dataclasses import dataclass
from typing import Any, Optional

@dataclass
class DoubleLinkedListNode:
    value: Any  # just for clarity
    prev_ : Optional["DoubleLinkedListNode"] = None
    next_ : Optional["DoubleLinkedListNode"] = None
