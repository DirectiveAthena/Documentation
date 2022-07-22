# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library
from AthenaColor import RGB
from AthenaCSS.models.athenalib_imports import (Degree, Percent)

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
COLOR_ATHENACOLOR:str = ",".join((
    Degree(90),
    " ".join(str(n) for n in (RGB(255,0,0), Percent(0))),
    " ".join(str(n) for n in (RGB(255,0,0), Percent(0))),
    " ".join(str(n) for n in (RGB(255,154,0), Percent(10))),
    " ".join(str(n) for n in (RGB(255,154,0), Percent(10))),
    " ".join(str(n) for n in (RGB(208,222,33), Percent(20))),
    " ".join(str(n) for n in (RGB(79,220,74), Percent(30))),
    " ".join(str(n) for n in (RGB(63,218,216), Percent(40))),
    " ".join(str(n) for n in (RGB(47,201,226), Percent(50))),
    " ".join(str(n) for n in (RGB(28,127,238), Percent(60))),
    " ".join(str(n) for n in (RGB(95,21,242), Percent(70))),
    " ".join(str(n) for n in (RGB(186,12,248), Percent(80))),
    " ".join(str(n) for n in (RGB(251,7,217), Percent(90))),
    " ".join(str(n) for n in (RGB(255,0,0), Percent(100))),
))

COLOR_ATHENALIB:str = ",".join((
    Degree(90),
    " ".join(str(n) for n in (RGB(207,30,70), Percent(0))),
    " ".join(str(n) for n in (RGB(57,81,163), Percent(100))),
))
