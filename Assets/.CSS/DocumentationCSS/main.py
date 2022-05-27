# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaCSS import CSSGenerator

# Custom Packages
from DocumentationCSS.Library.Objects import RuleGenerator
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
        for content in css_content:
            if issubclass(content,RuleGenerator):
                # generate method is possible, as it is a classmethod of a RuleClass
                for generated in content.generate():
                    structure.add(generated)
            else:
                structure.add(content)

    generator.to_console()

if __name__ == '__main__':
    main()
