from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Check if two binary trees are identical.
    Two trees are same if they have same structure and same node values.
    """
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    elif p.val == q.val:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    else:
        return False


if __name__ == "__main__":
    # Test case 1: Same trees
    #     1         1
    #    / \       / \
    #   2   3     2   3
    tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
    tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(f"Same trees: {is_same_tree(tree1, tree2)}")  # Expected: True

    # Test case 2: Different structure
    #     1         1
    #    /           \
    #   2             2
    tree3 = TreeNode(1, TreeNode(2), None)
    tree4 = TreeNode(1, None, TreeNode(2))
    print(f"Different structure: {is_same_tree(tree3, tree4)}")  # Expected: False

    # Test case 3: Different values
    #     1         1
    #    / \       / \
    #   2   3     2   4
    tree5 = TreeNode(1, TreeNode(2), TreeNode(3))
    tree6 = TreeNode(1, TreeNode(2), TreeNode(4))
    print(f"Different values: {is_same_tree(tree5, tree6)}")  # Expected: False

    # Test case 4: Both empty
    print(f"Both empty: {is_same_tree(None, None)}")  # Expected: True