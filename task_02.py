#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

This module imports data.py deletes a string and then replaces it, appends a
string and expands a set of strings


"""


# Import user libs
import data

BALLETS = data.BALLETS
ITEMS = ['Don Quixote', 'Sylvia']

del BALLETS[11]

BALLETS[1] = 'Swan Lake'

BALLETS.append('Herman Schmerman')

BALLETS.extend(ITEMS)
