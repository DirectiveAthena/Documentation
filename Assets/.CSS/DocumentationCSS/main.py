# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaCSS import CSSGenerator

# Custom Packages
from DocumentationCSS.Library.Headers import HeaderDefault, HeaderSizing

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def main():
    css_content = [
        HeaderDefault,
        HeaderSizing
    ]

    with (generator := CSSGenerator()) as structure:
        for ruleClass in css_content:
            for generated in ruleClass.generate():
                structure.add(generated)

    generator.to_console()

if __name__ == '__main__':
    main()
