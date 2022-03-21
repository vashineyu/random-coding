"""763
You are given a string s.
We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order,
the resultant string should be s.

Return a list of integers representing the size of these parts.
"""
import typing as t
from collections import defaultdict


class Solution:
    def partitionLabels(self, s: str) -> t.List[int]:
        strmap = defaultdict(list)

        # Keep position of each character
        for i, char in enumerate(s):
            strmap[char].append(i)

        partitions = []
        last_index = 0  # record the farest position of visited characters
        counter = 0
        for i, char in enumerate(s):
            last_index = max(last_index, strmap[char][-1])
            counter += 1
            if last_index == i:  # when we meet the farest position of visited char so far -> record
                partitions.append(counter)
                counter = 0
        return partitions
