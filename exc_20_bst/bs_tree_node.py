from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class BSTreeNode:
    key: int  # could be something comparable
    value: Any
    parent: Optional["BSTreeNode"] = None
    left: Optional["BSTreeNode"] = None
    right: Optional["BSTreeNode"] = None

    def draw_node(self, depth=0) -> str:
        pass

    def calc_max_depth(self) -> int:
        nodes_to_check = [(self, 0)]
        max_depth = 0
        while nodes_to_check:
            node, depth = nodes_to_check.pop()
            if max_depth < depth:
                max_depth = depth
            if node.left:
                nodes_to_check.append((node.left, depth + 1))
            if node.right:
                nodes_to_check.append((node.right, depth + 1))

        return max_depth
