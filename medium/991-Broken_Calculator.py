"""
There is a broken calculator that has the integer startValue on its display initially.
In one operation, you can:
* multiply the number on display by 2, or
* subtract 1 from the number on display.

Given two integers startValue and target,
return the minimum number of operations needed to display target on the calculator.
"""


class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:

        n_ops = 0
        while target > startValue:
            n_ops += 1
            if target % 2 == 0:  # is even
                target = target // 2
            else:
                target += 1
        return n_ops + startValue - target
