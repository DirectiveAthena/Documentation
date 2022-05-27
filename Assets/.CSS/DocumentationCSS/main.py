# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import inspect

# Custom Library
from AthenaCSS import CSSGenerator,CSSEmptyLine, CSSComment

# Custom Packages
from DocumentationCSS.Objects.RuleGenerator import RuleGenerator

from DocumentationCSS.Library.Headers import HeaderDefault, HeaderSizing
from DocumentationCSS.Library.PageClasses import PageAI, PagePythonPackages, PageWebsites
from DocumentationCSS.Library.Special import MetaDataHide

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
RULE_ORDER = [
    HeaderDefault,
    HeaderSizing,
    CSSEmptyLine(),
    PageAI,
    PagePythonPackages,
    PageWebsites,
    CSSEmptyLine(),
    CSSComment("SPECIAL ADDITIONS"),
    CSSEmptyLine(),
    MetaDataHide
]

def main():
    with (generator := CSSGenerator()) as structure:
        for content in RULE_ORDER:
            if inspect.isclass(content) and issubclass(content,RuleGenerator):
                 for generated in content.generate():
                    structure.add(generated)
            else:
                structure.add(content)

    generator.to_console()

if __name__ == '__main__':
    main()
