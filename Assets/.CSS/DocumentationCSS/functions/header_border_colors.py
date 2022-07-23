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
def header_border_colors():
    # comment structure
    yield LINE
    yield CSSComment("- Special Rule to make the File Embedded title hide -")
    yield LINE

    # actual rules
    for name, color in COLORS.items():
        yield f""".header_{name} {{border-color: rgb({color.r},{color.g},{color.b});}}"""