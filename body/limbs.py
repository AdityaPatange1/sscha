"""
Limbs: abstract 5D limb segment. Base for arms and legs.
"""

import math
from abc import ABC, abstractmethod
from typing import List, Tuple

from .geometry import Point5D, Vector5D


class LimbSegment(ABC):
    """
    A single limb segment in 5D: from origin to end.
    Subclasses define cross-section or thickness in 5D.
    """

    def __init__(self, origin: Point5D, end: Point5D):
        self.origin = origin
        self.end = end

    def axis(self) -> Vector5D:
        return self.end - self.origin

    def length(self) -> float:
        return self.axis().norm()

    def center_point(self) -> Point5D:
        return self.origin + self.axis().scale(0.5)

    @abstractmethod
    def vertices_5d(self) -> List[Point5D]:
        """Geometric vertices of this limb in 5D."""
        ...


class CylindricalLimb(LimbSegment):
    """
    Limb segment as a 5D cylinder: axis from origin to end, optional radial vertices.
    """

    def __init__(
        self,
        origin: Point5D,
        end: Point5D,
        radius: float = 0.12,
        num_radial: int = 6,
    ):
        super().__init__(origin, end)
        self.radius = radius
        self.num_radial = max(2, num_radial)

    def vertices_5d(self) -> List[Point5D]:
        out: List[Point5D] = [self.origin, self.end]
        axis = self.axis()
        n = axis.norm()
        if n < 1e-10:
            return out
        u = Vector5D(-axis.dy, axis.dx, 0, 0, 0)
        un = u.norm()
        if un < 1e-10:
            u = Vector5D(0, -axis.dz, axis.dy, 0, 0)
            un = u.norm()
        if un >= 1e-10:
            u = u.scale(1.0 / un)
        v = Vector5D(
            axis.dz * 0 - axis.dz * u.dy,
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
            out.append(self.origin + offset)
            out.append(self.end + offset)
        return out


class Leg(CylindricalLimb):
    """Leg: cylindrical limb from hip to foot."""

    pass


class Legs:
    """
    Pair of legs in 5D: left and right, from hips to feet.
    """

    def __init__(
        self,
        left_hip: Point5D,
        left_foot: Point5D,
        right_hip: Point5D,
        right_foot: Point5D,
        radius: float = 0.12,
        num_radial: int = 6,
    ):
        self.left = Leg(left_hip, left_foot, radius=radius, num_radial=num_radial)
        self.right = Leg(right_hip, right_foot, radius=radius, num_radial=num_radial)

    def vertices_5d(self) -> List[Point5D]:
        return self.left.vertices_5d() + self.right.vertices_5d()

    def segments(self) -> Tuple[Leg, Leg]:
        return (self.left, self.right)
