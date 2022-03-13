"""150
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid.
That means the expression would always evaluate to a result, and there will not be any division by zero operation.

"""
import typing as t


class Solution:
    def evalRPN(self, tokens: t.List[str]) -> int:
        available_ops = ['+', '-', '*', '/']

        stack = []
        for token in tokens:
            if token not in available_ops:
                stack.append(int(token))
            else:
                y = stack.pop()
                x = stack.pop()

                # v = int(eval(f'{x} {token} {y}'))  # It is more simple, but seems slower...
                if token == '+':
                    v = x + y
                elif token == '-':
                    v = x - y
                elif token == '*':
                    v = x * y
                elif token == '/':
                    v = int(x / y)
                else:
                    assert False, f'Operation {token} not found'
                stack.append(v)

        return stack[-1]


if __name__ == '__main__':
    testcases = [
        ["2", "1", "+", "3", "*"],
        ["4", "13", "5", "/", "+"],
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
    ]
    answers = [
        9,
        6,
        22,
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.evalRPN(testcase)
        print(f'Input: {testcase}, Output: {result}, Answers: {ans}')
