"""
You are given a string s, and an array of pairs of indices in the string pairs
  where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.
"""
import typing as t
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.paths = list(range(n))

    def union(self, x, y):
        self.paths[self.find(x)] = self.find(y)

    def find(self, x):
        if x != self.paths[x]:
            self.paths[x] = self.find(self.paths[x])
        return self.paths[x]


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        if len(pairs) == 0:
            return s

        result = []
        m = defaultdict(list)

        uf = UnionFind(len(s))
        for x, y in pairs:
            uf.union(x, y)
            print(uf.paths)

        for i in range(len(s)):
            m[uf.find(i)].append(s[i])

        for key in m.keys():
            m[key].sort(reverse=True)

        for i in range(len(s)):
            result.append(m[uf.find(i)].pop())

        return ''.join(result)


if __name__ == '__main__':
    testcases = [
        ["udyyek", [[3, 3], [3, 0], [5, 1], [3, 1], [3, 4], [3, 5]]],
        ["pwqlmqm", [[5, 3] ,[3, 0], [5, 1], [1, 1], [1, 5], [3, 0], [0, 2]]],
        ["dcab", [[0, 3], [1, 2], [0, 2]]],
        ["cba", [[0, 1] ,[1, 2]]],
        ["yhiihxbordwyjybyt", [
            [9, 1], [5, 11], [9, 7], [2, 7], [14, 16], [6, 16] ,[0, 5], [12,9],
            [6, 5], [9, 10], [4, 7], [3, 2], [10, 1], [3, 15], [12, 4], [10, 10], [15, 12]]],
    ]
    answers = [
        'deykuy',
        'lpqqmwm',
        "abcd",
        "abc",
        "bdhhibtirjoxwyyyy",
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.smallestStringWithSwaps(*testcase)
        print(f'Input: {testcase[0]}, Output: {result}, IsCorrect={ans==result}')
