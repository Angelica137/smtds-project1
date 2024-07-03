from src.problem_1 import LRU_Cache


test_cache = LRU_Cache(5)


def test_capcity():
    assert test_cache.get_capacity() == 5


def test_get_value_cache_empty():
    assert test_cache.get(1) == -1


test_cache.set(1, 1)
test_cache.set(2, 2)
test_cache.set(3, 3)
test_cache.set(4, 4)


"""
def test_set_values():
    assert test_cache.get(1) == 1
    assert test_cache.get(2) == 2
    assert test_cache.get(3) == 3
    assert test_cache.get(4) == 4
"""
