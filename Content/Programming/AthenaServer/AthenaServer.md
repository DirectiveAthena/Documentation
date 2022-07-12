---
copyright: "Andreas Sas 2022"
created: "2022-07-12 21:38"
cssclass: metaDataHide athena
aliases: [AthenaServer]
---

# AthenaServer

## Design

general idea:

```json
{
    "auth": {},
    "path": "/",
    "cmd": "GET",
    "args": {},
}
```

`{"token":"..."};root/help;GET;{"id"="6"}\r\n`

`{"login":["user", "1234"]};root;GET;{"":"help"}`

INPUT
```json
{
    "auth": {"token":"..."},
    "path": "/",
    "method": "GET",
    "args": {...},
}
```

OUTPUT
```json
{
    "data":... // for raw data
    "link":... // pats to more available datae
    "file":... // boolean option to signify a file will follow
}
```