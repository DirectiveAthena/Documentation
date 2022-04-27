---
copyright: "Andreas Sas 2022"
created: "2022-04-27 18:24"
cssclass: athenalib
aliases: [AthenaLib Paths]
---
# AthenaLib Paths

---
*union* AthenaLib.FileFolders.**PathTypes** ^917a39
- A union type, used by various functions of the accompanied [[Files]] and [[Folders]] modules.

*function* AthenaLib.FileFolders.**PathCombine(**`*PathSegements:PathTypes`,`Cwd:bool=False` **)**
- Combines two or more 