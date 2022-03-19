"""384
Given an integer array nums, design an algorithm to randomly shuffle the array.
All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

- Solution(int[] nums) Initializes the object with the integer array nums.
- int[] reset() Resets the array to its original configuration and returns it.
- int[] shuffle() Returns a random shuffling of the array.

(Not allow to use random.shuffle and deepcopy)
"""
import typing as t
import numpy as np


class Solution:
    def __init__(self, nums: t.List[int]):
        self.nums = nums

    def reset(self) -> t.List[int]:
        return self.nums

    def shuffle(self) -> t.List[int]:
        order = np.random.choice(
            range(len(self.nums)),
            len(self.nums),
            replace=False
        )
        x = np.take(self.nums, order).tolist()
        return x
