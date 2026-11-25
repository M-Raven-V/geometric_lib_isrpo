
import unittest

from circle import area, perimeter


class CircleTestCase(unittest.TestCase):

    def test_area_zero_radius(self):
        self.assertEqual(area(0), 0)

    def test_area_integer_radius(self):
        self.assertAlmostEqual(area(5), 78.5398163397)

    def test_area_float_radius(self):
        self.assertAlmostEqual(area(2.5), 19.6349540849)


    def test_perimeter_zero_radius(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_integer_radius(self):
        self.assertAlmostEqual(perimeter(5), 31.4159265359)

    def test_perimeter_float_radius(self):
        self.assertAlmostEqual(perimeter(2.5), 15.7079632679)


if __name__ == "__main__":
    unittest.main()