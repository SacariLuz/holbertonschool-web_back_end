#!/usr/bin/env python3
"""
Hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any

index_range = __import__("0-simple_helper_function").index_range


class Server:
    """
    Server class to paginate a database of popular baby names.
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
        """
        Gives a slice with the requested pagination
        Args:
        page: Number of pages
        page_size: the length of the returned dataset page
        Returns: a dictionary containing the following
        """
        assert isinstance(page, int) and page > 0, """La pag > 0"""
        assert isinstance(page_size, int) and page_size > 0, """El size > 0"""

        star_index, end_index = index_range(page, page_size)
        if star_index >= len(self.dataset()) or end_index <= 0:
            return []
        else:
            return self.dataset()[star_index: end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Method that takes the same arguments,
        and returns a dictionary containing the following key-value pairs.
        Args:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        assert isinstance(page, int) and page > 0, """La pag > 0"""
        assert isinstance(page_size, int) and page_size > 0, """El size > 0"""

        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        data {
                "page_size": len(page_data),
                "page": page,
                "data": page_data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
                }
        return data
