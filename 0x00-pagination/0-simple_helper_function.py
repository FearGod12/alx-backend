#!/usr/bin/env python3
"""helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns the index range"""
    if page < 1:
        offset = 1
    else:
        offset = page
    limit = page * page_size
    return page, limit
