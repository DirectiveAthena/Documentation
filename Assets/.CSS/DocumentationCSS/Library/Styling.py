# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
import AthenaCSS.Library.SelectorElementLibrary as ElementLib
import AthenaCSS.Library.PropertyLibrary as PropLib
from AthenaCSS import CSSSelection, CSSClass

from AthenaColor import RGB
from AthenaColor.Objects.Color.ColorObjectConversion import to_RGB
from AthenaColor.Functions.BlendModes import blend_multiply

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def page_header_styling(page_name, original_color:RGB) :
    selections = []
    for header in (ElementLib.H1,ElementLib.H2,ElementLib.H3,ElementLib.H4,ElementLib.H5,ElementLib.H6):
        selection = CSSSelection()
        with selection as s:
            s.add_descendants(
                CSSClass("markdown-rendered", page_name),
                header
            ),
            s.add_descendants(
                CSSClass("markdown-rendered", page_name),
                header(CSSClass("publish-article-heading"))
            ),
            s.add(header(CSSClass(page_name)))
        selections.append(selection)

    styling = (
        (PropLib.BorderColor(original_color),),
        (PropLib.BorderColor(to_RGB(blend_multiply(original_color, RGB(221,221,221)))),),
        (PropLib.BorderColor(to_RGB(blend_multiply(original_color, RGB(204,204,204)))),),
        (PropLib.BorderColor(to_RGB(blend_multiply(original_color, RGB(153,153,153)))),),
        (PropLib.BorderColor(to_RGB(blend_multiply(original_color, RGB(119,119,119)))),),
        (PropLib.BorderColor(to_RGB(blend_multiply(original_color, RGB(85,85,85)))),),
    )

    return zip(selections,styling)
