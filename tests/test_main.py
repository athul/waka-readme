'''
Tests for the main.py
'''
import unittest
import datetime
import base64
import os

try:
    # For travis build which uses
    # python -m unittest discover
    from main import make_graph, generate_new_readme, decode_readme
except Exception as e:
    print("Error: missing 'main.py'\nTrying ablsolute import...")

class TestMain(unittest.TestCase):

    def test_make_graph(self):
        '''Tests the make_graph function'''
        def test(percent: float, block: str, result: str):
            self.assertEqual(make_graph(percent, block), result,
                             f"{percent}% should return {result}")
        blocks = ["░▒▓█", "⚪⚫", "⓪①②③④⑤⑥⑦⑧⑨⑩"]
        percents = [0, 100, 49.999, 50, 25, 75, 3.14,
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
                       "⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
                       "⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
                       "⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
                       "⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪",
                       "⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
                       "⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
                       "⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪",
                       "⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪",
                       "⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
                       "⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪"],
                      ["⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪",
                       "⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩",
                       "⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑤⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪",
                       "⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑤⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪",
                       "⑩⑩⑩⑩⑩⑩③⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪",
                       "⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑧⓪⓪⓪⓪⓪⓪",
                       "⑧⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪",
                       "⑩⑩⑤⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪",
                       "⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑧⓪⓪⓪",
                       "⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑩⑧⓪⓪⓪",
                       "⑩②⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪",
                       "⑩②⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪"]]
        for i, graphs in enumerate(graphGroup):
            os.environ["INPUT_BLOCKS"] = blocks[i]
            for j, graph in enumerate(graphs):
                test(percents[j], blocks[i], graph)

    def test_generate_new_readme(self):
        '''Tests generate_new_readme method from main.py'''
        dummy_readme = '''My Readme Start
        <!--START_SECTION:waka-->
        <!--END_SECTION:waka-->
        My Readme End'''
        dummy_stats = '''```text
        Python     24 hrs 15 mins  █████████████████████████   100.00 %
        ```'''
        expected_generated_readme = '''My Readme Start
        <!--START_SECTION:waka-->\n```text
        Python     24 hrs 15 mins  █████████████████████████   100.00 %
        ```\n<!--END_SECTION:waka-->
        My Readme End
        '''
        expected_generated_readme = expected_generated_readme.strip()
        actual_generated_readme = generate_new_readme(dummy_stats, dummy_readme)
        self.assertEqual(actual_generated_readme, expected_generated_readme)

    def test_decode_readme(self):
        '''Tests decode_readme method from main.py'''
        dummy_data = base64.b64encode(bytes('Some Data From GitHub', 'utf-8'))
        expected_result = 'Some Data From GitHub'
        actual_result = decode_readme(dummy_data)
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    if __package__ is None:
        import sys
        # because test_main.py is one level below main.py
        # python test/test_main.py
        sys.path.append(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))
        from main import make_graph, generate_new_readme, decode_readme
    else:
        # Later on if WakaReadme is implemetaion as package
        # python -m tests/test_main
        from ..main import make_graph, generate_new_readme, decode_readme
    unittest.main()
