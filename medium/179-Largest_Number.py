"""179: String sort built-in function __lt__
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.
"""
import typing as t


class LargeNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums: t.List[int]) -> str:
        nums = map(str, nums)

        result = ''.join(sorted(nums, key=LargeNumKey))
        return '0' if result[0] == '0' else result


if __name__ == '__main__':
    testcases = [
        [0],
        [0, 0, 0],
        [0, 1],
        [10, 2],
        [3, 30, 34, 5, 9],
        [432, 43243],
        [111311, 1113],
        [34323, 3432],
    ]
    answers = [
        "0",
        "0",
        "10",
        "210",
        "9534330",
        "43243432",
        "1113111311",
        "343234323",
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.largestNumber(testcase)
        print(f'Output: {result}, IsCorrect={ans==result}')
