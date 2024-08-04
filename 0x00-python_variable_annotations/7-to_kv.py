#!/usr/bin/env python3
"""
a function to create a tuple with a str and the square of an int or float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple of  string k and the square of the integer or float v.

    Args:
        k (str): The string value.
        v (Union[int, float]): The integer or float value to be squared.

    Returns:
        Tuple[str, float]: A tuple of  str k and the square of v as a float.
    """
    return (k, float(v ** 2))
