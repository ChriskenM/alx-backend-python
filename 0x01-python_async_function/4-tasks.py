#!/usr/bin/env python3
"""
Asynchronous function spawns task_wait_random n times
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        Asynchronous function spawns task_wait_random n times

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay in Sec for each task_wait_random call

    Returns:
        List[float]: List of all the delays (float values) in ascending order.
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
