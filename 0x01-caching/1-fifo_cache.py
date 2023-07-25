#!/usr/bin/env python3
"""FIFOCache module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """first in first out caching class"""

    def __init__(self):
        """constructor"""
        super().__init__()
        self.keep_track = []

    def put(self, key, item):
        """puts item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.keep_track.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.keep_track[0]))
                del self.cache_data[self.keep_track[0]]
                self.keep_track.pop(0)

    def get(self, key):
        """returns item of key in self.cache_data"""
        if key is None:
            return None
        return self.cache_data.get(key, None)
