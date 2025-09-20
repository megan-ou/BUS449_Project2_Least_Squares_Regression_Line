#regress.py
#Calculates Least Squares Regression Line for a set of data
# Finds beta_0 and beta_1 coefficients
#@Author Megan Ou, Toby Okoji
#@Version September 2025

import math
from selectors import SelectSelector
from typing import Iterable


def regress(y, x): ->

if len(x) = len(y):
    return -1

if not isinstance(x, Iterable):
    return -2
if not isinstance(y, Iterable):
    return -3
