"""2
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.

Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
import typing as t


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        prev = node
        remain = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            if l1:
                l1 = l1.next

            v2 = l2.val if l2 else 0
            if l2:
                l2 = l2.next

            remain, v = divmod(v1 + v2 + remain, 10)
            prev.next = ListNode(val=v)
            prev = prev.next

        if remain:
            prev.next = ListNode(val=remain)
            prev = prev.next
        return node.next
