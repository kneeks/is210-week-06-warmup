#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

This module imports data.py deletes a string and then replaces it, appends a
string and expands a set of strings


"""


# Import user libs
import data

DIRECTIONS = data.DIRECTIONS

WEST = ('West')

DIRECTIONS[3] = WEST

DIRECTIONS = DIRECTIONS[0:3]


print DIRECTIONS
