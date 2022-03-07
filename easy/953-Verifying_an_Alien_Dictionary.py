"""
In an alien language, surprisingly, they also use English lowercase letters,
but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language,
and the order of the alphabet,
return true if and only if the given words are sorted lexicographically in this alien language.
"""
import typing as t
from itertools import zip_longest


class Solution:
    def isAlienSorted(self, words: t.List[str], order: str) -> bool:
        d = {s: i+1 for i, s in enumerate(order)}
        d[None] = 0

        for i in range(1, len(words)):

            for w1, w2 in zip_longest(*(words[i - 1], words[i])):
                # if the word is different and follow the rule, go to next word
                if d[w1] < d[w2]:
                    break

                # If obey the rule
                if d[w1] > d[w2]:
                    return False

                # otherwise, compare next letter
        return True


if __name__ == '__main__':
    testcases = [
        [["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"],
        [["word","world","row"], "worldabcefghijkmnpqstuvxyz"],
    ]
    answers = [
        True,
        False,
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.isAlienSorted(*testcase)
        print(f'Input: {testcase}\nOutput: {result}, IsCorrect:{result==ans}')
