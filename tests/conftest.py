"""Shared pytest fixtures for body tests."""

import pytest

from body.geometry import Point5D, Vector5D, origin_5d


@pytest.fixture
def origin():
    return origin_5d()


@pytest.fixture
def point_a():
    return Point5D(1.0, 0.0, 0.0, 0.0, 0.0)


@pytest.fixture
def point_b():
    return Point5D(0.0, 1.0, 0.0, 0.0, 0.0)


@pytest.fixture
def vec_x():
    return Vector5D(1.0, 0.0, 0.0, 0.0, 0.0)


@pytest.fixture
def vec_y():
    return Vector5D(0.0, 1.0, 0.0, 0.0, 0.0)
