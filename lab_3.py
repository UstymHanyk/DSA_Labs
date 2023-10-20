import pytest


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def check_height_recursive(node):
    if not node:
        return 0

    left_height = check_height_recursive(node.left)
    right_height = check_height_recursive(node.right)

    if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
        return -1

    return max(left_height, right_height) + 1


def is_balanced(root):
    return check_height_recursive(root) != -1


def test_balanced_tree():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)

    assert is_balanced(root)


def test_unbalanced_tree():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(3)

    assert not is_balanced(root)


def test_empty_tree():
    assert is_balanced(None)


if __name__ == '__main__':
    pytest.main()
