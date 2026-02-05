"""
Torso: central 5D volume of Sscha. Represented as a 5D box (32 vertices).
"""

from typing import List

from .geometry import Point5D, Vector5D


class Torso:
    """
    Torso in 5D: axis-aligned box centered at `center` with half-extents
    (sx, sy, sz, sw, sv). Vertices are all ± combinations along each axis.
    """

    def __init__(
        self,
        center: Point5D,
        half_extent_x: float = 1.0,
        half_extent_y: float = 1.0,
        half_extent_z: float = 1.0,
        half_extent_w: float = 0.2,
        half_extent_v: float = 0.2,
    ):
        self.center = center
        self._h = (
            half_extent_x,
            half_extent_y,
            half_extent_z,
            half_extent_w,
            half_extent_v,
        )

    @property
    def half_extents(self) -> tuple:
        return self._h

    def vertices_5d(self) -> List[Point5D]:
        """All 32 vertices of the 5D box."""
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

    def top_center(self, up: Vector5D) -> Point5D:
        """Center of the top face (toward +up)."""
        return self.center + up.scale(self._h[0])  # use first extent along up
