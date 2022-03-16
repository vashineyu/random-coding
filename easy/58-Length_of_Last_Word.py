"""58
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.rstrip().split(' ')
        return len(words[-1])


if __name__ == '__main__':
    testcases = {
        "Hello World": 5,
        "   fly me   to   the moon  ": 4,
        "luffy is still joyboy": 6
    }
    sol = Solution()
    for testcase, ans in testcases.items():
        result = sol.lengthOfLastWord(testcase)
        print(f'Input: {testcase}, Output: {result}, IsCorrect: {ans==result}')
