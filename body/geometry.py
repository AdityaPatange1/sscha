"""
5D geometric primitives for Sscha body construction on a 5D plane.
Coordinates: (x, y, z, w, v) where x,y,z are spatial; w,v are extended dimensions.
"""

from dataclasses import dataclass
from typing import Tuple, Iterator


@dataclass(frozen=True)
class Point5D:
    """A point in 5-dimensional space."""

    x: float
    y: float
    z: float
    w: float
    v: float

    def __iter__(self) -> Iterator[float]:
        return iter((self.x, self.y, self.z, self.w, self.v))

    def __getitem__(self, i: int) -> float:
        return (self.x, self.y, self.z, self.w, self.v)[i]

    def as_tuple(self) -> Tuple[float, float, float, float, float]:
        return (self.x, self.y, self.z, self.w, self.v)

    def __add__(self, other: "Vector5D") -> "Point5D":
        return Point5D(
            self.x + other.dx,
            self.y + other.dy,
            self.z + other.dz,
            self.w + other.dw,
            self.v + other.dv,
        )

    def __sub__(self, other: "Point5D") -> "Vector5D":
        return Vector5D(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
            self.w - other.w,
            self.v - other.v,
        )

    def __repr__(self) -> str:
        return f"Point5D({self.x}, {self.y}, {self.z}, {self.w}, {self.v})"


@dataclass(frozen=True)
class Vector5D:
    """A vector in 5-dimensional space."""

    dx: float
    dy: float
    dz: float
    dw: float
    dv: float

    def __iter__(self) -> Iterator[float]:
        return iter((self.dx, self.dy, self.dz, self.dw, self.dv))

    def as_tuple(self) -> Tuple[float, float, float, float, float]:
        return (self.dx, self.dy, self.dz, self.dw, self.dv)

    def scale(self, k: float) -> "Vector5D":
        return Vector5D(
            self.dx * k,
            self.dy * k,
            self.dz * k,
            self.dw * k,
            self.dv * k,
        )

    def __add__(self, other: "Vector5D") -> "Vector5D":
        return Vector5D(
            self.dx + other.dx,
            self.dy + other.dy,
            self.dz + other.dz,
            self.dw + other.dw,
            self.dv + other.dv,
        )

    def __sub__(self, other: "Vector5D") -> "Vector5D":
        return Vector5D(
            self.dx - other.dx,
            self.dy - other.dy,
            self.dz - other.dz,
            self.dw - other.dw,
            self.dv - other.dv,
        )

    def dot(self, other: "Vector5D") -> float:
        return (
            self.dx * other.dx
            + self.dy * other.dy
            + self.dz * other.dz
            + self.dw * other.dw
            + self.dv * other.dv
        )

    def norm_sq(self) -> float:
        return self.dot(self)

    def norm(self) -> float:
        return self.norm_sq() ** 0.5

    def __repr__(self) -> str:
        return f"Vector5D({self.dx}, {self.dy}, {self.dz}, {self.dw}, {self.dv})"


@dataclass
class Plane5D:
    """
    A 5D plane: origin + two spanning vectors (2D plane embedded in 5D).
    For a hyperplane (4D subspace), use origin + four spanning vectors;
    here we use the minimal 2D plane for 'geometrical form on a 5D plane'.
    """

    origin: Point5D
    u: Vector5D  # first spanning vector
    t: Vector5D  # second spanning vector (named t to avoid confusion with v coordinate)

    def point_at(self, s: float, r: float) -> Point5D:
        """Point at parameters (s, r): origin + s*u + r*t."""
        return self.origin + self.u.scale(s) + self.t.scale(r)

    def normal_3d_slice(self) -> Vector5D:
        """Approximate normal in the (x,y,z) slice (for visualization)."""
        u, t = self.u, self.t
        return Vector5D(
            u.dy * t.dz - u.dz * t.dy,
            u.dz * t.dx - u.dx * t.dz,
            u.dx * t.dy - u.dy * t.dx,
            0.0,
            0.0,
        )


def origin_5d() -> Point5D:
    """Canonical origin in 5D."""
    return Point5D(0.0, 0.0, 0.0, 0.0, 0.0)
