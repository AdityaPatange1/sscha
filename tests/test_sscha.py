"""Tests for body.sscha."""

import pytest

from body.geometry import Point5D, Vector5D, origin_5d
from body.sscha import Sscha, UP, FORWARD, RIGHT
from body import Sscha as SschaExport


class TestSscha:
    def test_construct_default_origin(self):
        s = Sscha()
        assert s.origin == origin_5d()
        assert s.scale == 1.0

    def test_construct_custom_origin_and_scale(self):
        origin = Point5D(1.0, 2.0, 3.0, 0.0, 0.0)
        s = Sscha(origin=origin, scale=2.0)
        assert s.origin == origin
        assert s.scale == 2.0

    def test_plane_w_and_plane_v(self):
        s = Sscha(plane_w=1.0, plane_v=0.5)
        assert s.plane_w == 1.0 and s.plane_v == 0.5

    def test_vertices_5d_returns_list(self):
        s = Sscha()
        verts = s.vertices_5d()
        assert isinstance(verts, list)
        assert len(verts) > 0
        assert all(hasattr(p, "x") and hasattr(p, "y") for p in verts[:5])

    def test_vertices_5d_count_consistent(self):
        s = Sscha(scale=1.0)
        expected = (
            len(s.torso.vertices_5d())
            + len(s.hips.vertices_5d())
            + len(s.neck.vertices_5d())
            + len(s.head.vertices_5d())
            + len(s.face.vertices_5d())
            + len(s.legs.vertices_5d())
            + len(s.arms.vertices_5d())
            + len(s.hands.vertices_5d())
            + len(s.feet.vertices_5d())
        )
        assert len(s.vertices_5d()) == expected

    def test_parts_iteration(self):
        s = Sscha()
        parts = list(s.parts())
        assert len(parts) == 9
        assert s.torso in parts
        assert s.hips in parts
        assert s.neck in parts
        assert s.head in parts
        assert s.face in parts
        assert s.legs in parts
        assert s.arms in parts
        assert s.hands in parts
        assert s.feet in parts

    def test_plane_5d(self):
        s = Sscha(plane_w=0.5, plane_v=0.25)
        plane = s.plane_5d()
        assert plane.origin.w == 0.5 and plane.origin.v == 0.25

    def test_scale_affects_proportions(self):
        s1 = Sscha(scale=1.0)
        s2 = Sscha(scale=2.0)
        # Torso center same logical position but extents scaled
        assert s2.torso.half_extents[0] == 2.0 * s1.torso.half_extents[0]
        assert s2.neck.length() == 2.0 * s1.neck.length()


class TestSschaAxes:
    def test_up_vector(self):
        assert UP.dy == 1.0 and UP.dx == UP.dz == UP.dw == UP.dv == 0.0

    def test_forward_vector(self):
        assert FORWARD.dz == 1.0 and FORWARD.dx == FORWARD.dy == 0.0

    def test_right_vector(self):
        assert RIGHT.dx == 1.0 and RIGHT.dy == RIGHT.dz == 0.0


class TestSschaExport:
    def test_sscha_importable_from_body(self):
        s = SschaExport()
        assert s.vertices_5d() is not None
