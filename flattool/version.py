# SPDX-FileCopyrightText: FlatTool | Copyright (c) 2025 Travis L. Seymour, PhD <nogard@ucsc.edu>
# SPDX-License-Identifier: GPL-3.0-or-later
"""
FlatTool. A commandline tool used to search for apps using flatpak and then install result with a single click.
"""

import importlib
from importlib.metadata import version


def get_version() -> str:
    try:
        return version("flattool")
    except importlib.metadata.PackageNotFoundError:
        return "???"
