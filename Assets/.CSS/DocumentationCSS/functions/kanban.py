# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library
from AthenaLib.HTML.models.css import CSSComment

# Custom Packages
from DocumentationCSS.data.comments import LINE
from DocumentationCSS.data.colors import COLORS

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def kanban():
    # comment structure
    yield LINE
    yield CSSComment("- Special Rules for the kanban plugin -")
    yield LINE

    # actual rules
    # language=CSS
    yield ".kanban-plugin {background-color: rgba(0,0,0,0) !important;}"
    # yield ".kanban-plugin {background-color: None #202020 !important;}"