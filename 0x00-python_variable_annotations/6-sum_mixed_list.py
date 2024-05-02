#!/usr/bin/env python3

"""
mixed variables annotated list
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ 
    Used union to allow different types
    returns sum as a float.
    """
    return float(sum(mxd_lst))