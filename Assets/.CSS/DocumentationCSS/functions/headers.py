# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library
from AthenaColor import RGB
from AthenaColor.func.blend_modes import blend_multiply
from AthenaLib.HTML.models.css import CSSProperty, CSSComment, CSSRule, CSSSelection, CSSSelectionType
import AthenaLib.HTML.models.html_library as HtmlLib
from AthenaLib.HTML.models.html import HTMLElement
from AthenaCSS.models.athenalib_imports import Pixel, RootElementFontSize, ElementFontSize

# Custom Packages
from DocumentationCSS.data.comments import LINE
from DocumentationCSS.data.classes import (
    CLASS_MARKDOWN_EMBED, CLASS_PUBLISH_ARTICLE_HEADING,CLASS_ADAM,CLASS_ATHENA,CLASS_EVA,CLASS_JUPITER,CLASS_VERITAS,
    CLASS_VULCANUS,CLASS_NEPTUNE,CLASS_MINERVA,CLASS_SOL,CLASS_AERO,CLASS_VENUS,CLASS_PLUTO,CLASS_CERES,
)
from DocumentationCSS.data.gradients import GRADIENT_HEADER
import DocumentationCSS.data.colors as Colors

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
_HEADERS:dict[type,dict] = {
    HtmlLib.H1 : {
        "color":Colors.WHITE,
        "padding":f"{Pixel(12)} {Pixel(12)} {Pixel(12)} {Pixel(35)}",
        "font-size":ElementFontSize(2),
        "margin-top":0,
    },
    HtmlLib.H2 : {
        "color":RGB(220, 220, 220),
        "padding":f"{Pixel(10)} {Pixel(10)} {Pixel(10)} {Pixel(35)}",
        "font-size":ElementFontSize(1.8),
        "margin-top":ElementFontSize(2),
    },
    HtmlLib.H3 : {
        "color":RGB(192, 192, 192),
        "padding":f"{Pixel(8)} {Pixel(8)} {Pixel(8)} {Pixel(35)}",
        "font-size":ElementFontSize(1.6),
        "margin-top":ElementFontSize(1.75),
    },
    HtmlLib.H4 : {
        "color":RGB(169, 169, 169),
        "padding":f"{Pixel(6)} {Pixel(6)} {Pixel(6)} {Pixel(35)}",
        "font-size":ElementFontSize(1.4),
        "margin-top":ElementFontSize(1.5),
    },
    HtmlLib.H5 : {
        "color":RGB(128, 128, 128),
        "padding":f"{Pixel(4)} {Pixel(4)} {Pixel(4)} {Pixel(35)}",
        "font-size":ElementFontSize(1.2),
        "margin-top":ElementFontSize(1.25),
    },
    HtmlLib.H6 : {
        "color":RGB(105, 105, 105),
        "padding":f"{Pixel(2)} {Pixel(2)} {Pixel(2)} {Pixel(35)}",
        "font-size":ElementFontSize(1.1),
        "margin-top":ElementFontSize(1),
    }
}

# ----------------------------------------------------------------------------------------------------------------------
# - Default Header -
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
            ) for h in _HEADERS
            ),
            *(CSSSelection(
                HTMLElement(classes=CLASS_MARKDOWN_EMBED),
                h(classes=CLASS_PUBLISH_ARTICLE_HEADING),
                selector_type=CSSSelectionType.inside
            ) for h in _HEADERS
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
    )
    for k, v in _HEADERS.items():
        yield CSSRule(
            selections=(
                CSSSelection(
                    HTMLElement(classes=CLASS_MARKDOWN_EMBED),
                    k(),
                    selector_type=CSSSelectionType.inside
                ),
                CSSSelection(
                    HTMLElement(classes=CLASS_MARKDOWN_EMBED),
                    k(classes=CLASS_PUBLISH_ARTICLE_HEADING),
                    selector_type=CSSSelectionType.inside
                )
            ),
            properties=(
                CSSProperty("color",v["color"]),
                CSSProperty("padding",v["padding"]),
                CSSProperty("font-size",v["font-size"]),
                CSSProperty("margin-top",v["margin-top"]),
            )
        )

# ----------------------------------------------------------------------------------------------------------------------
# - Repettitive Header -
# ----------------------------------------------------------------------------------------------------------------------
def header_repetitive():
    # comment structure
    yield LINE
    yield CSSComment("- Custom header border colors -")
    yield LINE
