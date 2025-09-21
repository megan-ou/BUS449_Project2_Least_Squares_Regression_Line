#regress.py
#Calculates Least Squares Regression Line for a set of data
# Finds beta_0 and beta_1 coefficients
#@Author Megan Ou, Toby Okoji
#@Version September 2025

import math
from numbers import Number
from wsgiref.util import request_uri
from toolz import isiterable

def regress(y, x):
    #Check to see if x and y amount same
    if len(x) != len(y):
        return -1

    #checking for proper x data type
    if not isiterable(x):
        return -2

    if not isiterable(y):
        return -3

    valid = None

    for i in range(len(x)):
        if not isinstance(x[i], Number) or not isinstance(y[i], Number):
            valid = False
            break
        else:
            valid = True

    if valid == False:
        return -4

    beta_0 = 0
    beta_1 = 0
    numerator = 0
    denominator = 0
    x_mean = 0
    y_mean = 0

    for i in range(len(x)):
        x_mean += x[i]
        y_mean += y[i]

    x_mean = x_mean/len(x)
    y_mean = y_mean/len(x)

    for i in range(len(x)):
        numerator += (x[i]-x_mean)*(y[i]-y_mean)
        denominator += (x[i]-x_mean)**2

    if denominator == 0:
        return -math.inf

    beta_1 = (numerator/denominator)
    beta_0 = (beta_1 * x_mean)

    return(beta_0, beta_1)