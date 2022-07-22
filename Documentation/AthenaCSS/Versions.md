---
copyright: "Andreas Sas 2022"
created: "2022-07-21 14:09"
cssclass: metaDataHide
aliases: [AthenaCSS Versions]
---
# AthenaCSS Version Notes

## v.0.8.0
This pre-release is a complete rewrite of the old package as  it isn't really expected to write working CSS with this package alone. This package is currently meant to help generating repetitive CSS.
This means that the old `ValueLogic` system is completely abandoned and replaced by a simple CSSProperty class from [[AthenaLib]] that simply holds a name and a value component.    

A similar system like the old `ValueLogic` might eventually return, but for now it is left aside.

## v0.7.0
/