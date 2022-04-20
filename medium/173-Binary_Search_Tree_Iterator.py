"""173: Inorder traversal
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

- BSTIterator(TreeNode root): Initializes an object of the BSTIterator class.
The root of the BST is given as part of the constructor.
The pointer should be initialized to a non-existent number smaller than any element in the BST.

- boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.

- int next() Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

"""
import typing as t


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: t.Optional[TreeNode]):
        inorder_list = []

        def inorder_visit(node):
            if node.left:
                inorder_visit(node.left)
            inorder_list.append(node.val)
            if node.right:
                inorder_visit(node.right)
        inorder_visit(root)
        self.inorder_list = inorder_list
        self.index = 0

    def next(self) -> int:
        if self.hasNext:
            val = self.inorder_list[self.index]
            self.index += 1
            return val

    def hasNext(self) -> bool:
        return self.index < len(self.inorder_list)
