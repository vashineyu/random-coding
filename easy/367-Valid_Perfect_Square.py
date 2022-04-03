"""367: binary search or simple looping
Given a positive integer num, write a function which
* returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 0
        while True:
            x = i ** 2
            if x == num:
                return True
            if x > num:
                return False
            i += 1
