---
copyright: "Andreas Sas 2022"
created: "2022-04-27 08:53"
cssclass: athenalib
aliases: [Strict Input]
---
# AthenaLib Strict Annotated

---
*exception* AthenaLib.StronglyTyped.**StrongError**: ^20fa43
- The exception thrown by the decorators [[#^882402|StronglyTyped]] and [[#^caee6b|StronglyTypedMethod]]. 

*decorator* AthenaLib.StrictInput.**StrictAnnotated()**: ^882402
- Uses the function's variables' annotations to match the used variables to the corresponding type. Will throw a [[#^20fa43|Strong Error]] on mismatch.
- Stores the method's arguments on method define, and does not search for them again on method call.

*decorator* AthenaLib.StrictInput.**StrictAnnotatedMethod()**: ^caee6b
- Uses the method's variables' annotations to match the used variables to the corresponding type. Will throw a [[#^20fa43|Strong Error]] on mismatch.
- Negates the `self` of a classmethod in the above mentioned check.
- Stores the method's arguments on method define, and does not search for them again on method call.