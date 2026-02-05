"""Tests for body.hips."""

import pytest

from body.geometry import Point5D, Vector5D, origin_5d
from body.hips import Hips


class TestHips:
    def test_vertices_count(self, origin):
        h = Hips(origin)
        assert len(h.vertices_5d()) == 32

    def test_center_point(self, origin):
        h = Hips(origin)
        assert h.center_point() == origin

    def test_left_anchor(self, origin):
        left_dir = Vector5D(-1, 0, 0, 0, 0)
        h = Hips(origin, half_extent_x=0.8)
        anchor = h.left_anchor(left_dir)
        assert anchor.x == origin.x - 0.8

    def test_right_anchor(self, origin):
        right_dir = Vector5D(1, 0, 0, 0, 0)
        h = Hips(origin, half_extent_x=0.8)
        anchor = h.right_anchor(right_dir)
        assert anchor.x == origin.x + 0.8
