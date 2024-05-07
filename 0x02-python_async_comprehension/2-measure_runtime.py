#!/usr/bin/env python3
"""
measure_runtime coroutine that will execute async_comprehension four times,
 in parallel using asyncio.gather
"""
import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension four times,
      in parallel using asyncio.gather.

    Returns:
        float: Total runtime.
    """
    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    end_time = asyncio.get_event_loop().time()

    total_runtime = end_time - start_time

    return total_runtime
