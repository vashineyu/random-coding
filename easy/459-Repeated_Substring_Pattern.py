"""459
Given a string s,
check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n == 1:
            return False

        pattern = ''
        for i in range(n // 2):
            pattern += s[i]
            if len(set(s.split(pattern))) == 1:
                return True
        return False


if __name__ == '__main__':
    testcases = {
        'abab': True,
        'aba': False,
        'abcabcabcabc': True,
        'a': False,
        'ab': False,
    }
    sol = Solution()
    for testcase, ans in testcases.items():
        result = sol.repeatedSubstringPattern(testcase)
        print(f'Input: {testcase}, Output: {result}, IsCorrect: {result==ans}')
