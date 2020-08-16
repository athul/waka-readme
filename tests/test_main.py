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
        self.assertEqual(make_graph(50), "████████████▒░░░░░░░░░░░░",
                         "50% should return ████████████▒░░░░░░░░░░░░")
        self.assertEqual(make_graph(50.001), "████████████▓░░░░░░░░░░░░",
                         "50.001% should return ████████████▓░░░░░░░░░░░░")
        self.assertEqual(make_graph(25), "██████▒░░░░░░░░░░░░░░░░░░",
                         "25% should return ██████▒░░░░░░░░░░░░░░░░░░")
        self.assertEqual(make_graph(75), "██████████████████▓░░░░░░",
                         "75% should return ██████████████████▓░░░░░░")
        self.assertEqual(make_graph(3.14), "▓░░░░░░░░░░░░░░░░░░░░░░░░",
                         "3.14% should return ▓░░░░░░░░░░░░░░░░░░░░░░░░")
        self.assertEqual(make_graph(9.901), "██▒░░░░░░░░░░░░░░░░░░░░░░",
                         "9.901% should return ██▒░░░░░░░░░░░░░░░░░░░░░░")
        self.assertEqual(make_graph(87.334), "██████████████████████░░░",
                         "87.334% should return ██████████████████████░░░")
        self.assertEqual(make_graph(87.333), "█████████████████████▓░░░",
                         "87.333% should return █████████████████████▓░░░")
        self.assertEqual(make_graph(4.666), "█░░░░░░░░░░░░░░░░░░░░░░░░",
                         "4.666% should return █░░░░░░░░░░░░░░░░░░░░░░░░")
        self.assertEqual(make_graph(4.667), "█▒░░░░░░░░░░░░░░░░░░░░░░░",
                         "4.667% should return █▒░░░░░░░░░░░░░░░░░░░░░░░")


if __name__ == '__main__':
    unittest.main()
