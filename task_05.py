#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module uses loop to reverse order"""


def flip_keys(to_flip):
    """
    Uses a for loop to loop the list and reverse the order of the
    inner sequence.

    Arguments:
        alist (mixed): takes item var and flips the str

        loop (for): flips everything inside the sequence

    Returns:
        mixed: data list set reversed and a string reveresed.

    Examples:

        >>> LIST = [(1, 2, 3), 'abc']
        >>> NEW = flip_keys(LIST)
        >>> LIST is NEW
        True
        >>> print LIST
        [(3, 2, 1), 'cba']

        >>> LIST = [(3, 2, 1), 'cba']
        >>> NEW = flip_keys(LIST)
        >>> LIST is NEW
        True
        >>> print LIST
        [(1, 2, 3), 'abc']

    """

    counter = 0

    for item in to_flip:
        alist = (item[::-1])
        to_flip[counter] = alist
        counter += 1

    return to_flip
