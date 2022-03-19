"""54
Given an m x n matrix, return all elements of the matrix in spiral order.

Key:
1. action-order: right -> down -> left -> top -> right -> ...
2. keep a visited_map to assure when to change action (switch to next action)
"""
import typing as t


class Solution:
    def spiralOrder(self, matrix: t.List[t.List[int]]) -> t.List[int]:
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        visited = [[0] * n_cols for _ in range(n_rows)]
        action_order = [
            (0, 1),  # right
            (1, 0),  # down
            (0, -1),  # left
            (-1, 0),  # up
        ]

        result = []
        current_action = 0
        i_row, i_col = 0, 0
        counter = 0
        while counter < (n_rows * n_cols):
            visited[i_row][i_col] = 1
            counter += 1
            result.append(matrix[i_row][i_col])

            action_to_row, action_to_col = action_order[current_action]
            ne_row = i_row + action_to_row
            ne_col = i_col + action_to_col
            if ne_row >= 0 and ne_row < n_rows and ne_col >= 0 and ne_col < n_cols and not visited[ne_row][ne_col]:
                i_row = ne_row
                i_col = ne_col
            else:
                current_action = (current_action + 1) % 4
                action_to_row, action_to_col = action_order[current_action]
                i_row = i_row + action_to_row
                i_col = i_col + action_to_col
        return result


if __name__ == '__main__':
    testcases = [
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]],
    ]
    answers = [
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        [1, 2, 3, 4, 8, 12, 16, 20, 19, 18, 17, 13, 9, 5, 6, 7, 11, 15, 14, 10]
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.spiralOrder(testcase)
        print(f'Output={result}, IsCorrect:{result==ans}')
