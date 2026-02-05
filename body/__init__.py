"""
Sscha body: 5D geometric humanoid construct.
Build a GHR on a 5D plane from body parts (torso, hips, neck, head, face, limbs, arms, hands, feet).
"""

from .geometry import (
    Point5D,
    Vector5D,
    Plane5D,
    origin_5d,
)
from .torso import Torso
from .hips import Hips
from .neck import Neck
from .head import Head
from .face import Face
from .limbs import (
    LimbSegment,
    CylindricalLimb,
    Leg,
    Legs,
)
from .arms import Arms
from .hands import Hand, Hands
from .feet import Foot, Feet
from .sscha import Sscha, UP, FORWARD, RIGHT

__all__ = [
    "Point5D",
    "Vector5D",
    "Plane5D",
    "origin_5d",
    "Torso",
    "Hips",
    "Neck",
    "Head",
    "Face",
    "LimbSegment",
    "CylindricalLimb",
    "Leg",
    "Legs",
    "Arms",
    "Hand",
    "Hands",
    "Foot",
    "Feet",
    "Sscha",
    "UP",
    "FORWARD",
    "RIGHT",
]
