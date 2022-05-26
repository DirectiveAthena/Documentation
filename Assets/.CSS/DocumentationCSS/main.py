# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaCSS import CSSPrinter, CSSSelection, CSSProperty, CSSClass

import AthenaCSS.Library.PropertyLibrary as PropLib

from AthenaColor import RGB

# Custom Packages
from DocumentationCSS.Library.Styling import page_header_styling
from DocumentationCSS.Library.DefinedColors import AI_COLORS

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def main():
    printer = CSSPrinter()
    with printer as p:
        for ai_color in AI_COLORS:
            for selection, styling in page_header_styling(ai_color, AI_COLORS.):
                p.add_style(
                    selection=selection,
                    styling=styling
                )

    printer.to_console()


if __name__ == '__main__':
    main()







































def additon(a, b):
    return a+b

result = additon(1,2)

...
...

if result == 3:
    print(result)

if (result := additon(1,2)) == 3:
    print(result)
