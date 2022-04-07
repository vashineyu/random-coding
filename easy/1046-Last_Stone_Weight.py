"""1046: heapq
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
Suppose the heaviest two stones have weights x and y with x <= y.

The result of this smash is:
- If x == y, both stones are destroyed, and
- If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone.
If there are no stones left, return 0.
"""
import typing as t
import heapq


class Solution:
    def lastStoneWeight(self, stones: t.List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x - y < 0:
                heapq.heappush(stones, x - y)

        if len(stones) > 0:
            return -stones[0]
        return 0
