"""289: inplace modification, indexing
According to Wikipedia's article: "The Game of Life, also known simply as Life,
  is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state:
  - live (represented by a 1) or
  - dead (represented by a 0).

Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state,
  where births and deaths occur simultaneously.

Given the current state of the m x n grid board, return the next state.
"""
import typing as t
import numpy as np


class Solution:
    def gameOfLife(self, board: t.List[t.List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_copy = np.array(board)
        nrows, ncols = board_copy.shape

        for row in range(nrows):
            for col in range(ncols):
                outcome = self.cell_is_live_or_death(board_copy, row, col)
                board[row][col] = int(outcome)

        return board

    def cell_is_live_or_death(self, board, row, col):

        current = board[row, col]
        top = max(0, row - 1)
        left = max(0, col - 1)
        count_live = (board[top:(row + 2), left:(col + 2)] > 0).sum()

        if current:
            # current is live cell
            count_live -= 1
            return count_live in (2, 3)
        else:
            # current is dead cell
            return count_live == 3


if __name__ == '__main__':
    testcases = [
        [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
    ]
    answers = [
        [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]],
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.gameOfLife(testcase)
        print(f'Result={result}, IsCorrect={ans==result}')
