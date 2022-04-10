""" 682: Stack
You are keeping score for a baseball game with strange rules.
The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

At the beginning of the game, you start with an empty record.
You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:
1. An integer x - Record a new score of x.
2. "+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
3. "D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
4. "C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.

Return the sum of all the scores on the record.
"""
import typing as t


class Solution:
    def calPoints(self, ops: t.List[str]) -> int:

        record = []
        for op in ops:
            if op == 'C':
                record.pop()
            elif op == 'D':
                record.append(record[-1] * 2)
            elif op == '+':
                record.append(record[-2] + record[-1])
            else:
                record.append(int(op))
        return sum(record)


if __name__ == '__main__':
    testcases = [
        ["5", "2", "C", "D", "+"],
        ["5", "-2", "4", "C", "D", "9", "+", "+"]
    ]
    answers = [
        30,
        27,
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.calPoints(testcase)
        print(f'Input: {testcase}, Output: {result}, IsCorrect={result==ans}')
