#!/usr/bin/env python3
"""
a fuction mixed list
"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    return
    sum as a float
    """

    return float(sum(mxd_lst))
