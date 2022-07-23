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
from AthenaCSS.models.athenalib_imports import Pixel, RootElementFontSize, ElementFontSize

# Custom Packages
from DocumentationCSS.data.comments import LINE
from DocumentationCSS.data.classes import (
    CLASS_MARKDOWN_RENDERED, CLASS_PUBLISH_ARTICLE_HEADING,AI_CLASSES,WEBSITE_NAME_CLASSES, CLASS_ATHENACOLOR,
    CLASS_ATHENALIB
)
from DocumentationCSS.data.gradients import GRADIENT_HEADER, GRADIENT_ATHENACOLOR, GRADIENT_ATHENALIB
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
                HTMLElement(classes=CLASS_MARKDOWN_RENDERED),
                h(),
                selector_type=CSSSelectionType.inside
            ) for h in _HEADERS
            ),
            *(CSSSelection(
                HTMLElement(classes=CLASS_MARKDOWN_RENDERED),
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
                    HTMLElement(classes=CLASS_MARKDOWN_RENDERED),
                    k(),
                    selector_type=CSSSelectionType.inside
                ),
                CSSSelection(
                    HTMLElement(classes=CLASS_MARKDOWN_RENDERED),
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
def header_pages():
    # comment structure
    yield LINE
    yield CSSComment("- Custom header border colors -")

    for classname, color in itertools.chain(
            zip(AI_CLASSES, Colors.AI_COLORS), zip(WEBSITE_NAME_CLASSES, Colors.WEBSITE_NAME_COLORS)
    ):
        yield LINE
        for k,v in _HEADERS.items():
            yield CSSRule(
                selections=(
                    CSSSelection(
                        HTMLElement(classes=(CLASS_MARKDOWN_RENDERED, classname)),
                        HtmlLib.H1(),
                        selector_type=CSSSelectionType.inside
                    ),
                    CSSSelection(
                        HTMLElement(classes=(CLASS_MARKDOWN_RENDERED, classname)),
                        HtmlLib.H1(classes=CLASS_PUBLISH_ARTICLE_HEADING),
                        selector_type=CSSSelectionType.inside
                    ),
                    CSSSelection(HtmlLib.H1(classes=classname))
                ),
                properties=(
                    CSSProperty("border-color", color)),
                ),
                force_one_line=True
            )

def header_pages_special():
    # comment structure
    yield LINE
    yield CSSComment("- Custom header border colors (special cases)-")

    for classname, color in itertools.chain(
            (CLASS_ATHENACOLOR, GRADIENT_ATHENACOLOR),
            (CLASS_ATHENALIB, GRADIENT_ATHENALIB)
    ):
        yield LINE
        for k,v in _HEADERS.items():
            yield CSSRule(
                selections=(
                    CSSSelection(
                        HTMLElement(classes=(CLASS_MARKDOWN_RENDERED, classname)),
                        k(),
                        selector_type=CSSSelectionType.inside
                    ),
                    CSSSelection(
                        HTMLElement(classes=(CLASS_MARKDOWN_RENDERED, classname)),
                        k(classes=CLASS_PUBLISH_ARTICLE_HEADING),
                        selector_type=CSSSelectionType.inside
                    ),
                    CSSSelection(k(classes=classname))
                ),
                properties=(
                    CSSProperty("border-color", blend_multiply(v["color"], color)),
                ),
                force_one_line=True
            )

