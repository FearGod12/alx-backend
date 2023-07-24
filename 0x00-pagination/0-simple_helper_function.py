#!/usr/bin/env python3
"""helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns the index range"""
    offset = (page - 1) * page_size
    limit = page * page_size
    return offset, limit
