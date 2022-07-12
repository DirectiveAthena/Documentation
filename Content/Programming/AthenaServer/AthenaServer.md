---
copyright: "Andreas Sas 2022"
created: "2022-07-12 21:38"
cssclass: metaDataHide athena
aliases: [AthenaServer]
---

# AthenaServer

## Design

general idea:

INPUT
```json
{
    "auth": {"token":"..."},
    "path": "/",
    "mthd": "GET",
    "args": {...},
}
```

OUTPUT
```json
{
    "data": ... , // for raw data
    "link": ... , // pats to more available datae
    "file": ... , // boolean option to signify a file will follow
}
```

## root keys
Root keys are the keys that are used at the first level of the JSON structure. These keys names are always 4 characters long, all belonging to the standard Alphabet (A-Z) and no numerical values. 
%%The one exception to this rules is a `_` on the first character. When a key name is marked with a underscore it will be ignored by the client or server parser and merely holds extra data that doesn't affect the input or output sequence%% %%LOOK INTO THIS BEING A GOOD IDEA?%% 

**Full list of allocated root keys**

| key name | stage   | explanation                                                                                                                                                                                 |
| -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"auth"` | #input  | Holds user credentials to be used by the server to authenticate the user. If the requested command does not need any credentials to be executed, the value of this key can be set to `Null` |
| `"path"` | #input  | A unique path which to a corresponding object/resource/...                                                                                                                                  |
| `"mthd"` | #input  | The REST-ish command which is used on the chosen resource                                                                                                                                   |
| `"args"` | #input  | Arguments to the `#mthd` command. If no arguments are required, the value of this key can be set to `Null`                                                                                  |
| `"data"` | #output |                                                                                                                                                                                             |
