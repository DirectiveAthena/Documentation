# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library
from AthenaColor import RGB
import AthenaColor.data.colors_html as Color

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - general colors -
# ----------------------------------------------------------------------------------------------------------------------
WHITE = Color.White

BACKGROUND_PRIMARY = RGB(32,32,32)
BACKGROUND_SECONDARY = RGB(22,22,22)

HEADER_COLORS = (WHITE, Color.Gainsboro, Color.Silver, Color.DarkGray, Color.Gray, Color.DimGray)

# ----------------------------------------------------------------------------------------------------------------------
# - AI colors -
# ----------------------------------------------------------------------------------------------------------------------
COLOR_ADAM = RGB(24,177,222)
COLOR_ATHENA = RGB(196,41,80)
COLOR_EVA = RGB(234,39,79)
COLOR_JUPITER = RGB(235,233,67)
COLOR_VERITAS = RGB(213,55,146)
COLOR_VULCANUS = RGB(236,133,33)
COLOR_NEPTUNE = RGB(66,115,185)
COLOR_MINERVA = RGB(105,59,144)
COLOR_SOL = RGB(246,231,134)
COLOR_AERO = RGB(251,251,251)
COLOR_VENUS = RGB(115,195,125)
COLOR_PLUTO = RGB(84,85,87)
COLOR_CERES = RGB(213,224,68)

AI_COLORS = (
    COLOR_ADAM,COLOR_AERO,COLOR_ATHENA,COLOR_CERES,COLOR_EVA,COLOR_JUPITER,COLOR_MINERVA,COLOR_NEPTUNE,COLOR_PLUTO,
    COLOR_SOL,COLOR_VENUS,COLOR_VERITAS,COLOR_VULCANUS
)

# ----------------------------------------------------------------------------------------------------------------------
# - Website Name colors -
# ----------------------------------------------------------------------------------------------------------------------
COLOR_DISCORD = RGB(86,98,246)
COLOR_TWITCH = RGB(169,112,255)
COLOR_TWITTER = RGB(26,140,216)
COLOR_YOUTUBE = RGB(255,0,0)

WEBSITE_NAME_COLORS = (COLOR_DISCORD,COLOR_TWITCH,COLOR_TWITTER,COLOR_YOUTUBE)

# ----------------------------------------------------------------------------------------------------------------------
# - MARKERS -
# ----------------------------------------------------------------------------------------------------------------------
MARKERS = {
    "pink": "rgba(255, 0, 255,0.5)",
    "blue": "rgba(51, 51, 255,0.5)",
    "green": "rgba(51, 204, 51,0.5)",
    "yellow": "rgba(255, 255, 102,0.5)",
}
