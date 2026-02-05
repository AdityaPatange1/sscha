"""
Hips: base anchor of Sscha in 5D. A compact 5D region (box) below the torso.
"""

from typing import List

from .geometry import Point5D, Vector5D


class Hips:
    """
    Hips in 5D: axis-aligned box at the base of the body.
    Serves as anchor for legs and lower spine.
    """

    def __init__(
        self,
        center: Point5D,
        half_extent_x: float = 0.8,
        half_extent_y: float = 0.4,
        half_extent_z: float = 0.5,
        half_extent_w: float = 0.15,
        half_extent_v: float = 0.15,
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
        """All 32 vertices of the 5D hip box."""
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

    def left_anchor(self, left_dir: Vector5D) -> Point5D:
        """Attachment point for left leg."""
        return self.center + left_dir.scale(self._h[0])

    def right_anchor(self, right_dir: Vector5D) -> Point5D:
        """Attachment point for right leg."""
        return self.center + right_dir.scale(self._h[0])
