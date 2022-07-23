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
def clean_embed():
    # comment structure
    yield LINE
    yield CSSComment("- Special Rule to make the File Embedded title hide -")
    yield LINE

    # actual rules
    yield """.markdown-rendered.cleanEmbed .markdown-embed,
.markdown-rendered.cleanEmbed .markdown-embed .markdown-preview-view {
    border: medium none transparent;
    padding: 0 0 0 0;
    margin: 0 0 0 0;
}
.markdown-rendered.cleanEmbed .markdown-embed-link,
.markdown-rendered.cleanEmbed .markdown-embed-link {
    display: none;
}    
"""