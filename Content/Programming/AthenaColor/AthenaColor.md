---
copyright: "Andreas Sas 2022"
created: "2022-04-23 17:09"
cssclass: athenacolor
---
# AthenaColor
A "True No-dependency"[^1] Python package which allows for commonly used HTML color names to be printed to the console (permitting the console can take advantage of RGB ANSI codes).

Made by [[Andreas Sas]] 2022, during his [[Directive Athena]] project. Andreas started work on this smaller project out of sheer spite of using as little third party tools, libraries and other things, as possible. 
> "To be fair, making my own color printer, might not have been the best use of my time"
~ Andreas Sas 2022 - While on vacation in Yorkshire

Supported Python versions: **3.7**, **3.8**, **3.9**, **3.10** <span class="small"/>(Only for AthenaColor version 4.0.0, which is currently it's [final stages of development](https://github.com/DirectiveAthena/VerSC-AthenaColor/pull/8))

Other older versions of Python are not currently supported. These older versions will probably not be supported by Andreas Sas himself, but if you want to contribute to the project and make this package compatible with older versions of Python, Pull requests are always welcome.

## Installation
**Source Code:** [GitHub Repository](https://github.com/DirectiveAthena/VerSC-AthenaColor)
**PyPi link**: [PyPi AthenaColor](https://pypi.org/project/AthenaColor/)

> [!code]- PIP
> Use Pip to install the package:
> ```bash
> pip install AthenaColor --upgrade
> ```

## Index
- Documentation
    - [[AthenaColor ColorSystems|Color Systems]]
        - [[AthenaColor ColorSystems#^rgb|RGB]]
        - [[AthenaColor ColorSystems#^rgba|RGBA]]
        - [[AthenaColor ColorSystems#^hex|HEX]]
        - [[AthenaColor ColorSystems#^hexa|HEXA]]
        - [[AthenaColor ColorSystems#^hsl|HSL]]
        - [[AthenaColor ColorSystems#^hsv|HSV]]
        - [[AthenaColor ColorSystems#^cmyk|CMYK]]
- [[AthenaColor Contributors|Contributors]]

---

%%Contributors moved to separate file, to allow for easy editing%%

![[AthenaColor Contributors]]

%%FootNotes%%

[^1]: In the spirit of "True No Dependency" the [[AthenaLib]] package is omitted from this project. Any code that depended on this package is directly imported into the project. This can be changed in the future, but will require a vote of active contributors.
