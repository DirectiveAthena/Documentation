# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaCSS import (
    CSSClass,
    SelectorElementLibrary as ElementLib,
)

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - general classes -
# ----------------------------------------------------------------------------------------------------------------------
class_markdown_rendered = CSSClass("markdown-rendered")
class_publish_article_heading = CSSClass("publish-article-heading")
class_markdown_embed = CSSClass("markdown-embed")
class_markdown_embed_title = CSSClass("markdown-embed-title")
class_markdown_embed_link = CSSClass("markdown-embed-link")
class_markdown_preview_view = CSSClass("markdown-preview-view")

HEADERS = (ElementLib.H1,ElementLib.H2,ElementLib.H3,ElementLib.H4,ElementLib.H5,ElementLib.H6)


# ----------------------------------------------------------------------------------------------------------------------
# - AI classes -
# ----------------------------------------------------------------------------------------------------------------------
class_adam = CSSClass("adam")
class_aero = CSSClass("aero")
class_athena = CSSClass("athena")
class_ceres = CSSClass("ceres")
class_eva = CSSClass("eva")
class_jupiter = CSSClass("jupiter")
class_minerva = CSSClass("minerva")
class_neptune = CSSClass("neptune")
class_pluto = CSSClass("pluto")
class_sol = CSSClass("sol")
class_venus = CSSClass("venus")
class_veritas = CSSClass("veritas")
class_vulcanus = CSSClass("vulcanus")

AI_CLASSES = (class_adam,class_aero,class_athena,class_ceres,class_eva,class_jupiter,class_minerva,class_neptune,class_pluto,class_sol,class_venus,class_veritas,class_vulcanus,)

# ----------------------------------------------------------------------------------------------------------------------
# - Python Package classes -
# ----------------------------------------------------------------------------------------------------------------------
class_athenacolor = CSSClass("athenacolor")
class_athenalib = CSSClass("athenalib")

PYTHON_PACKAGE_CLASSES = (class_athenacolor, class_athenalib)

# ----------------------------------------------------------------------------------------------------------------------
# - Website Name classes -
# ----------------------------------------------------------------------------------------------------------------------
class_discord= CSSClass("discord")
class_twitch= CSSClass("twitch")
class_twitter= CSSClass("twitter")
class_youtube= CSSClass("youtube")

WEBSITE_NAME_CLASSES = (class_discord,class_twitch,class_twitter,class_youtube,)