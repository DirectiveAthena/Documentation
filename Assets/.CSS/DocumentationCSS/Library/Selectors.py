# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaCSS import (
    CSSClass,CSSElement,
    SelectorElementLibrary as ElementLib,
)

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class_markdown_rendered = CSSClass("markdown-rendered")
class_publish_article_heading = CSSElement(CSSClass("publish-article-heading"))
HEADERS = (ElementLib.H1,ElementLib.H2,ElementLib.H3,ElementLib.H4,ElementLib.H5,ElementLib.H6)

class_adam = CSSClass("adam")