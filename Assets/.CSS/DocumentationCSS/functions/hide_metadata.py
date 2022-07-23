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
    CLASS_MARKDOWN_RENDERED, CLASS_PUBLISH_ARTICLE_HEADING,AI_CLASSES,WEBSITE_NAME_CLASSES
)
from DocumentationCSS.data.gradients import GRADIENT_HEADER
import DocumentationCSS.data.colors as Colors

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def hide_metadata():
    # comment structure
    yield LINE
    yield CSSComment("- Special Rule to make the File Embedded title hide -")
    yield LINE

    # actual rules
    # // language=CSS
    yield ".markdown-rendered.metaDataHide div.frontmatter-container { display: none; }"