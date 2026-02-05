"""Tests for body.geometry."""

import pytest

from body.geometry import Point5D, Vector5D, Plane5D, origin_5d


class TestPoint5D:
    def test_creation_and_as_tuple(self):
        p = Point5D(1.0, 2.0, 3.0, 4.0, 5.0)
        assert p.as_tuple() == (1.0, 2.0, 3.0, 4.0, 5.0)

    def test_getitem(self):
        p = Point5D(1.0, 2.0, 3.0, 4.0, 5.0)
        assert p[0] == 1.0 and p[4] == 5.0

    def test_iter(self):
        p = Point5D(1.0, 2.0, 3.0, 4.0, 5.0)
        assert list(p) == [1.0, 2.0, 3.0, 4.0, 5.0]

    def test_add_vector(self, origin):
        v = Vector5D(1.0, 0.0, 0.0, 0.0, 0.0)
        q = origin + v
        assert q.x == 1.0 and q.y == 0.0

    def test_sub_point_gives_vector(self):
        a = Point5D(1.0, 0.0, 0.0, 0.0, 0.0)
        b = Point5D(0.0, 1.0, 0.0, 0.0, 0.0)
        v = a - b
        assert v.dx == 1.0 and v.dy == -1.0

    def test_repr(self):
        p = Point5D(1.0, 2.0, 3.0, 0.0, 0.0)
        assert "Point5D" in repr(p) and "1.0" in repr(p)


class TestVector5D:
    def test_scale(self):
        v = Vector5D(1.0, 2.0, 0.0, 0.0, 0.0)
        w = v.scale(2.0)
        assert w.dx == 2.0 and w.dy == 4.0

    def test_add_sub(self):
        a = Vector5D(1.0, 0.0, 0.0, 0.0, 0.0)
        b = Vector5D(0.0, 1.0, 0.0, 0.0, 0.0)
        assert (a + b).dx == 1.0 and (a + b).dy == 1.0
        assert (a - b).dx == 1.0 and (a - b).dy == -1.0

    def test_dot_and_norm(self):
        v = Vector5D(3.0, 4.0, 0.0, 0.0, 0.0)
        assert v.dot(v) == 25.0
        assert v.norm() == 5.0
        assert v.norm_sq() == 25.0

    def test_dot_orthogonal(self):
        a = Vector5D(1.0, 0.0, 0.0, 0.0, 0.0)
        b = Vector5D(0.0, 1.0, 0.0, 0.0, 0.0)
        assert a.dot(b) == 0.0


class TestPlane5D:
    def test_point_at(self, origin):
        u = Vector5D(1.0, 0.0, 0.0, 0.0, 0.0)
        t = Vector5D(0.0, 1.0, 0.0, 0.0, 0.0)
        plane = Plane5D(origin, u, t)
        p = plane.point_at(2.0, 3.0)
        assert p.x == 2.0 and p.y == 3.0 and p.z == 0.0

    def test_normal_3d_slice(self, origin):
        u = Vector5D(1.0, 0.0, 0.0, 0.0, 0.0)
        t = Vector5D(0.0, 1.0, 0.0, 0.0, 0.0)
        plane = Plane5D(origin, u, t)
        n = plane.normal_3d_slice()
        assert n.dz != 0  # normal should be in z for xy-plane


class TestOrigin5d:
    def test_origin_is_zero(self):
        o = origin_5d()
        assert o.x == o.y == o.z == o.w == o.v == 0.0
