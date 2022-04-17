"""897: Inorder traversal
Given the root of a binary search tree, rearrange the tree in in-order
  so that the leftmost node in the tree is now the root of the tree,
  and every node has no left child and only one right child.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def helper(node):
            if node.left:
                helper(node.left)

            if node:
                visited.append(node.val)

            if node.right:
                helper(node.right)

        visited = []
        helper(root)

        new_tree = TreeNode()
        current = new_tree
        for val in visited:
            current.right = TreeNode(val=val)
            current = current.right
        return new_tree.right
