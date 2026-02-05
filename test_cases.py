#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1(self):
                self.assertEqual (1, calc(1, 1)) # 最小値

        def test_sample2(self):
                self.assertEqual (998001, calc(999, 999)) # 最大値

        def test_sample3(self):
                self.assertEqual (999, calc(1, 999))
                self.assertEqual (999, calc(999, 1)) # 入れ替え

        def test_sample4(self):
                self.assertEqual (-1, calc(1000, 1))
                self.assertEqual (-1, calc(1, 1000)) # 負の値

        def test_sample5(self):
                self.assertEqual (-1, calc(-1, 100))

        def test_sample6(self):
                self.assertEqual (-1, calc("a", 100))

