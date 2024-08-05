#!/usr/bin/env python3
"""
Module for asynchronous coroutine that waits for a random delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits a random delay between 0 and max_delay seconds and returns the delay.

    Args:
        max_delay(int, optional):Maximum number of seconds to wait. Default=10.

    Returns:
        float: The actual number of seconds waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
