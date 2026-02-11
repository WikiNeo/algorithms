# LeetCode 104: Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
#
# Time:  O(n) — each node is visited once; constant work per node.
# Space: O(h) — recursion stack depth equals tree height h.
#        Worst case (skewed tree): h = n → O(n).
#        Balanced tree: h = log(n) → O(log n).


# Definition for a binary tree node (LeetCode standard).
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode | None) -> int:
    """Return the number of nodes along the longest path from root to farthest leaf.
    Time O(n), space O(h) for recursion stack."""
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        return max_depth(root)


if __name__ == "__main__":
    # Example 1: [3,9,20,null,null,15,7] -> 3
    t1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(t1) == 3, "Example 1"

    # Example 2: [1,null,2] -> 2
    t2 = TreeNode(1, None, TreeNode(2))
    assert max_depth(t2) == 2, "Example 2"

    # Empty tree -> 0
    assert max_depth(None) == 0, "Empty tree"

    print("All tests passed.")
