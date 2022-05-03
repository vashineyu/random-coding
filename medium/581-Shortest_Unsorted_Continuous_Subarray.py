"""581: two indexes
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order,
 then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.
"""
import typing as t


class Solution:
    def findUnsortedSubarray(self, nums: t.List[int]) -> int:
        nums_sorted = sorted(nums)

        pin = []
        for i, (num1, num2) in enumerate(zip(nums, nums_sorted)):
            if num1 != num2:
                pin.append(i)

        if pin:
            return max(pin) - min(pin) + 1
        return 0


if __name__ == '__main__':
    testcases = [
        [3, 2, 1],
        [1, 3, 2],
    ]
    answers = [
        3,
        2,
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.findUnsortedSubarray(testcase)
        print(f'Output={result}, IsCorrect={ans==result}')
