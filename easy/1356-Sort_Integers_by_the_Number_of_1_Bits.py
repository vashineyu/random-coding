"""
You are given an integer array arr.
Sort the integers in the array in ascending order
- by the number of 1's in their binary representation, and
- in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the array after sorting it.
"""
import typing as t


class Solution:
    def sortByBits(self, arr: t.List[int]) -> t.List[int]:
        arr.sort(key=lambda x: (self.nbit(x), x))
        return arr

    def nbit(self, x):
        x = bin(x)[2:]
        b = 0
        for s in x:
            b += int(s)
        return b


if __name__ == '__main__':
    testcases = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8],
        [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],
    ]
    answers = [
        [0, 1, 2, 4, 8, 3, 5, 6, 7],
        [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.sortByBits(testcase)
        print(f'Input: {testcase}\nOutput: {result}\nIsCorrect:{result==ans}')
