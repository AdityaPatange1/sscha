"""
Sscha: Green Humanoid Reptile (GHR) as a 5D geometric construct.
Composes all body parts on a 5D plane from an origin and scale.
"""

from typing import List, Iterator

from .geometry import Point5D, Vector5D, Plane5D, origin_5d
from .torso import Torso
from .hips import Hips
from .neck import Neck
from .head import Head
from .face import Face
from .limbs import Legs
from .arms import Arms
from .hands import Hands
from .feet import Feet


# Default axes in 5D: +y = up, +z = forward, +x = right; w,v = extended dimensions
UP = Vector5D(0, 1, 0, 0, 0)
FORWARD = Vector5D(0, 0, 1, 0, 0)
RIGHT = Vector5D(1, 0, 0, 0, 0)


class Sscha:
    """
    Full GHR body constructible in 5D. Built from:
    - Torso (center)
    - Hips (below torso)
    - Neck + Head + Face (above torso)
    - Legs (hips → feet)
    - Arms (shoulders → hands)
    - Hands, Feet (end effectors)
    """

    def __init__(
        self,
        origin: Point5D | None = None,
        scale: float = 1.0,
        plane_w: float = 0.0,
        plane_v: float = 0.0,
    ):
        """
        Build Sscha on a 5D plane. The plane is the 3D (x,y,z) subspace at fixed (w, v) = (plane_w, plane_v).
        origin: center of the figure (default: 5D origin).
        scale: uniform scale for proportions.
        """
        self.origin = origin if origin is not None else origin_5d()
        self.scale = scale
        self.plane_w = plane_w
        self.plane_v = plane_v

        # Torso center (at origin in x,y,z; w,v on the plane)
        torso_center = Point5D(
            self.origin.x,
            self.origin.y,
            self.origin.z,
            plane_w,
            plane_v,
        )
        self.torso = Torso(
            torso_center,
            half_extent_x=0.5 * scale,
            half_extent_y=0.6 * scale,
            half_extent_z=0.3 * scale,
            half_extent_w=0.2 * scale,
            half_extent_v=0.2 * scale,
        )

        # Hips below torso
        hip_center = torso_center + UP.scale(-0.9 * scale)
        self.hips = Hips(
            hip_center,
            half_extent_x=0.4 * scale,
            half_extent_y=0.25 * scale,
            half_extent_z=0.25 * scale,
            half_extent_w=0.15 * scale,
            half_extent_v=0.15 * scale,
        )

        # Neck: from top of torso to bottom of head
        torso_top = torso_center + UP.scale(0.6 * scale)
        head_bottom = torso_center + UP.scale(1.2 * scale)
        self.neck = Neck(
            torso_top,
            head_bottom,
            num_radial=8,
            radius=0.12 * scale,
        )

        # Head
        head_center = torso_center + UP.scale(1.5 * scale)
        self.head = Head(
            head_center,
            half_extent_x=0.2 * scale,
            half_extent_y=0.2 * scale,
            half_extent_z=0.22 * scale,
            half_extent_w=0.1 * scale,
            half_extent_v=0.1 * scale,
        )

        # Face (front of head, normal = forward)
        face_center = head_center + FORWARD.scale(0.22 * scale)
        self.face = Face(
            face_center,
            normal=FORWARD,
            width=0.35 * scale,
            height=0.4 * scale,
            up=UP,
        )

        # Shoulders (for arms)
        left_shoulder = torso_center + UP.scale(0.4 * scale) + RIGHT.scale(-0.5 * scale)
        right_shoulder = torso_center + UP.scale(0.4 * scale) + RIGHT.scale(0.5 * scale)
        left_hand = left_shoulder + RIGHT.scale(-0.7 * scale) + UP.scale(-0.2 * scale)
        right_hand = right_shoulder + RIGHT.scale(0.7 * scale) + UP.scale(-0.2 * scale)
        self.arms = Arms(
            left_shoulder, left_hand,
            right_shoulder, right_hand,
            radius=0.08 * scale,
            num_radial=6,
        )
        self.hands = Hands(left_hand, right_hand)

        # Legs: hips to feet
        left_hip_anchor = hip_center + RIGHT.scale(-0.35 * scale)
        right_hip_anchor = hip_center + RIGHT.scale(0.35 * scale)
        left_foot_center = hip_center + UP.scale(-1.0 * scale) + RIGHT.scale(-0.2 * scale)
        right_foot_center = hip_center + UP.scale(-1.0 * scale) + RIGHT.scale(0.2 * scale)
        self.legs = Legs(
            left_hip_anchor, left_foot_center,
            right_hip_anchor, right_foot_center,
            radius=0.1 * scale,
            num_radial=6,
        )
        self.feet = Feet(left_foot_center, right_foot_center)

    def plane_5d(self) -> Plane5D:
        """The 5D plane this Sscha is constructed on (x,y,z free; w,v fixed)."""
        return Plane5D(
            Point5D(0, 0, 0, self.plane_w, self.plane_v),
            Vector5D(1, 0, 0, 0, 0),
            Vector5D(0, 1, 0, 0, 0),
        )

    def vertices_5d(self) -> List[Point5D]:
        """All vertices of the full body in 5D."""
        return (
            self.torso.vertices_5d()
            + self.hips.vertices_5d()
            + self.neck.vertices_5d()
            + self.head.vertices_5d()
            + self.face.vertices_5d()
            + self.legs.vertices_5d()
            + self.arms.vertices_5d()
            + self.hands.vertices_5d()
            + self.feet.vertices_5d()
        )

    def parts(self) -> Iterator[object]:
        """Iterate over all body part objects."""
        yield self.torso
        yield self.hips
        yield self.neck
        yield self.head
        yield self.face
        yield self.legs
        yield self.arms
        yield self.hands
        yield self.feet
