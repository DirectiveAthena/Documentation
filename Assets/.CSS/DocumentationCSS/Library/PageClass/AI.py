# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaCSS import (
    CSSRule, CSSComment, CSSCommentSeparator,
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
from DocumentationCSS.Library.Colors import background_secondary, background_primary
from DocumentationCSS.Objects.RuleGenerator import RuleGenerator
from DocumentationCSS.Library.Selectors import (
    class_markdown_rendered,class_publish_article_heading,
    HEADERS,
    class_adam
)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Page_AI(RuleGenerator):

    @classmethod
    def rule_comment(cls):
        yield CSSCommentSeparator()
        yield CSSComment("- Page Class for 'adam' -")
        yield CSSCommentSeparator()

    @classmethod
    def rule(cls):

        for ai in (class_adam,) :
            for header in zip(
                    HEADERS,
                    # h1            h2                  h3              h4              h5          h6
                    (Color.White,   RGB())
            :
                with (rule:=CSSRule()) as (selectors, declarations): #type: ManagerSelectors, ManagerDeclarations
                    selectors.add_descendants(
                        class_markdown_rendered(ai),
                        header
                    ).add_descendants(
                        class_markdown_rendered(ai),
                        header(class_publish_article_heading)
                    ).add(
                        header(ai)
                    )

                    declarations

                yield rule