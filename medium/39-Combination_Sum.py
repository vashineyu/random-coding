"""39
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.

You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""
import typing as t


class Solution:
    def combinationSum(
        self,
        candidates: t.List[int], target: int
    ) -> t.List[t.List[int]]:
        def helper(target, path):
            if target == 0:
                result.append(path)

            for candidate in candidates:
                if candidate > target:
                    break

                if path and candidate < path[-1]:
                    continue

                helper(
                    target - candidate,
                    path + [candidate]
                )

        candidates.sort()
        result = []
        helper(target, [])
        return result


if __name__ == '__main__':
    testcases = [
        [[2, 3, 6, 7], 7],
        [[2, 3, 5], 8]
    ]
    answers = [
        [[2, 2, 3], [7]],
        [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.combinationSum(*testcase)
        print(f'Input:{testcase}\nOutput:{result}\nIsCorrect:{result==ans}')
