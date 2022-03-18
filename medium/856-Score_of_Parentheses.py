"""856
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:
- "()" has score 1.
- AB has score A + B, where A and B are balanced parentheses strings.
- (A) has score 2 * A, where A is a balanced parentheses string.
"""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = [0]
        for char in s:
            if char == '(':
                stack.append(0)
            else:  # ')'
                value = stack.pop()
                stack[-1] += max(2 * value, 1)
        return stack[0]


if __name__ == '__main__':
    testcases = {
        '()': 1,
        '()()': 2,
        '(())': 2,
        '(()(()))': 6,
        '((()()()))()': 13,
        '(((()()()))())': 26,
    }
    sol = Solution()
    for testcase, ans in testcases.items():
        result = sol.scoreOfParentheses(testcase)
        print(f'Input: {testcase}, Output={result}, IsCorrect:{result==ans}')
