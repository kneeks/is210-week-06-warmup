#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module runs a loop for function process_data."""


def process_data(data):
    """
    This function takes gives you the sum and average of your input.

    Args:
        loop (for): takes what is entered in data

        avg (int): give the average of the sum

    Returns:
        int: sum of the data, average of the data

    Examples:

    >>> process_data([1, 2, 3])
    (6, 2.0)

    >>> process_data([1, 4, 5, 10])
    (20, 5.0)

    """
    total = 0

    for num in data:
        total += num

    avg = total/float(len(data))

    return total, avg
