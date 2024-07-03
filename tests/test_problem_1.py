from src.problem_1 import LRU_Cache


def test_capcity():
    capacity = 5
    cache = LRU_Cache(capacity)
    assert cache.get_capacity() == capacity
