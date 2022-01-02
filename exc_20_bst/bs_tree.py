import sys
from typing import Any, Optional, cast, no_type_check_decorator

from .bs_tree_node import BSTreeNode


class BSTree:
    def __init__(self, key: int, value: Any):
        self._sentinel = BSTreeNode(
            sys.maxsize, None, parent=None, right=None, left=None
        )
        root = BSTreeNode(key, value, parent=self._sentinel)
        self._sentinel.left = root

    @property
    def root(self):
        return self._sentinel.left

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
        prev_node = self._sentinel 
        cur_node = self.root

        while cur_node is not None:
            if cur_node.key > key:
                prev_node = cur_node
                cur_node = cur_node.left
            elif cur_node.key < key:
                prev_node = cur_node
                cur_node = cur_node.right
            else:
                cur_node.value = value
                break
        else:
            if key < prev_node.key:
                prev_node.left = BSTreeNode(key, value, parent=prev_node)
            else:
                prev_node.right = BSTreeNode(key, value, parent=prev_node)

    def _set_prev_node(self, key: int, previous: BSTreeNode, new_node: Optional[BSTreeNode]):
        if key < previous.key:
            previous.left =  new_node 
        else:
            previous.right = new_node

    def delete(self, key: int) -> None:
        node_to_delete = self.get(key)
        if node_to_delete is None:
            return

        previous = node_to_delete.parent
        previous = cast(BSTreeNode, previous)
        
        while node_to_delete is not None:
            if not node_to_delete.left and not node_to_delete.right:
                self._set_prev_node(key, previous, None)
                node_to_delete = None
                
            elif node_to_delete.left and not node_to_delete.right:
                self._set_prev_node(key, previous, node_to_delete.left)
                node_to_delete = None

            elif node_to_delete.right and not node_to_delete.left:
                self._set_prev_node(key, previous, node_to_delete.right)
                node_to_delete = None
