from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class BSTreeNode:
   key: int # could be something comparable 
   value: Any
   parent: Optional["BSTreeNode"] = None 
   left: Optional["BSTreeNode"] = None 
   right: Optional["BSTreeNode"] = None 


