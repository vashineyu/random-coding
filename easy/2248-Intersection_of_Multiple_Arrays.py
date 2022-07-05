"""2248: Counter
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers,
  return the list of integers that are present in each array of nums sorted in ascending order.
"""
import typing as t
from collections import defaultdict

class Solution:
    def intersection(self, nums: t.List[List[int]]) -> t.List[int]:

        counter = defaultdict(int)

        for lst in nums:
            for num in lst:
                counter[num] += 1

        result = []
        for k, v in counter.items():
            if v == len(nums):
                result.append(k)
        result.sort()
        return result
