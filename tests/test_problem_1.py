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


@pytest.fixture
def overfilled_cache_with_eviction_3():
    cache = LRU_Cache(5)
    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)
    cache.set(4, 4)

    cache.get(1)
    cache.get(2)

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


def test_lru_eviction_3(overfilled_cache_with_eviction_3):
    assert overfilled_cache_with_eviction_3.get(3) == -1


# Additional test cases
# Test Case 1: Check behavior with a single item cache
def test_single_item_cache():
    single_item_cache = LRU_Cache(1)
    single_item_cache.set(1, 10)
    assert single_item_cache.get(1) == 10

    single_item_cache.set(2, 20)
    assert single_item_cache.get(1) == -1
    assert single_item_cache.get(2) == 20


# Test Case 2: Edge case with null (None) values4
def test_null_cache():
    null_cache = LRU_Cache(2)
    null_cache.set(1, None)
    assert null_cache.get(1) is None

    null_cache.set(2, 20)
    null_cache.set(3, 30)
    assert null_cache.get(1) == -1


# Test Case 3: Large capacity
def test_large_cache():
    large_cache = LRU_Cache(1000)
    for i in range(1000):
        large_cache.set(i, i*10)
    assert large_cache.get(500) == 5000

    large_cache.set(1001, 10010)
    assert large_cache.get(0) == -1
