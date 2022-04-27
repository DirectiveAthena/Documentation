---
copyright: "Andreas Sas 2022"
created: "2022-04-27 18:24"
cssclass: athenalib
aliases: [AthenaLib Paths]
---
# AthenaLib Paths
A collection of useful content relating to Paths.

---

*union* AthenaLib.FileFolders.**PathTypes** ^917a39
- A union type, used by various functions of the accompanied [[Files]] and [[Folders]] modules.

*function* AthenaLib.FileFolders.**PathCombine(**`*PathSegements:PathTypes`,`Cwd:bool=False` **)**
- Combines two or more PathSegements (type: [[#^917a39|PathTypes]]) together.
- The Cwd property prefixes the `os.getcwd()`[^1] to the path output

> [!tip]- Spcial Notes
> - This function is [[Strict Annotated#^882402|Strongly Annotated]] and will throw an [[Strict Annotated#^20fa43|StrictError]] on exceptions.

%%Footnotes%%

[^1]: 'Return a string representing the current working directory.' [Python docs](https://docs.python.org/3/library/os.html#:~:text=Return%20a%20string%20representing%20the%20current%20working%20directory.)