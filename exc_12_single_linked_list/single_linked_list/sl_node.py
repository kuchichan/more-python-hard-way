from dataclasses import dataclass
from typing import Optional

@dataclass
class SingleLinkedNode:
    value : str
    next_ : Optional["SingleLinkedNode"] = None





