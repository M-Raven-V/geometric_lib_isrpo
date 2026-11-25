import unittest

from square import area, perimeter


class SquareTestCase(unittest.TestCase):

    def test_area_zero_side(self):
        self.assertEqual(area(0), 0)

    def test_area_integer_side(self):
        self.assertEqual(area(5), 25)

    def test_area_float_side(self):
        self.assertAlmostEqual(area(2.5), 6.25)


    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_integer_side(self):
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_float_side(self):
        self.assertAlmostEqual(perimeter(2.5), 10.0)


if __name__ == "__main__":
    unittest.main()