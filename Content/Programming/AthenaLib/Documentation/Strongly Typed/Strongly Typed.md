---
copyright: "Andreas Sas 2022"
created: "2022-04-27 08:53"
cssclass: athenalib
aliases: [Strongly Typed]
---
# AthenaLib Strongly Typed


---

*decorator* AthenaLib.StronglyTyped.**StronglyTyped()**: ^882402
- Uses the function's variables' annotations to match the used variables to the corresponding type. Will throw a `AssertionError` on mismatch.
- Stores the function's arguments on function define, and not again on function call.

*decorator* AthenaLib.StronglyTyped.**StronglyTypedMethod()**: ^caee6b
- Uses the method's variables' annotations to match the used variables to the corresponding type. Will throw a [[#^20fa43|StrongError]] on mismatch.
- Negates the `self` of a method in the above mentioned check.
- Stores the method's arguments on method define, and not again on method call.