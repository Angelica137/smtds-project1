from collections import OrderedDict


class LRU_Cache(object):
    def __init__(self, capacity: int):
        """
        Initialise the LRU Cache.
        Attributes:
        capacity (int): The maximum number of key-value pairs the cache can hold.
        cache (OrderedDict): A dictionary that stores the cache entries and their access order.
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get_capacity(self):
        return self.capacity

    def get(self, key: int) -> int:
        """
        Retrieve an item from the cache by it key.

        If the key exists, it is moved to the end to indicate recent use,
        and its value is returned. If the key doesn't exist, -1 is returned.

        Args:
            key (int): The key of the item to retrieve.

        Returns:
            int: The value associated with the key if it exists, else -1.

        Time Complexity:
            O(1) on average. OrderedDict provides constant-time complexity
            for get operations and moving elements.
        """
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def set(self, key: int, value: int) -> None:
        """
        Add or update a key-value pair in the cache.

        If the key already exists, its value is updated and it's moved to the end
        to indicate recent use. If the cache is at capacity and a new key is added,
        the least recently used item is removed before insertion.

        Args:
            key (int): The key of the item to add or update
            value (int): The value to associate with the key

        Time Complexity:
            O(1) on average. OrderedDict provides constant-time complexity for
            inserting, updating, and moving elements.
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value


"""
Test cases in test file
"""
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


our_cache.get(1)  # returns 1
our_cache.get(2)  # returns 2
our_cache.get(9)  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

our_cache.get(
    3
)  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
