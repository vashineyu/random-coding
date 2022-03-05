"""
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:
- Pick any nums[i] and delete it to earn nums[i] points.
  Afterwards, you must
    - delete every element equal to nums[i] - 1 and,
             every element equal to nums[i] + 1.

Return the maximum number of points you can earn by applying the above operation some number of times.
"""
import typing as t


class Solution:
    def deleteAndEarn(self, nums: t.List[int]) -> int:
        vals = [0] * (max(nums) + 1)
        for num in nums:
            vals[num] += num

        if len(vals) <= 2:
            return max(vals)

        dp = {
            0: 0,
            1: vals[1],
            2: vals[0] + vals[2]
        }

        for i in range(3, len(vals)):
            dp[i] = vals[i] + max(dp[i - 2], dp[i - 3])
        return max(dp.values())


if __name__ == '__main__':
    # Generate some testcases
    testcases = [
        [3, 4, 2],
        [2, 2, 3, 3, 3, 4],
        [1, 1, 1, 2, 4, 5, 5, 5, 6],
        [1],
        [1, 1],
        [1, 1, 2],
        [1, 1, 3],
    ]
    answers = [
        6,
        9,
        18,
        1,
        2,
        2,
        5,
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.deleteAndEarn(testcase)
        print(f"Input: {testcase}, Output: {result}, Ans: {ans}")
