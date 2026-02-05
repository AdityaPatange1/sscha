"""Tests for body.feet."""

import pytest

from body.geometry import Point5D, Vector5D, origin_5d
from body.feet import Foot, Feet


class TestFoot:
    def test_vertices_count(self, origin):
        f = Foot(origin)
        assert len(f.vertices_5d()) == 32

    def test_custom_half_extents(self, origin):
        f = Foot(origin, half_extent_x=0.12, half_extent_z=0.08)
        verts = f.vertices_5d()
        xs = [p.x for p in verts]
        zs = [p.z for p in verts]
        assert max(xs) <= origin.x + 0.12 and min(xs) >= origin.x - 0.12
        assert max(zs) <= origin.z + 0.08 and min(zs) >= origin.z - 0.08


class TestFeet:
    def test_vertices_5d_combines_both(self):
        left = Point5D(-0.2, -1, 0, 0, 0)
        right = Point5D(0.2, -1, 0, 0, 0)
        feet = Feet(left, right)
        verts = feet.vertices_5d()
        assert len(verts) == 32 + 32

    def test_left_and_right_vertices_5d(self):
        left = Point5D(-0.2, -1, 0, 0, 0)
        right = Point5D(0.2, -1, 0, 0, 0)
        feet = Feet(left, right)
        assert len(feet.left_vertices_5d()) == 32
        assert len(feet.right_vertices_5d()) == 32
