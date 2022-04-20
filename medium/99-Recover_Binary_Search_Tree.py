"""99: Inorder traversal
You are given the root of a binary search tree (BST),
where the values of exactly two nodes of the tree were swapped by mistake.

Recover the tree without changing its structure.
"""
import typing as t


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: tOptional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorder_list = []
        def inorder_visit(node):

            if node.left:
                inorder_visit(node.left)

            inorder_list.append(node)

            if node.right:
                inorder_visit(node.right)

        inorder_visit(root)
        sorted_inorder_list = sorted(inorder_list, key=lambda x: x.val)

        for i in range(len(inorder_list)):
            if inorder_list[i] != sorted_inorder_list[i]:
                inorder_list[i].val, sorted_inorder_list[i].val = sorted_inorder_list[i].val, inorder_list[i].val
                return
