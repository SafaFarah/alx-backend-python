#!/usr/bin/env python3
"""
Module for asynchronous coroutine that waits for a random delay
and spawns multiple such coroutines.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and returns
    a list of all the delays in ascending order.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [wait_random(max_delay) for i in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
