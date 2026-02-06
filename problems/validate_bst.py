from typing import Optional



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """
    Given the root of a binary tree, determine if it is a valid BST.
    """
    def validate(node, min_val, max_val):
        if node is None:
            return True

        if not (min_val < node.val < max_val):
            return False

        return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)

    return validate(root, float('-inf'), float('inf'))


if __name__ == "__main__":
    # Example 1: [2, 1, 3] -> True
    #     2
    #    / \
    #   1   3
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    print(f"Valid BST [2,1,3]: {is_valid_bst(root1)}")  # Expected: True

    # Example 2: [5, 1, 4, None, None, 3, 6] -> False
    #     5
    #    / \
    #   1   4
    #      / \
    #     3   6   <- 3 < 5, invalid!
    root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(f"Invalid BST [5,1,4,null,null,3,6]: {is_valid_bst(root2)}")  # Expected: False

    # Example 3: Empty tree -> True
    print(f"Empty tree: {is_valid_bst(None)}")  # Expected: True

    # Example 4: Single node -> True
    root4 = TreeNode(1)
    print(f"Single node [1]: {is_valid_bst(root4)}")  # Expected: True

    # Example 5: Duplicate values -> False
    #     2
    #    /
    #   2   <- duplicate, invalid!
    root5 = TreeNode(2, TreeNode(2), None)
    print(f"Duplicate [2,2]: {is_valid_bst(root5)}")  # Expected: False

    # Example 6: Larger valid BST -> True
    #       10
    #      /  \
    #     5    15
    #    / \   / \
    #   3   7 12  20
    root6 = TreeNode(10,
                     TreeNode(5, TreeNode(3), TreeNode(7)),
                     TreeNode(15, TreeNode(12), TreeNode(20)))
    print(f"Larger valid BST: {is_valid_bst(root6)}")  # Expected: True

    # Example 7: Right child less than ancestor -> False
    #     10
    #       \
    #       15
    #      /
    #     6   <- 6 < 10, invalid!
    root7 = TreeNode(10, None, TreeNode(15, TreeNode(6), None))
    print(f"Right child < ancestor: {is_valid_bst(root7)}")  # Expected: False