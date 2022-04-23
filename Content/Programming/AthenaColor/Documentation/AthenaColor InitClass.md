---
copyright: "Andreas Sas 2022"
created: "2022-04-23 17:09"
cssclass: athencolor
---
# AthenaColor InitClass
An InitClass object is used by the package to use setting across the package.

*class* AthenaColor.**InitClass(**`r:int=0`, `g:int=0`, `b:int=0`**)**
   - One instance of the class is used under `AthenaColor.init`. Use this object to edit properties mentioned down below

---
*property* InitClass.**roundUp**:
^roundUp
- A boolean setting, which when set to true, will always set functions which need to round floats to integers to round 0.5 values upwards.

---
*property* InitClass.**esc**:
^esc
- the specific escape code to be used, default set to `\x1b`

---
*property* InitClass.**transparentDefault**:
^transparentDefault
- Allows for an integer value between 0 and 255, or the equivalent hex value. Used for non transparent color to transparent color conversions which need to "create" a non existent transparent value

---
*property* InitClass.**decimalPlaces**:
^decimalPlaces
- Used for rounding functions, to set the to be stored decimal places. Default is 3 decimal places