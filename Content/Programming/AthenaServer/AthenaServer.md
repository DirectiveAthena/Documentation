---
copyright: "Andreas Sas 2022"
created: "2022-07-12 21:38"
cssclass: metaDataHide athena
aliases: [AthenaServer]
---

# AthenaServer API Design
This page defines the API design of the Applications that run on a AthenaServer library.
The API is meant to easily retrieve information from data resources with 

## Design

**Input** sent by the client to the server:
```json
{
    "auth": {"token":"..."},
    "path": "/",
    "mthd": "GET",
    "args": {...},
}
```

**Output** sent by the server to the client:
```json
{
    "data": ... ,
    "link": ... , 
    "flag": ... , 
}
```

## root keys
Root keys are the keys that are used at the first level of the JSON structure. These keys names are always 4 characters long, all belonging to the standard Alphabet (A-Z) and no numerical values. 
%%The one exception to this rules is a `_` on the first character. When a key name is marked with a underscore it will be ignored by the client or server parser and merely holds extra data that doesn't affect the input or output sequence%% %%LOOK INTO THIS BEING A GOOD IDEA?%% 

**Full list of allocated root keys**

| key name | stage          | explanation                                                                                                                                                                                                                                                                                                                                                                                 |
| -------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"auth"` | #input         | Holds user credentials to be used by the server to authenticate the user. If the requested command does not need any credentials to be executed, the value of this key can be set to `Null`                                                                                                                                                                                                 |
| `"path"` | #input         | A unique path which to a corresponding object/resource/...                                                                                                                                                                                                                                                                                                                                  |
| `"mthd"` | #input         | The REST-ish command which is used on the chosen resource                                                                                                                                                                                                                                                                                                                                   |
| `"args"` | #input         | Arguments to the `"mthd"` command. If no arguments are required, the value of this key can be set to `Null`                                                                                                                                                                                                                                                                                 |
| `"data"` | #output        | Simple data output of the requested input command and arguments                                                                                                                                                                                                                                                                                                                             |
| `"link"` | #output        | If not set to `Null` this key will point the client to more resources it should request                                                                                                                                                                                                                                                                                                     |
| `"flag"` | #output        | A general way of adding extra information to the returned data set. Will contain flags like the availability to get a file etc...                                                                                                                                                                                                                                                           |
| `"tmsp"` | #output #input | A key that is defined by both ends on structure generation. This does not add any logic to the package, but is simply meant for logging purposes as it holds the timestamp of creation.                                                                                                                                                                                                     |
| `"apiv"` | #output #input | Key to define which API version is expected in the #input stage, and defines which API version the #output stage is currently programmed at. The version format should follow the "Semantic Versioning" system of Major, Minor and Patch assignments. Minor versions are compatible with each other, but Major version discrepancies will not be allowed to be at a mismatch of each other. |

