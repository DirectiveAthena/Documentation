---
copyright: "Andreas Sas 2022"
created: "2022-04-27 18:21"
cssclass: metaDataHide athenalib
aliases: [AthenaLib Files]
---
# AthenaLib Files
*function* AthenaLib.FilesFolders.**FileExsists(**`file_path:PathTypes`,`fatal:bool=False`**)** -> `bool`: 
- A simple function to return the boolean state of the existence of a file at the given path.
- When fatal is set to True, the function will thrown an `FileNotFoundError` on an otherwise False output

> [!tip]- Spcial Notes
> - This function is [[Strict Annotated#^882402|Strongly Annotated]] and will throw an [[Strict Annotated#^20fa43|StrictError]] on exceptions.

*function* AthenaLib.FilesFolders.**FileExsistsNot(**`file_path:PathTypes`,`fatal:bool=False`**)** -> `bool`: 
- A simple function to return the boolean state of the existence of a file at the given path.
- When fatal is set to True, the function will thrown an `FileExistsError` on an otherwise True output

> [!tip]- Spcial Notes
> - This function is [[Strict Annotated#^882402|Strongly Annotated]] and will throw an [[Strict Annotated#^20fa43|StrictError]] on exceptions.