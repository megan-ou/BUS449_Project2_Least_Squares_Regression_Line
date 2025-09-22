import math
from numbers import Number
from toolz import isiterable

#regress.py
#Calculates Least Squares Regression Line for a set of data in two different ways.
#Finds beta_0 and beta_1 coefficients
#@Author Toby Okoji, Megan Ou
#@Version September 2025

def regress(y, x):
    """
    Calculates the Least Squares Regression Line for a data set without using
    any package or built-in aggregation functions or comprehensions to perform any of the work.

    Uses the equations β_1 = (∑(x_i-x̅ )(y_i-y̅ ))/(∑(x_i-x̅ )^2) and β_0 = y̅ - β_1 x̅

    :param y: List of numerical y-values from a data set
    :param x: List of numerical x-values from a data set
    :return: (beta_0, beta_1) as a tuple
    """
    #Check to see if x and y are iterable lists
    if not isiterable(x):
        return -2

    if not isiterable(y):
        return -3

    #Check to see if x and y amount same
    #Check length only if x or y are iterables because len() will not work on a non-iterable
    if len(x) != len(y):
        return -1

    #Iterate through each list and check to see if every value is numerical
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

    #Calculate the mean value of each list using for loop
    for i in range(len(x)):
        x_mean += x[i]
        y_mean += y[i]

    x_mean = x_mean/len(x)
    y_mean = y_mean/len(x)

    #Calculate the numerator and denominator for the beta_1 formula
    #Separation is for easier readability and to make sure calculations were typed out correctly
    for i in range(len(x)):
        numerator += (x[i]-x_mean)*(y[i]-y_mean)
        denominator += (x[i]-x_mean)**2

    #Checking for denominator value just in case, want to be able to catch anything that could
    # crash the program.
    if denominator == 0:
        return -math.inf

    #Final calculations for beta_1 and beta_0
    beta_1 = (numerator/denominator)
    beta_0 = y_mean - beta_1 * x_mean

    #Group the two values into a tuple before passing it through a return statement.
    #We tried writing return (beta_0, beta_1) but Python would not read those values as a tuple
    # and we are unsure why because we thought that by grouping the two values in (), it would
    # pass as a tuple.
    solution = (beta_0,beta_1)

    return solution

def regress_comp(y, x):
    """
    Calculates the Least Squares Regression Line for a data set using
    list comprehensions and built-in aggregate functions to eliminate
    explicit loops

    Uses the equations β_1 = (∑(x_i-x̅ )(y_i-y̅ ))/(∑(x_i-x̅ )^2) and β_0 = y̅ - β_1 x̅

    :param y: List of numerical y-values from a data set
    :param x: List of numerical x-values from a data set
    :return: (beta_0, beta_1) as a tuple
    """
    #Check to see if x and y are iterable lists
    if not isiterable(x):
        return -2

    if not isiterable(y):
        return -3

    # Check to see if x and y amount same
    # Check length only if x or y are iterables because len() will not work on a non-iterable
    if len(x) != len(y):
        return -1

    #Check to see if each value in the lists are numerical values
    #Originally both x and y were in one list comprehension; using 'or' but the
    # line of code got too long, so we separated the two for easier readability
    # Would seperating the two checks make the program run slower?
    if not all([isinstance(x[i], Number) for i in range(len(x))]):
        return -4

    if not all([isinstance(y[i],Number) for i in range(len(y))]):
        return -4

    beta_0 = 0
    beta_1 = 0
    numerator_list = 0
    denominator_list = 0
    numerator = 0
    denominator = 0
    x_mean = 0
    y_mean = 0

    #Calculate the mean value for x and y lists
    x_mean = sum(x)/len(x)
    y_mean = sum(y)/len(y)

    #Calculate the numerator and denominator for beta_1 formula
    numerator_list = [(x[i] - x_mean)*(y[i] - y_mean) for i in range(len(x))]
    denominator_list = [(x[i] - x_mean)**2 for i in range(len(x))]

    #Sum up the values produced by list comprehension
    numerator = sum(numerator_list)
    denominator = sum(denominator_list)

    # Checking for denominator value just in case, want to be able to catch anything that could
    # crash the program.
    if denominator == 0:
        return -math.inf

    #Final calculations for beta_1 and beta_0
    beta_1 = numerator/denominator
    beta_0 = y_mean - beta_1 * x_mean

    #Group the two values into a tuple before passing it through a return statement.
    solution = (beta_0,beta_1)

    return solution