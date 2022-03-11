"""61
Given the head of a linked list, rotate the list to the right by k places.
"""
import typing as t


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: t.Optional[ListNode], k: int) -> t.Optional[ListNode]:
        if head is None:
            return head
        
        slow = fast = head
        n = 0
        values = []
        while fast:
            values.append(fast.val)
            fast = fast.next
            n += 1
        
        k = k % n
        if k == 0:
            return head
        
        values = values[(n - k):] + values[:(n - k)]
        for value in values:
            slow.val = value
            slow = slow.next
            
        return head
