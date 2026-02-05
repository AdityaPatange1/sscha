"""Tests for body.face."""

import pytest

from body.geometry import Point5D, Vector5D, origin_5d
from body.face import Face


class TestFace:
    def test_vertices_count(self, origin):
        normal = Vector5D(0, 0, 1, 0, 0)
        f = Face(origin, normal, width=0.6, height=0.5)
        assert len(f.vertices_5d()) == 4

    def test_center_point(self, origin):
        normal = Vector5D(0, 0, 1, 0, 0)
        f = Face(origin, normal)
        assert f.center_point() == origin

    def test_plane_5d_returns_plane(self, origin):
        normal = Vector5D(0, 0, 1, 0, 0)
        f = Face(origin, normal)
        plane = f.plane_5d()
        assert plane.origin == origin

    def test_vertices_centered_around_face_center(self, origin):
        normal = Vector5D(0, 0, 1, 0, 0)
        up = Vector5D(0, 1, 0, 0, 0)
        f = Face(origin, normal, width=2.0, height=2.0, up=up)
        verts = f.vertices_5d()
        # Corners should be at ±1, ±1 in the plane
        xs = [p.x for p in verts]
        ys = [p.y for p in verts]
        assert min(xs) <= 0 <= max(xs)
        assert min(ys) <= 0 <= max(ys)
