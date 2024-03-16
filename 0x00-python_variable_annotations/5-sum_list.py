#!/usr/bin/env python3
"""Type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum of list elements"""
    a: float = 0.0
    for i in input_list:
        a += i
    return a
