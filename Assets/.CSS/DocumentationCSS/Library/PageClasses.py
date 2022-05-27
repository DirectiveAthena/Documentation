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
# - Support Code Code -
# ----------------------------------------------------------------------------------------------------------------------
def header_border_solid(page_name, color):
    selector_class_page = class_markdown_rendered(page_name)
    for header, color_multiply in zip(HEADERS, HEADER_COLORS):
        with (rule := CSSRule(one_line_overwrite=True)) as (selectors, declarations):  # type: ManagerSelectors, ManagerDeclarations
            selectors.add_descendants(
                selector_class_page, header
            ).add_descendants(
                selector_class_page, header(class_publish_article_heading)
            ).add(
                header(page_name)
            )

            declarations.add(
                PropertyLibrary.BorderColor(blend_multiply(color, color_multiply))
            )
        yield rule

def header_border_image(page_name, color):
    selector_class_page = class_markdown_rendered(page_name)
    for header, color_multiply in zip(HEADERS, HEADER_COLORS):
        with (rule := CSSRule(one_line_overwrite=True)) as (selectors, declarations):  # type: ManagerSelectors, ManagerDeclarations
            selectors.add_descendants(
                selector_class_page, header
            ).add_descendants(
                selector_class_page, header(class_publish_article_heading)
            ).add(
                header(page_name)
            )

            if header == ElementLib.H1:
                declarations.add(
                    PropertyLibrary.BorderImageSource(color),
                    PropertyLibrary.BorderImageSlice(1)
                )
            else:
                declarations.add(
                    PropertyLibrary.BorderColor(color_multiply)
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
            for header in header_border_solid(
                    page_name=page_name,
                    color=color
                ):
                yield header
            # seperate every AI name with a line, for better visibilty in file
            yield line_seperation

# ----------------------------------------------------------------------------------------------------------------------
class PagePythonPackages(RuleGenerator):
    @classmethod
    def rule_comment(cls):
        yield line_seperation
        yield CSSComment("- Page Class for Python Packages -")
        yield line_seperation

    @classmethod
    def rule(cls):
        for page_name, color in zip(PYTHON_PACKAGE_CLASSES,PYTHON_PACKAGE_COLORS):
            for header in header_border_image(
                    page_name=page_name,
                    color=color,
                ):
                yield header
            # seperate every AI name with a line, for better visibilty in file
            yield line_seperation

# ----------------------------------------------------------------------------------------------------------------------
class PageWebsites(RuleGenerator):
    @classmethod
    def rule_comment(cls):
        yield line_seperation
        yield CSSComment("- Page Class for Websites -")
        yield line_seperation

    @classmethod
    def rule(cls):
        for page_name, color in zip(WEBSITE_NAME_CLASSES,WEBSITE_NAME_COLORS):
            for header in header_border_solid(
                    page_name=page_name,
                    color=color,
            ):
                yield header
            # seperate every AI name with a line, for better visibilty in file
            yield line_seperation
