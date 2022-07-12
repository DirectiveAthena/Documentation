---
copyright: "Andreas Sas 2022"
created: "2022-07-12 21:38"
cssclass: metaDataHide athena
aliases: [AthenaServer]
---

# AthenaServer API Design
This page defines the API design of the Applications that run on a AthenaServer library.
The API is meant to easily retrieve information from data resources assigned to be accessed by different access levels by authentication tokens.
The API should also have easy systems in place to download larger files from the server.

## Design
The conversation structure is completely made in the JSON format.
The root keys of the JSON structure are reserved keywords that are strictly 4 characters long and only consist of the standard Alphabet (a-z) in lowercase format.

If the client requested a file, it will receive an output file with the `"data"` key holding values corresponding to the to be downloaded file name, hash value, size, etc... the `"link"` key will hold the next path for the client to request. This is done because the API servers have to prep the file first (calling it from storage, zipping, etc...), if it has not already been cached. The original request should not point to this location first, although the stateless manner of the API design means it is definitely possible if the user knows the correct path to the cached file, hash, etc...
This means that the result of the second request in this chain, will not result in a JSON file, but in the requested file. 

### Stage Concepts
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
    "code": ... ,
    "data": ... ,
    "link": ... , 
    "flag": ... , 
}
```

## Root keys
Root keys are the keys that are used at the first level of the JSON structure. These keys names are always 4 characters long, all belonging to the standard Alphabet (A-Z) and no numerical values. 

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
| `"code"` | #output        | Root key that holds a numerical value corresponding to the success of the execution of the input. Follows the same REST return codes.                                                                                                                                                                                                                                                                                                                                                                                   |
