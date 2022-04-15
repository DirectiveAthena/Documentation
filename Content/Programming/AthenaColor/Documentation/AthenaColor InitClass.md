---
cssclass: athenacolor
---
# AthenaColor InitClass
An InitClass object is used by the package to use setting across the package.

*class* AthenaColor.**InitClass(**`r:int=0`, `g:int=0`, `b:int=0`**)**
   - One instance of the class is used under `AthenaColor.init`. Use this object to edit properties mentioned down below

---
*property* InitClass.**roundUp**:
^roundUp
- A boolean setting, which when set to true, will always set functions which need to round floats to integers to round 0.5 values upwards.