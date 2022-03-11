"""896
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.
"""
import typing as t


class Solution:
    def isMonotonic(self, nums: t.List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        
        is_increase = None
        for i in range(1, n):
            prev = nums[i - 1]
            current = nums[i]
            
            if is_increase is None and current != prev:
                is_increase = current > prev
            
            if is_increase and current < prev:
                return False
            
            if not is_increase and current > prev:
                return False
            
        return True
      
      
if __name__ == '__main__':
  testcases = [
        [1, 1, 1, 1],
        [1, 1, 1, 2],
        [1, 1, 1, 0],
        [0],
        [1],
        [1, 2, 2, 2],
        [2, 1, 1, 1],
        [1, 5, -1, 2],
    ]
    answers = [
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        False,
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.isMonotonic(testcase)
        print(f'Input: {testcase}, IsCorrect:{result==ans}')
