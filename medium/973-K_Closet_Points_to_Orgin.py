"""973
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance

You may return the answer in any order.
The answer is guaranteed to be unique (except for the order that it is in).
"""
import typing as t
from collections import defaultdict


class Solution:
    def kClosest(self, points: t.List[t.List[int]], k: int) -> t.List[t.List[int]]:
        point_distances = defaultdict(list)

        for point in points:
            distance = self.compute_distance(point)
            point_distances[distance].append(point)

        point_distances = {k: v for k, v in sorted(point_distances.items())}
        point_distances = [j for k, v in point_distances.items() for j in v]
        return point_distances[:k]

    def compute_distance(self, point):
        x, y = point
        return (x ** 2 + y ** 2) ** 0.5
