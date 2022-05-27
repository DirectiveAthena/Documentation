# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaCSS import (
    CSSRule, CSSComment,
    PropertyLibrary,
    SubPropertyLibrary
)
from AthenaCSS.Generator.ManagerCSSRule import ManagerSelectors, ManagerDeclarations

from AthenaColor import RGB

from AthenaLib.Types.RelativeLength import (
    RootElementFontSize as REM,
    ElementFontSize as EM
)
from AthenaLib.Types.AbsoluteLength import Pixel
from AthenaLib.Types.Math import Degree, Percent

# Custom Packages
from DocumentationCSS.Objects.RuleGenerator import RuleGenerator

from DocumentationCSS.BaseLibrary.Colors import background_secondary, background_primary, HEADER_COLORS
from DocumentationCSS.BaseLibrary.Selectors import (
    class_markdown_rendered,class_publish_article_heading,
    HEADERS
)
from DocumentationCSS.BaseLibrary.Content import line_seperation

# ----------------------------------------------------------------------------------------------------------------------
# - Default for Header -
# ----------------------------------------------------------------------------------------------------------------------
class HeaderDefault(RuleGenerator):
    @classmethod
    def rule_comment(cls):
        yield line_seperation
        yield CSSComment("- All headers derive from this -")
        yield line_seperation

    @classmethod
    def rule(cls):
        with (rule := CSSRule()) as (selectors, declarations): #type: ManagerSelectors, ManagerDeclarations
            # SELECTORS of all headers:
            for header in HEADERS:
                selectors.add_descendants(
                    class_markdown_rendered,
                    header
                ).add_descendants(
                    class_markdown_rendered,
                    header(class_publish_article_heading)
                )

            # Properties
            declarations.add(
                PropertyLibrary.TextAlign("left"),
                PropertyLibrary.BackgroundColor(RGB(25,25,25)),
                PropertyLibrary.BackgroundImage(
                    SubPropertyLibrary.LinearGradient((
                        Degree(90),
                        (background_secondary, Percent(75)),
                        (background_primary, Percent(100)),
                        1 # important for some reason!
                    ))
                ),
                PropertyLibrary.BorderRadius(REM(.2)),
                PropertyLibrary.BorderBottomStyle("solid"),
                PropertyLibrary.BorderBottomWidth(Pixel(5))
            )

        # Yield the r
        yield rule

class HeaderSizing(RuleGenerator):
    @classmethod
    def rule_comment(cls):
        yield CSSComment("- Headers differ in size depending on the depth -")

    @classmethod
    def rule(cls):
        # premade these elements, as they stay consistent throughout the loop
        padding_left = PropertyLibrary.PaddingLeft(Pixel(35))

        for header, color, padding, font_size, margin_top in zip(
                HEADERS,
                # h1            h2                  h3              h4              h5          h6
                HEADER_COLORS,
                (Pixel(12),     Pixel(10),          Pixel(8),       Pixel(6),       Pixel(4),   Pixel(2)),
                (EM(2),         EM(1.8),            EM(1.6),        EM(1.4),        EM(1.2),    EM(1.1)),
                (None,          EM(2),              EM(1.75),       EM(1.5),        EM(1.25),   EM(1))
        ):
            with (rule := CSSRule()) as (selectors, declarations):
                selectors.add_descendants(
                    class_markdown_rendered,
                    header
                ).add_descendants(
                    class_markdown_rendered,
                    header(class_publish_article_heading)
                )
                declarations.add(
                    PropertyLibrary.Color(color),
                    PropertyLibrary.Padding(padding),
                    padding_left,
                    PropertyLibrary.FontSize(font_size)
                )
                if margin_top is not None:
                    declarations.add(PropertyLibrary.MarginTop(margin_top))

            yield rule