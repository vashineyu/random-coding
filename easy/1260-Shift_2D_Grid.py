"""1260: List shifting
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

- Element at grid[i][j] moves to grid[i][j + 1].
- Element at grid[i][n - 1] moves to grid[i + 1][0].
- Element at grid[m - 1][n - 1] moves to grid[0][0].

Return the 2D grid after applying shift operation k times.
"""
import typing as t


class Solution:
    def shiftGrid(self, grid: t.List[t.List[int]], k: int) -> t.List[t.List[int]]:

        nrows = len(grid)
        ncols = len(grid[0])

        grid = [j for i in grid for j in i]
        total_len = len(grid)
        k = k % total_len
        grid = grid[(total_len - k):] + grid[:(k + total_len)]

        result = []
        index = 0
        for _ in range(nrows):
            cols = []
            for _ in range(ncols):
                cols.append(grid[index])
                index += 1
            result.append(cols)
        return result


if __name__ == '__main__':
    testcases = [
        [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1],
        [[[1], [2], [3], [4], [7], [6], [5]], 23],
    ]
    answers = [
        [[[9, 1, 2], [3, 4, 5], [6, 7, 8]]],
        [[6], [5], [1], [2], [3], [4], [7]],
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.shiftGrid(*testcase)
        print(f'Output={result}, IsCorrect={result==ans}')
