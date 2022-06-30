# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaCSS import (
    CSSRule, CSSComment, CSSClass,
    Property as PropertyLibrary,
    SelectorElement as ElementLib
)
from AthenaCSS.models.generator.manager_rule import ManagerSelectors, ManagerDeclarations
from AthenaCSS.models.athenalib_imports import (
    Pixel,
)

from AthenaColor import RGB

# Custom Packages
from DocumentationCSS.Objects.RuleGenerator import RuleGenerator
from DocumentationCSS.BaseLibrary.Selectors import (
    class_markdown_rendered, class_markdown_embed, class_markdown_preview_view, class_markdown_embed_title,
    class_markdown_embed_link, todo_project
)
from DocumentationCSS.BaseLibrary.Content import line_seperation


# ----------------------------------------------------------------------------------------------------------------------
# - MetaDataHide -
# ----------------------------------------------------------------------------------------------------------------------
class MetaDataHide(RuleGenerator):
    # Special class used to define this set of rules
    MetaDataHide = CSSClass("metaDataHide")

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

# ----------------------------------------------------------------------------------------------------------------------
# - FileEmbed -
# ----------------------------------------------------------------------------------------------------------------------
class FileEmbed(RuleGenerator):
    # Special class used to define this set of rules
    FileEmbed = CSSClass("cleanEmbed")

    @classmethod
    def rule_comment(cls):
        yield line_seperation
        yield CSSComment("- Special Rule to make the File Embedded title hide -")
        yield line_seperation

    @classmethod
    def rule(cls):
        with (rule1:=CSSRule()) as (selectors, declarations):  # type: ManagerSelectors, ManagerDeclarations
            selectors.add_descendants(
                class_markdown_rendered(cls.FileEmbed),
                class_markdown_embed
            ).add_descendants(
                class_markdown_rendered(cls.FileEmbed),
                class_markdown_embed,
                class_markdown_preview_view
            )
            declarations.add(
                PropertyLibrary.Border(),
                PropertyLibrary.Padding(Pixel(0)),
                PropertyLibrary.Margin(Pixel(0)),
            )
        yield rule1

        with (rule2:=CSSRule()) as (selectors, declarations):  # type: ManagerSelectors, ManagerDeclarations
            selectors.add_descendants(
                class_markdown_rendered(cls.FileEmbed),
                class_markdown_embed_link
            ).add_descendants(
                class_markdown_rendered(cls.FileEmbed),
                class_markdown_embed_link
            )
            declarations.add(
                PropertyLibrary.Display(None)
            )
        yield rule2

        with (rule3:=CSSRule()) as (selectors, declarations):  # type: ManagerSelectors, ManagerDeclarations
            selectors.add(todo_project)
            declarations.add(
                PropertyLibrary.Color(RGB(25,25,25)),
                PropertyLibrary.FontWeight("bold")
            )
        yield rule3