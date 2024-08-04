#!/usr/bin/env python3
"""
a function to safely get a value from a dictionary with a default.
"""

from typing import TypeVar, Mapping, Any, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any], key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dict using a key, with an optional default.

    Args:
        dct (Mapping[Any, Any]): A dictionary from which to retrieve the value.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None]):The default to return if the key is not found.

    Returns:
        Union[Any, T]:The value associated with the key if found, else default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
