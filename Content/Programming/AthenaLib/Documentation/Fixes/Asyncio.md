---
copyright: "Andreas Sas 2022"
created: "2022-04-26 02:16"
cssclass: athenalib
aliases: [AthenaLib Fixes Asyncio]
---
# AthenaLib Fixes Asyncio
*function* AthenaLib.Fixes.**fix_nested_asyncio()**:   ^73634b
- Simply imports the [nest-asyncio](https://github.com/erdewit/nest_asyncio) package and executes the `nest_asyncio.apply()` function
- Creates one of the few dependencies for the AthenaLib package, as it uses the [nest-asyncio](https://github.com/erdewit/nest_asyncio) package to allow for nested asyncio event loops.