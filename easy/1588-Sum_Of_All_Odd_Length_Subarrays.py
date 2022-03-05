"""
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.
A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.
"""
import typing as t


class Solution:
    def sumOddLengthSubarrays(self, arr: t.List[int]) -> int:
        n = len(arr)

        total = 0
        for i, num in enumerate(arr):
            for arr_length in range(1, n - i + 1, 2):
                subarray = arr[i:(i + arr_length)]
                total += sum(subarray)
        return total


if __name__ == '__main__':
    testcases = [
        [1, 4, 2, 5, 3],
        [1, 2],
        [10, 11, 12],
    ]
    answers = [
        58,
        3,
        66,
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.sumOddLengthSubarrays(testcase)
        print(f'Input: {testcase}, Output: {result}, Ans={ans}')
