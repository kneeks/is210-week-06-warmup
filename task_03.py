#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

This module imports data.py deletes a string and then replaces it,
inside the tuple.

"""


# Import user libs
import data

DIRECTIONS = data.DIRECTIONS

DIRECTIONS = DIRECTIONS[:3] + ('West', )
