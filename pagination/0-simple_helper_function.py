#!/usr/bin/env python3

"""
Helper function
"""


def index_range(page, page_size):
    """
    function should return a tuple of size two containing a start index

    return: a list for those particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
