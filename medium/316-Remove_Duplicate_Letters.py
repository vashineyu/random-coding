"""316
Given a string s, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occur = {c: i for i, c in enumerate(s)}
        visited_char = set()

        result = ['']
        for i, char in enumerate(s):
            if char in visited_char:
                continue

            while char < result[-1] and last_occur[result[-1]] > i:
                visited_char.remove(result.pop())

            result.append(char)
            visited_char.add(char)
        return ''.join(result[1:])


if __name__ == '__main__':
    testcases = {
        'bcabc': 'abc',
        'cbacdcbc': 'acdb',
    }
    sol = Solution()
    for testcase, ans in testcases.items():
        result = sol.removeDuplicateLetters(testcase)
        print(f'Input: {testcase}, Output: {result}, IsCorrect: {result==ans}')
