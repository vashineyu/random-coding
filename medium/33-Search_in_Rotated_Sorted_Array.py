"""33
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
 such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""
import typing as t


class Solution:
    def search(self, nums: t.List[int], target: int) -> int:
        length = len(nums)
        i, j = 0, length - 1

        while i <= j:
            num_i, num_j = nums[i], nums[j]
            # print(i, num_i, j, num_j)
            if num_i == target:
                return i

            if num_j == target:
                return j

            if i >= j - 1:
                return -1

            if nums[j - 1] < num_j:
                j -= 1

            if nums[i + 1] > num_i:
                i += 1

        return -1


if __name__ == '__main__':
    testcases = [
        [[4, 5, 6, 7, 0, 1, 2], 4],
        [[4, 5, 6, 7, 0, 1, 2], 6],
        [[4, 5, 6, 7, 0, 1, 2], 7],
        [[4, 5, 6, 7, 0, 1, 2], 0],
        [[4, 5, 6, 7, 0, 1, 2], 2],
        [[4, 5, 6, 7, 0, 1, 2], 3],
        [[1], 0],
        [[1], 1],
        [[0, 1], 0],
        [[0, 1], 1],
        [[0, 1], 2],
        [[1, 3, 5], 3],
    ]
    answers = [0, 2, 3, 4, 6, -1, -1, 0, 0, 1, -1, 1]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.search(*testcase)
        print(f'Output={result},\tIsCorrect={result==ans}')
