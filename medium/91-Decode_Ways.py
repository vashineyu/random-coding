"""91
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
