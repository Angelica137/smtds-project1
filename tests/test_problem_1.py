from src.problem_1 import LRU_Cache


test_cache = LRU_Cache(5)


def test_capcity():
    assert test_cache.get_capacity() == 5


def test_get_value_cache_empty():
    assert test_cache.get(1) == -1
