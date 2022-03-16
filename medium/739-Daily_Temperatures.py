"""739
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.

If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""
import typing as t


class Solution:
    def dailyTemperatures(self, temperatures: t.List[int]) -> t.List[int]:
        n_days = len(temperatures)
        answers = [0] * n_days
        stack = []

        for i in range(len(temperatures)):
            temperature = temperatures[i]

            while stack and temperatures[stack[-1]] < temperature:
                prev_day = stack.pop()
                answers[prev_day] = i - prev_day

            stack.append(i)
        return answers


if __name__ == '__main__':
    testcases = [
        [73, 74, 75, 71, 69, 72, 76, 73],
        [30, 40, 50, 60]
    ]
    answers = [
        [1, 1, 4, 2, 1, 1, 0, 0],
        [1, 1, 1, 0]
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.dailyTemperatures(testcase)
        print(f'Output: {result}, IsCorrect: {result==ans}')
