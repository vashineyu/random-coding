"""299, counter
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is.
When your friend makes a guess, you provide a hint with the following info:

- The number of "bulls", which are digits in the guess that are in the correct position.
- The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position.
  Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
- Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.
"""
from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        secret_ = defaultdict(int)
        guess_ = defaultdict(int)

        bulls = 0
        for num1, num2 in zip(secret, guess):
            if num1 == num2:
                bulls += 1
            else:
                secret_[num1] += 1
                guess_[num2] += 1

        cows = 0
        for k, v in guess_.items():
            if k in secret_:
                cows += min(secret_[k], v)

        result = f'{bulls}A{cows}B'
        return result


if __name__ == '__main__':
    testcases = [
        ["1807", "7810"],
        ["1123", "0111"],
    ]
    answers = [
        "1A3B",
        "1A1B",
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.getHint(*testcase)
        print(f'Output: {result}, IsCorrect: {ans==result}')
