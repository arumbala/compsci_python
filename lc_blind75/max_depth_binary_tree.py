from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    """
    Given the root of a binary tree, return its maximum depth.
    Maximum depth is the number of nodes along the longest path
    from the root node down to the farthest leaf node.
    """

    if root is None:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)

if __name__ == "__main__":
    # Example 1: [3, 9, 20, None, None, 15, 7] -> 3
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(max_depth(root1))  # Expected: 3

    # Example 2: [1, None, 2] -> 2
    root2 = TreeNode(1, None, TreeNode(2))
    print(max_depth(root2))  # Expected: 2

    # Example 3: empty tree -> 0
    print(max_depth(None))  # Expected: 0
