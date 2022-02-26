'''
Tests for the main.py
'''
from importlib import import_module
from dataclasses import dataclass
# from inspect import cleandoc
# from json import loads
import unittest
import sys
import os

try:
    prime = import_module('main')
    # works when running as
    # python -m unittest discover
except ImportError as err:
    print(err)
    # sys.exit(1)


@dataclass
class TestData:
    """Test Data"""
    # for future tests
    # waka_json: dict | None = None
    bar_percent: tuple[float] | None = None
    graph_blocks: tuple[str] | None = None
    waka_graphs: tuple[list[str]] | None = None
    dummy_readme: str = ''

    def populate(self) -> None:
        """Populate Test Data"""
        # for future tests
        # with open(file='tests/sample_data.json', mode='rt', encoding='utf-8') as wkf:
        #     self.waka_json = loads(wkf.read())

        self.bar_percent = (
            0, 100, 49.999, 50, 25, 75, 3.14, 9.901, 87.334, 87.333, 4.666, 4.667
        )

        self.graph_blocks = ("░▒▓█", "⚪⚫", "⓪①②③④⑤⑥⑦⑧⑨⑩")

        self.waka_graphs = ([
            "░░░░░░░░░░░░░░░░░░░░░░░░░",
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
            "█▒░░░░░░░░░░░░░░░░░░░░░░░"
        ],
            [
            "⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
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
            "⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪"
        ],
            [
            "⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪",
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
            "⑩②⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪"
        ])

        # self.dummy_readme = cleandoc("""
        # My Test Readme Start
        # <!--START_SECTION:waka-->
        # <!--END_SECTION:waka-->
        # My Test Readme End
        # """)


class TestMain(unittest.TestCase):
    """Testing Main Module"""

    def test_make_graph(self) -> None:
        """Test graph maker"""
        for idx, grb in enumerate(tds.graph_blocks):
            for jdy, bpc in enumerate(tds.bar_percent):
                self.assertEqual(
                    prime.make_graph(grb, bpc, 25),
                    tds.waka_graphs[idx][jdy]
                )

    def test_make_title(self) -> None:
        """Test title maker"""
        self.assertRegex(
            prime.make_title('2022-01-11T23:18:19Z', '2021-12-09T10:22:06Z'),
            r'From: \d{2} \w{3,9} \d{4} - To: \d{2} \w{3,9} \d{4}'
        )

    # Known test limits
    # # prep_content() and churn():
    # requires additional modifications such as changing
    # globally passed values to parametrically passing them
    # # fetch_stats(): would required HTTP Authentication


tds = TestData()
tds.populate()

if __name__ == '__main__':
    try:
        sys.path.insert(0, os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..')
        ))
        import main as prime
        # works when running as
        # python tests/test_main.py
    except ImportError as im_er:
        print(im_er)
        sys.exit(1)
    unittest.main()
