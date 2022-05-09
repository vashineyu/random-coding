"""1122: custom sorting fn
Given two arrays arr1 and arr2, the elements of arr2 are distinct,
 and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
"""
import typing as t


class Solution:
    def relativeSortArray(
        self, arr1: t.List[int],
        arr2: t.List[int]
    ) -> t.List[int]:
        order = {}
        for i, num in enumerate(arr2):
            order[num] = i

        def fn_sort(num):
            if num in order:
                return order[num]
            return num + 1e+4

        arr1.sort(key=fn_sort)
        return arr1
