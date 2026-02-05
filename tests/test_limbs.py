"""Tests for body.limbs."""

import pytest

from body.geometry import Point5D, Vector5D, origin_5d
from body.limbs import CylindricalLimb, Leg, Legs


class TestCylindricalLimb:
    def test_axis_and_length(self):
        a = Point5D(0, 0, 0, 0, 0)
        b = Point5D(0, 1, 0, 0, 0)
        limb = CylindricalLimb(a, b)
        assert limb.length() == 1.0
        assert limb.axis().dy == 1.0

    def test_center_point(self):
        a = Point5D(0, 0, 0, 0, 0)
        b = Point5D(0, 2, 0, 0, 0)
        limb = CylindricalLimb(a, b)
        mid = limb.center_point()
        assert mid.y == 1.0

    def test_vertices_5d_includes_endpoints(self):
        a = Point5D(0, 0, 0, 0, 0)
        b = Point5D(0, 1, 0, 0, 0)
        limb = CylindricalLimb(a, b, num_radial=4)
        verts = limb.vertices_5d()
        assert a in verts
        assert b in verts

    def test_num_radial_clamped(self):
        a = Point5D(0, 0, 0, 0, 0)
        b = Point5D(0, 1, 0, 0, 0)
        limb = CylindricalLimb(a, b, num_radial=0)
        assert limb.num_radial >= 2


class TestLeg:
    def test_leg_is_cylindrical_limb(self):
        a = Point5D(0, 0, 0, 0, 0)
        b = Point5D(0, 1, 0, 0, 0)
        leg = Leg(a, b)
        assert leg.length() == 1.0
        assert len(leg.vertices_5d()) >= 2


class TestLegs:
    def test_segments(self):
        left_hip = Point5D(-0.3, 0, 0, 0, 0)
        left_foot = Point5D(-0.2, -1, 0, 0, 0)
        right_hip = Point5D(0.3, 0, 0, 0, 0)
        right_foot = Point5D(0.2, -1, 0, 0, 0)
        legs = Legs(left_hip, left_foot, right_hip, right_foot)
        left, right = legs.segments()
        assert left.origin == left_hip and left.end == left_foot
        assert right.origin == right_hip and right.end == right_foot

    def test_vertices_5d_combines_both(self):
        left_hip = Point5D(-0.3, 0, 0, 0, 0)
        left_foot = Point5D(-0.2, -1, 0, 0, 0)
        right_hip = Point5D(0.3, 0, 0, 0, 0)
        right_foot = Point5D(0.2, -1, 0, 0, 0)
        legs = Legs(left_hip, left_foot, right_hip, right_foot, num_radial=4)
        verts = legs.vertices_5d()
        assert len(verts) == len(legs.left.vertices_5d()) + len(legs.right.vertices_5d())
