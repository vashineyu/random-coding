from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: bool = None, right: bool = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        result = set()
        have_result = []
        def findpair(node):
            if node and node.val in result:
                have_result.append((node.val, k - node.val))

            if node:
                result.add(k - node.val)
                findpair(node.left)
                findpair(node.right)

        findpair(root)
        return len(have_result) > 0
