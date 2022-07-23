# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library
from AthenaLib.HTML.models.css import CSSComment

# Custom Packages
from DocumentationCSS.data.comments import LINE

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
    # language=CSS
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