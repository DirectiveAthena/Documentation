# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library
import copy

from AthenaColor import RGB
from AthenaCSS.models.generator import CSSGenerator
from AthenaLib.HTML.models.css import CSSProperty, CSSComment, CSSRule, CSSSelection, CSSSelectionType
import AthenaLib.HTML.models.html_library as HtmlLib
from AthenaLib.HTML.models.html import HTMLElement
from AthenaCSS.models.athenalib_imports import Pixel, RootElementFontSize

# Custom Packages
from DocumentationCSS.data.comments import LINE
from DocumentationCSS.data.classes import CLASS_MARKDOWN_EMBED, CLASS_PUBLISH_ARTICLE_HEADING
from DocumentationCSS.data.gradients import GRADIENT_HEADER

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
HEADERS = (HtmlLib.H1, HtmlLib.H2, HtmlLib.H3, HtmlLib.H4, HtmlLib.H5, HtmlLib.H6)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def header_default():
    # comment structure
    yield LINE
    yield CSSComment("- All headers derive from this -")
    yield LINE

    # actual rules
    yield CSSRule(
        selections=(
            *(CSSSelection(
                HTMLElement(classes=CLASS_MARKDOWN_EMBED),
                h(),
                selector_type=CSSSelectionType.inside
            ) for h in HEADERS
            ),
            *(CSSSelection(
                HTMLElement(classes=CLASS_MARKDOWN_EMBED),
                h(classes=CLASS_PUBLISH_ARTICLE_HEADING),
                selector_type=CSSSelectionType.inside
            ) for h in HEADERS
            ),
        ),
        properties=(
            CSSProperty("text-align","left"),
            CSSProperty("background-color",RGB(25,25,25)),
            CSSProperty("background-image",GRADIENT_HEADER),
            CSSProperty("border-radius",RootElementFontSize(0.2)),
            CSSProperty("border-bottom-style","solid"),
            CSSProperty("border-bottom-width",Pixel(5)),
        )
    ) # actual rules
    yield CSSRule(
        selections=(
            CSSSelection(
                HTMLElement(classes=CLASS_MARKDOWN_EMBED),
                HtmlLib.H1(),
                selector_type=CSSSelectionType.inside
            ),
            CSSSelection(
                HTMLElement(classes=CLASS_MARKDOWN_EMBED),
                HtmlLib.H1(classes=CLASS_PUBLISH_ARTICLE_HEADING),
                selector_type=CSSSelectionType.inside
            )
        ),
        properties=(
            CSSProperty("text-align","left"),
            CSSProperty("background-color",RGB(25,25,25)),
            CSSProperty("background-image",GRADIENT_HEADER),
            CSSProperty("border-radius",RootElementFontSize(0.2)),
            CSSProperty("border-bottom-style","solid"),
            CSSProperty("border-bottom-width",Pixel(5)),
        )
    )
