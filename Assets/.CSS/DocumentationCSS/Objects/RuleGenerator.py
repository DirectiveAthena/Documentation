# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Generator

# Custom Library
from AthenaCSS import CSSRule, CSSComment, CSSCommentSeparator

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class RuleGenerator:
    start_seperator:bool=False
    end_seperator:bool=False

    @classmethod
    def rule_comment(cls) -> Generator[CSSComment]:
        """A comment block meant to come right before the actual CSS rules """
        yield

    @classmethod
    def rule(cls) -> Generator[CSSRule]:
        """The actual CSS rule"""
        yield

    @classmethod
    def generate(cls):
        # Start the rule with a seperator comment
        if cls.start_seperator:
            yield CSSCommentSeparator()

        for rule_comment in cls.rule_comment():
            if rule_comment is not None:
                yield rule_comment

        for rule in cls.rule():
            if rule is not None:
                yield rule

        # End the rule with a seperator comment
        if cls.end_seperator:
            yield CSSCommentSeparator()