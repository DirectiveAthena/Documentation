# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import NamedTuple

# Custom Library
from AthenaColor import RGB

# Custom Packages
from DocumentationCSS.Objects.DefinedColors import Ai_Colors

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
AI_COLORS = Ai_Colors(
    adam=       RGB(24 , 177, 222),
    athena=     RGB(196, 41 , 80 ),
    eva=        RGB(234, 39 , 79 ),
    jupiter=    RGB(235, 233, 67 ),
    veritas=    RGB(213, 55 , 146),
    vulcanus=   RGB(236, 133, 33 ),
    neptune=    RGB(66 , 115, 185),
    minerva=    RGB(105, 59 , 144),
    sol=        RGB(246, 231, 134),
    aero=       RGB(251, 251, 251),
    venus=      RGB(115, 195, 125),
    pluto=      RGB(84 , 85 , 87 ),
    ceres=      RGB(213, 224, 68 ),
)