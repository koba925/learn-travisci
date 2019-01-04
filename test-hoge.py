#! /usr/bin/env python3

import unittest
from hoge import hogehoge


class TestHoge(unittest.TestCase):
    def test_hogehoge(self):
        self.assertEqual(hogehoge(2, 5), 7)
        self.assertEqual(hogehoge(5, 2), 3)


if __name__ == "__main__":
    unittest.main()
