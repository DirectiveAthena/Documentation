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
    "pink": "rgba(255, 102, 255,0.5)",
    "blue_dark": "rgba(0, 102, 255,0.5)",
    "blue": "rgba(0, 204, 255,0.5)",
    "green": "rgba(51, 204, 51,0.5)",
    "yellow": "rgba(255, 255, 102,0.5)",
    "orange": "rgba(255, 153, 0,0.5)",
    "purple": "rgba(153, 0, 153,0.5)",
}

# ----------------------------------------------------------------------------------------------------------------------
# - All AthenaColor Colors (aka defined css colors) -
# ----------------------------------------------------------------------------------------------------------------------
COLORS = {
    "Maroon" : Color.Maroon,
    "DarkRed" : Color.DarkRed,
    "Brown" : Color.Brown,
    "Firebrick" : Color.Firebrick,
    "Crimson" : Color.Crimson,
    "Red" : Color.Red,
    "Tomato" : Color.Tomato,
    "Coral" : Color.Coral,
    "IndianRed" : Color.IndianRed,
    "LightCoral" : Color.LightCoral,
    "DarkSalmon" : Color.DarkSalmon,
    "Salmon" : Color.Salmon,
    "LightSalmon" : Color.LightSalmon,
    "OrangeRed" : Color.OrangeRed,
    "DarkOrange" : Color.DarkOrange,
    "Orange" : Color.Orange,
    "Gold" : Color.Gold,
    "DarkGoldenRod" : Color.DarkGoldenRod,
    "GoldenRod" : Color.GoldenRod,
    "PaleGoldenRod" : Color.PaleGoldenRod,
    "DarkKhaki" : Color.DarkKhaki,
    "Khaki" : Color.Khaki,
    "Olive" : Color.Olive,
    "Yellow" : Color.Yellow,
    "YellowGreen" : Color.YellowGreen,
    "DarkOliveGreen" : Color.DarkOliveGreen,
    "OliveDrab" : Color.OliveDrab,
    "LawnGreen" : Color.LawnGreen,
    "Chartreuse" : Color.Chartreuse,
    "GreenYellow" : Color.GreenYellow,
    "DarkGreen" : Color.DarkGreen,
    "Green" : Color.Green,
    "ForestGreen" : Color.ForestGreen,
    "Lime" : Color.Lime,
    "LimeGreen" : Color.LimeGreen,
    "LightGreen" : Color.LightGreen,
    "PaleGreen" : Color.PaleGreen,
    "DarkSeaGreen" : Color.DarkSeaGreen,
    "MediumSpringGreen" : Color.MediumSpringGreen,
    "SpringGreen" : Color.SpringGreen,
    "SeaGreen" : Color.SeaGreen,
    "MediumAquaMarine" : Color.MediumAquaMarine,
    "MediumSeaGreen" : Color.MediumSeaGreen,
    "LightSeaGreen" : Color.LightSeaGreen,
    "DarkSlateGray" : Color.DarkSlateGray,
    "Teal" : Color.Teal,
    "DarkCyan" : Color.DarkCyan,
    "Aqua" : Color.Aqua,
    "Cyan" : Color.Cyan,
    "LightCyan" : Color.LightCyan,
    "DarkTurquoise" : Color.DarkTurquoise,
    "Turquoise" : Color.Turquoise,
    "MediumTurquoise" : Color.MediumTurquoise,
    "PaleTurquoise" : Color.PaleTurquoise,
    "AquaMarine" : Color.AquaMarine,
    "PowderBlue" : Color.PowderBlue,
    "CadetBlue" : Color.CadetBlue,
    "SteelBlue" : Color.SteelBlue,
    "CornFlowerBlue" : Color.CornFlowerBlue,
    "DeepSkyBlue" : Color.DeepSkyBlue,
    "DodgerBlue" : Color.DodgerBlue,
    "LightBlue" : Color.LightBlue,
    "SkyBlue" : Color.SkyBlue,
    "LightSkyBlue" : Color.LightSkyBlue,
    "MidnightBlue" : Color.MidnightBlue,
    "Navy" : Color.Navy,
    "DarkBlue" : Color.DarkBlue,
    "MediumBlue" : Color.MediumBlue,
    "Blue" : Color.Blue,
    "RoyalBlue" : Color.RoyalBlue,
    "BlueViolet" : Color.BlueViolet,
    "Indigo" : Color.Indigo,
    "DarkSlateBlue" : Color.DarkSlateBlue,
    "SlateBlue" : Color.SlateBlue,
    "MediumSlateBlue" : Color.MediumSlateBlue,
    "MediumPurple" : Color.MediumPurple,
    "DarkMagenta" : Color.DarkMagenta,
    "DarkViolet" : Color.DarkViolet,
    "DarkOrchid" : Color.DarkOrchid,
    "MediumOrchid" : Color.MediumOrchid,
    "Purple" : Color.Purple,
    "Thistle" : Color.Thistle,
    "Plum" : Color.Plum,
    "Violet" : Color.Violet,
    "Magenta" : Color.Magenta,
    "Orchid" : Color.Orchid,
    "MediumVioletRed" : Color.MediumVioletRed,
    "PaleVioletRed" : Color.PaleVioletRed,
    "DeepPink" : Color.DeepPink,
    "HotPink" : Color.HotPink,
    "LightPink" : Color.LightPink,
    "Pink" : Color.Pink,
    "AntiqueWhite" : Color.AntiqueWhite,
    "Beige" : Color.Beige,
    "Bisque" : Color.Bisque,
    "BlanchedAlmond" : Color.BlanchedAlmond,
    "Wheat" : Color.Wheat,
    "CornSilk" : Color.CornSilk,
    "LemonChiffon" : Color.LemonChiffon,
    "LightGoldenRodYellow" : Color.LightGoldenRodYellow,
    "LightYellow" : Color.LightYellow,
    "SaddleBrown" : Color.SaddleBrown,
    "Sienna" : Color.Sienna,
    "Chocolate" : Color.Chocolate,
    "Peru" : Color.Peru,
    "SandyBrown" : Color.SandyBrown,
    "BurlyWood" : Color.BurlyWood,
    "Tan" : Color.Tan,
    "RosyBrown" : Color.RosyBrown,
    "Moccasin" : Color.Moccasin,
    "NavajoWhite" : Color.NavajoWhite,
    "PeachPuff" : Color.PeachPuff,
    "MistyRose" : Color.MistyRose,
    "LavenderBlush" : Color.LavenderBlush,
    "Linen" : Color.Linen,
    "OldLace" : Color.OldLace,
    "PapayaWhip" : Color.PapayaWhip,
    "WeaShell" : Color.WeaShell,
    "MintCream" : Color.MintCream,
    "SlateGray" : Color.SlateGray,
    "LightSlateGray" : Color.LightSlateGray,
    "LightSteelBlue" : Color.LightSteelBlue,
    "Lavender" : Color.Lavender,
    "FloralWhite" : Color.FloralWhite,
    "AliceBlue" : Color.AliceBlue,
    "GhostWhite" : Color.GhostWhite,
    "Honeydew" : Color.Honeydew,
    "Ivory" : Color.Ivory,
    "Azure" : Color.Azure,
    "Snow" : Color.Snow,
    "Black" : Color.Black,
    "DimGray" : Color.DimGray,
    "Gray" : Color.Gray,
    "DarkGray" : Color.DarkGray,
    "Silver" : Color.Silver,
    "LightGray" : Color.LightGray,
    "Gainsboro" : Color.Gainsboro,
    "WhiteSmoke" : Color.WhiteSmoke,
    "White" : Color.White,
}