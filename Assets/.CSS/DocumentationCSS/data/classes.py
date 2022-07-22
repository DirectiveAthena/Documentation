# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library
import AthenaLib.HTML.models.html_library as HtmlLib

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - general classes -
# ----------------------------------------------------------------------------------------------------------------------
CLASS_MARKDOWN_RENDERED = "markdown-rendered"
CLASS_PUBLISH_ARTICLE_HEADING = "publish-article-heading"
CLASS_MARKDOWN_EMBED = "markdown-embed"
CLASS_MARKDOWN_EMBED_TITLE = "markdown-embed-title"
CLASS_MARKDOWN_EMBED_LINK = "markdown-embed-link"
CLASS_MARKDOWN_PREVIEW_VIEW = "markdown-preview-view"

HEADERS = (HtmlLib.H1,HtmlLib.H2,HtmlLib.H3,HtmlLib.H4,HtmlLib.H5,HtmlLib.H6)


# ----------------------------------------------------------------------------------------------------------------------
# - AI classes -
# ----------------------------------------------------------------------------------------------------------------------
CLASS_ADAM = "adam"
CLASS_AERO = "aero"
CLASS_ATHENA = "athena"
CLASS_CERES = "ceres"
CLASS_EVA = "eva"
CLASS_JUPITER = "jupiter"
CLASS_MINERVA = "minerva"
CLASS_NEPTUNE = "neptune"
CLASS_PLUTO = "pluto"
CLASS_SOL = "sol"
CLASS_VENUS = "venus"
CLASS_VERITAS = "veritas"
CLASS_VULCANUS = "vulcanus"

AI_CLASSES = (
    CLASS_ADAM,CLASS_AERO,CLASS_ATHENA,CLASS_CERES,CLASS_EVA,CLASS_JUPITER,CLASS_MINERVA,CLASS_NEPTUNE,CLASS_PLUTO,
    CLASS_SOL,CLASS_VENUS,CLASS_VERITAS,CLASS_VULCANUS,
)

# ----------------------------------------------------------------------------------------------------------------------
# - Python Package classes -
# ----------------------------------------------------------------------------------------------------------------------
CLASS_ATHENACOLOR = "athenacolor"
CLASS_ATHENALIB = "athenalib"

PYTHON_PACKAGE_CLASSES = (CLASS_ATHENACOLOR, CLASS_ATHENALIB)

# ----------------------------------------------------------------------------------------------------------------------
# - Website Name classes -
# ----------------------------------------------------------------------------------------------------------------------
CLASS_DISCORD= "discord"
CLASS_TWITCH= "twitch"
CLASS_TWITTER= "twitter"
CLASS_YOUTUBE= "youtube"

WEBSITE_NAME_CLASSES = (CLASS_DISCORD,CLASS_TWITCH,CLASS_TWITTER,CLASS_YOUTUBE,)