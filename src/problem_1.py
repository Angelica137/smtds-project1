from collections import OrderedDict


class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get_capacity(self):
        return self.capacity

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value
