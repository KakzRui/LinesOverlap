import unittest
from overlap_lines import overlap


class OverlapLinesTest(unittest.TestCase):
    def test_pos_int_overlap(self):
        line1 = (1, 2)
        line2 = (1, 4)
        result = overlap(line1, line2)
        self.assertEqual(result, '{} and {} overlaps on x-axis'.format(line1, line2))

    def test_neg_int_overlap(self):
        line1 = (-1, -3)
        line2 = (-2, -4)
        result = overlap(line1, line2)
        self.assertEqual(result, '{} and {} overlaps on x-axis'.format(line1, line2))

    def test_eq_int_overlap(self):
        line1 = (0, 1)
        line2 = (0, 1)
        result = overlap(line1, line2)
        self.assertEqual(result, '{} and {} overlaps on x-axis'.format(line1, line2))

    def test_pos_int_not_overlap(self):
        line1 = (1, 2)
        line2 = (3, 4)
        result = overlap(line1, line2)
        self.assertEqual(result, '{} and {} not overlaps on x-axis'.format(line1, line2))

    def test_neg_int_not_overlap(self):
        line1 = (-3, -4)
        line2 = (-5, -6)
        result = overlap(line1, line2)
        self.assertEqual(result, '{} and {} not overlaps on x-axis'.format(line1, line2))

    def test_comb_int_not_overlap(self):
        line1 = (-3, -4)
        line2 = (1, 2)
        result = overlap(line1, line2)
        self.assertEqual(result, '{} and {} not overlaps on x-axis'.format(line1, line2))

    def test_conv_str_coord(self):
        line1 = ('1', 2)
        line2 = (2, '3.4')
        result = overlap(line1, line2)
        self.assertEqual(result, '{} and {} overlaps on x-axis'.format((1, 2), (2, 3)))


if __name__ == '__main__':
    unittest.main()
