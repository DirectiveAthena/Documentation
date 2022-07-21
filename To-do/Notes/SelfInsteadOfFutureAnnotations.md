---
copyright: "Andreas Sas 2022"
created: "2022-07-21 19:08"
cssclass: metaDataHide
aliases: [Self instead of `__future__.annotations`]
---

# Todo card: *Self instead of `__future__.annotations`*


read the following: [[Python-Dev] The current state of typing PEPs](https://mail.python.org/archives/list/python-dev@python.org/message/VIZEBX5EYMSYIJNDBF6DMUMZOCWHARSO/)

This means I can't keep using `__future__.annotations` for the foreseeable future. This means that when python 3.11 comes out, I will be forced to redo a lot of smaller systems and type hinting as I relied on it a lot.

Anyways, the `typing.Self` should