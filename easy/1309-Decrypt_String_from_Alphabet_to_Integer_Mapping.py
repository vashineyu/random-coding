"""1309
You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:
-  Characters ('a' to 'i') are represented by ('1' to '9') respectively.
-  Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.

Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.
"""
from string import ascii_lowercase


class Solution:
    def freqAlphabets(self, s: str) -> str:
        strmap = {str(i + 1): char for i, char in enumerate(ascii_lowercase)}

        result = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                digit = s[(i - 2): i]
                i -= 3
            else:
                digit = s[i]
                i -= 1
            result.append(strmap[digit])
        result = result[::-1]
        result = ''.join(i for i in result)
        return result


if __name__ == '__main__':
    testcases = {
        "10#11#12": "jkab",
        "1326#": "acz",
    }
    sol = Solution()
    for testcase, ans in testcases.items():
        result = sol.freqAlphabets(testcase)
        print(f"Input: {testcase}, Output: {result}, Ans: {ans}")
