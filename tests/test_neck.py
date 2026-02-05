"""Tests for body.neck."""

import pytest

from body.geometry import Point5D, Vector5D, origin_5d
from body.neck import Neck


class TestNeck:
    def test_axis_and_length(self):
        base = Point5D(0, 0, 0, 0, 0)
        head_end = Point5D(0, 1, 0, 0, 0)
        n = Neck(base, head_end)
        assert n.length() == 1.0
        assert n.axis_vector().dy == 1.0

    def test_segment_endpoints(self):
        base = Point5D(0, 0, 0, 0, 0)
        head_end = Point5D(0, 0.6, 0, 0, 0)
        n = Neck(base, head_end)
        endpoints = n.segment_endpoints()
        assert len(endpoints) == 2
        assert endpoints[0] == base and endpoints[1] == head_end

    def test_center_point(self):
        base = Point5D(0, 0, 0, 0, 0)
        head_end = Point5D(0, 1, 0, 0, 0)
        n = Neck(base, head_end)
        mid = n.center_point()
        assert mid.y == 0.5

    def test_vertices_5d_includes_base_and_head(self):
        base = Point5D(0, 0, 0, 0, 0)
        head_end = Point5D(0, 1, 0, 0, 0)
        n = Neck(base, head_end, num_radial=4, radius=0.1)
        verts = n.vertices_5d()
        assert base in verts
        assert head_end in verts
        assert len(verts) >= 2

    def test_num_radial_clamped(self):
        base = Point5D(0, 0, 0, 0, 0)
        head_end = Point5D(0, 1, 0, 0, 0)
        n = Neck(base, head_end, num_radial=1)
        assert n.num_radial >= 3
