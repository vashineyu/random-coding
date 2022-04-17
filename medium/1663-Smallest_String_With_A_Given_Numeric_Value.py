"""1663
The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet,
so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.

The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values.
For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.

You are given two integers n and k. Return the lexicographically smallest string with length equal to n and numeric value equal to k.

Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order,
that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.
"""
import string


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        strmap = {(i + 1): c for i, c in enumerate(string.ascii_lowercase)}

        result = []
        while n > 0:
            # If k > 26 (z), watch out how many slots (n) we need to keep
            i = min(k - n + 1, 26)
            result.append(strmap[i])

            n -= 1
            k -= i

        # result.sort()  # lexicographically smallest
        result = ''.join(i for i in result[::-1])
        return result


if __name__ == '__main__':
    testcases = [
        [3, 27],
        [5, 73],
    ]
    answers = [
        'aay',
        'aaszz',
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.getSmallestString(*testcase)
        print(f'Input: {testcase}, Output: {result}, IsCorrect: {ans==result}')