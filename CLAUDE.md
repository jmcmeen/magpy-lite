# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this is

magpy-lite is a **Textual TUI front end for the `bioamla` library**, the
terminal sibling of MagPy (the PyQt6 GUI). bioamla owns the bioacoustics
domain; magpy-lite owns the terminal UI and the mutable state a functional
library can't hold. If you need domain functionality, add it to bioamla.

**0.1.0 is a placeholder release**: one "coming soon" screen, no bioamla
dependency yet. Features are planned as magpy and bioamla mature; don't invent
screens that haven't been asked for.

## Workflow

- **The user handles all commits.** Make changes in the working tree and stop
  there. Do not run `git commit`, and do not offer to, unless asked. Branching
  and pushing likewise only on request. Work happens on `dev`; `main` releases.
- Tooling (`Makefile`, CI, release workflow, ruff config) follows the laborae
  workspace template; `make consistency` at the workspace root checks it. Don't
  edit `.github/workflows/release.yml` or `.github/scripts/roll_changelog.py`
  here; change the template instead.

## Commands

The project uses **`uv`**; the `Makefile` wraps the common tasks:

```sh
make install   # uv sync --extra dev
make run       # launch the TUI (magpy-lite -> magpy_lite.app:main)
make test      # uv run pytest
make lint      # ruff check src tests
make fmt       # ruff format + ruff check --fix
make check     # lint + format check + test
```

`uv run python -m magpy_lite` also launches it. Python is `>=3.10`.

## Layout

- `src/magpy_lite/app.py` — the `App` subclass and the `main()` entry point.
- `src/magpy_lite/__main__.py` — `python -m` shim.
- Tests drive the app headlessly with Textual's `App.run_test()` inside
  `asyncio.run()`; there is no pytest-asyncio dependency. Tests must never
  block on real terminal input.

## Rules

- Keep runtime dependencies minimal: `textual` now, `bioamla` once a screen
  calls into it. Check whether a package already arrives transitively before
  declaring it.
- Once bioamla is wired in, keep its imports in one layer (as MagPy does with
  `services/`) so widgets never import bioamla directly.
