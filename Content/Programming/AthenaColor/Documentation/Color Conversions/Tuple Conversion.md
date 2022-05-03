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
>Only the actual conversion is shown below, not the type and length checking of the input string. The `hexadecimal` value used below is supposed to not have a leading `#`.
>```python
>rgb_tuple = tuple(int(hexadecimal[i:i + 2], 16) for i in (0, 2, 4))
>```

---
*function* AthenaColor.ColorTupleConversion.**hsv_to_rgb(**`h:int|float`, `s:int|float`, `v:int|float`**) ->** `tuple[int,int,int]` ^691e99
- Function to convert a hsv tuple to an rgb tuple.
- Value input is checked by [[General Use Case Functions#^485f78|StrictType Function]]
>[!code]- Conversion formula used
>Only the actual conversion is shown below, not the type and length checking of the input values. The Inserted value are constrained to their outer limits of [[General Use Case Functions#^77c3be|ConstrainHSV]].
>
>```python
>C = v*s  
>X = C*(1-math.fabs(math.fmod(h/60.0,2)-1))  
>  
># map rgb correctly  
>if      0   <= h < 60 :  r_,g_,b_ = C,X,0  
>elif    60  <= h < 120:  r_,g_,b_ = X,C,0  
>elif    120 <= h < 180:  r_,g_,b_ = 0,C,X  
>elif    180 <= h < 240:  r_,g_,b_ = 0,X,C  
>elif    240 <= h < 300:  r_,g_,b_ = X,0,C  
>else:                    r_,g_,b_ = C,0,X  # 5 <= h_ < 6  
>  
>m = v-C  
>  
>return (  
>    RoundHalfUp((r_ + m) * 255),  
>    RoundHalfUp((g_ + m) * 255),  
>    RoundHalfUp((b_ + m) * 255)  
>)
>```


---
*function* AthenaColor.ColorTupleConversion.**hsl_to_rgb(**`h:int|float`, `s:int|float`, `l:int|float`**) ->** `tuple[int,int,int]` ^691e99
- Function to convert a hsl tuple to an rgb tuple.
- Value input is checked by [[General Use Case Functions#^485f78|StrictType Function]]
>[!code]- Conversion formula used
>Only the actual conversion is shown below, not the type and length checking of the input values. The Inserted value are constrained to their outer limits of [[General Use Case Functions#^4c0c46|ConstrainHSL]].
>
>```python
>C = (1-math.fabs((2*l)-1))*s  
>X = C*(1-math.fabs(math.fmod(h/60,2)-1))  
>  
># map rgb correctly  
>if      0   <= h < 60 :  r_,g_,b_ = C,X,0  
>elif    60  <= h < 120:  r_,g_,b_ = X,C,0  
>elif    120 <= h < 180:  r_,g_,b_ = 0,C,X  
>elif    180 <= h < 240:  r_,g_,b_ = 0,X,C  
>elif    240 <= h < 300:  r_,g_,b_ = X,0,C  
>else:                    r_,g_,b_ = C,0,X  
>  
>m = l-(C/2)  
>  
>return (  
>    RoundHalfUp((r_ + m) * 255),  
>    RoundHalfUp((g_ + m) * 255),  
>    RoundHalfUp((b_ + m) * 255)  
>)
>```


---
*function* AthenaColor.ColorTupleConversion.**cmyk_to_rgb(**`c:int|float`, `m:int|float`, `y:int|float`, `k:int|float`**) ->** `tuple[int,int,int]` ^691e99
- Function to convert an cmyk tuple to an rgb tuple.
- Value input is checked by [[General Use Case Functions#^485f78|StrictType Function]]

