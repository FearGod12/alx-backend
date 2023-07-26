#!/usr/bin/env python3
"""LFU module"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """least frequenlty used caching class"""

    def __init__(self):
        """class constructor"""
        super().__init__()
        self.count = {}

    def put(self, key, item):
        """  assign to the dictionary self.cache_data the item value
        for the key key
        """
        if key and item:
            if (len(self.cache_data) == self.MAX_ITEMS
                    and key not in self.cache_data):
                discarded = min(self.count, key=self.count.get)
                del self.cache_data[discarded]
                del self.count[discarded]
                print("DISCARD: {}".format(discarded))

            if key in self.cache_data:
                self.count[key] += 1
            else:
                self.count[key] = 1
            self.cache_data[key] = item

    def get(self, key):
        """ returns the value in self.cache_data linked to key
        """
        if key in self.cache_data:
            self.count[key] += 1
            return self.cache_data.get(key)
