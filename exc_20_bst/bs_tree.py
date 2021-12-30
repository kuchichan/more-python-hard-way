from typing import Any 

from .bs_tree_node import BSTreeNode

class BSTree:
    def __init__(self, key: int, value: Any):
        self.root = BSTreeNode(key, value)
    
    def get(self, key) -> Any:
        cur_node = self.root

        while cur_node is not None:
            if cur_node.key > key:
                cur_node = cur_node.left
            elif cur_node.key < key:
                cur_node = cur_node.right
            else:
                return cur_node.value
        return None
