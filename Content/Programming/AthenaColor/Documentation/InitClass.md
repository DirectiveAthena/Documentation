---
copyright: "Andreas Sas 2022"
created: "2022-04-23 17:09"
cssclass: athenacolor
---
# AthenaColor InitClass
An InitClass object is used by the package to use setting across the package.
This is mostly used to set package wide defaults or

*class* AthenaColor.**InitClass()**
   - One instance of the class is used under `AthenaColor.init`. Use this object to edit properties mentioned down below

---
*property* InitClass.**esc**:
^esc
- the specific escape code to be used, default set to `\x1b`

---
*property* InitClass.**transparentDefault**:
^transparentDefault
- Allows for an integer value between 0 and 255, or the equivalent hex value. Used for non transparent color to transparent color conversions which need to "create" a non existent transparent value
- Default set to `255`

---
*property* InitClass.**decimalPlaces**:
^decimalPlaces
- Used for rounding functions, to set the to be stored decimal places. Default is 3 decimal places

---
*property* InitClass.**stringSeperation**:
^decimalPlaces
- Used for string returns of colors, defines the separation character between values. Default is set to `;`