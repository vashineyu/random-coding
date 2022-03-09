"""
Given the head of a sorted linked list,
delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.
Return the linked list sorted as well.
"""
import typing as t
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: t.Optional[ListNode]) -> t.Optional[ListNode]:
        if not head:
            return head

        node = ListNode()
        prev = node

        scan_node = head
        record = defaultdict(int)
        while scan_node:
            record[scan_node.val] += 1
            scan_node = scan_node.next

        for val, cnt in record.items():
            if cnt > 1:
                for _ in range(cnt):
                    head = head.next
            else:
                prev.next = head
                prev = prev.next
                head = head.next
        if cnt > 1:
            # Prevent Last element is duplicated.
            prev.next = None
        return node.next


if __name__ == '__main__':
    testcases = [
        ListNode(val=1, next=ListNode(val=2, next=ListNode(val=2))),
        ListNode(val=None),
    ]
    sol = Solution()
    for testcase in testcases:
        result = sol.deleteDuplicates(testcase)
        print(f"Input: {testcase}\nOutput: {result}")