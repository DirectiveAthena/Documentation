---
copyright: "Andreas Sas 2022"
created: "2022-05-03 12:28"
cssclass: metaDataHide athenacolor
aliases: [Tuple Conversion]
---

# AthenaColor Color Tuple Conversion
All following functions do not create [[ColorSystems| Color System objects]] but rather return a tuple of the corresponding color format.

## Color conversions to RGB tuple

*function* AthenaColor.ColorTupleConversion.**hex_to_rgb(**`hexadecimal:str`**) ->** `tuple[int,int,int]`
- Function to convert a hexadecimal string to a rgb tuple.
- A `hexadecimal` can start with or without the ``