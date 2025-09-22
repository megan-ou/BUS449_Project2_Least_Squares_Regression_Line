import pandas as pd
import regress
import math

#regress_tests.py
#Test edge cases for regress.py
#@Author Megan Ou
#@Version September 2025

#Define data list from csv as instance variables; used to test for valid cases
#Import method found on Stack Overflow
#https://stackoverflow.com/questions/45708626/read-data-in-excel-column-into-python-list
df = pd.read_csv('regress_data.csv')
x_data_list = df['x'].tolist()
y_data_list = df['y'].tolist()

def test_regress():
    """
    Test to see is regress() works in edge cases
    """
    #First test for valid cases
    regress_expected = (2144.73728, 2.774427114)
    regress_actual = regress.regress(y_data_list,x_data_list)

    if math.isclose(regress_expected[0], regress_actual[0]) and math.isclose(regress_expected[1], regress_actual[1]):
        print("Valid test for valid input: passed")
    else:
        print("Invlaid test for valid input: failed")

    #Test to see if regress() can handle invalid arguments
    #Test when x and y are different lengths
    invalid_x = [3,4,5,6]
    invalid_y = [1,2,3]
    regress_expected = -1
    regress_actual = regress.regress(invalid_y,invalid_x)

    if (regress_expected == regress_actual):
        print("Valid test for different list lengths: passed")
    else:
        print("Invalid test for different list lengths: failed")

    #Test when x and y are not iterables
    invalid_x = 3.4897
    invalid_y = [1]
    regress_expected = -2
    regress_actual = regress.regress(invalid_y,invalid_x)

    if (regress_expected == regress_actual):
        print("Valid test for x is non-iterable: passed")
    else:
        print("Invalid test for x is non-iterable: failed")

    invalid_x = [1]
    invalid_y = 3.4897
    regress_expected = -3
    regress_actual = regress.regress(invalid_y, invalid_x)

    if (regress_expected == regress_actual):
        print("Valid test for y is non-iterable: passed")
    else:
        print("Invalid test for y is non-iterable: failed")

    #Test when x or y contain non-numerical values
    #First test with an entire list of strings
    invalid_x = ["hello","world","my","name","is","megan"]
    invalid_y = [1,2,3,4,5,6]
    regress_expected = -4
    regress_actual = regress.regress(invalid_y,invalid_x)

    if (regress_expected == regress_actual):
        print("Valid test for non-numerical values: passed")
    else:
        print("Invlaid test for non-numerical values: failed")

    #Now test with a list of mixed types of numbers and strings
    invalid_x = [1,2,3,4,5]
    invalid_y = [1,2,3,4,"5"]
    regress_actual = regress.regress(invalid_y,invalid_x)

    if (regress_expected == regress_actual):
        print("Valid test for non-numerical values, mixed list: passed")
    else:
        print("Invalid test for non-numerical values, mixed list: failed")

    #Test when denominator in beta_1 calculation is 0
    invalid_x = [0,0,0,0,0]
    invalid_y = [1,2,3,4,5]
    regress_expected = -math.inf
    regress_actual = regress.regress(invalid_y,invalid_x)

    if (regress_expected == regress_actual):
        print("Valid test for denominator is 0: passed")
    else:
        print("Invalid test for denominator is 0: failed")

def test_regress_comp():
    """
    Test to see is regress_comp() works in edge cases
    Copy/pasted tests from test_regress() because test cases are the exact same. I'm not
    entirely sure if I can come up with more unique tests for this?
    """
    # First test for valid cases
    regress_expected = (2144.73728, 2.774427114)
    regress_actual = regress.regress(y_data_list, x_data_list)

    if math.isclose(regress_expected[0], regress_actual[0]) and math.isclose(regress_expected[1], regress_actual[1]):
        print("Valid test for valid input: passed")
    else:
        print("Invlaid test for valid input: failed")

    # Test to see if regress_comp() can handle invalid arguments
    # Test when x and y are different lengths
    invalid_x = [3, 4, 5, 6]
    invalid_y = [1, 2, 3]
    regress_expected = -1
    regress_actual = regress.regress_comp(invalid_y, invalid_x)

    if (regress_expected == regress_actual):
        print("Valid test for different list lengths: passed")
    else:
        print("Invalid test for different list lengths: failed")

    # Test when x and y are not iterables
    invalid_x = 3.4897
    invalid_y = [1]
    regress_expected = -2
    regress_actual = regress.regress_comp(invalid_y, invalid_x)

    if (regress_expected == regress_actual):
        print("Valid test for x is non-iterable: passed")
    else:
        print("Invalid test for x is non-iterable: failed")

    invalid_x = [1]
    invalid_y = 3.4897
    regress_expected = -3
    regress_actual = regress.regress_comp(invalid_y, invalid_x)

    if (regress_expected == regress_actual):
        print("Valid test for y is non-iterable: passed")
    else:
        print("Invalid test for y is non-iterable: failed")

    # Test when x or y contain non-numerical values
    # First test with an entire list of strings
    invalid_x = ["hello", "world", "my", "name", "is", "megan"]
    invalid_y = [1, 2, 3, 4, 5, 6]
    regress_expected = -4
    regress_actual = regress.regress_comp(invalid_y, invalid_x)

    if (regress_expected == regress_actual):
        print("Valid test for non-numerical values: passed")
    else:
        print("Invlaid test for non-numerical values: failed")

    # Now test with a list of mixed types of numbers and strings
    invalid_x = [1, 2, 3, 4, 5]
    invalid_y = [1, 2, 3, 4, "5"]
    regress_actual = regress.regress_comp(invalid_y, invalid_x)

    if (regress_expected == regress_actual):
        print("Valid test for non-numerical values, mixed list: passed")
    else:
        print("Invalid test for non-numerical values, mixed list: failed")

    # Test when denominator in beta_1 calculation is 0
    invalid_x = [0, 0, 0, 0, 0]
    invalid_y = [1, 2, 3, 4, 5]
    regress_expected = -math.inf
    regress_actual = regress.regress_comp(invalid_y,invalid_x)

    if (regress_expected == regress_actual):
        print("Valid test for denominator is 0: passed")
    else:
        print("Invalid test for denominator is 0: failed")


#run both tests
test_regress()
test_regress_comp()





