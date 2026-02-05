"""
Head: upper 5D volume of Sscha. A 5D box or ellipsoid-like region.
"""

from typing import List

from .geometry import Point5D, Vector5D


class Head:
    """
    Head in 5D: axis-aligned box (or bounding volume) for the skull.
    """

    def __init__(
        self,
        center: Point5D,
        half_extent_x: float = 0.4,
        half_extent_y: float = 0.4,
        half_extent_z: float = 0.45,
        half_extent_w: float = 0.1,
        half_extent_v: float = 0.1,
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
        """All 32 vertices of the 5D head box."""
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

    def center_point(self) -> Point5D:
        return self.center

    def front_center(self, forward: Vector5D) -> Point5D:
        """Center of the front face (for face attachment)."""
        return self.center + forward.scale(self._h[0])

    def bottom_center(self, down: Vector5D) -> Point5D:
        """Center of bottom (neck attachment)."""
        return self.center + down.scale(self._h[0])
