#!/usr/bin/env python3
"""
module provides a function to sum a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of int and float numbers.

    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(mxd_lst)
