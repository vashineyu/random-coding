"""888: hash two sum
Alice and Bob have a different total number of candies.
You are given two integer arrays aliceSizes and bobSizes where
  - aliceSizes[i] is the number of candies of the ith box of candy that Alice has and
  - bobSizes[j] is the number of candies of the jth box of candy that Bob has.

Since they are friends, they would like to exchange one candy box each so that after the exchange,
  they both have the same total amount of candy.
The total amount of candy a person has is the sum of the number of candies in each box they have.

Return an integer array answer where answer[0] is the number of candies in the box that Alice must exchange,
and answer[1] is the number of candies in the box that Bob must exchange.

If there are multiple answers, you may return any one of them.

It is guaranteed that at least one answer exists.

--- Thought
According to the rule: A - i + j = B - j + i
Hence, (A - B) / 2 = i - j
Then, it becomes a two-sum problem.
"""
import typing as t


class Solution:
    def fairCandySwap(
        self,
        aliceSizes: t.List[int],
        bobSizes: t.List[int]
    ) -> t.List[int]:

        A = sum(aliceSizes)
        B = sum(bobSizes)

        target_diff = (A - B) / 2
        hashmap = {}
        for a in aliceSizes:
            d = a - target_diff
            hashmap[d] = a

        for b in bobSizes:
            if b in hashmap:
                return [hashmap[b], b]


if __name__ == '__main__':
    testcases = [
        [[1, 1], [2, 2]],
        [[1, 2], [2, 3]],
        [[2], [1, 3]],
    ]
    answers = [
        [1, 2],
        [1, 2],
        [2, 3],
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.fairCandySwap(*testcase)
        print(f'Output: {result}, IsCorrect:{ans==result}')
