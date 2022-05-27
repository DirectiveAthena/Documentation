# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class RuleGenerator:
    @classmethod
    def rule_comment(cls):
        yield

    @classmethod
    def rule(cls):
        yield

    @classmethod
    def generate(cls):
        for rule_comment in cls.rule_comment():
            yield rule_comment
        for rule in cls.rule():
            yield rule