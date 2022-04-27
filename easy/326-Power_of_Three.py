"""326: math
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3^x.
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False

        if n == 1:
            return True

        while n > 1:
            n, remain = divmod(n, 3)
            if remain != 0:
                return False
            if n == 1:
                return True
        return True


if __name__ == '__main__':
    testcases = [27, 0, 9, 243, 8, 12, 2, 4, 1]
    answers = [True, False, True, True, False, False, False, False, True]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.isPowerOfThree(testcase)
        print(f'Input: {testcase}, Output: {result}, IsCorrect: {ans==result}')
