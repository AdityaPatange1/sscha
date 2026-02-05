"""Tests for body.torso."""

import pytest

from body.geometry import Point5D, Vector5D, origin_5d
from body.torso import Torso


class TestTorso:
    def test_vertices_count(self, origin):
        t = Torso(origin)
        verts = t.vertices_5d()
        assert len(verts) == 32

    def test_center_point(self, origin):
        t = Torso(origin)
        assert t.center_point() == origin

    def test_half_extents(self, origin):
        t = Torso(origin, half_extent_x=1.0, half_extent_y=0.5)
        assert t.half_extents[0] == 1.0 and t.half_extents[1] == 0.5

    def test_vertices_symmetric_around_center(self, origin):
        t = Torso(origin, half_extent_x=1.0, half_extent_y=1.0, half_extent_z=1.0, half_extent_w=0.1, half_extent_v=0.1)
        verts = t.vertices_5d()
        for p in verts:
            assert -1.0 <= p.x - origin.x <= 1.0
            assert -1.0 <= p.y - origin.y <= 1.0

    def test_top_center(self, origin):
        up = Vector5D(0, 1, 0, 0, 0)
        t = Torso(origin, half_extent_x=0.5, half_extent_y=0.6)
        top = t.top_center(up)
        assert top.y == origin.y + 0.5  # uses first extent along up
