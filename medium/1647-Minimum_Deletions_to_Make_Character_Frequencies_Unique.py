"""1647: stack
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string.
For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.
"""
from collections import defaultdict


class Solution:
    def minDeletions(self, s: str) -> int:

        strmap = defaultdict(int)
        for char in s:
            strmap[char] += 1

        occupied = [0] * (max(strmap.values()) + 1)
        for k, v in strmap.items():
            occupied[v] += 1

        to_del = 0
        prev_slot = []
        for pos in range(1, len(occupied[1:]) + 1):
            value = occupied[pos]
            if value == 0:
                prev_slot.append(pos)

            while value > 1:
                if len(prev_slot) > 0:
                    pslot = prev_slot.pop()
                else:
                    pslot = 0
                diff = pos - pslot
                to_del += diff
                value -= 1

        return to_del


if __name__ == '__main__':
    testcases = [
        'aab',
        'aaabbbcc',
        'ceabaacb',
    ]
    answers = [
        0,
        2,
        2,
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.minDeletions(testcase)
        print(f'Input={testcase}, Result={result}, IsCorrect={ans==result}')
