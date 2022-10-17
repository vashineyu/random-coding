"""1832: set, string
A pangram is a sentence where every letter of the English alphabet
  appears at least once.

Given a string sentence containing only lowercase English letters,
return true if sentence is a pangram, or false otherwise.
"""

from string import ascii_lowercase


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        pangram = set(list(ascii_lowercase))
        letter_set_of_sentence = set(sorted(sentence))
        return len(pangram - letter_set_of_sentence) == 0
