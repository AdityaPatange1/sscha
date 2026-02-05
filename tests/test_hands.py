"""Tests for body.hands."""

import pytest

from body.geometry import Point5D, Vector5D, origin_5d
from body.hands import Hand, Hands


class TestHand:
    def test_vertices_count(self, origin):
        h = Hand(origin)
        assert len(h.vertices_5d()) == 32

    def test_custom_half_extents(self, origin):
        h = Hand(origin, half_extent_x=0.1, half_extent_y=0.05)
        verts = h.vertices_5d()
        xs = [p.x for p in verts]
        assert max(xs) <= origin.x + 0.1 and min(xs) >= origin.x - 0.1


class TestHands:
    def test_vertices_5d_combines_both(self):
        left = Point5D(-1, 0, 0, 0, 0)
        right = Point5D(1, 0, 0, 0, 0)
        hands = Hands(left, right)
        verts = hands.vertices_5d()
        assert len(verts) == 32 + 32

    def test_left_vertices_5d_center_near_left(self):
        left = Point5D(-1, 0, 0, 0, 0)
        right = Point5D(1, 0, 0, 0, 0)
        hands = Hands(left, right)
        lverts = hands.left_vertices_5d()
        cx = sum(p.x for p in lverts) / len(lverts)
        assert cx < 0

    def test_right_vertices_5d_center_near_right(self):
        left = Point5D(-1, 0, 0, 0, 0)
        right = Point5D(1, 0, 0, 0, 0)
        hands = Hands(left, right)
        rverts = hands.right_vertices_5d()
        cx = sum(p.x for p in rverts) / len(rverts)
        assert cx > 0
