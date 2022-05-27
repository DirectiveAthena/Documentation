# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaCSS import CSSGenerator

# Custom Packages
from DocumentationCSS.Library.Headers import header_default, header_sizing

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def main():
    css_content = [
        header_default,
        header_sizing
    ]

    with (generator := CSSGenerator()) as structure:
        for content in css_content:
            for rule in content():
                structure.add_rule(
                    rule
                )

    generator.to_console()

if __name__ == '__main__':
    main()
