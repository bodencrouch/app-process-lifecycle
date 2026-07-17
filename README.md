# app-process-lifecycle

Graceful/forceful child-process termination, shutdown watchdog, and process-pool utilities for frozen/PyInstaller GUI apps.

## Install

```bash
pip install -e .
# or from GitHub:
pip install git+https://github.com/bodencrouch/app-process-lifecycle
```

## Origin

Extracted from the [PyKotor](https://github.com/bodencrouch/PyKotor) monorepo `utility` / related packages.
KotOR-specific couplings were removed or made optional for standalone use.

### DAG
Optional peer: `loggerplus`. Used by Holocron/HoloPatcher-style apps and `github-app-updater`.

## License

LGPL-3.0-or-later
