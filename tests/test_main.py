'''
Tests for the main.py
'''
from main import make_graph
import unittest


class TestMain(unittest.TestCase):

    def test_make_graph(self):
        '''Tests the make_graph function'''
        def test(percent: float, result: str):
            self.assertEqual(make_graph(percent), result, f"{percent}% should return {result}")
        test(0, "░░░░░░░░░░░░░░░░░░░░░░░░░")
        test(100, "█████████████████████████")
        test(50, "████████████▒░░░░░░░░░░░░")
        test(50.001, "████████████▓░░░░░░░░░░░░")
        test(25, "██████▒░░░░░░░░░░░░░░░░░░")
        test(75, "██████████████████▓░░░░░░")
        test(3.14, "▓░░░░░░░░░░░░░░░░░░░░░░░░")
        test(9.901, "██▒░░░░░░░░░░░░░░░░░░░░░░")
        test(87.334, "██████████████████████░░░")
        test(87.333, "█████████████████████▓░░░")
        test(4.666, "█░░░░░░░░░░░░░░░░░░░░░░░░")
        test(4.667, "█▒░░░░░░░░░░░░░░░░░░░░░░░")


if __name__ == '__main__':
    unittest.main()
