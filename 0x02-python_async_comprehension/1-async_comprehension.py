#!/usr/bin/env python3
""" a coroutine called async_comprehension that takes no arguments."""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehending
    over async_generator, then returns the 10 random numbers.
    """
    return [i async for i in async_generator()]
