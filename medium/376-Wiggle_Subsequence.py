"""376: greedy method

A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative.
The first difference (if one exists) may be either positive or negative.
A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.
In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences.
The first is not because its first two differences are positive, and the second is not because its last difference is zero.
A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

Given an integer array nums, return the length of the longest wiggle subsequence of nums.
"""
import typing as t

class Solution:
    def wiggleMaxLength(self, nums: t.List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        prev_diff = nums[1] - nums[0]
        current_len = 1 if prev_diff == 0 else 2
        for i in range(2, len(nums)):

            diff = nums[i] - nums[i - 1]
            if (prev_diff >= 0 and diff < 0) or (prev_diff <= 0 and diff > 0):
                current_len += 1
                prev_diff = diff

        return current_len


if __name__ == '__main__':
    testcases = [
        [0, 0],
        [1, 7, 4, 9, 2, 5],
        [126,37,130,225,239,77,235,333,30,69,294,128,163,17,224,229,128,59,205,265,328,259,337,93,354,316,309,67,36,88,133,359,8,335,247,209,279,94,41,62]
    ]
    answers = [
        1,
        6,
        25,
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.wiggleMaxLength(testcase)
        print(f'Output={result}, IsCorrect={result==ans}')
