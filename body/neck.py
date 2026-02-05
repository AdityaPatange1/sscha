"""
Neck: 5D link between torso and head. A segment (line) or thin cylinder in 5D.
"""

import math
from typing import List

from .geometry import Point5D, Vector5D


class Neck:
    """
    Neck in 5D: segment from torso_top to head_bottom.
    Geometrically a line segment plus optional radial vertices (cylinder).
    """

    def __init__(
        self,
        base: Point5D,
        head_end: Point5D,
        num_radial: int = 8,
        radius: float = 0.15,
    ):
        self.base = base
        self.head_end = head_end
        self.num_radial = max(3, num_radial)
        self.radius = radius

    def axis_vector(self) -> Vector5D:
        return self.head_end - self.base

    def length(self) -> float:
        return self.axis_vector().norm()

    def center_point(self) -> Point5D:
        axis = self.axis_vector()
        return self.base + axis.scale(0.5)

    def vertices_5d(self) -> List[Point5D]:
        """
        Vertices along the neck: base, head_end, and radial rings at both ends.
        In 5D we project radius into the two principal perpendicular directions.
        """
        out: List[Point5D] = [self.base, self.head_end]
        axis = self.axis_vector()
        n = axis.norm()
        if n < 1e-10:
            return out
        # Two orthonormal directions in 5D (simplified: use dx,dy,dz for radial)
        u = Vector5D(-axis.dy, axis.dx, 0, 0, 0)
        un = u.norm()
        if un < 1e-10:
            u = Vector5D(0, -axis.dz, axis.dy, 0, 0)
            un = u.norm()
        if un >= 1e-10:
            u = u.scale(1.0 / un)
        v = Vector5D(
            axis.dy * 0 - axis.dz * u.dy,
            axis.dz * u.dx - axis.dx * 0,
            axis.dx * u.dy - axis.dy * u.dx,
            0,
            0,
        )
        vn = v.norm()
        if vn >= 1e-10:
            v = v.scale(1.0 / vn)
        else:
            v = Vector5D(1, 0, 0, 0, 0)
        for i in range(self.num_radial):
            angle = 2 * math.pi * i / self.num_radial
            r_u = self.radius * math.cos(angle)
            r_v = self.radius * math.sin(angle)
            offset = u.scale(r_u) + v.scale(r_v)
            out.append(self.base + offset)
            out.append(self.head_end + offset)
        return out

    def segment_endpoints(self) -> List[Point5D]:
        """Just the two endpoints for line geometry."""
        return [self.base, self.head_end]
