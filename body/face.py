"""
Face: 5D frontal surface of the head. A 2D plane embedded in 5D.
"""

from typing import List

from .geometry import Point5D, Vector5D, Plane5D


class Face:
    """
    Face in 5D: a planar patch (rectangle on a 5D plane) at the front of the head.
    """

    def __init__(
        self,
        center: Point5D,
        normal: Vector5D,
        width: float = 0.6,
        height: float = 0.5,
        up: Vector5D | None = None,
    ):
        self.center = center
        self.normal = normal
        self.width = width
        self.height = height
        # Spanning vectors for the plane (tangent to face)
        n = normal.norm()
        if n < 1e-10:
            self._plane = Plane5D(center, Vector5D(1, 0, 0, 0, 0), Vector5D(0, 1, 0, 0, 0))
            return
        norm_u = 1.0 / n
        nvec = Vector5D(
            normal.dx * norm_u,
            normal.dy * norm_u,
            normal.dz * norm_u,
            normal.dw * norm_u,
            normal.dv * norm_u,
        )
        if up is not None and up.norm() >= 1e-10:
            u_dir = up.scale(1.0 / up.norm())
        else:
            u_dir = Vector5D(0, 1, 0, 0, 0)
        # u = tangent along "up" on face
        u = u_dir.scale(1.0) - nvec.scale(nvec.dot(u_dir))
        un = u.norm()
        if un < 1e-10:
            u = Vector5D(1, 0, 0, 0, 0) - nvec.scale(nvec.dx)
            un = u.norm()
        if un >= 1e-10:
            u = u.scale(1.0 / un)
        # t = second tangent (right on face)
        t = Vector5D(
            nvec.dy * u.dz - nvec.dz * u.dy,
            nvec.dz * u.dx - nvec.dx * u.dz,
            nvec.dx * u.dy - nvec.dy * u.dx,
            nvec.dw * u.dz - nvec.dz * u.dw,
            nvec.dv * u.dx - nvec.dx * u.dv,
        )
        tn = t.norm()
        if tn >= 1e-10:
            t = t.scale(1.0 / tn)
        else:
            t = Vector5D(1, 0, 0, 0, 0)
        self._plane = Plane5D(center, u, t)

    def plane_5d(self) -> Plane5D:
        return self._plane

    def vertices_5d(self) -> List[Point5D]:
        """Four corners of the rectangular face in 5D."""
        hw = self.width * 0.5
        hh = self.height * 0.5
        return [
            self._plane.point_at(-hw, -hh),
            self._plane.point_at(hw, -hh),
            self._plane.point_at(hw, hh),
            self._plane.point_at(-hw, hh),
        ]

    def center_point(self) -> Point5D:
        return self.center
