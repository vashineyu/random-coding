"""74
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:

  - Integers in each row are sorted from left to right.
  - The first integer of each row is greater than the last integer of the previous row.
"""
import typing as t


class Solution:
  def searchMatrix(self, matrix: t.List[t.List[int]], target: int) -> bool:
    nrows = len(matrix)
    for row in range(nrows):
      if target > max(matrix[row]):
        continue

      if target in matrix[row]:
        return True

      if min(matrix[row]) > target:
        return False


if __name__ == '__main__':
  testcases = [
    [
      [[1, 3, 5, 7],
       [10, 11, 16, 20],
       [23, 30, 34, 60]],
      3,
    ],
  ]
  answers = [
    True,
  ]
  sol = Solution()
  for testcase, ans in zip(testcases, answers):
    result = sol.searchMatrix(*testcase)
    print(f'Output: {result}, Ans: {ans}')
