#!/usr/bin/env python3
""" Zooms in on a tuple by repeating each element `factor` times"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on a tuple by repeating each element `factor` times.

    Args:
        lst (Tuple[int, ...]): The tuple of integers to zoom in on.
        factor (int):The number of times to repeat each element. Defaults to 2.

    Returns:
        List[int]: A list with each element repeated `factor` times.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
