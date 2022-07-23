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
def hide_metadata():
    # comment structure
    yield LINE
    yield CSSComment("- Special Rule to make the File Embedded title hide -")
    yield LINE

    # actual rules
    # language=CSS
    yield ".markdown-rendered.metaDataHide div.frontmatter-container {display:flex;}"
    # language=CSS
    yield """
    body > div.app-container > div.horizontal-main-container > div > div.workspace-split.mod-vertical.mod-root > div.workspace-leaf.mod-active > div > div.view-content > div.markdown-reading-view > div.markdown-preview-view.markdown-rendered.node-insert-event.is-readable-line-width.allow-fold-headings.show-indentation-guide.allow-fold-lists.metaDataHide > div > div:nth-child(2) > div > div.frontmatter-container-header{
        color: #00a7aa;
    }"""