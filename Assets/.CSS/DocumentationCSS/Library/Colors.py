# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaColor import RGB
from AthenaColor.Color.HtmlColors import HtmlColorObjects as Color


# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - general colors -
# ----------------------------------------------------------------------------------------------------------------------
background_primary = RGB(32,32,32)
background_secondary =RGB(22,22,22)

BLEND_HEADER_COLORS = (Color.White, RGB(221, 221, 221), RGB(204, 204, 204), RGB(153, 153, 153), RGB(119, 119, 199), RGB(85, 85, 85))

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
# - Website colors -
# ----------------------------------------------------------------------------------------------------------------------
color_youtube=    RGB(255, 0  , 0  )
color_twitch=     RGB(169, 112, 255)
color_twitter=    RGB(26 , 140, 216)
color_discord=    RGB(86 , 98 , 246)