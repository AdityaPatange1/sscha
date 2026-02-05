"""
Feet: left and right foot volumes in 5D.
"""

from typing import List

from .geometry import Point5D


class Foot:
    """
    A single foot in 5D: box (sole) at the given center.
    """

    def __init__(
        self,
        center: Point5D,
        half_extent_x: float = 0.12,
        half_extent_y: float = 0.05,
        half_extent_z: float = 0.08,
        half_extent_w: float = 0.04,
        half_extent_v: float = 0.04,
    ):
        self.center = center
        self._h = (
            half_extent_x,
            half_extent_y,
            half_extent_z,
            half_extent_w,
            half_extent_v,
        )

    def vertices_5d(self) -> List[Point5D]:
        hx, hy, hz, hw, hv = self._h
        cx, cy, cz, cw, cv = self.center.as_tuple()
        out: List[Point5D] = []
        for ix in (-1, 1):
            for iy in (-1, 1):
                for iz in (-1, 1):
                    for iw in (-1, 1):
                        for iv in (-1, 1):
                            out.append(
                                Point5D(
                                    cx + ix * hx,
                                    cy + iy * hy,
                                    cz + iz * hz,
                                    cw + iw * hw,
                                    cv + iv * hv,
                                )
                            )
        return out


class Feet:
    """
    Pair of feet in 5D: left and right.
    """

    def __init__(self, left_center: Point5D, right_center: Point5D):
        self.left = Foot(left_center)
        self.right = Foot(right_center)

    def vertices_5d(self) -> List[Point5D]:
        return self.left.vertices_5d() + self.right.vertices_5d()

    def left_vertices_5d(self) -> List[Point5D]:
        return self.left.vertices_5d()

    def right_vertices_5d(self) -> List[Point5D]:
        return self.right.vertices_5d()
