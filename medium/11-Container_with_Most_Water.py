"""11: two indexes
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""
import typing as t


class Solution:
    def maxArea(self, height: t.List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_area = 0
        while left < right:
            l_height = height[left]
            r_height = height[right]
            area = min(l_height, r_height) * (right - left)
            max_area = max(area, max_area)

            if l_height <= r_height:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == '__main__':
    testcases = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
        [1, 2, 4, 3],
    ]
    anses = [
        49,
        4,
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, anses):
        result = sol.maxArea(testcase)
        print(f"result: {result}, ans: {ans}")
