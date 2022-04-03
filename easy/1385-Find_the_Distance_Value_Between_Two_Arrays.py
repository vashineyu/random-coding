"""1385: array operation
Given two integer arrays arr1 and arr2, and the integer d,
return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
"""
import typing as t
import numpy as np


class Solution:
    def findTheDistanceValue(
        self,
        arr1: t.List[int],
        arr2: t.List[int],
        d: int
    ) -> int:

        arr1 = np.asarray(arr1)
        arr2 = np.asarray(arr2)

        diff_mat = np.abs(arr1 - arr2.reshape((-1, 1)))
        colmin = diff_mat.min(axis=0)
        result = sum(colmin > d)
        return result
