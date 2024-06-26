#!/usr/bin/env python3
"""
Combined types - string and int or float to tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int OR float v as arguments
    returns a tuple.
    """

    return (k, v**2)
