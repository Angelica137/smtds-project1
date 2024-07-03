from src.problem_1 import LRU_Cache

import pytest


@pytest.fixture
def empty_cache():
    return LRU_Cache(5)


@pytest.fixture
def filled_cache():
    cache = LRU_Cache(5)
    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)
    cache.set(4, 4)
    return cache


@pytest.fixture
def overfilled_cache():
    cache = LRU_Cache(5)
    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)
    cache.set(4, 4)
    cache.set(5, 5)
    cache.set(6, 6)
    return cache


def test_capacity(empty_cache):
    assert empty_cache.get_capacity() == 5


def test_get_value_cache_empty(empty_cache):
    assert empty_cache.get(1) == -1


def test_set_values(filled_cache):
    assert filled_cache.get(1) == 1
    assert filled_cache.get(2) == 2
    assert filled_cache.get(3) == 3
    assert filled_cache.get(4) == 4

    assert filled_cache.get(9) == -1


def test_lru_eviction(overfilled_cache):
    assert overfilled_cache.get(1) == -1
    assert overfilled_cache.get(2) == 2
