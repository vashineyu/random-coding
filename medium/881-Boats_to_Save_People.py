"""881: Two indexes
You are given an array people where people[i] is the weight of the ith person, 
and an infinite number of boats where each boat can carry a maximum weight of limit.

Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
"""
import typing as t


class Solution:
    def numRescueBoats(self, people: t.List[int], limit: int) -> int:
        people.sort(reverse=True)

        n = len(people)
        i = 0
        j = n - 1

        rounds = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                i += 1
            rounds += 1
        return rounds
