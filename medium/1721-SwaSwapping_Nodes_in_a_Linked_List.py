""" 1721: LinkedList traverse
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning
 and the kth node from the end (the list is 1-indexed).
"""
import typing as t


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: t.Optional[ListNode], k: int) -> t.Optional[ListNode]:
        return self.sol2(head, k)

    def sol1(self, head: t.Optional[ListNode], k: int) -> t.Optional[ListNode]:
        values = []

        while head:
            values.append(head.val)
            head = head.next

        n = len(values)
        values[k - 1], values[n - k] = values[n - k], values[k - 1]

        node = ListNode()
        prev = node
        for value in values:
            prev.next = ListNode(val=value)
            prev = prev.next
        return node.next

    def sol2(self, head: t.Optional[ListNode], k: int) -> t.Optional[ListNode]:
        fast = slow = head
        for i in range(k - 1):
            fast = fast.next

        niddle = fast
        while niddle.next:
            slow = slow.next
            niddle = niddle.next
        fast.val, slow.val = slow.val, fast.val
        return head


if __name__ == '__main__':
    testcases = [
        [ListNode(val=1), 1],
        [ListNode(val=1, next=ListNode(val=2)), 1],
        [ListNode(val=1, next=ListNode(val=2)), 2],
    ]
    sol = Solution()
    for testcase in testcases:
        result = sol.swapNodes(*testcase)
        print(f'Output: {result}')