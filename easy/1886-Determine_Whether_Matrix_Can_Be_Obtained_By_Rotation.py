"""
Given two n x n binary matrices mat and target,
return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.
"""
import typing as t
import numpy as np


class Solution:
    def findRotation(self, mat: t.List[t.List[int]], target: t.List[t.List[int]]) -> bool:
        mat = np.asarray(mat)
        target = np.asarray(target)

        for _ in range(4):
            if np.all(mat == target):
                return True
            mat = np.rot90(mat)

        return False


if __name__ == '__main__':
    testcases = [
        [
            [[0, 0], [1, 1]],
            [[0, 1], [1, 0]]
        ],
        [
            [[1, 1], [0, 0]],
            [[0, 1], [0, 1]]
        ],
    ]
    answers = [
        False,
        True,
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.findRotation(*testcase)
        print(f'Output: {result}, IsCorrent: {result==ans}')
