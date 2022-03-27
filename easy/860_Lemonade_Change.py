"""860: Simple DP, Conditions
At a lemonade stand, each lemonade costs $5.
Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills).
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays,
return true if you can provide every customer with the correct change, or false otherwise.
"""
import typing as t
from collections import defaultdict


class Solution:
    def lemonadeChange(self, bills: t.List[int]) -> bool:

        pocket = defaultdict(int)
        for bill in bills:
            if bill == 5:
                pocket[bill] += 1
                continue

            if bill == 10:
                if pocket[5] > 0:
                    pocket[5] -= 1
                    pocket[bill] += 1
                else:
                    return False
                continue

            if bill == 20:
                if pocket[10] > 0 and pocket[5] > 0:
                    pocket[5] -= 1
                    pocket[10] -= 1
                elif pocket[5] > 2:
                    pocket[5] -= 3
                else:
                    return False
                pocket[bill] += 1
                continue
        return True


if __name__ == '__main__':
    testcases = [
        [5, 5, 5, 10, 20],
        [5, 5, 10, 10, 20],
    ]
    answers = [
        True,
        False,
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.lemonadeChange(testcase)
        print(f'Output: {result}, IsCorrect:{ans==result}')
