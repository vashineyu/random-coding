"""
Given a binary tree root and a linked list with head as the first node.

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.
"""
import typing as t


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: t.Optional[ListNode], root: t.Optional[TreeNode]) -> bool:
        def helper(treenode, listnode):
            if listnode is None:
                return True
            if treenode is None:
                return False

            return listnode.val == treenode.val and (
                helper(treenode.left, listnode.next) or
                helper(treenode.right, listnode.next)
            )

        if head is None:
            return True
        if root is None:
            return False

        return helper(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
