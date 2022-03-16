"""946
Given two integer arrays pushed and popped each with distinct values,
return true if this could have been the result of a sequence of push and pop operations on an initially empty stack,
  or false otherwise.
"""
import typing as t


class Solution:
    def validateStackSequences(self, pushed: t.List[int], popped: t.List[int]) -> bool:
        if len(pushed) == 0:
            return True

        pushed = pushed[::-1]
        stack = []
        i = 0

        while pushed:
            if len(stack) > 0 and popped[i] == stack[-1]:
                stack.pop()
                i += 1
            else:
                latest = pushed.pop()
                stack.append(latest)

        if len(stack) == 0:
            return True
        return stack == popped[i:][::-1]


if __name__ == '__main__':
    testcases = [
        [
            [1, 2, 3, 4, 5, 6, 7],
            [4, 6, 5, 7, 3, 2, 1],
        ]
    ]
    answers = [
        True
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.validateStackSequences(*testcase)
        print(f'Output: {result}')
