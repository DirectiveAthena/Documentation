# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library
from AthenaColor import RGB
from AthenaColor import RGB
import AthenaColor.data.colors_html as Color
from AthenaCSS.models.athenalib_imports import (Degree, Percent)

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - general colors -
# ----------------------------------------------------------------------------------------------------------------------
background_primary = RGB(32,32,32)
background_secondary =RGB(22,22,22)

HEADER_COLORS = (Color.White,   Color.Gainsboro,    Color.Silver,   Color.DarkGray, Color.Gray, Color.DimGray)

# ----------------------------------------------------------------------------------------------------------------------
# - AI colors -
# ----------------------------------------------------------------------------------------------------------------------
color_adam=       RGB(24 , 177, 222)
color_athena=     RGB(196, 41 , 80 )
color_eva=        RGB(234, 39 , 79 )
color_jupiter=    RGB(235, 233, 67 )
color_veritas=    RGB(213, 55 , 146)
color_vulcanus=   RGB(236, 133, 33 )
color_neptune=    RGB(66 , 115, 185)
color_minerva=    RGB(105, 59 , 144)
color_sol=        RGB(246, 231, 134)
color_aero=       RGB(251, 251, 251)
color_venus=      RGB(115, 195, 125)
color_pluto=      RGB(84 , 85 , 87 )
color_ceres=      RGB(213, 224, 68 )

AI_COLORS = (color_adam,color_aero,color_athena,color_ceres,color_eva,color_jupiter,color_minerva,color_neptune,color_pluto,color_sol,color_venus,color_veritas,color_vulcanus)

# ----------------------------------------------------------------------------------------------------------------------
# - Python Package classes -
# ----------------------------------------------------------------------------------------------------------------------
color_athenacolor = (
    Degree(90),
    (RGB(255,0,0), Percent(0)),
    (RGB(255,0,0), Percent(0)),
    (RGB(255,154,0), Percent(10)),
    (RGB(255,154,0), Percent(10)),
    (RGB(208,222,33), Percent(20)),
    (RGB(79,220,74), Percent(30)),
    (RGB(63,218,216), Percent(40)),
    (RGB(47,201,226), Percent(50)),
    (RGB(28,127,238), Percent(60)),
    (RGB(95,21,242), Percent(70)),
    (RGB(186,12,248), Percent(80)),
    (RGB(251,7,217), Percent(90)),
    (RGB(255,0,0), Percent(100))
)
color_athenalib = SubPropertyLibrary.LinearGradient(
    Degree(90),
    (RGB(207,30,70), Percent(0)),
    (RGB(57,81,163), Percent(100))
)

PYTHON_PACKAGE_COLORS = (color_athenacolor, color_athenalib)
# ----------------------------------------------------------------------------------------------------------------------
# - Website Name colors -
# ----------------------------------------------------------------------------------------------------------------------
color_discord= RGB(255, 0  , 0  )
color_twitch= RGB(169, 112, 255)
color_twitter= RGB(26 , 140, 216)
color_youtube= RGB(86 , 98 , 246)

WEBSITE_NAME_COLORS = (color_discord,color_twitch,color_twitter,color_youtube,)
