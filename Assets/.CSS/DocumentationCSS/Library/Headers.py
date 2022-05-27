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
from AthenaColor.Color.HtmlColors import HtmlColorObjects as Color

from AthenaLib.Types.RelativeLength import RootElementFontSize as REM
from AthenaLib.Types.AbsoluteLength import Pixel
from AthenaLib.Types.Math import Degree, Percent

# Custom Packages
from DocumentationCSS.Library.Colors import background_secondary, background_primary

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
class_markdown_rendered = CSSClass("markdown-rendered")
class_publish_article_heading = CSSClass("publish-article-heading")

HEADERS = (ElementLib.H1,ElementLib.H2,ElementLib.H3,ElementLib.H4,ElementLib.H5,ElementLib.H6)

# ----------------------------------------------------------------------------------------------------------------------
# - Default for Header -
# ----------------------------------------------------------------------------------------------------------------------
def header_default() -> CSSRule:
    with (rule := CSSRule()) as (selectors, declarations): #type: ManagerSelectors, ManagerDeclarations
        # SELECTORS of all headers:
        for header in HEADERS:
            selectors.add_descendants(
                class_markdown_rendered,
                header
            ).add_descendants(
                class_markdown_rendered,
                header(class_publish_article_heading)
            )

        # Properties
        declarations.add(
            PropertyLibrary.TextAlign("left"),
            PropertyLibrary.BackgroundColor(RGB(25,25,25)),
            PropertyLibrary.BackgroundImage(
                SubPropertyLibrary.LinearGradient((
                    Degree(90),
                    (background_secondary, Percent(75)),
                    (background_primary, Percent(100))
                ))
            ),
            PropertyLibrary.BorderRadius(REM(.2)),
            PropertyLibrary.BorderBottomStyle("solid"),
            PropertyLibrary.BorderBottomWidth(Pixel(5))
        )

    return rule

def header_sizing():
    for header, color, padding, font_size, margin_top in zip(
        HEADERS,
        # h1            h2                  h3              h4              h5          h6
        (Color.White,   Color.Gainsboro,    Color.Silver,   Color.DarkGray, Color.Gray, Color.    )
    )