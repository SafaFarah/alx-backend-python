#!/usr/bin/env python3
""" a measure_runtime coroutine that will execute async_comprehension /
four times in parallel using asyncio.gather """

import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    using asyncio.gather, measures the total runtime, and returns it.
    """
    start_time = asyncio.get_event_loop().time()

    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)

    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
