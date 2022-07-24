---
copyright: "Andreas Sas 2022"
created: "2022-07-21 19:34"
cssclass: metaDataHide athenalib
aliases: [AthenaLib Versions]
---

# AthenaLib Version Notes
These are the version notes for the [[AthenaLib]] package


## v1.6.0
- A simple addition to the Library: "Force one line" for a CSSRule. Which results in the rule always being outputted on one line

### v1.6.1
- A small fix to the HTML's sub lib CSS class to string casting

### v1.6.2
- Cleaned up all `__init__` files to hold minimal data so they don't cause any circular imports

---
## v1.5.0
- Addition of `CSSComment` in the CSS sub package.
This is added to the package as [[AthenaCSS]] lost it's native component and now relies on this component.
- `CSSProperty` got updated to have a better string casting for [[AthenaColor]] Color components

---
## v1.4.0
/