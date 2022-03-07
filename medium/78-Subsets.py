"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""
import typing as t


class Solution:
    def subsets(self, nums: t.List[int]) -> t.List[t.List[int]]:
        def helper(remain_nums, path):
            if path not in result:
                result.append(path)

            for i in range(len(remain_nums)):
                helper(remain_nums[(i + 1):], path + [remain_nums[i]])

        result = [[]]
        for i in range(len(nums)):
            helper(nums[(i + 1):], [nums[i]])
        return result


if __name__ == '__main__':
    testcases = [
        [1, 2, 3],
    ]
    answers = [
        [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.subsets(testcase)
        print(f'Input: {testcase}\nOutput: {result}\nAnswer: {ans}')
