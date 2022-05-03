---
copyright: "Andreas Sas 2022"
created: "2022-05-03 12:28"
cssclass: metaDataHide athenacolor
aliases: [Tuple Conversion]
---

# AthenaColor Color Tuple Conversion
All following functions do not create [[ColorSystems| Color System objects]] but rather return a tuple of the corresponding color format.

## Color conversions to RGB tuple

*function* AthenaColor.ColorTupleConversion.**hex_to_rgb(**`hexadecimal:str`**) ->** `tuple[int,int,int]` ^ad1b2e
- Function to convert a hexadecimal string to an rgb tuple.
- A `hexadecimal` can start with or without the leading `#`
- If the length of the string cannot be parsed, it will throw a [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)

---
*function* AthenaColor.ColorTupleConversion.**hsv_to_rgb(**`h:int|float`,`s:int|float`,`v:int|float`**) ->** `tuple[int,int,int]` ^691e99
- Function to convert a hsv tuple to an rgb tuple.
- On wrong value input, the 
