"""1679: Hashtable, two-sum
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
"""
import typing as t
from collections import defaultdict


class Solution:
    def maxOperations(self, nums: t.List[int], k: int) -> int:
        hashtable = defaultdict(int)
        counts = 0

        for num in nums:
            if k - num in hashtable and hashtable[k - num] > 0:
                counts += 1
                hashtable[k - num] -= 1

            else:
                hashtable[num] += 1
        return counts
