# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaColor import RGB
from AthenaCSS.models.generator import CSSGenerator
from AthenaLib.HTML.models.css import CSSProperty, CSSComment, CSSRule, CSSSelection, CSSSelectionType
import AthenaLib.HTML.models.html_library as HtmlLib
from AthenaLib.HTML.models.html import HTMLElement

# Custom Packages
from DocumentationCSS.Objects.RuleGenerator import RuleGenerator
from DocumentationCSS.BaseLibrary.Colors import (
    color_pluto,
)
from DocumentationCSS.BaseLibrary.Content import line_seperation


# ----------------------------------------------------------------------------------------------------------------------
# - MetaDataHide -
# ----------------------------------------------------------------------------------------------------------------------
class ObsidianStatusBar(RuleGenerator):
    @classmethod
    def rule_comment(cls):
        yield line_seperation
        yield CSSComment("- Special Rules to affect the status bar -")
        yield line_seperation

    @classmethod
    def rule(cls):
        # Chages the status bar
        with (rule1:=CSSRule()) as (selectors, declarations):  # type: ManagerSelectors, ManagerDeclarations
            selectors.add(
                ElementLib.Div(CSSClass("status-bar"))
            )
            declarations.add(
                PropertyLibrary.BackgroundColor(color_pluto),
                PropertyLibrary.Color(RGB(184, 184, 184))
            )
        yield rule1

        #changes the status icon for obsidianSYNC
        with (rule2:=CSSRule(one_line_overwrite=True)) as (selectors, declarations):
            selectors.add(
                ElementLib.Span(CSSClass("sync-status-icon", "mod-working"))
            )
            declarations.add(
                PropertyLibrary.Color(RGB(47, 36, 97))
            )
        yield rule2
