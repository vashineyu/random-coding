"""
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].

Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
"""
import typing as t


class Solution:
    def addToArrayForm(self, num: t.List[int], k: int) -> t.List[int]:
        num1 = ''.join(str(i) for i in num)
        output = int(num1) + k

        output = [i for i in str(output)]
        return output


if __name__ == '__main__':
    testcases = [
        [[1, 2, 0, 0], 34],
        [[2, 7, 4], 181],
    ]
    answers = [
        [1, 2, 3, 4],
        [4, 5, 5],
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.addToArrayForm(*testcase)
        print(f'Input: {testcase}, IsCorrect: {result==ans}')
