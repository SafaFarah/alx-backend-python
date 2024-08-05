#!/usr/bin/env python3
"""
Module for creating an asyncio Task from wait_random coroutine.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns asyncio Task for the wait_random coroutine with given max_delay.

    Args:
        max_delay (int): Maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: The created asyncio Task.
    """
    return asyncio.create_task(wait_random(max_delay))
