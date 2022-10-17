class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        s = list(palindrome)
        if len(s) == 1:
            return ''

        for i in range(len(s) // 2):
            if s[i] > 'a':
                s[i] = 'a'
                return ''.join(s)

        s[-1] = 'b'
        return ''.join(s)


if __name__ == '__main__':
    testcases = [
        'abccba',
        'a',
        'aaabaaa',
    ]
    answers = [
        'aaccba',
        '',
        'aaabaab'
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.breakPalindrome(testcase)
        print(f'Input: {testcase}, Output: {result}, IsCorrect={result==ans}')
