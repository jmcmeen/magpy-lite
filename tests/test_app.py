import asyncio

from magpy_lite import __version__
from magpy_lite.app import ComingSoon, MagpyLiteApp


def test_app_shows_version_and_quits():
    async def run() -> str:
        app = MagpyLiteApp()
        async with app.run_test() as pilot:
            panel = app.query_one(ComingSoon)
            title = panel.query("Label").first().render().plain
            await pilot.press("q")
        assert app.return_code == 0
        return str(title)

    title = asyncio.run(run())
    assert __version__ in title


def test_console_script_target_is_importable():
    from magpy_lite.app import main

    assert callable(main)
