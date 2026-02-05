"""Tests for body.head."""

import pytest

from body.geometry import Point5D, Vector5D, origin_5d
from body.head import Head


class TestHead:
    def test_vertices_count(self, origin):
        h = Head(origin)
        assert len(h.vertices_5d()) == 32

    def test_center_point(self, origin):
        h = Head(origin)
        assert h.center_point() == origin

    def test_front_center(self, origin):
        forward = Vector5D(0, 0, 1, 0, 0)
        h = Head(origin, half_extent_x=0.4)
        front = h.front_center(forward)
        assert front.z == origin.z + 0.4

    def test_bottom_center(self, origin):
        down = Vector5D(0, -1, 0, 0, 0)
        h = Head(origin, half_extent_x=0.4)
        bottom = h.bottom_center(down)
        assert bottom.y == origin.y - 0.4
