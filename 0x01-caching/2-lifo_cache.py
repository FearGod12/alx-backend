#!/usr/bin/env python3
"""LIFOCaching Module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Last in first out caching class"""

    def __init__(self):
        """constructor"""
        super().__init__()
        self.keep_track = []

    def put(self, key, item):
        """puts item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                to_delete = self.keep_track[-1]
                print("DISCARD: {}".format(to_delete))
                del self.cache_data[to_delete]
            self.keep_track.append(key)

    def get(self, key):
        """returns item of key in self.cache_data"""
        if key is None:
            return None
        return self.cache_data.get(key, None)
