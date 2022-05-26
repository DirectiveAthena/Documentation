---
copyright: "Andreas Sas 2022"
created: "2022-05-26 13:52"
cssclass: metaDataHide athenacolor
aliases: [RgbControlled]
---

# AthenaColor: RgbControlled
*class* AthenaColor.Console.Styling.Inline.**RgbControlled(**`param_code:str`**)**
- RgbControlled is a base class for the inline style formatting of some text.
- It simply creates an object with all the [[HTML Named Colors]] as it's attributes, with it's values being the color itself preceded by the correct escaping and defining ANSI characters.
    - Calls on the [[ANSI Sequences#^7dd891|ColorSequence]] function to create this string value.
- uses `__slots__` to define it's attributes

---
*method* RgbControlled.**custom(**`color:RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA`**)**
- Allows you to use a custom RGB object to define the output color.
- Uses the correctly defined parameter code for the specific part of the styling it should output
