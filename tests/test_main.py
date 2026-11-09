"""Unit Tests."""

# standard
from dataclasses import dataclass  # , field
from importlib import import_module
from itertools import product
import os
import sys
import unittest
from unittest.mock import Mock, patch

# from pathlib import Path
# from inspect import cleandoc
# from typing import Any
# from json import load

try:
    prime = import_module("main")
    # works when running as
    # python -m unittest discover
except ImportError as err:
    print(err)
    # sys.exit(1)


@dataclass
class TestData:
    """Test Data."""

    # for future tests
    # waka_json: dict[str, dict[str, Any]] = field(
    #     default_factory=lambda: {}
    # )
    bar_percent: tuple[int | float, ...] | None = None
    graph_blocks: tuple[str, ...] | None = None
    waka_graphs: tuple[list[str], ...] | None = None
    dummy_readme: str = ""

    def populate(self) -> None:
        """Populate Test Data."""
        # for future tests
        # with open(
        #     file=Path(__file__).parent / "sample_data.json",
        #     encoding="utf-8",
        #     mode="rt",
        # ) as wkf:
        #     self.waka_json = load(wkf)

        self.bar_percent = (0, 100, 49.999, 50, 25, 75, 3.14, 9.901, 87.334, 87.333, 4.666, 4.667)

        self.graph_blocks = ("░▒▓█", "⚪⚫", "⓪①②③④⑤⑥⑦⑧⑨⑩")

        self.waka_graphs = (
            [
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
                "█▒░░░░░░░░░░░░░░░░░░░░░░░",
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
                "⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
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
                "⑩②⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪⓪",
            ],
        )

        # self.dummy_readme = cleandoc("""
        # My Test Readme Start
        # <!--START_SECTION:waka-->
        # <!--END_SECTION:waka-->
        # My Test Readme End
        # """)


class TestMain(unittest.TestCase):
    """Testing Main Module."""

    def test_make_graph(self) -> None:
        """Test graph maker."""
        if not tds.graph_blocks or not tds.waka_graphs or not tds.bar_percent:
            raise AssertionError("Data population failed")

        for (idx, grb), (jdy, bpc) in product(
            enumerate(tds.graph_blocks), enumerate(tds.bar_percent)
        ):
            self.assertEqual(prime.make_graph(grb, bpc, 25), tds.waka_graphs[idx][jdy])

    def test_make_title(self) -> None:
        """Test title maker."""
        self.assertRegex(
            prime.make_title("2022-01-11T23:18:19Z", "2021-12-09T10:22:06Z"),
            r"From: \d{2} \w{3,9} \d{4} - To: \d{2} \w{3,9} \d{4}",
        )

    def test_strtobool(self) -> None:
        """Test string to bool."""
        self.assertTrue(prime.strtobool("Yes"))
        self.assertFalse(prime.strtobool("nO"))
        self.assertTrue(prime.strtobool(True))
        self.assertRaises(AttributeError, prime.strtobool, None)
        self.assertRaises(ValueError, prime.strtobool, "yo!")
        self.assertRaises(AttributeError, prime.strtobool, 20.5)

    def test_is_wakatime_provider(self) -> None:
        """Test which API hosts send the token as a query parameter."""
        self.assertTrue(prime.is_wakatime_provider("https://wakatime.com/api"))
        self.assertTrue(prime.is_wakatime_provider("https://api.wakatime.com/api/"))
        self.assertFalse(prime.is_wakatime_provider("https://wakapi.dev/api"))
        self.assertFalse(prime.is_wakatime_provider("https://hakatime.mtx-dev.xyz/api"))

    def test_redact_secret(self) -> None:
        """Test that raw and URL-encoded secrets are removed from errors."""
        secret = "oauth/token?value"
        self.assertEqual(prime.redact_secret(f"url?api_key={secret}", secret), "url?api_key=***")
        self.assertEqual(
            prime.redact_secret("url?api_key=oauth%2Ftoken%3Fvalue", secret),
            "url?api_key=***",
        )

    @patch.object(prime, "sleep")
    @patch.object(prime, "rq_get")
    def test_fetch_stats_uses_wakatime_query_auth(self, mock_get: Mock, _mock_sleep: Mock) -> None:
        """WakaTime OAuth tokens are passed as api_key rather than Basic auth."""
        response = Mock(status_code=200, reason="OK")
        response.json.return_value = {"data": {"languages": []}}
        mock_get.return_value = response
        old_wk_i = getattr(prime, "wk_i", None)
        prime.wk_i = prime.WakaInput(
            waka_key="oauth-token",
            api_base_url="https://wakatime.com/api",
            time_range="last_7_days",
        )

        try:
            self.assertEqual(prime.fetch_stats(), {"languages": []})
            request = mock_get.call_args.kwargs
            self.assertEqual(request["params"], {"api_key": "oauth-token"})
            self.assertNotIn("Authorization", request["headers"])
        finally:
            if old_wk_i is None:
                del prime.wk_i
            else:
                prime.wk_i = old_wk_i

    @patch.object(prime, "sleep")
    @patch.object(prime, "rq_get")
    def test_fetch_stats_keeps_basic_auth_for_compatible_provider(
        self, mock_get: Mock, _mock_sleep: Mock
    ) -> None:
        """Compatible providers continue to receive Basic API-key auth."""
        response = Mock(status_code=200, reason="OK")
        response.json.return_value = {"data": {"languages": []}}
        mock_get.return_value = response
        old_wk_i = getattr(prime, "wk_i", None)
        prime.wk_i = prime.WakaInput(
            waka_key="api-key",
            api_base_url="https://wakapi.dev/api",
            time_range="last_7_days",
        )

        try:
            self.assertEqual(prime.fetch_stats(), {"languages": []})
            request = mock_get.call_args.kwargs
            self.assertEqual(request["params"], {})
            self.assertEqual(request["headers"]["Authorization"], "Basic YXBpLWtleQ==")
        finally:
            if old_wk_i is None:
                del prime.wk_i
            else:
                prime.wk_i = old_wk_i

    def test_make_ai_code_stats(self) -> None:
        """Test AI code graph and stats maker."""
        stats = {
            "ai_additions": 1200,
            "ai_deletions": 300,
            "human_additions": 450,
            "human_deletions": 50,
            "ai_input_tokens": 12345,
            "ai_output_tokens": 678,
            "ai_prompt_events_total": 42,
            "ai_sessions": 3,
            "ai_model_total_cost": 1.25,
            "ai_model_breakdown": [
                {"name": "GPT", "lines": 1000},
                {"name": "Claude", "lines": 500},
            ],
        }
        old_wk_i = getattr(prime, "wk_i", None)
        prime.wk_i = prime.WakaInput(block_style="-#")

        try:
            self.assertEqual(
                prime.make_ai_code_stats(stats, True, True),
                "\n".join(
                    (
                        "AI Code      1,500 lines           ###################------   75.00 %",
                        "Human Code   500 lines             ######-------------------   25.00 %",
                        "",
                        "AI Stats",
                        "  Prompts      42",
                        "  Sessions     3",
                        "  Tokens       12,345 in / 678 out",
                        "  Est. Cost    $1.25",
                        "",
                        "AI Models",
                        "  GPT    1,000 lines",
                        "  Claude 500 lines",
                    )
                ),
            )
        finally:
            if old_wk_i is None:
                del prime.wk_i
            else:
                prime.wk_i = old_wk_i

    def test_make_ai_code_stats_without_fields(self) -> None:
        """Test AI code stats maker skips older API responses."""
        self.assertEqual(prime.make_ai_code_stats({"languages": []}), "")
        self.assertEqual(
            prime.make_ai_code_stats({"ai_prompt_events_total": 2}),
            "AI Stats\n  Prompts      2",
        )

    def test_make_ai_code_stats_switches(self) -> None:
        """Test AI code graph and statistics switches."""
        stats = {
            "ai_additions": 75,
            "ai_deletions": 25,
            "human_additions": 25,
            "human_deletions": 25,
            "ai_prompt_events_total": 2,
            "ai_input_tokens": 1000,
            "ai_output_tokens": 200,
            "ai_model_line_changes": {"GPT": 100},
        }
        old_wk_i = getattr(prime, "wk_i", None)
        prime.wk_i = prime.WakaInput(block_style="-#")

        try:
            graph_only = prime.make_ai_code_stats(stats, True, False)
            self.assertIn("AI Code", graph_only)
            self.assertNotIn("AI Prompts", graph_only)

            stats_only = prime.make_ai_code_stats(stats, False, True)
            self.assertNotIn("AI Code", stats_only)
            self.assertIn("AI Stats", stats_only)
            self.assertIn("  Prompts      2", stats_only)
            self.assertIn("  Tokens       1,000 in / 200 out", stats_only)
            self.assertIn("AI Models", stats_only)
            self.assertIn("  GPT 100 lines", stats_only)

            self.assertEqual(prime.make_ai_code_stats(stats, False, False), "")
        finally:
            if old_wk_i is None:
                del prime.wk_i
            else:
                prime.wk_i = old_wk_i


tds = TestData()
tds.populate()

if __name__ == "__main__":
    try:
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
        import main as prime

        # works when running as
        # python tests/test_main.py
    except ImportError as im_er:
        print(im_er)
        sys.exit(1)
    unittest.main()
