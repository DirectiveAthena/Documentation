---
copyright: "Andreas Sas 2022"
created: "2022-05-03 12:38"
cssclass: metaDataHide athenacolor
aliases: [General Use Case Functions]
---
# AthenaColor General Use Case Functions
## Constraints
*function* AthenaColor.Functions.Constraints.**Constrain(**`value`, `maximum`, `minimum=0`,**) **
- Constrains a given `value` between the `maximum` and `minimum`
- Will throw a [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) if `minimum` is larger than `maximum`
- Serves as the base constrain function to the other ones written down below

---
*function* AthenaColor.Functions.Constraints.**ConstrainHSV(**`h`, `s`, `v`,**) ** ^77c3be
- Constrains the `h` value to within 0 and 360 (both including)
- Constrains the `s` and `v` vales within 0 and 1 (both including)


---
*function* AthenaColor.Functions.Constraints.**ConstrainHSL(**`h`, `s`, `l`,**) ** ^4c0c46
- Constrains the `h` value to within 0 and 360 (both including)
- Constrains the `s` and `l` vales within 0 and 1 (both including)


---
*function* AthenaColor.Functions.Constraints.**ConstrainCMYK(**`c`, `m`, `y`, `k`**) ** ^eb4997
- Constrains the `c`, `m`, `y` and `k` vales within 0 and 1 (both including)


---
*function* AthenaColor.Functions.Constraints.**ConstrainRGBA(**`r`, `g`, `b`, `a`**) **
- Constrains the `r`, `g`, `b` and `a` vales within 0 and 255 (both including)


---
*function* AthenaColor.Functions.Constraints.**ConstrainRGB(**`r`, `g`, `b`**) **
- Constrains the `r`, `g` and `b` vales within 0 and 255 (both including)

## General
*function* AthenaColor.Functions.General.**StrictType(**`object_`, `type_`**) ->** `object_` ^485f78
- Raises a [TypeError](https://docs.python.org/3/library/exceptions.html#TypeError) on failure of the Type Check of the `object_`
- Returns the `object_` unmodified

---
