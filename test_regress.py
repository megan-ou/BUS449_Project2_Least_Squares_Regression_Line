from unittest import TestCase
from unittest import main

import pandas as pd
import statsmodels.api as sm

from regress import regress
from regress import regress_comp


class Test(TestCase):
    def setUp(self):
        dat = pd.read_csv('regress_data.csv')
        self.x = dat['x'].to_list()
        self.y = dat['y'].to_list()

        # establish expected regression results using statsmodels OLS
        # Add a constant to the independent variable for the intercept
        self.X = sm.add_constant(self.x)

        # Create and fit the OLS model
        self.model = sm.OLS(self.y, self.X)
        self.results = self.model.fit()

        # extract the regression coefficients for test clarity
        self.beta0, self.beta1 = self.results.params

    def test_regress_valid_arguments(self):
        # test with valid data
        actual = regress(self.y, self.x)

        self.assertAlmostEqual(self.beta0, actual[0])
        self.assertAlmostEqual(self.beta1, actual[1])

    def test_regress_different_lengths(self):

        # test with mismatched lengths
        # drop the first observations
        x = self.x[1:]
        y = self.y[1:]

        self.assertEqual(-1, regress(self.y, x))
        self.assertEqual(-1, regress(y, self.x))

    def test_regress_xy_not_iterable(self):
        # Test with invalid data (x and/or y not Iterables)
        self.assertEqual(-2, regress(self.y, 5))
        self.assertEqual(-3, regress(5, self.y))

    def test_regress_xy_not_numeric(self):

        # Test with non-numeric data
        x = self.x
        y = self.y
        x[1] = 'word'
        y[0] = 'word'
        self.assertEqual(-4, regress(y, self.x))
        self.assertEqual(-4, regress(self.y, x))
        self.assertEqual(-4, regress(y, x))


    def test_regress_comp_valid_arguments(self):
        # test with valid data
        actual = regress_comp(self.y, self.x)

        self.assertAlmostEqual(self.beta0, actual[0])
        self.assertAlmostEqual(self.beta1, actual[1])

    def test_regress_comp_different_lengths(self):

        # test with mismatched lengths
        # drop the first observations
        x = self.x[1:]
        y = self.y[1:]

        self.assertEqual(-1, regress_comp(self.y, x))
        self.assertEqual(-1, regress_comp(y, self.x))

    def test_regress_comp_xy_not_iterable(self):
        # Test with invalid data (x and/or y not Iterables)
        self.assertEqual(-2, regress_comp(self.y, 5))
        self.assertEqual(-3, regress_comp(5, self.y))

    def test_regress_comp_xy_not_numeric(self):

        # Test with non-numeric data
        x = self.x
        y = self.y
        x[1] = 'word'
        y[0] = 'word'
        self.assertEqual(-4, regress_comp(y, self.x))
        self.assertEqual(-4, regress_comp(self.y, x))
        self.assertEqual(-4, regress_comp(y, x))


if __name__ == '__main__':
    rslt = main(verbosity=2, exit=False)

    print('done')