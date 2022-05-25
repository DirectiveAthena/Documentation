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
def page_header_styling(page_name, original_color:RGB) -> list[CSSSelection]:
    border_color = lambda blend_color: PropLib.BorderColor(to_RGB(blend_multiply(original_color, blend_color)))

    selections = []
    for header, blend_color in (
            (ElementLib.H1, RGB(255,255,255)),
            (ElementLib.H2, RGB(221,221,221)),
            (ElementLib.H3, RGB(204,204,204)),
            (ElementLib.H4, RGB(153,153,153)),
            (ElementLib.H5, RGB(119,119,119)),
            (ElementLib.H6, RGB(85,85,85))
    ):
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

            s.properties.add(
                border_color(blend_color),
            )

        selections.append(selection)

    return selections
