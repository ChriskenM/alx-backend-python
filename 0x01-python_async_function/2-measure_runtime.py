#!/usr/bin/env python3
"""
Function Measures total execution time: wait_n and return total_time / n
"""
import asyncio
import time
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        Measures total execution time: wait_n and return total_time / n

    Args:
        n (int): Number of times to call wait_n.
        max_delay (int): Maximum delay in seconds for each wait_n call.

    Returns:
        float: Average execution time for wait_n(n, max_delay).
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
