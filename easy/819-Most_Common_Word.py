"""819: Regular expression + counting
Given a string paragraph and a string array of the banned words banned,
return the most frequent word that is not banned.

It is guaranteed there is at least one word that is not banned,
and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.
"""
import typing as t
import re
from collections import defaultdict


class Solution:
    def mostCommonWord(self, paragraph: str, banned: t.List[str]) -> str:

        banned = [char.lower() for char in banned]

        word_counter = defaultdict(int)
        for word in re.findall(string=paragraph, pattern='\w+'):
            word = word.lower()
            if word not in banned:
                word_counter[word] += 1

        counter_word = {v: k for k, v in word_counter.items()}
        max_count = max(counter_word)
        return counter_word[max_count]


if __name__ == '__main__':
    testcases = [
        ["Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]],
    ]
    answers = [
        'ball'
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.mostCommonWord(*testcase)
        print(f'Output: {result}, IsCorrect: {ans==result}')
