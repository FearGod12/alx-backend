#!/usr/bin/env python3
"""LFU module"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """least frequenlty used caching class"""

    def __init__(self):
        """class constructor"""
        super().__init__()
        self.keep_track = []
        self.count = {}

    def put(self, key, item):
        """puts items in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if self.count.get(key):
                self.count[key] += 1
            else:
                self.count[key] = 1

            if key in self.keep_track:
                self.keep_track.remove(key)
            self.keep_track.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                val_to_find_key = min(self.count.values())
                list_of_leasts = []
                for k, v in self.count.items():
                    if v == val_to_find_key:
                        list_of_leasts.append(k)
                if len(list_of_leasts) > 1:
                    for j in self.keep_track:
                        if j in list_of_leasts:
                            to_delete = j
                            break
                elif len(list_of_leasts) == 1:
                    to_delete = list_of_leasts[0]
                print(list_of_leasts)
                print("DISCARD: {}".format(to_delete))
                del self.cache_data[to_delete]
                del self.count[to_delete]
                self.keep_track.remove(to_delete)

    def get(self, key):
        """returns the value for the specified key"""
        if key is None:
            return None
        if key in self.cache_data:
            self.count[key] += 1
            self.keep_track.remove(key)
            self.keep_track.append(key)
            return self.cache_data[key]
