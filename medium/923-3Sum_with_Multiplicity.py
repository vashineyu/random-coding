"""923: 3Sum + combinations
Given an integer array arr, and an integer target, return the number of tuples i, j, k
  such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.
"""
import typing as t
from math import factorial
from collections import defaultdict


class Solution:
    def threeSumMulti(self, arr: t.List[int], target: int) -> int:

        record = set()
        digit_counts = defaultdict(int)
        for i, num1 in enumerate(arr):
            digit_counts[num1] += 1
            target_num = target - num1
            hashmap = {}
            for num2 in arr[(i + 1):]:
                if (num2 not in hashmap):
                    hashmap[target_num - num2] = num2
                else:
                    pair = [num1, num2, target_num - num2]
                    pair.sort()
                    record.add(tuple(pair))

        total_counts = 0
        for pair in record:
            nmap = defaultdict(int)
            for digit in pair:
                nmap[digit] += 1

            count = 1
            for digit, m in nmap.items():
                n = digit_counts[digit]
                count *= self.combinations(n, m)
            total_counts += count

        _, total_counts = divmod(total_counts, 10 ** 9 + 7)
        return total_counts

    @staticmethod
    def combinations(n, m):
        return factorial(n) // (factorial(n - m) * factorial(m))


if __name__ == '__main__':
    testcases = [
        [[3, 3, 3, 3, 4], 9],
        [[1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8],
        [[1, 1, 2, 2, 2, 2], 5],
    ]
    answers = [
        4,
        20,
        12,
    ]
    sol = Solution()
    for testcase in testcases:
        result = sol.threeSumMulti(*testcase)
        print(f'Output={result}')
