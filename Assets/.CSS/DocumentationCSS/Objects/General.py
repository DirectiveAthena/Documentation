# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import NamedTuple

# Custom Library
from AthenaCSS import CSSSelection
from AthenaCSS import CSSProperty, CSSPropertyShorthand

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class FullStyleSelection(NamedTuple):
    selections:tuple[CSSSelection]
    styling:tuple[CSSProperty|CSSPropertyShorthand,]