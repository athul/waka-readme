'''
Tests for the main.py
'''
import unittest
import os

try:
    # For travis build which uses
    # python -m unittest discover
    from main import make_graph
except Exception as e:
    print("Error: missing 'main.py'\nTrying ablsolute import...")

class TestMain(unittest.TestCase):

    def test_make_graph(self):
        '''Tests the make_graph function'''
        def test(percent: float, block: str, result: str):
            self.assertEqual(make_graph(percent, block), result,
                             f"{percent}% should return {result}")
        blocks = ["░▒▓█", "⚪⚫"]
        percents = [0, 100, 50, 50.001, 25, 75, 3.14,
                    9.901, 87.334, 87.333, 4.666, 4.667]
        graphGroup = [["░░░░░░░░░░░░░░░░░░░░░░░░░",
                       "█████████████████████████",
                       "████████████▒░░░░░░░░░░░░",
                       "████████████▓░░░░░░░░░░░░",
                       "██████▒░░░░░░░░░░░░░░░░░░",
                       "██████████████████▓░░░░░░",
                       "▓░░░░░░░░░░░░░░░░░░░░░░░░",
                       "██▒░░░░░░░░░░░░░░░░░░░░░░",
                       "██████████████████████░░░",
                       "█████████████████████▓░░░",
                       "█░░░░░░░░░░░░░░░░░░░░░░░░",
                       "█▒░░░░░░░░░░░░░░░░░░░░░░░"],
                      ["⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
                       "⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫",
                       "⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
                       "⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
                       "⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
                       "⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪",
                       "⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
                       "⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
                       "⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚪⚪",
                       "⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪",
                       "⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
                       "⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪"]]
        for i, graphs in enumerate(graphGroup):
            os.environ["INPUT_BLOCKS"] = blocks[i]
            for j, graph in enumerate(graphs):
                test(percents[j], blocks[i], graph)


if __name__ == '__main__':
    if __package__ is None:
        import sys
        # because test_main.py is one level below main.py
        # python test/test_main.py
        sys.path.append(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))
        from main import make_graph
    else:
        # Later on if WakaReadme is implemetaion as package
        # python -m tests/test_main
        from ..main import make_graph
    unittest.main()
