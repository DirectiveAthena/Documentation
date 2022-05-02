---
copyright: "Andreas Sas 2022"
created: "2022-04-27 18:21"
cssclass: metaDataHide athenalib
aliases: [AthenaLib Folders]
---
# AthenaLib Folders

*function* AthenaLib.FilesFolders.**FolderExist(folder_path:PathTypes, fatal:bool=False)** -> bool
- A simple function to return the boolean state of the existence of a folder at the given path.
- When fatal is set to True, the function will thrown an `FileNotFoundError` on an otherwise False output

---

*function* AthenaLib.FilesFolders.**FolderExistNot(folder_path:PathTypes, fatal:bool=False)** -> bool
- A simple function to return the boolean state of the existence of a folder at the given path.
- When fatal is set to True, the function will thrown an `FileExistsError` on an otherwise True output

---

*function* AthenaLib.FilesFolders.**FolderContent_All(folder_path:PathTypes, fullpaths:bool=False)** -> set

---

*function* AthenaLib.FilesFolders.**FolderContent_Folders(folder_path:PathTypes, fullpaths:bool=False)** -> set

---

*function* AthenaLib.FilesFolders.**FolderContent_Files(folder_path:PathTypes, fullpaths:bool=False)** -> set

---

*function* AthenaLib.FilesFolders.**FolderContent_Files_Extension(folder_path:PathTypes, extension:str|Iterable[str], fullpaths:bool=False)** -> set

---

*function* AthenaLib.FilesFolders.**FolderMove(folder_path_start:PathTypes,folder_path_end:PathTypes, fatal:bool=True)** -> None
