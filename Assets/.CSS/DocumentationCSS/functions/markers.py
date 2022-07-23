# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library
from AthenaLib.HTML.models.css import CSSComment

# Custom Packages
from DocumentationCSS.data.comments import LINE
from DocumentationCSS.data.colors import MARKERS

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def markers():
    # comment structure
    yield LINE
    yield CSSComment("- Specially coloured markers (per page) -")
    yield LINE

    # actual rules
    for marker,color in MARKERS.items():
        yield f"""mark.{marker} {{background-color: {color};}}"""