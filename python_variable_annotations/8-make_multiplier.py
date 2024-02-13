#!/usr/bin/env python3
"""
type-annotated function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ return a callable """
    def multiply(m: float) -> float:
        """return m * multiplier :)"""
        return m * multiplier
    return multiply
