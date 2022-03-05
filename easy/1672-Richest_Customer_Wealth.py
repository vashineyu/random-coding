"""
You are given an m x n integer grid accounts
  where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank.

Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts.
The richest customer is the customer that has the maximum wealth.
"""
import typing as t


class Solution:
    def maximumWealth(self, accounts: t.List[t.List[int]]) -> int:
        wealth = [sum(i) for i in accounts]
        return max(wealth)


if __name__ == '__main__':
    testcases = [
        [[1, 2, 3], [3, 2, 1]],
    ]
    answers = [
        6
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.maximumWealth(testcase)
        print(f'Input: {testcase}, Output: {result}, Ans: {ans}')
