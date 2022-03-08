"""15
Given an integer array nums,
return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
import typing as t


class Solution:
    def threeSum(self, nums: t.List[int]) -> t.List[t.List[int]]:
        result = set()
        nums.sort()
        if len(nums) < 3:
            return result

        for i in range(len(nums)):
            keep = {}
            target = nums[i]

            for num in nums[(i + 1):]:
                if num in keep:
                    out = (target, num, keep[num])
                    result.add(out)

                keep[0 - (num + target)] = num
        return result


if __name__ == '__main__':
    testcases = [
        [-1,0,1,2,-1,-4],
        [0],
    ]
    answers = [
        [[-1,-1,2],[-1,0,1]],
        [],
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.threeSum(testcase)
        print(f'Input:{testcase}\nOutput: {result}\nAns:{ans}')
