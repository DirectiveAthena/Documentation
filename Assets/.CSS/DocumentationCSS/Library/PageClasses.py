# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Callable

# Custom Library
from AthenaCSS import (
    CSSRule, CSSComment,
    PropertyLibrary,
    SelectorElementLibrary as ElementLib,
)
from AthenaCSS.Generator.ManagerCSSRule import ManagerSelectors, ManagerDeclarations

from AthenaColor.Color.BlendModes import blend_multiply

# Custom Packages
from DocumentationCSS.Library.Colors import (
    AI_COLORS,
    BLEND_HEADER_COLORS, PYTHON_PACKAGE_COLORS
)
from DocumentationCSS.Objects.RuleGenerator import RuleGenerator
from DocumentationCSS.Library.Selectors import (
    class_markdown_rendered,class_publish_article_heading,
    HEADERS,
    AI_CLASSES, PYTHON_PACKAGE_CLASSES
)
from DocumentationCSS.Library.Content import line_seperation

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code Code -
# ----------------------------------------------------------------------------------------------------------------------
def header_border(page_name, color, color_function:Callable):
    selector_class_page = class_markdown_rendered(page_name)
    for header, color_multiply in zip(HEADERS, BLEND_HEADER_COLORS):
        with (rule := CSSRule(one_line_overwrite=True)) as (selectors, declarations):  # type: ManagerSelectors, ManagerDeclarations
            selectors.add_descendants(
                selector_class_page, header
            ).add_descendants(
                selector_class_page, header(class_publish_article_heading)
            ).add(
                header(page_name)
            )

            declarations.add(
                PropertyLibrary.BorderColor(color_function(header, color, color_multiply))
            )
        yield rule

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
        for page_name, color in zip(AI_CLASSES,AI_COLORS):
            for header in header_border(
                    page_name=page_name,
                    color=color,
                    color_function= lambda _, color_, color_multiply: blend_multiply(color_, color_multiply)
                ):
                yield header
            # seperate every AI name with a line, for better visibilty in file
            yield line_seperation

class PagePythonPackages(RuleGenerator):
    @classmethod
    def rule_comment(cls):
        yield line_seperation
        yield CSSComment("- Page Class for Python Packages -")
        yield line_seperation

    @classmethod
    def rule(cls):
        for page_name, color in zip(PYTHON_PACKAGE_CLASSES,PYTHON_PACKAGE_COLORS):
            for header in header_border(
                    page_name=page_name,
                    color=color,
                    color_function= lambda h, color_, color_multiply: color_ if h == ElementLib.H1 else color_multiply
                ):
                yield header
            # seperate every AI name with a line, for better visibilty in file
            yield line_seperation