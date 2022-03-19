"""895
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

- FreqStack() constructs an empty frequency stack.
- void push(int val) pushes an integer val onto the top of the stack.
- int pop() removes and returns the most frequent element in the stack.
    - If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
"""
from collections import defaultdict


class FreqStack:
    """
    Keep 2 dictionaries,
        - one for val current state (main_storage)
        - one for occurance of each state (occurance)

    For main storage, m[val] + 1 when push, m[val] - 1 when pop
    For occurance, o[freq].append(val) when push, o[freq].remove(val) when pop
    """
    def __init__(self):
        self.main_storage = defaultdict(int)  # keep val current state
        self.occurance = defaultdict(list)  # keep freq history

    def push(self, val: int) -> None:
        self.main_storage[val] += 1
        self.occurance[self.main_storage[val]].append(val)

    def pop(self) -> int:
        k = max(self.occurance.keys())
        val = self.occurance[k].pop()
        self.main_storage[val] -= 1

        if len(self.occurance[k]) == 0:
            del self.occurance[k]
        return val

