# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaCSS import (
    CSSRule, CSSComment, CSSClass,
    PropertyLibrary,
    SelectorElementLibrary as ElementLib,
)
from AthenaCSS.Generator.ManagerCSSRule import ManagerSelectors, ManagerDeclarations

from AthenaColor.Color.BlendModes import blend_multiply

# Custom Packages
from DocumentationCSS.Objects.RuleGenerator import RuleGenerator
from DocumentationCSS.BaseLibrary.Colors import (
    AI_COLORS,
    HEADER_COLORS, PYTHON_PACKAGE_COLORS, WEBSITE_NAME_COLORS
)
from DocumentationCSS.BaseLibrary.Selectors import (
    class_markdown_rendered,class_publish_article_heading,
    HEADERS,
    AI_CLASSES, PYTHON_PACKAGE_CLASSES, WEBSITE_NAME_CLASSES
)
from DocumentationCSS.BaseLibrary.Content import line_seperation


# ----------------------------------------------------------------------------------------------------------------------
# - MetaDataHide -
# ----------------------------------------------------------------------------------------------------------------------
class MetaDataHide(RuleGenerator):
    @classmethod
    def rule_comment(cls):
        yield line_seperation
        yield CSSComment("- Special Rule to make all meta data dissapear from the view -")
        yield line_seperation

    @classmethod
    def rule(cls):
        with (rule:=CSSRule(one_line_overwrite=True)) as (selectors, declarations):  # type: ManagerSelectors, ManagerDeclarations
            selectors.add_descendants(
                class_markdown_rendered(CSSClass("metaDataHide")), # page class
                ElementLib.Div(CSSClass("frontmatter-container")) # actual container which displays the metadata block
            )
            declarations.add(
                PropertyLibrary.Display(None)
            )
        yield rule
