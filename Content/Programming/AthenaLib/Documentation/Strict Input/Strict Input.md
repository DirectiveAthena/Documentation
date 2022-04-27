---
copyright: "Andreas Sas 2022"
created: "2022-04-27 08:53"
cssclass: athenalib
aliases: [Strict Input]
---
# AthenaLib Strict Input

---

*decorator* AthenaLib.StrictInput.**StrictInput()**: ^882402
- Uses the function's variables' annotations to match the used variables to the corresponding type. Will throw a `AssertionError` on mismatch.
- Stores the method's arguments on method define, and does not search for them again on method call.

*decorator* AthenaLib.StrictInput.**StrictInput()**: ^caee6b
- Uses the method's variables' annotations to match the used variables to the corresponding type. Will throw a `AssertionError` on mismatch.
- Negates the `self` of a method in the above mentioned check.
- Stores the method's arguments on method define, and does not search for them again on method call.