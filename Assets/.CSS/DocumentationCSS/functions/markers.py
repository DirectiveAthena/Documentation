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
def markers():
    # comment structure
    yield LINE
    yield CSSComment("- Specially coloured markers (per page) -")
    yield LINE

    # actual rules
    # language=CSS
    yield """#marker_pink {
    background-color: rgba(255,0,128,0.53);
}"""