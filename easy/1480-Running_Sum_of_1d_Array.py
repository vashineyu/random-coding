"""1480
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""
import typing as t


class Solution:
    def runningSum(self, nums: t.List[int]) -> t.List[int]:
        result = []
        current = 0
        for num in nums:
            current += num
            result.append(current)
        return result


if __name__ == '__main__':
    testcases = [
        [1, 2, 3, 4],
        [1, 1, 1, 1, 1],
    ]
    answers = [
        [1, 3, 6, 10],
        [1, 2, 3, 4, 5],
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.runningSum(testcase)
        print(f'Input: {testcase}, Output: {ans}, IsCorrect: {ans==result}')
