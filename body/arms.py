"""
Arms: left and right arm segments in 5D.
"""

from typing import List, Tuple

from .geometry import Point5D, Vector5D
from .limbs import CylindricalLimb


class Arms:
    """
    Pair of arms in 5D. Each arm is a limb from shoulder to hand.
    """

    def __init__(
        self,
        left_shoulder: Point5D,
        left_hand: Point5D,
        right_shoulder: Point5D,
        right_hand: Point5D,
        radius: float = 0.1,
        num_radial: int = 6,
    ):
        self.left = CylindricalLimb(
            left_shoulder, left_hand, radius=radius, num_radial=num_radial
        )
        self.right = CylindricalLimb(
            right_shoulder, right_hand, radius=radius, num_radial=num_radial
        )

    def vertices_5d(self) -> List[Point5D]:
        return self.left.vertices_5d() + self.right.vertices_5d()

    def left_vertices_5d(self) -> List[Point5D]:
        return self.left.vertices_5d()

    def right_vertices_5d(self) -> List[Point5D]:
        return self.right.vertices_5d()

    def segments(self) -> Tuple[CylindricalLimb, CylindricalLimb]:
        return (self.left, self.right)
