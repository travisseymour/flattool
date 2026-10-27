# flattool

[![Commit activity](https://img.shields.io/github/commit-activity/m/travisseymour/flattool)](https://img.shields.io/github/commit-activity/m/travisseymour/flattool)
[![License](https://img.shields.io/github/license/travisseymour/flattool)](https://img.shields.io/github/license/travisseymour/flattool)

A TUI tool for managing [Flatpak](https://flatpak.org/) applications. Search and install new apps, list and launch installed apps, or uninstall apps you no longer need. Use the arrow keys to navigate and press ENTER to act on your selection.

- **Github repository**: <https://github.com/travisseymour/flattool/>

## Usage

### Search and Install

```
flattool search [-y|--assumeyes] <search term>
```

Search for flatpak apps and optionally install a selected one.

```bash
flattool search comic
```

This will prompt you to verify before installing any app you choose.

```bash
flattool search -y comic
```

With `-y`, flatpak will start installing immediately without confirmation.

### List and Launch

```
flattool list [filter term]
```

Display installed flatpak apps. Select one to launch it.

```bash
flattool list
```

Shows all installed flatpak apps in a table. Select one to launch.

```bash
flattool list firefox
```

Filter the list to show only apps matching "firefox".

### Uninstall

```
flattool uninstall [-y|--assumeyes] [filter term]
```

Display installed flatpak apps and uninstall a selected one.

```bash
flattool uninstall
```

Shows all installed flatpak apps in a table. Select one to uninstall.

```bash
flattool uninstall firefox
```

Filter the list to show only apps matching "firefox".

```bash
flattool uninstall -y firefox
```

With `-y`, skip the confirmation prompt before uninstalling.

### Help

```bash
flattool --help           # Show all commands
flattool search --help    # Help for search command
flattool list --help      # Help for list command
flattool uninstall --help # Help for uninstall command
```

<mark>NOTICE:</mark> This tool has only tested on Linux Mint (Debian/Ubuntu base) with the flatpak tool installed.

## Installation

### Preparation

1. Make sure you have [uv (preferred)](https://docs.astral.sh/uv/) or [PipX](https://pipx.pypa.io/stable/) installed.

2. Make sure you have Python 3.10 or higher installed. If you need to install a version of Python, you can use `uv` to do this, for example:

   To check to see which versions of Python you already have

   ```bash
   uv python list
   ```

   To install Python 3.11

   ```bash
   uv python install 3.11
   ```

### Installation

```bash
uv tool install git+https://github.com/travisseymour/flattool.git
```

or

```bash
pipx install git+https://github.com/travisseymour/flattool.git
```

### Upgrade

```bash
uv tool upgrade flattool
```

or

```bash
pipx upgrade flattool
```

### Removal

```bash
uv tool uninstall flattool
```

or

```bash
pipx uninstall flattool
```
