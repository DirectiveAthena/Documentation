---
copyright: "Andreas Sas 2022"
created: "2022-05-03 12:38"
cssclass: metaDataHide athenacolor
aliases: [General Use Case Functions]
---
# AthenaColor General Use Case Functions
## Constraints
*function* AthenaColor.Functions.Constraints.**ConstrainHSV(**`h`, `s`,`v`,**) **
- Constrains the `h` value to within 0 and 3

## General
*function* AthenaColor.Functions.General.**StrictType(**`object_`, `type_`**) ->** `object_` ^485f78
- Raises a [TypeError](https://docs.python.org/3/library/exceptions.html#TypeError) on failure of the Type Check of the `object_`
- Returns the `object_` unmodified

---
