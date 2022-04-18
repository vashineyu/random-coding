"""230: inorder visit
Given the root of a binary search tree, and an integer k,
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""
import typing as t


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: t.Optional[TreeNode], k: int) -> int:
        # inorder visit
        def visit_inorder(node):
            if node.left:
                visit_inorder(node.left)

            result.append(node.val)

            if node.right:
                visit_inorder(node.right)

        result = []
        visit_inorder(root)
        return result[k - 1]
