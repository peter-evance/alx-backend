#!/usr/bin/env python3
"""
Contains function index_range and class Server
"""
from typing import Tuple, Dict
import csv
import math
from typing import List


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
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Creates a list of paginated data.

        Args:
            page (int, optional): Number of pages. Defaults to 1.
            page_size (int, optional): Number of items per page.
                                       Defaults to 10.

        Returns:
            List[List]: List of items of the appropriate page of the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_indx, end_indx = index_range(page, page_size)
        dataset = self.dataset()
        if start_indx > len(dataset) or end_indx > len(dataset):
            return []
        return dataset[start_idx: end_indx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Creates HyperMedia Metadata pagination.

        Args:
            page (int, optional): Page Number. Defaults to 1.
            page_size (int, optional): Items per Page. Defaults to 10.

        Returns:
            Dict: Dictionary containing data and metadata.
        """
        data = self.get_page(page, page_size)
        dataset = self.dataset()
        start_indx, end_indx = index_range(page, page_size)

        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1
        if end_indx > len(dataset):
            next_page = None
        else:
            next_page = page + 1

        total_pages = math.ceil(len(dataset) / page_size)

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
