'''
Tests for the main.py
'''
from main import make_graph
import unittest


class TestMain(unittest.TestCase):

    def test_make_graph(self):
        '''Tests the make_graph function'''
        self.assertEqual(make_graph(0), "░░░░░░░░░░░░░░░░░░░░░░░░░",
                         "0% should return ░░░░░░░░░░░░░░░░░░░░░░░░░")
        self.assertEqual(make_graph(100), "█████████████████████████",
                         "100% should return █████████████████████████")
        self.assertEqual(make_graph(50), "████████████░░░░░░░░░░░░░",
                         "50% should return ████████████░░░░░░░░░░░░░")
        self.assertEqual(make_graph(25), "██████░░░░░░░░░░░░░░░░░░░",
                         "25% should return ██████░░░░░░░░░░░░░░░░░░░")
        self.assertEqual(make_graph(75), "██████████████████░░░░░░░",
                         "75% should return ██████████████████░░░░░░░")
        self.assertEqual(make_graph(3.14), "░░░░░░░░░░░░░░░░░░░░░░░░░",
                         "3.14% should return ░░░░░░░░░░░░░░░░░░░░░░░░░")
        self.assertEqual(make_graph(9.901), "██░░░░░░░░░░░░░░░░░░░░░░░",
                         "9.901% should return ██░░░░░░░░░░░░░░░░░░░░░░░")
        self.assertEqual(make_graph(87.5), "██████████████████████░░░",
                         "87.5% should return ██████████████████████░░░")


if __name__ == '__main__':
    unittest.main()
