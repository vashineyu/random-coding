"""202: hash/set
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while True:
            visited.add(n)
            total = sum([int(i) ** 2 for i in str(n)])
            if total == 1:
                return True

            if total in visited:
                return False

            n = total


if __name__ == '__main__':
    testcases = [19, 2]
    answers = [True, False]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.isHappy(testcase)
        print(f'Input: {testcase}, Output={result}, IsCorrect={result==ans}')
