import pytest
from ..bs_tree import BSTree
from ..bs_tree_node import BSTreeNode


@pytest.fixture
def two_level_deep_tree() -> BSTree:
    tree = BSTree(18, "Hehe")
    left = BSTreeNode(15, "Hi", parent=tree.root)
    right = BSTreeNode(21, "Hallo", parent=tree.root)
    left_left = BSTreeNode(4, "Hola", parent=left)
    left_right = BSTreeNode(16, "Bonjour", parent=left)
    right_left = BSTreeNode(19, "Nihao", parent=right)
    right_right = BSTreeNode(24, "Czesc", parent=right)

    left.left = left_left
    left.right = left_right
    right.right = right_right
    right.left = right_left

    tree.root.left = left
    tree.root.right = right

    return tree


def test_get_is_taking_existing_value(two_level_deep_tree):
    assert two_level_deep_tree.get(18).value == "Hehe"
    assert two_level_deep_tree.get(24).value == "Czesc"
    assert two_level_deep_tree.get(16).value == "Bonjour"
    
def test_get_returns_None_when_value_does_not_exist_in_tree(two_level_deep_tree):
    assert two_level_deep_tree.get(20) is None
    assert two_level_deep_tree.get(10) is None
    assert two_level_deep_tree.get(0) is None
    assert two_level_deep_tree.get(770) is None


def test_set_new_value_smallest_value(two_level_deep_tree):
    two_level_deep_tree.set(3, "Bye Bye")
    result = two_level_deep_tree.get(3)

    assert result.value == "Bye Bye"
    assert result.parent.left == result
    assert result.parent.key == 4


def test_set_existing_value(two_level_deep_tree):
    two_level_deep_tree.set(18, "HAHA")

    assert two_level_deep_tree.root.value == "HAHA"
    assert two_level_deep_tree.root.left.key == 15
    assert two_level_deep_tree.root.left.value == "Hi" 
    assert two_level_deep_tree.root.right.key == 21 
    assert two_level_deep_tree.root.right.value == "Hallo" 
