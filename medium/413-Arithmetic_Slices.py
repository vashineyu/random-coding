"""
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.

Given an integer array nums, return the number of arithmetic subarrays of nums.
"""
import typing as t


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
      n = len(nums)
      if n < 3:
          return 0

      result = [0 for _ in range(n)]
      for i in range(2, n):
          if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
              result[i] = result[i - 1] + 1
      return sum(result)
 

if __name__ == '__main__':
  testcases = [
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5, 6],
        [1],
    ]
    answers = [
        3,
        10,
        0,
    ]
    sol = Solution()
    for testcase in testcases:
        result = sol.numberOfArithmeticSlices(testcase)
        print(f"Output: {result}")
