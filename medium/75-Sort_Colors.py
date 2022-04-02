"""75: index swapping
Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""
import typing as t


class Solution:
    def sortColors(self, nums: t.List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        while i < n:
            num = nums[i]
            for j in range(i + 1, n):
                if nums[j] < num:
                    nums[i], nums[j] = nums[j], nums[i]
                    num = nums[i]
            i += 1
        return nums


if __name__ == '__main__':
    testcases = [
        [2, 1, 0, 2, 1, 0],
        [1, 2, 0, 1, 1, 0],
        [2, 2, 1, 1, 0, 0, 2],
        [0, 1, 1, 0, 1],
    ]
    sol = Solution()
    for testcase in testcases:
        result = sol.sortColors(testcase)
        print(f'Output: {result}')
