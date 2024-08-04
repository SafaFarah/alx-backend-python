#!/usr/bin/env python3
"""
a function to return a list of tuples with each element and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains  element and its length.

    Args:
        lst (Iterable[Sequence]): iterable of sequences (like list or tuple).

    Returns:
        List[Tuple[Sequence, int]]: list of tuples where each tuple contains /
        an element from lst and its length.
    """
    return [(i, len(i)) for i in lst]
