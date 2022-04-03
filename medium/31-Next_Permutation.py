"""31: Backtracking + indexing
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order,
 then the next permutation of that array is the permutation that follows it in the sorted container.

If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
"""
import typing as t
from collections import defaultdict


class Solution:
    def nextPermutation(self, nums: t.List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return nums

        record = defaultdict(list)
        for i in range(n - 1):
            # back-tracking
            num = nums[n - i - 1]
            num_prev = nums[n - i - 2]
            record[num].append(n - i - 1)
            if num > num_prev:
                diffs = [x - num_prev for x in record.keys()]
                diff = min([x for x in diffs if x > 0])
                target = num_prev + diff
                target_pos = record[target][0]
                nums[n - i - 2], nums[target_pos] = target, num_prev
                nums[(n - i - 1):] = sorted(nums[(n - i - 1):])
                return nums
        # if nothing happend before (is already max, go to first permutation)
        nums.reverse()
        return nums


if __name__ == '__main__':
    testcases = [
        [1, 2, 3, 4],
        [1, 2, 4, 3],
        [1, 3, 2, 4],
        [1, 3, 4, 2],
        [1, 4, 3, 2],
        [1, 2],
        [2, 1],
        [2, 3, 1],
    ]
    sol = Solution()
    for testcase in testcases:
        result = sol.nextPermutation(testcase)
        print(f'Output: {result}')
