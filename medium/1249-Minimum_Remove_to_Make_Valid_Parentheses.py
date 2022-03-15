"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:
- It is the empty string, contains only lowercase characters, or
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        parenthese_stack = []
        unpair = []

        for i, char in enumerate(s):
            if char == '(':
                parenthese_stack.append(i)

            if char == ')':
                if len(parenthese_stack) > 0:
                    parenthese_stack.pop()
                else:
                    unpair.append(i)
        unpair = parenthese_stack + unpair
        result = ''.join(c for i, c in enumerate(s) if i not in unpair)
        return result
