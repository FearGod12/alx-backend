#!/usr/bin/env python3
"""BasicCVache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""

    def put(self, key, item):
        """assigns item to the dict key"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """returns item of key in self.cache_data"""
        if key is None:
            return None
        return self.cache_data.get(key, None)
