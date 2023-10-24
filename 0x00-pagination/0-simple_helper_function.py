#!/usr/bin/env python3
"""
Contains function index_range
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Creates a Tuple containing start and end index, based on page
    and page_size.

    Args:
        page (int): Page numbers indexed from 1.
        page_size (int): Items in page.

    Returns:
        Tuple: size of page containing start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
