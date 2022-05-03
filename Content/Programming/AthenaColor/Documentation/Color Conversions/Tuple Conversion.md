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
- Value input is checked by [[General Use Case Functions#^485f78|StrictType Function]]
>[!code]- Conversion formula used
>Only the actual conversion is shown 
>```python
>rgb_tuple = tuple(int(hex_v[i:i + 2], 16) for i in (0, 2, 4))
>```

---
*function* AthenaColor.ColorTupleConversion.**hsv_to_rgb(**`h:int|float`,`s:int|float`,`v:int|float`**) ->** `tuple[int,int,int]` ^691e99
- Function to convert a hsv tuple to an rgb tuple.
- Value input is checked by [[General Use Case Functions#^485f78|StrictType Function]]


---
*function* AthenaColor.ColorTupleConversion.**hsl_to_rgb(**`h:int|float`,`s:int|float`,`l:int|float`**) ->** `tuple[int,int,int]` ^691e99
- Function to convert a hsl tuple to an rgb tuple.
- Value input is checked by [[General Use Case Functions#^485f78|StrictType Function]]


---
*function* AthenaColor.ColorTupleConversion.**cmyk_to_rgb(**`c:int|float`,`m:int|float`,`y:int|float`,`k:int|float`**) ->** `tuple[int,int,int]` ^691e99
- Function to convert an cmyk tuple to an rgb tuple.
- Value input is checked by [[General Use Case Functions#^485f78|StrictType Function]]

