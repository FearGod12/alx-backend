#!/usr/bin/env python3
"""helper function for pagination and a class"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns the index range"""
    offset = (page - 1) * page_size
    limit = page * page_size
    return offset, limit


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns the requested list of rows"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        try:
            result = self.dataset()[start:end]
        except IndexError:
            return []
        return result

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """return hyper pagination"""
        data = self.get_page(page, page_size)

        result = {"page_size": len(data),
                  "page": page,
                  "data": data,
                  "next_page": page + 1 if self.get_page(page + 1, page_size)
                  else None,
                  "prev_page": page - 1 if page > 1 else None,
                  "total_pages": len(self.__dataset)
                  }
        return result
