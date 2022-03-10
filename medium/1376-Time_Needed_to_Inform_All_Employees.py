"""1376
A company has n employees with a unique ID for each employee from 0 to n - 1.
The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, 
  manager[headID] = -1.
Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news.
He will inform his direct subordinates, and they will inform their subordinates,
  and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates
  (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.
"""
import typing as t
from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: t.List[int], informTime: t.List[int]) -> int:
        def helper(employee, path):
            if informTime[employee] == 0:
                t = sum([informTime[p] for p in path])
                times.append(t)

            for e in contact[employee]:
                helper(e, path + [e])

        contact = defaultdict(list)
        for i, m in enumerate(manager):
            contact[m].append(i)
        times = []
        helper(headID, [headID])
        return max(times)


if __name__ == '__main__':
    testcases = [
        [6, 2, [2, 2, -1, 2, 2, 3, 3], [0, 0, 1, 3, 0, 0, 0]],
        [7, 6, [1, 2, 3, 4, 5, 6, -1], [0, 6, 5, 4, 3, 2, 1]],
    ]
    answers = [
        4,
        21,
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.numOfMinutes(*testcase)
        print(f'Result: {result}, Ans={ans}')
