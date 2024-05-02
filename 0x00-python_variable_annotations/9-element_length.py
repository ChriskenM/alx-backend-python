#!/usr/bin/env python3
"""
Duck typing an iterable object
"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Element's length
    """
    return [(i, len(i)) for i in lst]