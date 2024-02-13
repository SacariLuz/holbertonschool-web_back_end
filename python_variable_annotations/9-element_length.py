#!/usr/bin/env python3
"""
a function parameters, elemnt length
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    return values with apropiate types
    """
    return [(i, len(i)) for i in lst]
