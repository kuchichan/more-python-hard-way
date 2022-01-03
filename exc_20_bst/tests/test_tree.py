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
    right_left_right = BSTreeNode(20, "Sayonara", parent=right_left)
    right_right = BSTreeNode(24, "Czesc", parent=right)

    left.left = left_left
    left.right = left_right
    right.right = right_right
    right.left = right_left
    right_left.right = right_left_right

    tree.root.left = left
    tree.root.right = right

    return tree


def test_get_is_taking_existing_value(two_level_deep_tree):
    assert two_level_deep_tree.get(18).value == "Hehe"
    assert two_level_deep_tree.get(24).value == "Czesc"
    assert two_level_deep_tree.get(16).value == "Bonjour"
    
def test_get_returns_None_when_value_does_not_exist_in_tree(two_level_deep_tree):
    assert two_level_deep_tree.get(27) is None
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


def test_delete_single_element_bst_tree():
    tree = BSTree(10, "aaa")

    assert tree.root.value == "aaa" 
    assert tree.root.key == 10 
    
    tree.delete(10)

    assert tree.root == None


def test_delete_element_with_one_child():
    tree = BSTree(10, "aaa")
    tree.set(20, "bbb")
    tree.set(30, "ccc")

    middle_node = tree.get(20)
    last_node = tree.get(30)

    assert middle_node.value == "bbb"
    assert middle_node.parent == tree.root
    assert middle_node.right.key == 30
    assert middle_node.right.value ==  "ccc"

    tree.delete(20)

    assert tree.root.right == last_node 
    assert tree.get(20) is None



def test_get_min_value_from_root(two_level_deep_tree):
    node = two_level_deep_tree.find_min_node(two_level_deep_tree.root)

    assert node.key == 4

    node = two_level_deep_tree.find_min_node(two_level_deep_tree.root.right)

    assert node.key == 19
    

def test_delete_with_both_nested_children(two_level_deep_tree):
    two_level_deep_tree.delete(18)
    
    assert two_level_deep_tree.root.key == 19
    assert two_level_deep_tree.root.value == "Nihao" 

    assert two_level_deep_tree.root.left.key == 15
    assert two_level_deep_tree.root.right.key == 21  
    assert two_level_deep_tree.root.right.left.key == 20  
    assert two_level_deep_tree.root.right.right.key == 24

    
def test_calculate_max_depth(two_level_deep_tree):
    assert two_level_deep_tree.root.calc_max_depth() == 3 
    
    two_level_deep_tree.set(1, "hi")
    assert two_level_deep_tree.root.calc_max_depth() == 3
    
    two_level_deep_tree.set(28, "hi")
    assert two_level_deep_tree.root.calc_max_depth() == 3
    
    two_level_deep_tree.set(32, "hi")
    assert two_level_deep_tree.root.calc_max_depth() == 4
    

