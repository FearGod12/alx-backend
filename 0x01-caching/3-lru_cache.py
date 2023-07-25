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
            if key in self.keep_track:
                self.keep_track.remove(key)
            self.keep_track.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                to_delete = self.keep_track[0]
                print(self.keep_track)
                print("DISCARD: {}".format(to_delete))
                print(self.cache_data)
                del self.cache_data[to_delete]
                self.keep_track.pop(0)

    def get(self, key):
        """returns item of key in self.cache_data"""
        if key is None:
            return None
        if key in self.cache_data:
            # Remove the key to update its access order
            self.keep_track.remove(key)
            self.keep_track.append(key)  # Add the key to the end of the list
            return self.cache_data[key]
        return None
