# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import itertools

# Custom Library
from AthenaColor import RGB
from AthenaColor.func.blend_modes import blend_multiply
from AthenaLib.HTML.models.css import CSSProperty, CSSComment, CSSRule, CSSSelection, CSSSelectionType
import AthenaLib.HTML.models.html_library as HtmlLib
from AthenaLib.HTML.models.html import HTMLElement
from AthenaCSS.models.athenalib_imports import Pixel, ElementFontSize

# Custom Packages
from DocumentationCSS.data.comments import LINE
from DocumentationCSS.data.classes import (
    CLASS_MARKDOWN_RENDERED,AI_CLASSES,WEBSITE_NAME_CLASSES, PYTHON_PACKAGE_CLASSES
)
from DocumentationCSS.data.gradients import (PYTHON_PACKAGE_GRADIENTS,GRADIENT_HEADER)
import DocumentationCSS.data.colors as Colors

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
_HEADERS:dict[type,dict] = {
    HtmlLib.H1 : {
        "color":Colors.WHITE,
        "padding":ElementFontSize(.4),
        "font-size":ElementFontSize(2),
    },
    HtmlLib.H2 : {
        "color":RGB(220, 220, 220),
        "padding":ElementFontSize(.4),
        "font-size":ElementFontSize(1.8),
    },
    HtmlLib.H3 : {
        "color":RGB(192, 192, 192),
        "padding":ElementFontSize(.4),
        "font-size":ElementFontSize(1.6),
    },
    HtmlLib.H4 : {
        "color":RGB(169, 169, 169),
        "padding":ElementFontSize(.4),
        "font-size":ElementFontSize(1.4),
    },
    HtmlLib.H5 : {
        "color":RGB(128, 128, 128),
        "padding":ElementFontSize(.4),
        "font-size":ElementFontSize(1.2),
    },
    HtmlLib.H6 : {
        "color":RGB(105, 105, 105),
        "padding":ElementFontSize(.4),
        "font-size":ElementFontSize(1.1),
    }
}

selectors:tuple[CSSSelection,...] = (
    *(CSSSelection(
        HTMLElement(classes=CLASS_MARKDOWN_RENDERED),
        h(),
        selector_type=CSSSelectionType.inside
    ) for h in _HEADERS),
)
selector = lambda classname, heading_level: (
    CSSSelection(
        HTMLElement(classes=(CLASS_MARKDOWN_RENDERED,classname)),
        heading_level(),
        selector_type=CSSSelectionType.inside
    ),
    CSSSelection(heading_level(classes=classname))
)

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
        selections=selectors,
        properties=(
            CSSProperty("text-align","left"),
            CSSProperty("background-color",RGB(25,25,25)),
            CSSProperty("background-image",GRADIENT_HEADER),
            CSSProperty("border-radius",ElementFontSize(0.25)),
            CSSProperty("border-bottom-style","solid"),
            CSSProperty("border-bottom-width",ElementFontSize(0.25)),
        )
    )
    for k, v in _HEADERS.items():
        yield CSSRule(
            selections=selector("",k),
            properties=(
                CSSProperty("color",v["color"]),
                CSSProperty("padding",v["padding"]),
                CSSProperty("font-size",v["font-size"]),
            )
        )

# ----------------------------------------------------------------------------------------------------------------------
# - Repettitive Header -
# ----------------------------------------------------------------------------------------------------------------------
def header_pages():
    # comment structure
    yield LINE
    yield CSSComment("- Custom header border colors -")
    yield LINE

    for classname, color in itertools.chain(
            zip(AI_CLASSES, Colors.AI_COLORS), zip(WEBSITE_NAME_CLASSES, Colors.WEBSITE_NAME_COLORS)
    ):
        for k,v in _HEADERS.items():
            yield CSSRule(
                selections=selector(classname, k),
                properties=CSSProperty("border-color", blend_multiply(v["color"], color)),
            )

def header_pages_special():
    # comment structure
    yield LINE
    yield CSSComment("- Custom header border colors (special cases)-")
    yield LINE

    for classname, color in zip(PYTHON_PACKAGE_CLASSES, PYTHON_PACKAGE_GRADIENTS):
        yield CSSRule(
            selections=selector(classname, HtmlLib.H1),
            properties=CSSProperty("border-image", color),
        )

