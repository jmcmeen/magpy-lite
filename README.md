# magpy-lite

[![PyPI version](https://img.shields.io/pypi/v/magpy-lite.svg)](https://pypi.org/project/magpy-lite/)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/jmcmeen/magpy-lite/blob/main/LICENSE)
[![CI](https://github.com/jmcmeen/magpy-lite/actions/workflows/ci.yml/badge.svg)](https://github.com/jmcmeen/magpy-lite/actions/workflows/ci.yml)

A terminal interface for the [bioamla](https://github.com/jmcmeen/bioamla)
bioacoustics toolkit, built with [Textual](https://textual.textualize.io/).
It is the keyboard-driven, runs-over-SSH sibling of
[MagPy](https://github.com/jmcmeen/magpy), the desktop GUI.

> **Status: coming soon.** 0.1.0 is a placeholder release that claims the name
> and ships a single announcement screen. Features will be planned as magpy and
> bioamla mature.

## Install

```sh
pip install magpy-lite
magpy-lite            # or: python -m magpy_lite
```

Press `q` to quit.

## Roadmap

Nothing here is committed yet. Likely first screens, in rough order:

- Browse and inspect recordings
- Run acoustic indices and event detection
- Batch-process directories of audio
- Query species catalogs

The division of labour follows MagPy: bioamla owns the bioacoustics domain,
magpy-lite owns only the terminal UI and the state a functional library can't
hold. Domain functionality goes into bioamla, not here.

## Development

```sh
make install   # create .venv with dev tooling
make run       # launch the TUI
make check     # lint, format check, tests
```

## License

MIT. See [LICENSE](LICENSE).
