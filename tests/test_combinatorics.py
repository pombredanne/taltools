import unittest
from taltools.combinatorics import n_choose_k, n_next_to_k


class TestNChooseK(unittest.TestCase):
    def test_6_choose_anything(self):
        expected_values = [1, 6, 6*5//2, 6*5*4//2//3]
        expected_values.extend(list(reversed(expected_values[-6//2:])))

        for x in range(6+1):
            with self.subTest("n_choose_k(6, {})".format(x)):
                self.assertEquals(n_choose_k(6, x), expected_values[x])


class TestNNextToK(unittest.TestCase):
    def test_6_next_to_anything(self):
        expected_values = [1, 6, 6*5, 6*5*4, 6*5*4*3, 6*5*4*3*2, 6*5*4*3*2*1]
        expected_values.extend(list(reversed(expected_values[-6//2:])))

        for x in range(6+1):
            with self.subTest("n_next_to_k(6, {})".format(x)):
                self.assertEquals(n_next_to_k(6, x), expected_values[x])
