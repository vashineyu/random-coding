"""503
"""
import typing as t


class Solution:
    def nextGreaterElements(self, nums: t.List[int]) -> t.List[int]:
        return self.sol2(nums)

    def sol1(self, nums: t.List[int]) -> t.List[int]:
        # Brute-Force (Accepted)
        n = len(nums)

        result = [-1] * n
        for i in range(n):
            num = nums[i]
            for num_j in nums[(i + 1):] + nums[:i]:
                if num_j > num:
                    result[i] = num_j
                    break
        return result

    def sol2(self, nums: t.List[int]) -> t.List[int]:
        # Stacking
        n = len(nums)
        result = [-1] * n

        stack = []
        for i in range(n * 2):  # loop twice for the circular condition
            i = i % n
            num = nums[i]
            while stack and nums[stack[-1]] < num:
                prev_index = stack.pop()
                result[prev_index] = num
            stack.append(i)
        return result


if __name__ == '__main__':
    testcases = [
        [1, 2, 1],
        [1, 2, 3, 4, 3],
        [1, 2, 3, 2, 1],
        [1, 2, 3, 4, 5, 6, 5, 4, 5, 1, 2, 3],
    ]
    answers = [
        [2, -1, 2],
        [2, 3, 4, -1, 4],
        [2, 3, -1, 3, 2],
        [2, 3, 4, 5, 6, -1, 6, 5, 6, 2, 3, 4],
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.nextGreaterElements(testcase)
        print(f'Output: {result}, IsCorrect: {result==ans}')
