"""The magpy-lite Textual application.

For 0.1.0 this is a placeholder: a single screen announcing the project.
Real screens arrive as magpy and bioamla settle.
"""

from __future__ import annotations

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Center, Middle, Vertical
from textual.widgets import Footer, Label, Static

from magpy_lite import __version__

TAGLINE = "A terminal interface for the bioamla bioacoustics toolkit"

PLANNED = (
    "Browse and inspect recordings",
    "Run acoustic indices and event detection",
    "Batch-process directories of audio",
    "Query species catalogs",
)


class ComingSoon(Static):
    """The one panel on the 0.1.0 screen."""

    DEFAULT_CSS = """
    ComingSoon {
        width: auto;
        height: auto;
        padding: 1 4;
        border: round $primary;
    }
    ComingSoon > Vertical {
        width: auto;
        height: auto;
    }
    ComingSoon .title {
        text-style: bold;
        color: $primary;
    }
    ComingSoon .tagline {
        margin-bottom: 1;
    }
    ComingSoon .status {
        text-style: bold;
        margin-bottom: 1;
    }
    ComingSoon .planned {
        color: $text-muted;
    }
    """

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Label(f"magpy-lite {__version__}", classes="title")
            yield Label(TAGLINE, classes="tagline")
            yield Label("Coming soon.", classes="status")
            yield Label("Planned:", classes="planned")
            for item in PLANNED:
                yield Label(f"  • {item}", classes="planned")


class MagpyLiteApp(App[None]):
    """Top-level app. Press q to quit."""

    TITLE = "magpy-lite"
    SUB_TITLE = "coming soon"
    BINDINGS = [Binding("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        with Middle(), Center():
            yield ComingSoon()
        yield Footer()


def main() -> None:
    """Console-script entry point (``magpy-lite``)."""
    MagpyLiteApp().run()


if __name__ == "__main__":
    main()
