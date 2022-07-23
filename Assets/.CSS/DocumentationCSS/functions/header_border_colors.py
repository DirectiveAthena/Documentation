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
    CLASS_MARKDOWN_RENDERED, CLASS_PUBLISH_ARTICLE_HEADING,AI_CLASSES,WEBSITE_NAME_CLASSES, PYTHON_PACKAGE_CLASSES
)
from DocumentationCSS.data.gradients import (PYTHON_PACKAGE_GRADIENTS,GRADIENT_HEADER)
from DocumentationCSS.data.colors import COLORS

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def header_border_colors():
    # comment structure
    yield LINE
    yield CSSComment("- Special Rule to make the File Embedded title hide -")
    yield LINE

    # actual rules
    for name, color in COLORS.items():
        yield f""".header_{name} {{border-color: rgb({color.r},{color.g},{color.b});}}"""