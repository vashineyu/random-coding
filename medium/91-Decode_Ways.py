"""91
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above
  (there may be multiple ways).
For example, "11106" can be mapped into:
* "AAJF" with the grouping (1 1 10 6)
* "KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        strs = [str(i + 1) for i in range(26)]

        result = [0] * len(s)
        result[0] = 1

        for i in range(1, len(s)):
            single = s[i]
            double = s[(i - 1):(i + 1)]
            if single in strs:
                result[i] = result[i - 1]

            if double in strs:
                if i - 2 >= 0:
                    result[i] += result[i - 2]
                else:
                    result[i] += 1
        return result[-1]


if __name__ == '__main__':
    testcases = {
        '12': 2,
        '226': 3,
        '06': 0,
        '106': 1,
    }
    sol = Solution()
    for testcase, ans in testcases.items():
        result = sol.numDecodings(testcase)
        print(f'Input: {testcase}, Output: {result}, IsCorrect:{result==ans}')
