#!/usr/bin/env python3
"""
Module for measuring runtime of wait_n function.
"""
import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns
    the average time per call.

    Args:
        n (int): Number of times to call wait_n.
        max_delay (int): Maximum delay for each call to wait_n.

    Returns:
        float: Average execution time per call of wait_n.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
