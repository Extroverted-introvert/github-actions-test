# test_calculator.py
import unittest
from src.calculator import simple_interest, compound_interest


class TestInterestCalculator(unittest.TestCase):
    def test_simple_interest(self):
        # Test case for simple interest calculation
        principal = 1000
        rate = 5
        time = 2
        expected_result = 100

        result = simple_interest(principal, rate, time)
        self.assertEqual(result, expected_result)

    def test_compound_interest_annual(self):
        # Test case for compound interest with annual compounding
        principal = 1000
        rate = 5
        time = 2
        compounding_frequency = 1
        expected_result = 102.5  # Compound interest is approximately 102.5

        result = compound_interest(principal, rate, time, compounding_frequency)
        self.assertAlmostEqual(result, expected_result, places=1)

    def test_compound_interest_semiannual(self):
        # Test case for compound interest with semiannual compounding
        principal = 1000
        rate = 5
        time = 2
        compounding_frequency = 2
        expected_result = 103.81  # Compound interest is approximately 103.06

        result = compound_interest(principal, rate, time, compounding_frequency)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_compound_interest_quarterly(self):
        # Test case for compound interest with quarterly compounding
        principal = 1000
        rate = 5
        time = 2
        compounding_frequency = 4
        expected_result = 104.49  # Compound interest is approximately 103.29

        result = compound_interest(principal, rate, time, compounding_frequency)
        self.assertAlmostEqual(result, expected_result, places=2)


if __name__ == "__main__":
    unittest.main()
