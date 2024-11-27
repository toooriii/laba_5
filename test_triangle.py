import unittest
from triangle import area_T, perimeter_T

class TestTriangle(unittest.TestCase):
    def test_triangle_area_positive(self):
        self.assertEqual(area_T(10, 5), 25)
        self.assertEqual(area_T(0, 5), 0)

    def test_triangle_perimeter_valid(self):
        self.assertEqual(perimeter_T(3, 4, 5), 12)
        self.assertEqual(perimeter_T(5, 5, 5), 15)

    def test_triangle_perimeter_invalid_sides(self):
        with self.assertRaises(ValueError):
            perimeter_T(1, 1, 10)  # Invalid triangle

    def test_triangle_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter_T(-3, 4, 5)

if __name__ == "__main__":
    unittest.main()