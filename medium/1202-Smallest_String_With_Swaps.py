"""
You are given a string s, and an array of pairs of indices in the string pairs
  where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.
"""
import typing as t
from collections import defaultdict


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: t.List[t.List[int]]) -> str:
        if len(pairs) == 0:
            return s

        for pair in pairs:
            pair.sort()
        pairs.sort(key=lambda x:x[0])

        paths = defaultdict(set)
        for pair in pairs:
            v1, v2 = min(pair), max(pair)
            if v2 in paths:
                paths[v2].add(v1)
            else:
                paths[v1].add(v1)
                paths[v1].add(v2)

        p = []
        while len(paths) > 0:
            has_union = False
            pkeys = list(paths.keys())
            k1 = pkeys[0]
            v1 = paths[k1]
            for k2 in pkeys[1:]:
                v2 = paths[k2]
                if len(v1 & v2) > 0:
                    has_union = True
                    v1 = v1 | v2
                    paths.pop(k2)
            paths.pop(k1)
            if has_union:
                paths[k1] = v1
            else:
                v1 = sorted(v1)
                p.append(v1)

        strings = [None] * len(s)
        for path in p:
            string = [s[i] for i in path]
            string.sort()
            for i, j in enumerate(path):
                strings[j] = string[i]

        for i, char in enumerate(strings):
            if char is None:
                strings[i] = s[i]
        return ''.join(i for i in strings)


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
