"""303
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
"""
import typing as t


class NumArray:
    def __init__(self, nums: t.List[int]):
        self.nums = nums
        self.dp = {
            0: 0
        }
        for i in range(1, len(nums) + 1):
            self.dp[i] = self.dp[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.dp[right + 1] - self.dp[left]
