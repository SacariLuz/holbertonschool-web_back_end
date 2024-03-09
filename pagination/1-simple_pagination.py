#!/usr/bin/env python3

"""
Simple pagination
"""

import csv
import math
from typing import List

index_range = __import__("0-simple_helper_function").index_range


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
        """
        Range of the page
        """
        assert isinstance(page, int) and page > 0, """La pag > 0"""
        assert isinstance(page_size, int) and page_size > 0, """El size > 0"""

        star_index, end_index = index_range(page, page_size)
        if star_index >= len(self.dataset()) or end_index <= 0:
            return []
        else:
            return self.dataset()[star_index: end_index]
