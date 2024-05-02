#!/usr/bin/env python3
""" 
types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument,
    returns a function that multiplies a float by multiplier.
    """
    def f(n: float) -> float:
        """ 
        multiplies a float by the multiplier
        """
        return float(n * multiplier)

    return f