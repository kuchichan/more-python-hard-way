from typing import Any, Optional

from .bs_tree_node import BSTreeNode

class BSTree:
    def __init__(self, key: int, value: Any):
        self.root = BSTreeNode(key, value)
    
    def get(self, key) -> Optional[BSTreeNode]:
        cur_node = self.root

        while cur_node is not None:
            if cur_node.key > key:
                cur_node = cur_node.left
            elif cur_node.key < key:
                cur_node = cur_node.right
            else:
                return cur_node
        return None

    def set(self, key: int, value: Any) -> None:
        prev_node = None
        cur_node = self.root
        was_left = True 

        while cur_node is not None:
            if cur_node.key > key:
                prev_node = cur_node
                cur_node = cur_node.left
                was_left = True
            elif cur_node.key < key:
                prev_node = cur_node
                cur_node = cur_node.right
                was_left = False 
            else:
                cur_node.value = value
                break
        else: 
            if was_left:
                prev_node.left = BSTreeNode(key, value, parent=prev_node)
            else:
                prev_node.right = BSTreeNode(key, value, parent=prev_node)
