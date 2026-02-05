"""Tests for body.arms."""

import pytest

from body.geometry import Point5D, Vector5D, origin_5d
from body.arms import Arms


class TestArms:
    def test_segments(self):
        ls = Point5D(-0.5, 0.4, 0, 0, 0)
        lh = Point5D(-1.2, 0.2, 0, 0, 0)
        rs = Point5D(0.5, 0.4, 0, 0, 0)
        rh = Point5D(1.2, 0.2, 0, 0, 0)
        arms = Arms(ls, lh, rs, rh)
        left, right = arms.segments()
        assert left.origin == ls and left.end == lh
        assert right.origin == rs and right.end == rh

    def test_vertices_5d_combines_both(self):
        ls = Point5D(-0.5, 0.4, 0, 0, 0)
        lh = Point5D(-1.2, 0.2, 0, 0, 0)
        rs = Point5D(0.5, 0.4, 0, 0, 0)
        rh = Point5D(1.2, 0.2, 0, 0, 0)
        arms = Arms(ls, lh, rs, rh, num_radial=4)
        verts = arms.vertices_5d()
        assert len(verts) == len(arms.left_vertices_5d()) + len(arms.right_vertices_5d())

    def test_left_and_right_vertices_5d(self):
        ls = Point5D(-0.5, 0, 0, 0, 0)
        lh = Point5D(-1.0, 0, 0, 0, 0)
        rs = Point5D(0.5, 0, 0, 0, 0)
        rh = Point5D(1.0, 0, 0, 0, 0)
        arms = Arms(ls, lh, rs, rh)
        assert len(arms.left_vertices_5d()) >= 2
        assert len(arms.right_vertices_5d()) >= 2
