# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaCSS import (
    CSSRule, CSSComment, CSSCommentSeparator,CSSClass,
    PropertyLibrary,
    SubPropertyLibrary
)
from AthenaCSS.Generator.ManagerCSSRule import ManagerSelectors, ManagerDeclarations

from AthenaColor import RGB
from AthenaColor.Color.BlendModes import blend_multiply
from AthenaColor.Color.HtmlColors import HtmlColorObjects as Color

from AthenaLib.Types.RelativeLength import (
    RootElementFontSize as REM,
    ElementFontSize as EM
)
from AthenaLib.Types.AbsoluteLength import Pixel
from AthenaLib.Types.Math import Degree, Percent

# Custom Packages
from DocumentationCSS.Library.Colors import (
    background_secondary, background_primary,
    AI_COLORS,
    BLEND_HEADER_COLORS
)
from DocumentationCSS.Objects.RuleGenerator import RuleGenerator
from DocumentationCSS.Library.Selectors import (
    class_markdown_rendered,class_publish_article_heading,
    HEADERS,
    AI_CLASSES
)
from DocumentationCSS.Library.Content import line_seperation

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class PageAI(RuleGenerator):

    @classmethod
    def rule_comment(cls):
        yield line_seperation
        yield CSSComment("- Page Class for named Artificial Intelligences -")
        yield line_seperation

    @classmethod
    def rule(cls):

        for ai, ai_color in zip(AI_CLASSES,AI_COLORS):
            for header, color_multiply in zip(HEADERS,BLEND_HEADER_COLORS):
                selector_class_ai = class_markdown_rendered(ai)
                with (rule:=CSSRule(one_line_overwrite=True)) as (selectors, declarations): #type: ManagerSelectors, ManagerDeclarations
                    selectors.add_descendants(
                        selector_class_ai,
                        header
                    ).add_descendants(
                        selector_class_ai,
                        header(class_publish_article_heading)
                    ).add(
                        header(ai)
                    )

                    declarations.add(
                        PropertyLibrary.BorderColor(blend_multiply(ai_color, color_multiply))
                    )

                yield rule
            # seperate every AI name with a line, for better visibilty in file
            yield line_seperation