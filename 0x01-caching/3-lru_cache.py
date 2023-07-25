#!/usr/bin/env python3
"""LRUCaching module"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """least frequently used caching class"""

    def __init__(self):
        super().__init__()
        self.keep_track = []

    def put(self, key, item):
        """puts an item into the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                to_delete = self.keep_track.pop(0)
                del self.cache_data[to_delete]
                print("DISCARD: {}".format(to_delete))
            if key in self.keep_track:
                self.keep_track.remove(key)
            self.keep_track.append(key)

    def get(self, key):
        """returns the value associated with a key"""
        if key is None:
            return None
        if key in self.keep_track:
            self.keep_track.remove(key)
            self.keep_track.append(key)
        return self.cache_data.get(key, None)
