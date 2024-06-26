#!/usr/bin/env python3
"""
Create a function with annotated types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list input_list of floats as argument
    returns their sum as a float.
    """

    return sum(input_list)
