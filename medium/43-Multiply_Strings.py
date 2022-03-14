"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the *inputs* to integer directly.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        if num1 == "1":
            return num2

        if num2 == "1":
            return num1

        base = ord("0")
        num = 0
        for i, n in enumerate(num1[::-1]):
            n = (ord(n) - base) * 10 ** i
            num_single_pos = 0
            for j, m in enumerate(num2[::-1]):
                m = (ord(m) - base) * 10 ** j
                y = m * n
                num_single_pos += y
            num += num_single_pos
        return str(num)


if __name__ == '__main__':
    testcases = [
        [['2', '3'], '6'],
        [['123', '45'], '5535'],
        [['1', '456789'], '456789'],
        [['0', '1000'], '0'],
        [['9876', '1234'], '12186984'],
    ]
    sol = Solution()
    for testcase in testcases:
        testcase, ans = testcase
        result = sol.multiply(*testcase)
        print(f"Input: {testcase}, Output: {result}, Ans: {ans}")
