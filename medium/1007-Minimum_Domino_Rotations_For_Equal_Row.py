"""
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino.
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same,
or all the values in bottoms are the same.

If it cannot be done, return -1.
"""
import typing as t


class Solution:
    def minDominoRotations(self, tops: t.List[int], bottoms: t.List[int]) -> int:
        candidates = (tops[0], bottoms[0])  # one row must fit

        for x in candidates:
            if all(x in pair for pair in zip(tops, bottoms)):
                return len(tops) - max(tops.count(x), bottoms.count(x))

        return -1


if __name__ == '__main__':
    testcases = [
        [
            [3, 5, 3, 5, 3, 5],
            [3, 3, 3, 3, 3, 4],
        ],
        [
            [3, 5, 3, 5, 3, 5],
            [3, 3, 3, 3, 3, 3],
        ],
        [
            [3, 5, 3, 5, 3, 5, 3],
            [3, 3, 2, 3, 4, 3, 3],
        ],
        [
            [1, 2, 1, 1, 1, 2, 2, 2],
            [2, 1, 2, 2, 2, 2, 2, 2],
        ]
    ]
    answers = [
        -1,
        0,
        2,
        1,
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.minDominoRotations(*testcase)
        print(f'Result={result}, IsCorrect={result==ans}')
