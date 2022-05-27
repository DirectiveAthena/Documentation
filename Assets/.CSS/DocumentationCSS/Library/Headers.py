# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaCSS import (
    CSSRule, CSSProperty, CSSElement, CSSClass,
    SelectorElementLibrary as ElementLib,
    PropertyLibrary,
    SubPropertyLibrary
)
from AthenaCSS.Generator.ManagerCSSRule import ManagerSelectors, ManagerDeclarations

from AthenaColor import RGB

from AthenaLib.Types.RelativeLength import RootElementFontSize as REM
from AthenaLib.Types.AbsoluteLength import Pixel
from AthenaLib.Types.Math import Degree

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
class_markdown_rendered = CSSClass("markdown-rendered")
class_publish_article_heading = CSSClass("publish-article-heading")

HEADERS = (ElementLib.H1,ElementLib.H2,ElementLib.H3,ElementLib.H4,ElementLib.H5,ElementLib.H6)

# ----------------------------------------------------------------------------------------------------------------------
# - Default Header -
# ----------------------------------------------------------------------------------------------------------------------
def header_default() -> CSSRule:
    with (rule := CSSRule()) as (selectors, declarations): #type: ManagerSelectors, ManagerDeclarations
        # SELECTORS of all headers:
        for header in HEADERS:
            selectors.add_descendants(
                class_markdown_rendered,
                header
            ).add(
                class_markdown_rendered,
                header(class_publish_article_heading)
            )

        # Properties
        declarations.add(
            PropertyLibrary.TextAlign("left"),
            PropertyLibrary.Background(RGB(25,25,25)),
            SubPropertyLibrary.LinearGradient(Degree(90))
            PropertyLibrary.BorderRadius(REM(.2)),
            PropertyLibrary.BorderBottomStyle("solid"),
            PropertyLibrary.BorderBottomWidth(Pixel(5))
        )

    return rule
# .markdown-rendered h1,
# .markdown-rendered h2,
# .markdown-rendered h3,
# .markdown-rendered h4,
# .markdown-rendered h5,
# .markdown-rendered h6,
# .markdown-rendered h1.publish-article-heading,
# .markdown-rendered h2.publish-article-heading,
# .markdown-rendered h3.publish-article-heading,
# .markdown-rendered h4.publish-article-heading,
# .markdown-rendered h5.publish-article-heading,
# .markdown-rendered h6.publish-article-heading
# {
#     text-align: left;
#     background: rgb(25,25,25);
#     background: linear-gradient(90deg, var(--background-secondary) 75%, var(--background-primary) 100%);
#     border-radius: .2em;
#     border-bottom-style: solid;
#     border-bottom-width: 5px;
# }
# #