#!/usr/bin/env python3
"""
This module provides a function to safely retrieve the first element of a list.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieves the first element of a list.

    Args:
        lst(Sequence[Any]):sequence (like list or tuple) elements of any type.

    Returns:
        Union[Any, None]:first element of lst if lst is not empty, else None.
    """
    if lst:
        return lst[0]
    else:
        return None
