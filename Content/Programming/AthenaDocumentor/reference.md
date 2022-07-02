#class <small>AthenaDocumentor.</small>**Output**()

Standardized way of outputting correctly parsed objects into string objects.

$\qquad$**format_documentation**(cls, parsed_object: Parsed) -> str

<span class="parent_indent">Formats the `parsed_object.doc` into a correct string.
Parameters:
- parsed_object:Parsed
Returns: str</span>

$\qquad$**format_type**(cls, parsed_object: Parsed) -> str

<span class="parent_indent">Formats the `parsed_object.type` into a correct string.
Parameters:
- parsed_object:Parsed
Returns: str</span>

$\qquad$**format_module_name**(cls, parsed_object: Parsed) -> str

<span class="parent_indent">Formats the `parsed_object.module_name` into a correct string.
Parameters:
- parsed_object:Parsed
Returns: str</span>

$\qquad$**format_object_name**(cls, parsed_object: Parsed) -> str

<span class="parent_indent">Formats the `parsed_object.name` into a correct string.
Parameters:
- parsed_object:Parsed
Returns: str</span>

$\qquad$**format_signature**(cls, parsed_object: Parsed) -> str

<span class="parent_indent">Formats the `parsed_object.signature` into a correct string.
Parameters:
- parsed_object:Parsed
Returns: str</span>

$\qquad$**format_header**(cls, parsed_object: Parsed) -> str

<span class="parent_indent">Formats multiple components of `parsed_object` together.
This forms the piece of documentation that display the name, signature, type and other similar components.
Parameters:
- parsed_object:Parsed
Returns: str</span>

$\qquad$**format_footer**(cls, parsed_object: Parsed) -> str

<span class="parent_indent">Formats multiple components of `parsed_object` together.
This forms the piece of documentation that display the end of the piece of documentation for that `parsed_object`
Parameters:
- parsed_object:Parsed
Returns: str</span>

$\qquad$**structure_function**(cls, parsed_object: Parsed) -> str

<span class="parent_indent">Calls on other `Output` methods to export a sensible string for a function object
Parameters:
- parsed_object:Parsed
Returns: str</span>

$\qquad$**structure_class**(cls, parsed_object: Parsed) -> str

<span class="parent_indent">Calls on other `Output` methods to export a sensible string for a class object
Parameters:
- parsed_object:Parsed
Returns: str</span>

$\qquad$**structure_method**(cls, parsed_object: Parsed) -> str

<span class="parent_indent">Calls on other `Output` methods to export a sensible string for a method object
Parameters:
- parsed_object:Parsed
Returns: str</span>

---

#class <small>AthenaDocumentor.</small>**OutputMarkdown**()

The OutputMarkdown supports the `Parser` in formatting `Parsed` objects to the defined format.

$\qquad$**format_documentation**(cls, parsed_object: Parsed) -> str

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**format_type**(cls, parsed_object: Parsed) -> str

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**format_module_name**(cls, parsed_object: Parsed) -> str

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**format_object_name**(cls, parsed_object: Parsed) -> str

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**format_signature**(cls, parsed_object: ParsedFunction | ParsedMethod | ParsedClass) -> str

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**format_header**(cls, parsed_object: ParsedFunction | ParsedMethod | ParsedClass) -> str

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**format_footer**(cls, parsed_object: Parsed) -> str

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**structure_function**(cls, parsed_object: ParsedFunction | ParsedMethod) -> str

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**structure_class**(cls, parsed_object: ParsedClass) -> str

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**structure_method**(cls, parsed_object: ParsedFunction | ParsedMethod) -> str

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>AthenaDocumentor.</small>**Parser**(*, root_module: types.ModuleType, markdown_structure: type[Output] = <class AthenaDocumentor.models.outputs.output_markdown.OutputMarkdown>, parse_items_with_underscore: bool = True) -> None

Object to control the correct handling of parsing through a Python package

$\qquad$**__post_init__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**parse**(self) -> Parser

<span class="parent_indent">Main method of the Parser object.
Running this will start the pared and populate the 'parsed_items' slot of the Parser object</span>

$\qquad$**_parse_recursive**(self, module_to_parse: Any)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**output_to_dict**(self, *, flat: bool = False) -> dict[str:list[dict]]

<span class="parent_indent">Output the 'parsed_items' dictionary as is, or with custom parameters.</span>

$\qquad$**output_to_json_file**(self, filepath: str)

<span class="parent_indent">Output the 'parsed_items' dictionary to a json file.
This method calls the `self.output_to_dict` method with the 'flat' parameter set to `True`</span>

$\qquad$**output_to_json_string**(self) -> str

<span class="parent_indent">Output the 'parsed_items' dictionary to a json formatted string.
This method calls the `self.output_to_dict` method with the 'flat' parameter set to `True`</span>

$\qquad$**_output_to_markdown**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**output_to_markdown_file**(self, *filepath: str)

<span class="parent_indent">Output the 'parsed_items' to a structured MarkDown file.</span>

$\qquad$**output_to_markdown_string**(self) -> str

<span class="parent_indent">Output the 'parsed_items' to string, formatted in MarkDown</span>

$\qquad$**__init__**(self, *, root_module: types.ModuleType, markdown_structure: type[Output] = <class AthenaDocumentor.models.outputs.output_markdown.OutputMarkdown>, parse_items_with_underscore: bool = True) -> None

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

---

#class <small>enum.</small>**Enum**(value, names=None, *, module=None, qualname=None, type=None, start=1)

Generic enumeration.

Derive from this class to define new enumerations.

$\qquad$**_generate_next_value_**(name, start, count, last_values)

<span class="parent_indent">Generate the next value when not given.
name: the name of the member
start: the initial start value or None
count: the number of existing members
last_value: the last value assigned or None</span>

$\qquad$**_missing_**(cls, value)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**__str__**(self)

<span class="parent_indent">Return str(self).</span>

$\qquad$**__dir__**(self)

<span class="parent_indent">Returns all members and all public methods</span>

$\qquad$**__format__**(self, format_spec)

<span class="parent_indent">Returns format using actual value type unless __str__ has been overridden.</span>

$\qquad$**__hash__**(self)

<span class="parent_indent">Return hash(self).</span>

$\qquad$**__reduce_ex__**(self, proto)

<span class="parent_indent">Helper for pickle.</span>

$\qquad$**object**()

<span class="parent_indent">The base class of the class hierarchy.
When called, it accepts no arguments and returns a new featureless
instance that has no instance attributes and cannot be given any.</span>

---

#class <small>enum.</small>**IntEnum**(value, names=None, *, module=None, qualname=None, type=None, start=1)

Enum where members are also (and must be) ints

$\qquad$**_generate_next_value_**(name, start, count, last_values)

<span class="parent_indent">Generate the next value when not given.
name: the name of the member
start: the initial start value or None
count: the number of existing members
last_value: the last value assigned or None</span>

$\qquad$**int**None

<span class="parent_indent">int([x]) -> integer
int(x, base=10) -> integer
Convert a number or string to an integer, or return 0 if no arguments
are given.If x is a number, return x.__int__().For floating point
numbers, this truncates towards zero.
If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.The literal can be preceded by '+' or '-' and be surrounded
by whitespace.The base defaults to 10.Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**__format__**(self, format_spec)

<span class="parent_indent">Returns format using actual value type unless __str__ has been overridden.</span>

$\qquad$**__new__**(cls, value)

<span class="parent_indent">Create and return a new object.See help(type) for accurate signature.</span>

---

#class <small>enum.</small>**auto**()

Instances are replaced with an appropriate value in Enum class suites.



---

#class <small>enum.</small>**EnumMeta**(cls, bases, classdict, **kwds)

Metaclass for Enum

$\qquad$**__prepare__**(metacls, cls, bases, **kwds)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__bool__**(self)

<span class="parent_indent">classes/types should always be True.</span>

$\qquad$**__call__**(cls, value, names=None, *, module=None, qualname=None, type=None, start=1)

<span class="parent_indent">Either returns an existing member, or creates a new enum class.
This method is used both when an enum class is given a value to match
to an enumeration member (i.e. Color(3)) and for the functional API
(i.e. Color = Enum('Color', names='RED GREEN BLUE')).
When used for the functional API:
`value` will be the name of the new class.
`names` should be either a string of white-space/comma delimited names
(values will start at `start`), or an iterator/mapping of name, value pairs.
`module` should be set to the module this class is being created in;
if it is not set, an attempt to find that module will be made, but if
it fails the class will not be picklable.
`qualname` should be set to the actual location this class can be found
at in its module; by default it is set to the global scope.If this is
not correct, unpickling will fail in some circumstances.
`type`, if set, will be mixed in as the first base class.</span>

$\qquad$**__contains__**(cls, obj)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__delattr__**(cls, attr)

<span class="parent_indent">Implement delattr(self, name).</span>

$\qquad$**__dir__**(self)

<span class="parent_indent">Specialized __dir__ implementation for types.</span>

$\qquad$**__getattr__**(cls, name)

<span class="parent_indent">Return the enum member matching `name`
We use __getattr__ instead of descriptors or inserting into the enum
class' __dict__ in order to support `name` and `value` being both
properties for enum members (which live in the class' __dict__) and
enum members themselves.</span>

$\qquad$**__getitem__**(cls, name)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__iter__**(cls)

<span class="parent_indent">Returns members in definition order.</span>

$\qquad$**__len__**(cls)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__repr__**(cls)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**__reversed__**(cls)

<span class="parent_indent">Returns members in reverse definition order.</span>

$\qquad$**__setattr__**(cls, name, value)

<span class="parent_indent">Block attempts to reassign Enum members.
A simple assignment to the class namespace only changes one of the
several possible ways to get an Enum member from the Enum class,
resulting in an inconsistent Enumeration.</span>

$\qquad$**_create_**(cls, class_name, names, *, module=None, qualname=None, type=None, start=1)

<span class="parent_indent">Convenience method to create a new Enum class.
`names` can be:
* A string containing member names, separated either with spaces or
commas.Values are incremented by 1 from `start`.
* An iterable of member names.Values are incremented by 1 from `start`.
* An iterable of (member name, value) pairs.
* A mapping of member name -> value pairs.</span>

$\qquad$**_convert_**(cls, name, module, filter, source=None)

<span class="parent_indent">Create a new Enum subclass that replaces a collection of global constants</span>

---

#class <small>enum.</small>**Flag**(value, names=None, *, module=None, qualname=None, type=None, start=1)

Support for flags

$\qquad$**_generate_next_value_**(name, start, count, last_values)

<span class="parent_indent">Generate the next value when not given.
name: the name of the member
start: the initial start value or None
count: the number of existing members
last_value: the last value assigned or None</span>

$\qquad$**_missing_**(cls, value)

<span class="parent_indent">Returns member (possibly creating it) if one can be found for value.</span>

$\qquad$**_create_pseudo_member_**(cls, value)

<span class="parent_indent">Create a composite member iff value contains only members.</span>

$\qquad$**__contains__**(self, other)

<span class="parent_indent">Returns True if self has at least the same flags set as other.</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**__str__**(self)

<span class="parent_indent">Return str(self).</span>

$\qquad$**__bool__**(self)

<span class="parent_indent">classes/types should always be True.</span>

$\qquad$**__or__**(self, other)

<span class="parent_indent">Return self|value.</span>

$\qquad$**__and__**(self, other)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__xor__**(self, other)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__invert__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**object**()

<span class="parent_indent">The base class of the class hierarchy.
When called, it accepts no arguments and returns a new featureless
instance that has no instance attributes and cannot be given any.</span>

$\qquad$**__new__**(cls, value)

<span class="parent_indent">Create and return a new object.See help(type) for accurate signature.</span>

---

#class <small>enum.</small>**IntFlag**(value, names=None, *, module=None, qualname=None, type=None, start=1)

Support for integer-based Flags

$\qquad$**_generate_next_value_**(name, start, count, last_values)

<span class="parent_indent">Generate the next value when not given.
name: the name of the member
start: the initial start value or None
count: the number of existing members
last_value: the last value assigned or None</span>

$\qquad$**_missing_**(cls, value)

<span class="parent_indent">Returns member (possibly creating it) if one can be found for value.</span>

$\qquad$**_create_pseudo_member_**(cls, value)

<span class="parent_indent">Create a composite member iff value contains only members.</span>

$\qquad$**__or__**(self, other)

<span class="parent_indent">Return self|value.</span>

$\qquad$**__and__**(self, other)

<span class="parent_indent">Return self&value.</span>

$\qquad$**__xor__**(self, other)

<span class="parent_indent">Return self^value.</span>

$\qquad$**__or__**(self, other)

<span class="parent_indent">Return self|value.</span>

$\qquad$**__and__**(self, other)

<span class="parent_indent">Return self&value.</span>

$\qquad$**__xor__**(self, other)

<span class="parent_indent">Return self^value.</span>

$\qquad$**__invert__**(self)

<span class="parent_indent">~self</span>

$\qquad$**int**None

<span class="parent_indent">int([x]) -> integer
int(x, base=10) -> integer
Convert a number or string to an integer, or return 0 if no arguments
are given.If x is a number, return x.__int__().For floating point
numbers, this truncates towards zero.
If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.The literal can be preceded by '+' or '-' and be surrounded
by whitespace.The base defaults to 10.Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**__format__**(self, format_spec)

<span class="parent_indent">Returns format using actual value type unless __str__ has been overridden.</span>

$\qquad$**__new__**(cls, value)

<span class="parent_indent">Create and return a new object.See help(type) for accurate signature.</span>

---

#class <small>enum.</small>**_EnumDict**()

Track enum member order and ensure member names are not reused.

EnumMeta will use the names found in self._member_names as the
enumeration member names.

$\qquad$**__init__**(self)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__setitem__**(self, key, value)

<span class="parent_indent">Changes anything not dundered or not a descriptor.
If an enum member name is used twice, an error is raised; duplicate
values are not checked for.
Single underscore (sunder) names are reserved.</span>

---

#func <small>enum.</small>**_decompose**(flag, value)

Extract all members from the value.

---

#func <small>enum.</small>**_high_bit**(value)

returns index of highest bit, or -1 if value is zero or negative

---

#func <small>enum.</small>**_is_descriptor**(obj)

Returns True if obj is a descriptor, False otherwise.

---

#func <small>enum.</small>**_is_dunder**(name)

Returns True if a __dunder__ name, False otherwise.

---

#func <small>enum.</small>**_is_private**(cls_name, name)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>enum.</small>**_is_sunder**(name)

Returns True if a _sunder_ name, False otherwise.

---

#func <small>enum.</small>**_make_class_unpicklable**(cls)

Make the given class un-picklable.

---

#func <small>enum.</small>**_reduce_ex_by_name**(self, proto)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>enum.</small>**unique**(enumeration)

Class decorator for enumerations ensuring unique member values.

---

#class <small>AthenaDocumentor.data.types.</small>**Types**(value, names=None, *, module=None, qualname=None, type=None, start=1)

An enumeration.

$\qquad$**_generate_next_value_**(name, start, count, last_values)

<span class="parent_indent">Generate the next value when not given.
name: the name of the member
start: the initial start value or None
count: the number of existing members
last_value: the last value assigned or None</span>

$\qquad$**object**()

<span class="parent_indent">The base class of the class hierarchy.
When called, it accepts no arguments and returns a new featureless
instance that has no instance attributes and cannot be given any.</span>

$\qquad$**__new__**(cls, value)

<span class="parent_indent">Create and return a new object.See help(type) for accurate signature.</span>

---

#func <small>AthenaDocumentor.functions.markdown_string_manipulations.</small>**indent_all_lines**(text: str, indent: int) -> str

Indents all lines in a string with a defined amount of indentation

Parameters:
- text : str -> input text
- indent : int -> amount of whitespaces that has to be added before everything else

---

#func <small>AthenaDocumentor.functions.markdown_string_manipulations.</small>**quote_all_lines**(text: str) -> str

Places a quote prefix in front of all lines in a string

Parameters:
- text : str -> input text

---

#func <small>AthenaDocumentor.functions.markdown_string_manipulations.</small>**remove_empty_prefix**(text: str) -> str

Removes any double spaces ("  ")

Parameters:
- text : str -> input text

---

#class <small>abc.</small>**ABC**()

Helper class that provides a standard way to create an ABC using
inheritance.



---

#func <small>abc.</small>**abstractmethod**(funcobj)

A decorator indicating abstract methods.

Requires that the metaclass is ABCMeta or derived from it.  A
class that has a metaclass derived from ABCMeta cannot be
instantiated unless all of its abstract methods are overridden.
The abstract methods can be called using any of the normal
'super' call mechanisms.  abstractmethod() may be used to declare
abstract methods for properties and descriptors.

Usage:

    class C(metaclass=ABCMeta):
        @abstractmethod
        def my_abstract_method(self, ...):
            ...

---

#class <small>abc.</small>**ABCMeta**(name, bases, namespace, **kwargs)

Metaclass for defining Abstract Base Classes (ABCs).

Use this metaclass to create an ABC.  An ABC can be subclassed
directly, and then acts as a mix-in class.  You can also register
unrelated concrete classes (even built-in classes) and unrelated
ABCs as 'virtual subclasses' -- these and their descendants will
be considered subclasses of the registering ABC by the built-in
issubclass() function, but the registering ABC won't show up in
their MRO (Method Resolution Order) nor will method
implementations defined by the registering ABC be callable (not
even via super()).

$\qquad$**register**(cls, subclass)

<span class="parent_indent">Register a virtual subclass of an ABC.
Returns the subclass, to allow usage as a class decorator.</span>

$\qquad$**__instancecheck__**(cls, instance)

<span class="parent_indent">Override for isinstance(instance, cls).</span>

$\qquad$**__subclasscheck__**(cls, subclass)

<span class="parent_indent">Override for issubclass(subclass, cls).</span>

$\qquad$**_dump_registry**(cls, file=None)

<span class="parent_indent">Debug helper to print the ABC registry.</span>

$\qquad$**_abc_registry_clear**(cls)

<span class="parent_indent">Clear the registry (for debugging or testing).</span>

$\qquad$**_abc_caches_clear**(cls)

<span class="parent_indent">Clear the caches (for debugging or testing).</span>

---

#class <small>abc.</small>**abstractclassmethod**None

A decorator indicating abstract classmethods.

Deprecated, use 'classmethod' with 'abstractmethod' instead:

    class C(ABC):
        @classmethod
        @abstractmethod
        def my_abstract_classmethod(cls, ...):
            ...

$\qquad$**__init__**(self, callable)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

---

#class <small>abc.</small>**abstractproperty**(fget=None, fset=None, fdel=None, doc=None)

A decorator indicating abstract properties.

Deprecated, use 'property' with 'abstractmethod' instead:

    class C(ABC):
        @property
        @abstractmethod
        def my_abstract_property(self):
            ...



---

#class <small>abc.</small>**abstractstaticmethod**None

A decorator indicating abstract staticmethods.

Deprecated, use 'staticmethod' with 'abstractmethod' instead:

    class C(ABC):
        @staticmethod
        @abstractmethod
        def my_abstract_staticmethod(...):
            ...

$\qquad$**__init__**(self, callable)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

---

#func <small>abc.</small>**update_abstractmethods**(cls)

Recalculate the set of abstract methods of an abstract class.

If a class has had one of its abstract methods implemented after the
class was created, the method will not be considered implemented until
this function is called. Alternatively, if a new abstract method has been
added to the class, it will only be considered an abstract method of the
class after this function is called.

This function should be called before any use is made of the class,
usually in class decorators that add methods to the subject class.

Returns cls, to allow usage as a class decorator.

If cls is not an instance of ABCMeta, does nothing.

---

#class <small>AthenaDocumentor.models.parsed.parsed.</small>**Parsed**(obj)

Parsed(obj)

$\qquad$**__init__**(self, obj)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**to_dict**(self) -> dict

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

---

#class <small>AthenaDocumentor.models.parsed.parsed_class.</small>**ParsedClass**(obj)

ParsedClass(obj)

$\qquad$**__init__**(self, obj)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**to_dict**(self) -> dict

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

---

#class <small>AthenaDocumentor.models.parsed.parsed_function.</small>**ParsedFunction**(obj)

ParsedFunction(obj)

$\qquad$**__init__**(self, obj)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**to_dict**(self) -> dict

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

---

#class <small>AthenaDocumentor.models.parsed.parsed_method.</small>**ParsedMethod**(obj)

ParsedMethod(obj)

$\qquad$**__init__**(self, obj)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**to_dict**(self) -> dict

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

---

#class <small>AthenaDocumentor.models.parsed.parsed_module.</small>**ParsedModule**(obj)

ParsedModule(obj)

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

---

#func <small>dataclasses.</small>**dataclass**(cls=None, /, *, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True, kw_only=False, slots=False)

Returns the same class as was passed in, with dunder methods
added based on the fields defined in the class.

Examines PEP 526 __annotations__ to determine fields.

If init is true, an __init__() method is added to the class. If
repr is true, a __repr__() method is added. If order is true, rich
comparison dunder methods are added. If unsafe_hash is true, a
__hash__() method function is added. If frozen is true, fields may
not be assigned to after instance creation. If match_args is true,
the __match_args__ tuple is added. If kw_only is true, then by
default all fields are keyword-only. If slots is true, an
__slots__ attribute is added.

---

#func <small>dataclasses.</small>**field**(*, default=<dataclasses._MISSING_TYPE object at 0x00000177D8F33C10>, default_factory=<dataclasses._MISSING_TYPE object at 0x00000177D8F33C10>, init=True, repr=True, hash=None, compare=True, metadata=None, kw_only=<dataclasses._MISSING_TYPE object at 0x00000177D8F33C10>)

Return an object to identify dataclass fields.

default is the default value of the field.  default_factory is a
0-argument function called to initialize a field's value.  If init
is true, the field will be a parameter to the class's __init__()
function.  If repr is true, the field will be included in the
object's repr().  If hash is true, the field will be included in the
object's hash().  If compare is true, the field will be used in
comparison functions.  metadata, if specified, must be a mapping
which is stored but not otherwise examined by dataclass.  If kw_only
is true, the field will become a keyword-only parameter to
__init__().

It is an error to specify both default and default_factory.

---

#class <small>inspect.</small>**ArgInfo**(args, varargs, keywords, locals)

ArgInfo(args, varargs, keywords, locals)

$\qquad$**_make**(cls, iterable)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**_replace**(self, /, **kwds)

<span class="parent_indent">Return a new ArgInfo object replacing specified fields with new values</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return a nicely formatted representation string</span>

$\qquad$**_asdict**(self)

<span class="parent_indent">Return a new dict which maps field names to their values.</span>

$\qquad$**__getnewargs__**(self)

<span class="parent_indent">Return self as a plain tuple.Used by copy and pickle.</span>

---

#class <small>inspect.</small>**ArgSpec**(args, varargs, keywords, defaults)

ArgSpec(args, varargs, keywords, defaults)

$\qquad$**_make**(cls, iterable)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**_replace**(self, /, **kwds)

<span class="parent_indent">Return a new ArgSpec object replacing specified fields with new values</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return a nicely formatted representation string</span>

$\qquad$**_asdict**(self)

<span class="parent_indent">Return a new dict which maps field names to their values.</span>

$\qquad$**__getnewargs__**(self)

<span class="parent_indent">Return self as a plain tuple.Used by copy and pickle.</span>

---

#class <small>inspect.</small>**Arguments**(args, varargs, varkw)

Arguments(args, varargs, varkw)

$\qquad$**_make**(cls, iterable)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**_replace**(self, /, **kwds)

<span class="parent_indent">Return a new Arguments object replacing specified fields with new values</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return a nicely formatted representation string</span>

$\qquad$**_asdict**(self)

<span class="parent_indent">Return a new dict which maps field names to their values.</span>

$\qquad$**__getnewargs__**(self)

<span class="parent_indent">Return self as a plain tuple.Used by copy and pickle.</span>

---

#class <small>inspect.</small>**Attribute**(name, kind, defining_class, object)

Attribute(name, kind, defining_class, object)

$\qquad$**_make**(cls, iterable)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**_replace**(self, /, **kwds)

<span class="parent_indent">Return a new Attribute object replacing specified fields with new values</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return a nicely formatted representation string</span>

$\qquad$**_asdict**(self)

<span class="parent_indent">Return a new dict which maps field names to their values.</span>

$\qquad$**__getnewargs__**(self)

<span class="parent_indent">Return self as a plain tuple.Used by copy and pickle.</span>

---

#class <small>inspect.</small>**BlockFinder**()

Provide a tokeneater() method to detect the end of a code block.

$\qquad$**__init__**(self)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**tokeneater**(self, type, token, srowcol, erowcol, line)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>inspect.</small>**BoundArguments**(signature, arguments)

Result of `Signature.bind` call.  Holds the mapping of arguments
to the function's parameters.

Has the following public attributes:

* arguments : dict
    An ordered mutable mapping of parameters' names to arguments' values.
    Does not contain arguments' default values.
* signature : Signature
    The Signature object that created this instance.
* args : tuple
    Tuple of positional arguments values.
* kwargs : dict
    Dict of keyword arguments values.

$\qquad$**__init__**(self, signature, arguments)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**apply_defaults**(self)

<span class="parent_indent">Set default values for missing arguments.
For variable-positional arguments (*args) the default is an
empty tuple.
For variable-keyword arguments (**kwargs) the default is an
empty dict.</span>

$\qquad$**__eq__**(self, other)

<span class="parent_indent">Return self==value.</span>

$\qquad$**__setstate__**(self, state)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__getstate__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

---

#class <small>inspect.</small>**ClassFoundException**None

Common base class for all non-exit exceptions.



---

#class <small>inspect.</small>**ClosureVars**(nonlocals, globals, builtins, unbound)

ClosureVars(nonlocals, globals, builtins, unbound)

$\qquad$**_make**(cls, iterable)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**_replace**(self, /, **kwds)

<span class="parent_indent">Return a new ClosureVars object replacing specified fields with new values</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return a nicely formatted representation string</span>

$\qquad$**_asdict**(self)

<span class="parent_indent">Return a new dict which maps field names to their values.</span>

$\qquad$**__getnewargs__**(self)

<span class="parent_indent">Return self as a plain tuple.Used by copy and pickle.</span>

---

#class <small>inspect.</small>**EndOfBlock**None

Common base class for all non-exit exceptions.



---

#class <small>inspect.</small>**FrameInfo**(frame, filename, lineno, function, code_context, index)

FrameInfo(frame, filename, lineno, function, code_context, index)

$\qquad$**_make**(cls, iterable)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**_replace**(self, /, **kwds)

<span class="parent_indent">Return a new FrameInfo object replacing specified fields with new values</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return a nicely formatted representation string</span>

$\qquad$**_asdict**(self)

<span class="parent_indent">Return a new dict which maps field names to their values.</span>

$\qquad$**__getnewargs__**(self)

<span class="parent_indent">Return self as a plain tuple.Used by copy and pickle.</span>

---

#class <small>inspect.</small>**FullArgSpec**(args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations)

FullArgSpec(args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations)

$\qquad$**_make**(cls, iterable)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**_replace**(self, /, **kwds)

<span class="parent_indent">Return a new FullArgSpec object replacing specified fields with new values</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return a nicely formatted representation string</span>

$\qquad$**_asdict**(self)

<span class="parent_indent">Return a new dict which maps field names to their values.</span>

$\qquad$**__getnewargs__**(self)

<span class="parent_indent">Return self as a plain tuple.Used by copy and pickle.</span>

---

#class <small>inspect.</small>**Parameter**(name, kind, *, default, annotation)

Represents a parameter in a function signature.

Has the following public attributes:

* name : str
    The name of the parameter as a string.
* default : object
    The default value for the parameter if specified.  If the
    parameter has no default value, this attribute is set to
    `Parameter.empty`.
* annotation
    The annotation for the parameter if specified.  If the
    parameter has no annotation, this attribute is set to
    `Parameter.empty`.
* kind : str
    Describes how argument values are bound to the parameter.
    Possible values: `Parameter.POSITIONAL_ONLY`,
    `Parameter.POSITIONAL_OR_KEYWORD`, `Parameter.VAR_POSITIONAL`,
    `Parameter.KEYWORD_ONLY`, `Parameter.VAR_KEYWORD`.

$\qquad$**_empty**()

<span class="parent_indent">Marker object for Signature.empty and Parameter.empty.</span>

$\qquad$**__init__**(self, name, kind, *, default, annotation)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__reduce__**(self)

<span class="parent_indent">Helper for pickle.</span>

$\qquad$**__setstate__**(self, state)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**replace**(self, *, name=<class inspect._void>, kind=<class inspect._void>, annotation=<class inspect._void>, default=<class inspect._void>)

<span class="parent_indent">Creates a customized copy of the Parameter.</span>

$\qquad$**__str__**(self)

<span class="parent_indent">Return str(self).</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**__hash__**(self)

<span class="parent_indent">Return hash(self).</span>

$\qquad$**__eq__**(self, other)

<span class="parent_indent">Return self==value.</span>

---

#class <small>inspect.</small>**Signature**(parameters=None, *, return_annotation, __validate_parameters__=True)

A Signature object represents the overall signature of a function.
It stores a Parameter object for each parameter accepted by the
function, as well as information specific to the function itself.

A Signature object has the following public attributes and methods:

* parameters : OrderedDict
    An ordered mapping of parameters' names to the corresponding
    Parameter objects (keyword-only arguments are in the same order
    as listed in `code.co_varnames`).
* return_annotation : object
    The annotation for the return type of the function if specified.
    If the function has no annotation for its return type, this
    attribute is set to `Signature.empty`.
* bind(*args, **kwargs) -> BoundArguments
    Creates a mapping from positional and keyword arguments to
    parameters.
* bind_partial(*args, **kwargs) -> BoundArguments
    Creates a partial mapping from positional and keyword arguments
    to parameters (simulating 'functools.partial' behavior.)

$\qquad$**Parameter**(name, kind, *, default, annotation)

<span class="parent_indent">Represents a parameter in a function signature.
Has the following public attributes:
* name : str
The name of the parameter as a string.
* default : object
The default value for the parameter if specified.If the
parameter has no default value, this attribute is set to
`Parameter.empty`.
* annotation
The annotation for the parameter if specified.If the
parameter has no annotation, this attribute is set to
`Parameter.empty`.
* kind : str
Describes how argument values are bound to the parameter.
Possible values: `Parameter.POSITIONAL_ONLY`,
`Parameter.POSITIONAL_OR_KEYWORD`, `Parameter.VAR_POSITIONAL`,
`Parameter.KEYWORD_ONLY`, `Parameter.VAR_KEYWORD`.</span>

$\qquad$**BoundArguments**(signature, arguments)

<span class="parent_indent">Result of `Signature.bind` call.Holds the mapping of arguments
to the function's parameters.
Has the following public attributes:
* arguments : dict
An ordered mutable mapping of parameters' names to arguments' values.
Does not contain arguments' default values.
* signature : Signature
The Signature object that created this instance.
* args : tuple
Tuple of positional arguments values.
* kwargs : dict
Dict of keyword arguments values.</span>

$\qquad$**_empty**()

<span class="parent_indent">Marker object for Signature.empty and Parameter.empty.</span>

$\qquad$**__init__**(self, parameters=None, *, return_annotation, __validate_parameters__=True)

<span class="parent_indent">Constructs Signature from the given list of Parameter
objects and 'return_annotation'.All arguments are optional.</span>

$\qquad$**from_function**(cls, func)

<span class="parent_indent">Constructs Signature for the given python function.
Deprecated since Python 3.5, use `Signature.from_callable()`.</span>

$\qquad$**from_builtin**(cls, func)

<span class="parent_indent">Constructs Signature for the given builtin function.
Deprecated since Python 3.5, use `Signature.from_callable()`.</span>

$\qquad$**from_callable**(cls, obj, *, follow_wrapped=True, globals=None, locals=None, eval_str=False)

<span class="parent_indent">Constructs Signature for the given callable object.</span>

$\qquad$**replace**(self, *, parameters=<class inspect._void>, return_annotation=<class inspect._void>)

<span class="parent_indent">Creates a customized copy of the Signature.
Pass 'parameters' and/or 'return_annotation' arguments
to override them in the new copy.</span>

$\qquad$**_hash_basis**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__hash__**(self)

<span class="parent_indent">Return hash(self).</span>

$\qquad$**__eq__**(self, other)

<span class="parent_indent">Return self==value.</span>

$\qquad$**_bind**(self, args, kwargs, *, partial=False)

<span class="parent_indent">Private method. Don't use directly.</span>

$\qquad$**bind**(self, /, *args, **kwargs)

<span class="parent_indent">Get a BoundArguments object, that maps the passed `args`
and `kwargs` to the function's signature.Raises `TypeError`
if the passed arguments can not be bound.</span>

$\qquad$**bind_partial**(self, /, *args, **kwargs)

<span class="parent_indent">Get a BoundArguments object, that partially maps the
passed `args` and `kwargs` to the function's signature.
Raises `TypeError` if the passed arguments can not be bound.</span>

$\qquad$**__reduce__**(self)

<span class="parent_indent">Helper for pickle.</span>

$\qquad$**__setstate__**(self, state)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**__str__**(self)

<span class="parent_indent">Return str(self).</span>

---

#class <small>inspect.</small>**Traceback**(filename, lineno, function, code_context, index)

Traceback(filename, lineno, function, code_context, index)

$\qquad$**_make**(cls, iterable)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**_replace**(self, /, **kwds)

<span class="parent_indent">Return a new Traceback object replacing specified fields with new values</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return a nicely formatted representation string</span>

$\qquad$**_asdict**(self)

<span class="parent_indent">Return a new dict which maps field names to their values.</span>

$\qquad$**__getnewargs__**(self)

<span class="parent_indent">Return self as a plain tuple.Used by copy and pickle.</span>

---

#class <small>inspect.</small>**_ClassFinder**(qualname)

A node visitor base class that walks the abstract syntax tree and calls a
visitor function for every node found.  This function may return a value
which is forwarded by the `visit` method.

This class is meant to be subclassed, with the subclass adding visitor
methods.

Per default the visitor functions for the nodes are ``'visit_'`` +
class name of the node.  So a `TryFinally` node visit function would
be `visit_TryFinally`.  This behavior can be changed by overriding
the `visit` method.  If no visitor function exists for a node
(return value `None`) the `generic_visit` visitor is used instead.

Don't use the `NodeVisitor` if you want to apply changes to nodes during
traversing.  For this a special visitor exists (`NodeTransformer`) that
allows modifications.

$\qquad$**__init__**(self, qualname)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**visit_FunctionDef**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_FunctionDef**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_ClassDef**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>inspect.</small>**_ParameterKind**(value, names=None, *, module=None, qualname=None, type=None, start=1)

An enumeration.

$\qquad$**_generate_next_value_**(name, start, count, last_values)

<span class="parent_indent">Generate the next value when not given.
name: the name of the member
start: the initial start value or None
count: the number of existing members
last_value: the last value assigned or None</span>

$\qquad$**__str__**(self)

<span class="parent_indent">Return str(self).</span>

$\qquad$**int**None

<span class="parent_indent">int([x]) -> integer
int(x, base=10) -> integer
Convert a number or string to an integer, or return 0 if no arguments
are given.If x is a number, return x.__int__().For floating point
numbers, this truncates towards zero.
If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.The literal can be preceded by '+' or '-' and be surrounded
by whitespace.The base defaults to 10.Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4</span>

$\qquad$**__new__**(cls, value)

<span class="parent_indent">Create and return a new object.See help(type) for accurate signature.</span>

---

#func <small>inspect.</small>**_check_class**(klass, attr)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>inspect.</small>**_check_instance**(obj, attr)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#class <small>inspect.</small>**_empty**()

Marker object for Signature.empty and Parameter.empty.



---

#func <small>inspect.</small>**_findclass**(func)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>inspect.</small>**_finddoc**(obj)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>inspect.</small>**_has_code_flag**(f, flag)

Return true if ``f`` is a function (or a method or functools.partial
wrapper wrapping a function) whose code object has the given ``flag``
set in its flags.

---

#func <small>inspect.</small>**_is_type**(obj)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>inspect.</small>**_main**()

Logic for inspecting an object given at command line 

---

#func <small>inspect.</small>**_missing_arguments**(f_name, argnames, pos, values)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>inspect.</small>**_shadowed_dict**(klass)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>inspect.</small>**_signature_bound_method**(sig)

Private helper to transform signatures for unbound
functions to bound methods.

---

#func <small>inspect.</small>**_signature_from_builtin**(cls, func, skip_bound_arg=True)

Private helper function to get signature for
builtin callables.

---

#func <small>inspect.</small>**_signature_from_callable**(obj, *, follow_wrapper_chains=True, skip_bound_arg=True, globals=None, locals=None, eval_str=False, sigcls)

Private helper function to get signature for arbitrary
callable objects.

---

#func <small>inspect.</small>**_signature_from_function**(cls, func, skip_bound_arg=True, globals=None, locals=None, eval_str=False)

Private helper: constructs Signature for the given python function.

---

#func <small>inspect.</small>**_signature_fromstr**(cls, obj, s, skip_bound_arg=True)

Private helper to parse content of '__text_signature__'
and return a Signature based on it.

---

#func <small>inspect.</small>**_signature_get_bound_param**(spec)

Private helper to get first parameter name from a
__text_signature__ of a builtin method, which should
be in the following format: '($param1, ...)'.
Assumptions are that the first argument won't have
a default value or an annotation.

---

#func <small>inspect.</small>**_signature_get_partial**(wrapped_sig, partial, extra_args=())

Private helper to calculate how 'wrapped_sig' signature will
look like after applying a 'functools.partial' object (or alike)
on it.

---

#func <small>inspect.</small>**_signature_get_user_defined_method**(cls, method_name)

Private helper. Checks if ``cls`` has an attribute
named ``method_name`` and returns it only if it is a
pure python function.

---

#func <small>inspect.</small>**_signature_is_builtin**(obj)

Private helper to test if `obj` is a callable that might
support Argument Clinic's __text_signature__ protocol.

---

#func <small>inspect.</small>**_signature_is_functionlike**(obj)

Private helper to test if `obj` is a duck type of FunctionType.
A good example of such objects are functions compiled with
Cython, which have all attributes that a pure Python function
would have, but have their code statically compiled.

---

#func <small>inspect.</small>**_signature_strip_non_python_syntax**(signature)

Private helper function. Takes a signature in Argument Clinic's
extended signature format.

Returns a tuple of three things:
  * that signature re-rendered in standard Python syntax,
  * the index of the "self" parameter (generally 0), or None if
    the function does not have a "self" parameter, and
  * the index of the last "positional only" parameter,
    or None if the signature has no positional-only parameters.

---

#func <small>inspect.</small>**_static_getmro**(klass)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>inspect.</small>**_too_many**(f_name, args, kwonly, varargs, defcount, given, values)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#class <small>inspect.</small>**_void**()

A private marker - used in Parameter & Signature.



---

#func <small>inspect.</small>**classify_class_attrs**(cls)

Return list of attribute-descriptor tuples.

For each name in dir(cls), the return list contains a 4-tuple
with these elements:

    0. The name (a string).

    1. The kind of attribute this is, one of these strings:
           'class method'    created via classmethod()
           'static method'   created via staticmethod()
           'property'        created via property()
           'method'          any other flavor of method or descriptor
           'data'            not a method

    2. The class which defined this attribute (a class).

    3. The object as obtained by calling getattr; if this fails, or if the
       resulting object does not live anywhere in the class' mro (including
       metaclasses) then the object is looked up in the defining class's
       dict (found by walking the mro).

If one of the items in dir(cls) is stored in the metaclass it will now
be discovered and not have None be listed as the class in which it was
defined.  Any items whose home class cannot be discovered are skipped.

---

#func <small>inspect.</small>**cleandoc**(doc)

Clean up indentation from docstrings.

Any whitespace that can be uniformly removed from the second line
onwards is removed.

---

#func <small>inspect.</small>**currentframe**()

Return the frame of the caller or None if this is not possible.

---

#func <small>inspect.</small>**findsource**(object)

Return the entire source file and starting line number for an object.

The argument may be a module, class, method, function, traceback, frame,
or code object.  The source code is returned as a list of all the lines
in the file and the line number indexes a line in that list.  An OSError
is raised if the source code cannot be retrieved.

---

#func <small>inspect.</small>**formatannotation**(annotation, base_module=None)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>inspect.</small>**formatannotationrelativeto**(object)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>inspect.</small>**formatargspec**(args, varargs=None, varkw=None, defaults=None, kwonlyargs=(), kwonlydefaults={}, annotations={}, formatarg=<class str>, formatvarargs=<function <lambda> at 0x00000177D8FB2D40>, formatvarkw=<function <lambda> at 0x00000177D8FB2DD0>, formatvalue=<function <lambda> at 0x00000177D8FB2E60>, formatreturns=<function <lambda> at 0x00000177D8FB2EF0>, formatannotation=<function formatannotation at 0x00000177D8FB2C20>)

Format an argument spec from the values returned by getfullargspec.

The first seven arguments are (args, varargs, varkw, defaults,
kwonlyargs, kwonlydefaults, annotations).  The other five arguments
are the corresponding optional formatting functions that are called to
turn names and values into strings.  The last argument is an optional
function to format the sequence of arguments.

Deprecated since Python 3.5: use the `signature` function and `Signature`
objects.

---

#func <small>inspect.</small>**formatargvalues**(args, varargs, varkw, locals, formatarg=<class str>, formatvarargs=<function <lambda> at 0x00000177D8FB30A0>, formatvarkw=<function <lambda> at 0x00000177D8FB3130>, formatvalue=<function <lambda> at 0x00000177D8FB31C0>)

Format an argument spec from the 4 values returned by getargvalues.

The first four arguments are (args, varargs, varkw, locals).  The
next four arguments are the corresponding optional formatting functions
that are called to turn names and values into strings.  The ninth
argument is an optional function to format the sequence of arguments.

---

#func <small>inspect.</small>**get_annotations**(obj, *, globals=None, locals=None, eval_str=False)

Compute the annotations dict for an object.

obj may be a callable, class, or module.
Passing in an object of any other type raises TypeError.

Returns a dict.  get_annotations() returns a new dict every time
it's called; calling it twice on the same object will return two
different but equivalent dicts.

This function handles several details for you:

  * If eval_str is true, values of type str will
    be un-stringized using eval().  This is intended
    for use with stringized annotations
    ("from __future__ import annotations").
  * If obj doesn't have an annotations dict, returns an
    empty dict.  (Functions and methods always have an
    annotations dict; classes, modules, and other types of
    callables may not.)
  * Ignores inherited annotations on classes.  If a class
    doesn't have its own annotations dict, returns an empty dict.
  * All accesses to object members and dict values are done
    using getattr() and dict.get() for safety.
  * Always, always, always returns a freshly-created dict.

eval_str controls whether or not values of type str are replaced
with the result of calling eval() on those values:

  * If eval_str is true, eval() is called on values of type str.
  * If eval_str is false (the default), values of type str are unchanged.

globals and locals are passed in to eval(); see the documentation
for eval() for more information.  If either globals or locals is
None, this function may replace that value with a context-specific
default, contingent on type(obj):

  * If obj is a module, globals defaults to obj.__dict__.
  * If obj is a class, globals defaults to
    sys.modules[obj.__module__].__dict__ and locals
    defaults to the obj class namespace.
  * If obj is a callable, globals defaults to obj.__globals__,
    although if obj is a wrapped function (using
    functools.update_wrapper()) it is first unwrapped.

---

#func <small>inspect.</small>**getabsfile**(object, _filename=None)

Return an absolute path to the source or compiled file for an object.

The idea is for each object to have a unique origin, so this routine
normalizes the result as much as possible.

---

#func <small>inspect.</small>**getargs**(co)

Get information about the arguments accepted by a code object.

Three things are returned: (args, varargs, varkw), where
'args' is the list of argument names. Keyword-only arguments are
appended. 'varargs' and 'varkw' are the names of the * and **
arguments or None.

---

#func <small>inspect.</small>**getargspec**(func)

Get the names and default values of a function's parameters.

A tuple of four things is returned: (args, varargs, keywords, defaults).
'args' is a list of the argument names, including keyword-only argument names.
'varargs' and 'keywords' are the names of the * and ** parameters or None.
'defaults' is an n-tuple of the default values of the last n parameters.

This function is deprecated, as it does not support annotations or
keyword-only parameters and will raise ValueError if either is present
on the supplied callable.

For a more structured introspection API, use inspect.signature() instead.

Alternatively, use getfullargspec() for an API with a similar namedtuple
based interface, but full support for annotations and keyword-only
parameters.

Deprecated since Python 3.5, use `inspect.getfullargspec()`.

---

#func <small>inspect.</small>**getargvalues**(frame)

Get information about arguments passed into a particular frame.

A tuple of four things is returned: (args, varargs, varkw, locals).
'args' is a list of the argument names.
'varargs' and 'varkw' are the names of the * and ** arguments or None.
'locals' is the locals dictionary of the given frame.

---

#func <small>inspect.</small>**getattr_static**(obj, attr, default=<object object at 0x00000177D89749B0>)

Retrieve attributes without triggering dynamic lookup via the
descriptor protocol,  __getattr__ or __getattribute__.

Note: this function may not be able to retrieve all attributes
that getattr can fetch (like dynamically created attributes)
and may find attributes that getattr can't (like descriptors
that raise AttributeError). It can also return descriptor objects
instead of instance members in some cases. See the
documentation for details.

---

#func <small>inspect.</small>**getblock**(lines)

Extract the block of code at the top of the given list of lines.

---

#func <small>inspect.</small>**getcallargs**(func, /, *positional, **named)

Get the mapping of arguments to values.

A dict is returned, with keys the function argument names (including the
names of the * and ** arguments, if any), and values the respective bound
values from 'positional' and 'named'.

---

#func <small>inspect.</small>**getclasstree**(classes, unique=False)

Arrange the given list of classes into a hierarchy of nested lists.

Where a nested list appears, it contains classes derived from the class
whose entry immediately precedes the list.  Each entry is a 2-tuple
containing a class and a tuple of its base classes.  If the 'unique'
argument is true, exactly one entry appears in the returned structure
for each class in the given list.  Otherwise, classes using multiple
inheritance and their descendants will appear multiple times.

---

#func <small>inspect.</small>**getclosurevars**(func)

Get the mapping of free variables to their current values.

Returns a named tuple of dicts mapping the current nonlocal, global
and builtin references as seen by the body of the function. A final
set of unbound names that could not be resolved is also provided.

---

#func <small>inspect.</small>**getcomments**(object)

Get lines of comments immediately preceding an object's source code.

Returns None when source can't be found.

---

#func <small>inspect.</small>**getcoroutinelocals**(coroutine)

Get the mapping of coroutine local variables to their current values.

A dict is returned, with the keys the local variable names and values the
bound values.

---

#func <small>inspect.</small>**getcoroutinestate**(coroutine)

Get current state of a coroutine object.

Possible states are:
  CORO_CREATED: Waiting to start execution.
  CORO_RUNNING: Currently being executed by the interpreter.
  CORO_SUSPENDED: Currently suspended at an await expression.
  CORO_CLOSED: Execution has completed.

---

#func <small>inspect.</small>**getdoc**(object)

Get the documentation string for an object.

All tabs are expanded to spaces.  To clean up docstrings that are
indented to line up with blocks of code, any whitespace than can be
uniformly removed from the second line onwards is removed.

---

#func <small>inspect.</small>**getfile**(object)

Work out which source or compiled file an object was defined in.

---

#func <small>inspect.</small>**getframeinfo**(frame, context=1)

Get information about a frame or traceback object.

A tuple of five things is returned: the filename, the line number of
the current line, the function name, a list of lines of context from
the source code, and the index of the current line within that list.
The optional second argument specifies the number of lines of context
to return, which are centered around the current line.

---

#func <small>inspect.</small>**getfullargspec**(func)

Get the names and default values of a callable object's parameters.

A tuple of seven things is returned:
(args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations).
'args' is a list of the parameter names.
'varargs' and 'varkw' are the names of the * and ** parameters or None.
'defaults' is an n-tuple of the default values of the last n parameters.
'kwonlyargs' is a list of keyword-only parameter names.
'kwonlydefaults' is a dictionary mapping names from kwonlyargs to defaults.
'annotations' is a dictionary mapping parameter names to annotations.

Notable differences from inspect.signature():
  - the "self" parameter is always reported, even for bound methods
  - wrapper chains defined by __wrapped__ *not* unwrapped automatically

---

#func <small>inspect.</small>**getgeneratorlocals**(generator)

Get the mapping of generator local variables to their current values.

A dict is returned, with the keys the local variable names and values the
bound values.

---

#func <small>inspect.</small>**getgeneratorstate**(generator)

Get current state of a generator-iterator.

Possible states are:
  GEN_CREATED: Waiting to start execution.
  GEN_RUNNING: Currently being executed by the interpreter.
  GEN_SUSPENDED: Currently suspended at a yield expression.
  GEN_CLOSED: Execution has completed.

---

#func <small>inspect.</small>**getinnerframes**(tb, context=1)

Get a list of records for a traceback's frame and all lower frames.

Each record contains a frame object, filename, line number, function
name, a list of lines of context, and index within the context.

---

#func <small>inspect.</small>**getlineno**(frame)

Get the line number from a frame object, allowing for optimization.

---

#func <small>inspect.</small>**getmembers**(object, predicate=None)

Return all members of an object as (name, value) pairs sorted by name.
Optionally, only return members that satisfy a given predicate.

---

#func <small>inspect.</small>**getmodule**(object, _filename=None)

Return the module an object was defined in, or None if not found.

---

#func <small>inspect.</small>**getmodulename**(path)

Return the module name for a given file, or None.

---

#func <small>inspect.</small>**getmro**(cls)

Return tuple of base classes (including cls) in method resolution order.

---

#func <small>inspect.</small>**getouterframes**(frame, context=1)

Get a list of records for a frame and all higher (calling) frames.

Each record contains a frame object, filename, line number, function
name, a list of lines of context, and index within the context.

---

#func <small>inspect.</small>**getsource**(object)

Return the text of the source code for an object.

The argument may be a module, class, method, function, traceback, frame,
or code object.  The source code is returned as a single string.  An
OSError is raised if the source code cannot be retrieved.

---

#func <small>inspect.</small>**getsourcefile**(object)

Return the filename that can be used to locate an object's source.
Return None if no way can be identified to get the source.

---

#func <small>inspect.</small>**getsourcelines**(object)

Return a list of source lines and starting line number for an object.

The argument may be a module, class, method, function, traceback, frame,
or code object.  The source code is returned as a list of the lines
corresponding to the object and the line number indicates where in the
original source file the first line of code was found.  An OSError is
raised if the source code cannot be retrieved.

---

#func <small>inspect.</small>**indentsize**(line)

Return the indent size, in spaces, at the start of a line of text.

---

#func <small>inspect.</small>**isabstract**(object)

Return true if the object is an abstract base class (ABC).

---

#func <small>inspect.</small>**isasyncgen**(object)

Return true if the object is an asynchronous generator.

---

#func <small>inspect.</small>**isasyncgenfunction**(obj)

Return true if the object is an asynchronous generator function.

Asynchronous generator functions are defined with "async def"
syntax and have "yield" expressions in their body.

---

#func <small>inspect.</small>**isawaitable**(object)

Return true if object can be passed to an ``await`` expression.

---

#func <small>inspect.</small>**isbuiltin**(object)

Return true if the object is a built-in function or method.

Built-in functions and methods provide these attributes:
    __doc__         documentation string
    __name__        original name of this function or method
    __self__        instance to which a method is bound, or None

---

#func <small>inspect.</small>**isclass**(object)

Return true if the object is a class.

Class objects provide these attributes:
    __doc__         documentation string
    __module__      name of module in which this class was defined

---

#func <small>inspect.</small>**iscode**(object)

Return true if the object is a code object.

Code objects provide these attributes:
    co_argcount         number of arguments (not including *, ** args
                        or keyword only arguments)
    co_code             string of raw compiled bytecode
    co_cellvars         tuple of names of cell variables
    co_consts           tuple of constants used in the bytecode
    co_filename         name of file in which this code object was created
    co_firstlineno      number of first line in Python source code
    co_flags            bitmap: 1=optimized | 2=newlocals | 4=*arg | 8=**arg
                        | 16=nested | 32=generator | 64=nofree | 128=coroutine
                        | 256=iterable_coroutine | 512=async_generator
    co_freevars         tuple of names of free variables
    co_posonlyargcount  number of positional only arguments
    co_kwonlyargcount   number of keyword only arguments (not including ** arg)
    co_lnotab           encoded mapping of line numbers to bytecode indices
    co_name             name with which this code object was defined
    co_names            tuple of names other than arguments and function locals
    co_nlocals          number of local variables
    co_stacksize        virtual machine stack space required
    co_varnames         tuple of names of arguments and local variables

---

#func <small>inspect.</small>**iscoroutine**(object)

Return true if the object is a coroutine.

---

#func <small>inspect.</small>**iscoroutinefunction**(obj)

Return true if the object is a coroutine function.

Coroutine functions are defined with "async def" syntax.

---

#func <small>inspect.</small>**isdatadescriptor**(object)

Return true if the object is a data descriptor.

Data descriptors have a __set__ or a __delete__ attribute.  Examples are
properties (defined in Python) and getsets and members (defined in C).
Typically, data descriptors will also have __name__ and __doc__ attributes
(properties, getsets, and members have both of these attributes), but this
is not guaranteed.

---

#func <small>inspect.</small>**isframe**(object)

Return true if the object is a frame object.

Frame objects provide these attributes:
    f_back          next outer frame object (this frame's caller)
    f_builtins      built-in namespace seen by this frame
    f_code          code object being executed in this frame
    f_globals       global namespace seen by this frame
    f_lasti         index of last attempted instruction in bytecode
    f_lineno        current line number in Python source code
    f_locals        local namespace seen by this frame
    f_trace         tracing function for this frame, or None

---

#func <small>inspect.</small>**isfunction**(object)

Return true if the object is a user-defined function.

Function objects provide these attributes:
    __doc__         documentation string
    __name__        name with which this function was defined
    __code__        code object containing compiled function bytecode
    __defaults__    tuple of any default values for arguments
    __globals__     global namespace in which this function was defined
    __annotations__ dict of parameter annotations
    __kwdefaults__  dict of keyword only parameters with defaults

---

#func <small>inspect.</small>**isgenerator**(object)

Return true if the object is a generator.

Generator objects provide these attributes:
    __iter__        defined to support iteration over container
    close           raises a new GeneratorExit exception inside the
                    generator to terminate the iteration
    gi_code         code object
    gi_frame        frame object or possibly None once the generator has
                    been exhausted
    gi_running      set to 1 when generator is executing, 0 otherwise
    next            return the next item from the container
    send            resumes the generator and "sends" a value that becomes
                    the result of the current yield-expression
    throw           used to raise an exception inside the generator

---

#func <small>inspect.</small>**isgeneratorfunction**(obj)

Return true if the object is a user-defined generator function.

Generator function objects provide the same attributes as functions.
See help(isfunction) for a list of attributes.

---

#func <small>inspect.</small>**isgetsetdescriptor**(object)

Return true if the object is a getset descriptor.

getset descriptors are specialized descriptors defined in extension
modules.

---

#func <small>inspect.</small>**ismemberdescriptor**(object)

Return true if the object is a member descriptor.

Member descriptors are specialized descriptors defined in extension
modules.

---

#func <small>inspect.</small>**ismethod**(object)

Return true if the object is an instance method.

Instance method objects provide these attributes:
    __doc__         documentation string
    __name__        name with which this method was defined
    __func__        function object containing implementation of method
    __self__        instance to which this method is bound

---

#func <small>inspect.</small>**ismethoddescriptor**(object)

Return true if the object is a method descriptor.

But not if ismethod() or isclass() or isfunction() are true.

This is new in Python 2.2, and, for example, is true of int.__add__.
An object passing this test has a __get__ attribute but not a __set__
attribute, but beyond that the set of attributes varies.  __name__ is
usually sensible, and __doc__ often is.

Methods implemented via descriptors that also pass one of the other
tests return false from the ismethoddescriptor() test, simply because
the other tests promise more -- you can, e.g., count on having the
__func__ attribute (etc) when an object passes ismethod().

---

#func <small>inspect.</small>**ismodule**(object)

Return true if the object is a module.

Module objects provide these attributes:
    __cached__      pathname to byte compiled file
    __doc__         documentation string
    __file__        filename (missing for built-in modules)

---

#func <small>inspect.</small>**isroutine**(object)

Return true if the object is any kind of function or method.

---

#func <small>inspect.</small>**istraceback**(object)

Return true if the object is a traceback.

Traceback objects provide these attributes:
    tb_frame        frame object at this level
    tb_lasti        index of last attempted instruction in bytecode
    tb_lineno       current line number in Python source code
    tb_next         next inner traceback object (called by this level)

---

#func <small>inspect.</small>**signature**(obj, *, follow_wrapped=True, globals=None, locals=None, eval_str=False)

Get a signature object for the passed callable.

---

#func <small>inspect.</small>**stack**(context=1)

Return a list of records for the stack above the caller's frame.

---

#func <small>inspect.</small>**trace**(context=1)

Return a list of records for the stack below the current exception.

---

#func <small>inspect.</small>**unwrap**(func, *, stop=None)

Get the object wrapped by *func*.

Follows the chain of :attr:`__wrapped__` attributes returning the last
object in the chain.

*stop* is an optional callback accepting an object in the wrapper chain
as its sole argument that allows the unwrapping to be terminated early if
the callback returns a true value. If the callback never returns a true
value, the last object in the chain is returned as usual. For example,
:func:`signature` uses this to stop unwrapping if any object in the
chain has a ``__signature__`` attribute defined.

:exc:`ValueError` is raised if a cycle is encountered.

 

---

#func <small>inspect.</small>**walktree**(classes, children, parent)

Recursive helper function for getclasstree().

---

#class <small>collections.</small>**OrderedDict**None

Dictionary that remembers insertion order



---

#class <small>collections.</small>**ChainMap**(*maps)

A ChainMap groups multiple dicts (or other mappings) together
to create a single, updateable view.

The underlying mappings are stored in a list.  That list is public and can
be accessed or updated using the *maps* attribute.  There is no other
state.

Lookups search the underlying mappings successively until a key is found.
In contrast, writes, updates, and deletions only operate on the first
mapping.

$\qquad$**__init__**(self, *maps)

<span class="parent_indent">Initialize a ChainMap by setting *maps* to the given mappings.
If no mappings are provided, a single empty dictionary is used.</span>

$\qquad$**__missing__**(self, key)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__getitem__**(self, key)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**get**(self, key, default=None)

<span class="parent_indent">D.get(k[,d]) -> D[k] if k in D, else d.d defaults to None.</span>

$\qquad$**__len__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__iter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__contains__**(self, key)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__bool__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**fromkeys**(cls, iterable, *args)

<span class="parent_indent">Create a ChainMap with a single dict created from the iterable.</span>

$\qquad$**copy**(self)

<span class="parent_indent">New ChainMap or subclass with a new copy of maps[0] and refs to maps[1:]</span>

$\qquad$**copy**(self)

<span class="parent_indent">New ChainMap or subclass with a new copy of maps[0] and refs to maps[1:]</span>

$\qquad$**new_child**(self, m=None, **kwargs)

<span class="parent_indent">New ChainMap with a new map followed by all previous maps.
If no map is provided, an empty dict is used.
Keyword arguments update the map or new empty dict.</span>

$\qquad$**__setitem__**(self, key, value)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__delitem__**(self, key)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**popitem**(self)

<span class="parent_indent">Remove and return an item pair from maps[0]. Raise KeyError is maps[0] is empty.</span>

$\qquad$**pop**(self, key, *args)

<span class="parent_indent">Remove *key* from maps[0] and return its value. Raise KeyError if *key* not in maps[0].</span>

$\qquad$**clear**(self)

<span class="parent_indent">Clear maps[0], leaving maps[1:] intact.</span>

$\qquad$**__ior__**(self, other)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__or__**(self, other)

<span class="parent_indent">Return self|value.</span>

$\qquad$**__ror__**(self, other)

<span class="parent_indent">Return value|self.</span>

---

#class <small>collections.</small>**Counter**(iterable=None, /, **kwds)

Dict subclass for counting hashable items.  Sometimes called a bag
or multiset.  Elements are stored as dictionary keys and their counts
are stored as dictionary values.

>>> c = Counter('abcdeabcdabcaba')  # count elements from a string

>>> c.most_common(3)                # three most common elements
[('a', 5), ('b', 4), ('c', 3)]
>>> sorted(c)                       # list all unique elements
['a', 'b', 'c', 'd', 'e']
>>> ''.join(sorted(c.elements()))   # list elements with repetitions
'aaaaabbbbcccdde'
>>> sum(c.values())                 # total of all counts
15

>>> c['a']                          # count of letter 'a'
5
>>> for elem in 'shazam':           # update counts from an iterable
...     c[elem] += 1                # by adding 1 to each element's count
>>> c['a']                          # now there are seven 'a'
7
>>> del c['b']                      # remove all 'b'
>>> c['b']                          # now there are zero 'b'
0

>>> d = Counter('simsalabim')       # make another counter
>>> c.update(d)                     # add in the second counter
>>> c['a']                          # now there are nine 'a'
9

>>> c.clear()                       # empty the counter
>>> c
Counter()

Note:  If a count is set to zero or reduced to zero, it will remain
in the counter until the entry is deleted or the counter is cleared:

>>> c = Counter('aaabbc')
>>> c['b'] -= 2                     # reduce the count of 'b' by two
>>> c.most_common()                 # 'b' is still in, but its count is zero
[('a', 3), ('c', 1), ('b', 0)]

$\qquad$**__init__**(self, iterable=None, /, **kwds)

<span class="parent_indent">Create a new, empty Counter object.And if given, count elements
from an input iterable.Or, initialize the count from another mapping
of elements to their counts.
>>> c = Counter() # a new, empty counter
>>> c = Counter('gallahad') # a new counter from an iterable
>>> c = Counter({'a': 4, 'b': 2}) # a new counter from a mapping
>>> c = Counter(a=4, b=2) # a new counter from keyword args</span>

$\qquad$**__missing__**(self, key)

<span class="parent_indent">The count of elements not in the Counter is zero.</span>

$\qquad$**total**(self)

<span class="parent_indent">Sum of the counts</span>

$\qquad$**most_common**(self, n=None)

<span class="parent_indent">List the n most common elements and their counts from the most
common to the least.If n is None, then list all element counts.
>>> Counter('abracadabra').most_common(3)
[('a', 5), ('b', 2), ('r', 2)]</span>

$\qquad$**elements**(self)

<span class="parent_indent">Iterator over elements repeating each as many times as its count.
>>> c = Counter('ABCABC')
>>> sorted(c.elements())
['A', 'A', 'B', 'B', 'C', 'C']
# Knuth's example for prime factors of 1836:2**2 * 3**3 * 17**1
>>> prime_factors = Counter({2: 2, 3: 3, 17: 1})
>>> product = 1
>>> for factor in prime_factors.elements(): # loop over factors
... product *= factor # and multiply them
>>> product
1836
Note, if an element's count has been set to zero or is a negative
number, elements() will ignore it.</span>

$\qquad$**fromkeys**(cls, iterable, v=None)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**update**(self, iterable=None, /, **kwds)

<span class="parent_indent">Like dict.update() but add counts instead of replacing them.
Source can be an iterable, a dictionary, or another Counter instance.
>>> c = Counter('which')
>>> c.update('witch') # add elements from another iterable
>>> d = Counter('watch')
>>> c.update(d) # add elements from another counter
>>> c['h']# four 'h' in which, witch, and watch
4</span>

$\qquad$**subtract**(self, iterable=None, /, **kwds)

<span class="parent_indent">Like dict.update() but subtracts counts instead of replacing them.
Counts can be reduced below zero.Both the inputs and outputs are
allowed to contain zero and negative counts.
Source can be an iterable, a dictionary, or another Counter instance.
>>> c = Counter('which')
>>> c.subtract('witch') # subtract elements from another iterable
>>> c.subtract(Counter('watch'))# subtract elements from another counter
>>> c['h']# 2 in which, minus 1 in witch, minus 1 in watch
0
>>> c['w']# 1 in which, minus 1 in witch, minus 1 in watch
-1</span>

$\qquad$**copy**(self)

<span class="parent_indent">Return a shallow copy.</span>

$\qquad$**__reduce__**(self)

<span class="parent_indent">Helper for pickle.</span>

$\qquad$**__delitem__**(self, elem)

<span class="parent_indent">Like dict.__delitem__() but does not raise KeyError for missing values.</span>

$\qquad$**__eq__**(self, other)

<span class="parent_indent">True if all counts agree. Missing counts are treated as zero.</span>

$\qquad$**__ne__**(self, other)

<span class="parent_indent">True if any counts disagree. Missing counts are treated as zero.</span>

$\qquad$**__le__**(self, other)

<span class="parent_indent">True if all counts in self are a subset of those in other.</span>

$\qquad$**__lt__**(self, other)

<span class="parent_indent">True if all counts in self are a proper subset of those in other.</span>

$\qquad$**__ge__**(self, other)

<span class="parent_indent">True if all counts in self are a superset of those in other.</span>

$\qquad$**__gt__**(self, other)

<span class="parent_indent">True if all counts in self are a proper superset of those in other.</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**__add__**(self, other)

<span class="parent_indent">Add counts from two counters.
>>> Counter('abbb') + Counter('bcc')
Counter({'b': 4, 'c': 2, 'a': 1})</span>

$\qquad$**__sub__**(self, other)

<span class="parent_indent">Subtract count, but keep only results with positive counts.
>>> Counter('abbbc') - Counter('bccd')
Counter({'b': 2, 'a': 1})</span>

$\qquad$**__or__**(self, other)

<span class="parent_indent">Union is the maximum of value in either of the input counters.
>>> Counter('abbb') | Counter('bcc')
Counter({'b': 3, 'c': 2, 'a': 1})</span>

$\qquad$**__and__**(self, other)

<span class="parent_indent">Intersection is the minimum of corresponding counts.
>>> Counter('abbb') & Counter('bcc')
Counter({'b': 1})</span>

$\qquad$**__pos__**(self)

<span class="parent_indent">Adds an empty counter, effectively stripping negative and zero counts</span>

$\qquad$**__neg__**(self)

<span class="parent_indent">Subtracts from an empty counter.Strips positive and zero counts,
and flips the sign on negative counts.</span>

$\qquad$**_keep_positive**(self)

<span class="parent_indent">Internal method to strip elements with a negative or zero count</span>

$\qquad$**__iadd__**(self, other)

<span class="parent_indent">Inplace add from another counter, keeping only positive counts.
>>> c = Counter('abbb')
>>> c += Counter('bcc')
>>> c
Counter({'b': 4, 'c': 2, 'a': 1})</span>

$\qquad$**__isub__**(self, other)

<span class="parent_indent">Inplace subtract counter, but keep only results with positive counts.
>>> c = Counter('abbbc')
>>> c -= Counter('bccd')
>>> c
Counter({'b': 2, 'a': 1})</span>

$\qquad$**__ior__**(self, other)

<span class="parent_indent">Inplace union is the maximum of value from either counter.
>>> c = Counter('abbb')
>>> c |= Counter('bcc')
>>> c
Counter({'b': 3, 'c': 2, 'a': 1})</span>

$\qquad$**__iand__**(self, other)

<span class="parent_indent">Inplace intersection is the minimum of corresponding counts.
>>> c = Counter('abbb')
>>> c &= Counter('bcc')
>>> c
Counter({'b': 1})</span>

---

#class <small>collections.</small>**UserDict**(dict=None, /, **kwargs)

A MutableMapping is a generic container for associating
key/value pairs.

This class provides concrete generic implementations of all
methods except for __getitem__, __setitem__, __delitem__,
__iter__, and __len__.

$\qquad$**__init__**(self, dict=None, /, **kwargs)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__len__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__getitem__**(self, key)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__setitem__**(self, key, item)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__delitem__**(self, key)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__iter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__contains__**(self, key)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**__or__**(self, other)

<span class="parent_indent">Return self|value.</span>

$\qquad$**__ror__**(self, other)

<span class="parent_indent">Return value|self.</span>

$\qquad$**__ior__**(self, other)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__copy__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**copy**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**fromkeys**(cls, iterable, value=None)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>collections.</small>**UserList**(initlist=None)

A more or less complete user-defined wrapper around list objects.

$\qquad$**__init__**(self, initlist=None)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**__lt__**(self, other)

<span class="parent_indent">Return self<value.</span>

$\qquad$**__le__**(self, other)

<span class="parent_indent">Return self<=value.</span>

$\qquad$**__eq__**(self, other)

<span class="parent_indent">Return self==value.</span>

$\qquad$**__gt__**(self, other)

<span class="parent_indent">Return self>value.</span>

$\qquad$**__ge__**(self, other)

<span class="parent_indent">Return self>=value.</span>

$\qquad$**__cast**(self, other)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__contains__**(self, item)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__len__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__getitem__**(self, i)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__setitem__**(self, i, item)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__delitem__**(self, i)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__add__**(self, other)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__radd__**(self, other)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__iadd__**(self, other)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__mul__**(self, n)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__mul__**(self, n)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__imul__**(self, n)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__copy__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**append**(self, item)

<span class="parent_indent">S.append(value) -- append value to the end of the sequence</span>

$\qquad$**insert**(self, i, item)

<span class="parent_indent">S.insert(index, value) -- insert value before index</span>

$\qquad$**pop**(self, i=-1)

<span class="parent_indent">S.pop([index]) -> item -- remove and return item at index (default last).
Raise IndexError if list is empty or index is out of range.</span>

$\qquad$**remove**(self, item)

<span class="parent_indent">S.remove(value) -- remove first occurrence of value.
Raise ValueError if the value is not present.</span>

$\qquad$**clear**(self)

<span class="parent_indent">S.clear() -> None -- remove all items from S</span>

$\qquad$**copy**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**count**(self, item)

<span class="parent_indent">S.count(value) -> integer -- return number of occurrences of value</span>

$\qquad$**index**(self, item, *args)

<span class="parent_indent">S.index(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.
Supporting start and stop arguments is optional, but
recommended.</span>

$\qquad$**reverse**(self)

<span class="parent_indent">S.reverse() -- reverse *IN PLACE*</span>

$\qquad$**sort**(self, /, *args, **kwds)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**extend**(self, other)

<span class="parent_indent">S.extend(iterable) -- extend sequence by appending elements from the iterable</span>

---

#class <small>collections.</small>**UserString**(seq)

All the operations on a read-only sequence.

Concrete subclasses must override __new__ or __init__,
__getitem__, and __len__.

$\qquad$**__init__**(self, seq)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__str__**(self)

<span class="parent_indent">Return str(self).</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**__int__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__float__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__complex__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__hash__**(self)

<span class="parent_indent">Return hash(self).</span>

$\qquad$**__getnewargs__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__eq__**(self, string)

<span class="parent_indent">Return self==value.</span>

$\qquad$**__lt__**(self, string)

<span class="parent_indent">Return self<value.</span>

$\qquad$**__le__**(self, string)

<span class="parent_indent">Return self<=value.</span>

$\qquad$**__gt__**(self, string)

<span class="parent_indent">Return self>value.</span>

$\qquad$**__ge__**(self, string)

<span class="parent_indent">Return self>=value.</span>

$\qquad$**__contains__**(self, char)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__len__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__getitem__**(self, index)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__add__**(self, other)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__radd__**(self, other)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__mul__**(self, n)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__mul__**(self, n)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__mod__**(self, args)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__rmod__**(self, template)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**capitalize**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**casefold**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**center**(self, width, *args)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**count**(self, sub, start=0, end=9223372036854775807)

<span class="parent_indent">S.count(value) -> integer -- return number of occurrences of value</span>

$\qquad$**removeprefix**(self, prefix, /)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**removesuffix**(self, suffix, /)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**encode**(self, encoding=utf-8, errors=strict)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**endswith**(self, suffix, start=0, end=9223372036854775807)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**expandtabs**(self, tabsize=8)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**find**(self, sub, start=0, end=9223372036854775807)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**format**(self, /, *args, **kwds)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**format_map**(self, mapping)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**index**(self, sub, start=0, end=9223372036854775807)

<span class="parent_indent">S.index(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.
Supporting start and stop arguments is optional, but
recommended.</span>

$\qquad$**isalpha**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**isalnum**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**isascii**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**isdecimal**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**isdigit**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**isidentifier**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**islower**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**isnumeric**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**isprintable**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**isspace**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**istitle**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**isupper**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**join**(self, seq)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**ljust**(self, width, *args)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**lower**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**lstrip**(self, chars=None)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**partition**(self, sep)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**replace**(self, old, new, maxsplit=-1)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**rfind**(self, sub, start=0, end=9223372036854775807)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**rindex**(self, sub, start=0, end=9223372036854775807)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**rjust**(self, width, *args)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**rpartition**(self, sep)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**rstrip**(self, chars=None)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**split**(self, sep=None, maxsplit=-1)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**rsplit**(self, sep=None, maxsplit=-1)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**splitlines**(self, keepends=False)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**startswith**(self, prefix, start=0, end=9223372036854775807)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**strip**(self, chars=None)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**swapcase**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**title**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**translate**(self, *args)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**upper**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**zfill**(self, width)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>collections.</small>**_Link**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>collections.</small>**_OrderedDictItemsView**(mapping)

A set is a finite, iterable container.

This class provides concrete generic implementations of all
methods except for __contains__, __iter__ and __len__.

To override the comparisons (presumably for speed, as the
semantics are fixed), redefine __le__ and __ge__,
then the other operations will automatically follow suit.

$\qquad$**__reversed__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>collections.</small>**_OrderedDictKeysView**(mapping)

A set is a finite, iterable container.

This class provides concrete generic implementations of all
methods except for __contains__, __iter__ and __len__.

To override the comparisons (presumably for speed, as the
semantics are fixed), redefine __le__ and __ge__,
then the other operations will automatically follow suit.

$\qquad$**__reversed__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>collections.</small>**_OrderedDictValuesView**(mapping)

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__reversed__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>collections.</small>**defaultdict**None

defaultdict(default_factory=None, /, [...]) --> dict with default factory

The default factory is called without arguments to produce
a new value when a key is not present, in __getitem__ only.
A defaultdict compares equal to a dict with the same items.
All remaining arguments are treated the same as if they were
passed to the dict constructor, including keyword arguments.



---

#class <small>collections.</small>**deque**None

deque([iterable[, maxlen]]) --> deque object

A list-like sequence optimized for data accesses near its endpoints.



---

#func <small>collections.</small>**namedtuple**(typename, field_names, *, rename=False, defaults=None, module=None)

Returns a new subclass of tuple with named fields.

>>> Point = namedtuple('Point', ['x', 'y'])
>>> Point.__doc__                   # docstring for the new class
'Point(x, y)'
>>> p = Point(11, y=22)             # instantiate with positional args or keywords
>>> p[0] + p[1]                     # indexable like a plain tuple
33
>>> x, y = p                        # unpack like a regular tuple
>>> x, y
(11, 22)
>>> p.x + p.y                       # fields also accessible by name
33
>>> d = p._asdict()                 # convert to a dictionary
>>> d['x']
11
>>> Point(**d)                      # convert from a dictionary
Point(x=11, y=22)
>>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
Point(x=100, y=22)

---

#class <small>builtins.</small>**classmethod_descriptor**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**method-wrapper**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**wrapper_descriptor**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**ArithmeticError**None

Base class for arithmetic errors.



---

#class <small>builtins.</small>**AssertionError**None

Assertion failed.



---

#class <small>builtins.</small>**AttributeError**None

Attribute not found.



---

#class <small>builtins.</small>**BaseException**None

Common base class for all exceptions



---

#class <small>builtins.</small>**BlockingIOError**None

I/O operation would block.



---

#class <small>builtins.</small>**BrokenPipeError**None

Broken pipe.



---

#class <small>builtins.</small>**BufferError**None

Buffer error.



---

#class <small>builtins.</small>**BytesWarning**None

Base class for warnings about bytes and buffer related problems, mostly
related to conversion from str or comparing to str.



---

#class <small>builtins.</small>**ChildProcessError**None

Child process error.



---

#class <small>builtins.</small>**ConnectionAbortedError**None

Connection aborted.



---

#class <small>builtins.</small>**ConnectionError**None

Connection error.



---

#class <small>builtins.</small>**ConnectionRefusedError**None

Connection refused.



---

#class <small>builtins.</small>**ConnectionResetError**None

Connection reset.



---

#class <small>builtins.</small>**DeprecationWarning**None

Base class for warnings about deprecated features.



---

#class <small>builtins.</small>**EOFError**None

Read beyond end of file.



---

#class <small>builtins.</small>**EncodingWarning**None

Base class for warnings about encodings.



---

#class <small>builtins.</small>**OSError**None

Base class for I/O related errors.



---

#class <small>builtins.</small>**Exception**None

Common base class for all non-exit exceptions.



---

#class <small>builtins.</small>**FileExistsError**None

File already exists.



---

#class <small>builtins.</small>**FileNotFoundError**None

File not found.



---

#class <small>builtins.</small>**FloatingPointError**None

Floating point operation failed.



---

#class <small>builtins.</small>**FutureWarning**None

Base class for warnings about constructs that will change semantically
in the future.



---

#class <small>builtins.</small>**GeneratorExit**None

Request that a generator exit.



---

#class <small>builtins.</small>**OSError**None

Base class for I/O related errors.



---

#class <small>builtins.</small>**ImportError**None

Import can't find module, or can't find name in module.



---

#class <small>builtins.</small>**ImportWarning**None

Base class for warnings about probable mistakes in module imports



---

#class <small>builtins.</small>**IndentationError**None

Improper indentation.



---

#class <small>builtins.</small>**IndexError**None

Sequence index out of range.



---

#class <small>builtins.</small>**InterruptedError**None

Interrupted by signal.



---

#class <small>builtins.</small>**IsADirectoryError**None

Operation doesn't work on directories.



---

#class <small>builtins.</small>**KeyError**None

Mapping key not found.



---

#class <small>builtins.</small>**KeyboardInterrupt**None

Program interrupted by user.



---

#class <small>builtins.</small>**LookupError**None

Base class for lookup errors.



---

#class <small>builtins.</small>**MemoryError**None

Out of memory.



---

#class <small>builtins.</small>**ModuleNotFoundError**None

Module not found.



---

#class <small>builtins.</small>**NameError**None

Name not found globally.



---

#class <small>builtins.</small>**NotADirectoryError**None

Operation only works on directories.



---

#class <small>builtins.</small>**NotImplementedError**None

Method or function hasn't been implemented yet.



---

#class <small>builtins.</small>**OSError**None

Base class for I/O related errors.



---

#class <small>builtins.</small>**OverflowError**None

Result too large to be represented.



---

#class <small>builtins.</small>**PendingDeprecationWarning**None

Base class for warnings about features which will be deprecated
in the future.



---

#class <small>builtins.</small>**PermissionError**None

Not enough permissions.



---

#class <small>builtins.</small>**ProcessLookupError**None

Process not found.



---

#class <small>builtins.</small>**RecursionError**None

Recursion limit exceeded.



---

#class <small>builtins.</small>**ReferenceError**None

Weak ref proxy used after referent went away.



---

#class <small>builtins.</small>**ResourceWarning**None

Base class for warnings about resource usage.



---

#class <small>builtins.</small>**RuntimeError**None

Unspecified run-time error.



---

#class <small>builtins.</small>**RuntimeWarning**None

Base class for warnings about dubious runtime behavior.



---

#class <small>builtins.</small>**StopAsyncIteration**None

Signal the end from iterator.__anext__().



---

#class <small>builtins.</small>**StopIteration**None

Signal the end from iterator.__next__().



---

#class <small>builtins.</small>**SyntaxError**None

Invalid syntax.



---

#class <small>builtins.</small>**SyntaxWarning**None

Base class for warnings about dubious syntax.



---

#class <small>builtins.</small>**SystemError**None

Internal error in the Python interpreter.

Please report this to the Python maintainer, along with the traceback,
the Python version, and the hardware/OS platform and version.



---

#class <small>builtins.</small>**SystemExit**None

Request to exit from the interpreter.



---

#class <small>builtins.</small>**TabError**None

Improper mixture of spaces and tabs.



---

#class <small>builtins.</small>**TimeoutError**None

Timeout expired.



---

#class <small>builtins.</small>**TypeError**None

Inappropriate argument type.



---

#class <small>builtins.</small>**UnboundLocalError**None

Local name referenced but not bound to a value.



---

#class <small>builtins.</small>**UnicodeDecodeError**None

Unicode decoding error.



---

#class <small>builtins.</small>**UnicodeEncodeError**None

Unicode encoding error.



---

#class <small>builtins.</small>**UnicodeError**None

Unicode related error.



---

#class <small>builtins.</small>**UnicodeTranslateError**None

Unicode translation error.



---

#class <small>builtins.</small>**UnicodeWarning**None

Base class for warnings about Unicode related problems, mostly
related to conversion problems.



---

#class <small>builtins.</small>**UserWarning**None

Base class for warnings generated by user code.



---

#class <small>builtins.</small>**ValueError**None

Inappropriate argument value (of correct type).



---

#class <small>builtins.</small>**Warning**None

Base class for warning categories.



---

#class <small>builtins.</small>**OSError**None

Base class for I/O related errors.



---

#class <small>builtins.</small>**ZeroDivisionError**None

Second argument to a division or modulo operation was zero.



---

#class <small>builtins.</small>**bool**None

bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.



---

#class <small>builtins.</small>**bytearray**None

bytearray(iterable_of_ints) -> bytearray
bytearray(string, encoding[, errors]) -> bytearray
bytearray(bytes_or_buffer) -> mutable copy of bytes_or_buffer
bytearray(int) -> bytes array of size given by the parameter initialized with null bytes
bytearray() -> empty bytes array

Construct a mutable bytearray object from:
  - an iterable yielding integers in range(256)
  - a text string encoded using the specified encoding
  - a bytes or a buffer object
  - any object implementing the buffer API.
  - an integer



---

#class <small>builtins.</small>**bytes**None

bytes(iterable_of_ints) -> bytes
bytes(string, encoding[, errors]) -> bytes
bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
bytes(int) -> bytes object of size given by the parameter initialized with null bytes
bytes() -> empty bytes object

Construct an immutable array of bytes from:
  - an iterable yielding integers in range(256)
  - a text string encoded using the specified encoding
  - any object implementing the buffer API.
  - an integer



---

#class <small>builtins.</small>**classmethod**None

classmethod(function) -> method

Convert a function to be a class method.

A class method receives the class as implicit first argument,
just like an instance method receives the instance.
To declare a class method, use this idiom:

  class C:
      @classmethod
      def f(cls, arg1, arg2, ...):
          ...

It can be called either on the class (e.g. C.f()) or on an instance
(e.g. C().f()).  The instance is ignored except for its class.
If a class method is called for a derived class, the derived class
object is passed as the implied first argument.

Class methods are different than C++ or Java static methods.
If you want those, see the staticmethod builtin.



---

#class <small>builtins.</small>**complex**(real=0, imag=0)

Create a complex number from a real part and an optional imaginary part.

This is equivalent to (real + imag*1j) where imag defaults to 0.



---

#class <small>builtins.</small>**dict**None

dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
    d = {}
    for k, v in iterable:
        d[k] = v
dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)



---

#class <small>builtins.</small>**enumerate**(iterable, start=0)

Return an enumerate object.

  iterable
    an object supporting iteration

The enumerate object yields pairs containing a count (from start, which
defaults to zero) and a value yielded by the iterable argument.

enumerate is useful for obtaining an indexed list:
    (0, seq[0]), (1, seq[1]), (2, seq[2]), ...



---

#class <small>builtins.</small>**filter**None

filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.



---

#class <small>builtins.</small>**float**(x=0, /)

Convert a string or number to a floating point number, if possible.



---

#class <small>builtins.</small>**frozenset**None

frozenset() -> empty frozenset object
frozenset(iterable) -> frozenset object

Build an immutable unordered collection of unique elements.



---

#class <small>builtins.</small>**int**None

int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4



---

#class <small>builtins.</small>**list**(iterable=(), /)

Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.



---

#class <small>builtins.</small>**map**None

map(func, *iterables) --> map object

Make an iterator that computes the function using arguments from
each of the iterables.  Stops when the shortest iterable is exhausted.



---

#class <small>builtins.</small>**memoryview**(object)

Create a new memoryview object which references the given object.



---

#class <small>builtins.</small>**object**()

The base class of the class hierarchy.

When called, it accepts no arguments and returns a new featureless
instance that has no instance attributes and cannot be given any.



---

#class <small>builtins.</small>**property**(fget=None, fset=None, fdel=None, doc=None)

Property attribute.

  fget
    function to be used for getting an attribute value
  fset
    function to be used for setting an attribute value
  fdel
    function to be used for del'ing an attribute
  doc
    docstring

Typical use is to define a managed attribute x:

class C(object):
    def getx(self): return self._x
    def setx(self, value): self._x = value
    def delx(self): del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")

Decorators make defining new properties or modifying existing ones easy:

class C(object):
    @property
    def x(self):
        "I am the 'x' property."
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    @x.deleter
    def x(self):
        del self._x



---

#class <small>builtins.</small>**range**None

range(stop) -> range object
range(start, stop[, step]) -> range object

Return an object that produces a sequence of integers from start (inclusive)
to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
These are exactly the valid indices for a list of 4 elements.
When step is given, it specifies the increment (or decrement).



---

#class <small>builtins.</small>**reversed**(sequence, /)

Return a reverse iterator over the values of the given sequence.



---

#class <small>builtins.</small>**set**None

set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.



---

#class <small>builtins.</small>**staticmethod**None

staticmethod(function) -> method

Convert a function to be a static method.

A static method does not receive an implicit first argument.
To declare a static method, use this idiom:

     class C:
         @staticmethod
         def f(arg1, arg2, ...):
             ...

It can be called either on the class (e.g. C.f()) or on an instance
(e.g. C().f()). Both the class and the instance are ignored, and
neither is passed implicitly as the first argument to the method.

Static methods in Python are similar to those found in Java or C++.
For a more advanced concept, see the classmethod builtin.



---

#class <small>builtins.</small>**str**None

str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.



---

#class <small>builtins.</small>**super**None

super() -> same as super(__class__, <first argument>)
super(type) -> unbound super object
super(type, obj) -> bound super object; requires isinstance(obj, type)
super(type, type2) -> bound super object; requires issubclass(type2, type)
Typical use to call a cooperative superclass method:
class C(B):
    def meth(self, arg):
        super().meth(arg)
This works for class methods too:
class C(B):
    @classmethod
    def cmeth(cls, arg):
        super().cmeth(arg)



---

#class <small>builtins.</small>**tuple**(iterable=(), /)

Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.



---

#class <small>builtins.</small>**type**None

type(object) -> the object's type
type(name, bases, dict, **kwds) -> a new type



---

#class <small>builtins.</small>**zip**None

zip(*iterables, strict=False) --> Yield tuples until an input is exhausted.

   >>> list(zip('abcdefg', range(3), range(4)))
   [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]

The zip object yields n-length tuples, where n is the number of iterables
passed as positional arguments to zip().  The i-th element in every tuple
comes from the i-th iterable argument to zip().  This continues until the
shortest argument is exhausted.

If strict is true and one of the arguments is exhausted before the others,
raise a ValueError.



---

#class <small>builtins.</small>**ellipsis**None

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**async_generator**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**bytearray_iterator**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**bytes_iterator**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**coroutine**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**dict_itemiterator**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**dict_items**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**dict_keyiterator**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**dict_keys**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**dict_valueiterator**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**dict_values**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**generator**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**list_iterator**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**list_reverseiterator**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**longrange_iterator**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**mappingproxy**None

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**range_iterator**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**set_iterator**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**str_iterator**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**tuple_iterator**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**zip**None

zip(*iterables, strict=False) --> Yield tuples until an input is exhausted.

   >>> list(zip('abcdefg', range(3), range(4)))
   [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]

The zip object yields n-length tuples, where n is the number of iterables
passed as positional arguments to zip().  The i-th element in every tuple
comes from the i-th iterable argument to zip().  This continues until the
shortest argument is exhausted.

If strict is true and one of the arguments is exhausted before the others,
raise a ValueError.



---

#class <small>builtins.</small>**mappingproxy**None

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**code**(argcount, posonlyargcount, kwonlyargcount, nlocals, stacksize, flags, codestring, constants, names, varnames, filename, name, firstlineno, linetable, freevars=(), cellvars=(), /)

Create a code object.  Not for the faint of heart.



---

#class <small>builtins.</small>**OSError**None

Base class for I/O related errors.



---

#class <small>builtins.</small>**PyHKEY**()

PyHKEY Object - A Python object, representing a win32 registry key.

This object wraps a Windows HKEY object, automatically closing it when
the object is destroyed.  To guarantee cleanup, you can call either
the Close() method on the PyHKEY, or the CloseKey() method.

All functions which accept a handle object also accept an integer --
however, use of the handle object is encouraged.

Functions:
Close() - Closes the underlying handle.
Detach() - Returns the integer Win32 handle, detaching it from the object

Properties:
handle - The integer Win32 handle.

Operations:
__bool__ - Handles with an open object return true, otherwise false.
__int__ - Converting a handle to an integer returns the Win32 handle.
rich comparison - Handle objects are compared using the handle value.



---

#class <small>builtins.</small>**weakcallableproxy**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**weakproxy**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**weakref**None

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**weakref**None

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>builtins.</small>**builtin_function_or_method**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>ast.</small>**AST**None

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>ast.</small>**Add**None

Add



---

#class <small>ast.</small>**And**None

And



---

#class <small>ast.</small>**AnnAssign**None

AnnAssign(expr target, expr annotation, expr? value, int simple)



---

#class <small>ast.</small>**Assert**None

Assert(expr test, expr? msg)



---

#class <small>ast.</small>**Assign**None

Assign(expr* targets, expr value, string? type_comment)



---

#class <small>ast.</small>**AsyncFor**None

AsyncFor(expr target, expr iter, stmt* body, stmt* orelse, string? type_comment)



---

#class <small>ast.</small>**AsyncFunctionDef**None

AsyncFunctionDef(identifier name, arguments args, stmt* body, expr* decorator_list, expr? returns, string? type_comment)



---

#class <small>ast.</small>**AsyncWith**None

AsyncWith(withitem* items, stmt* body, string? type_comment)



---

#class <small>ast.</small>**AugAssign**None

AugAssign(expr target, operator op, expr value)



---

#class <small>ast.</small>**AugLoad**None

Deprecated AST node class.  Unused in Python 3.



---

#class <small>ast.</small>**AugStore**None

Deprecated AST node class.  Unused in Python 3.



---

#class <small>ast.</small>**Await**None

Await(expr value)



---

#class <small>ast.</small>**BinOp**None

BinOp(expr left, operator op, expr right)



---

#class <small>ast.</small>**BitAnd**None

BitAnd



---

#class <small>ast.</small>**BitOr**None

BitOr



---

#class <small>ast.</small>**BitXor**None

BitXor



---

#class <small>ast.</small>**BoolOp**None

BoolOp(boolop op, expr* values)



---

#class <small>ast.</small>**Break**None

Break



---

#class <small>ast.</small>**Bytes**(*args, **kwargs)

Deprecated AST node class. Use ast.Constant instead



---

#class <small>ast.</small>**Call**None

Call(expr func, expr* args, keyword* keywords)



---

#class <small>ast.</small>**ClassDef**None

ClassDef(identifier name, expr* bases, keyword* keywords, stmt* body, expr* decorator_list)



---

#class <small>ast.</small>**Compare**None

Compare(expr left, cmpop* ops, expr* comparators)



---

#class <small>ast.</small>**Constant**None

Constant(constant value, string? kind)



---

#class <small>ast.</small>**Continue**None

Continue



---

#class <small>ast.</small>**Del**None

Del



---

#class <small>ast.</small>**Delete**None

Delete(expr* targets)



---

#class <small>ast.</small>**Dict**None

Dict(expr* keys, expr* values)



---

#class <small>ast.</small>**DictComp**None

DictComp(expr key, expr value, comprehension* generators)



---

#class <small>ast.</small>**Div**None

Div



---

#class <small>ast.</small>**Ellipsis**(*args, **kwargs)

Deprecated AST node class. Use ast.Constant instead



---

#class <small>ast.</small>**Eq**None

Eq



---

#class <small>ast.</small>**ExceptHandler**None

ExceptHandler(expr? type, identifier? name, stmt* body)



---

#class <small>ast.</small>**Expr**None

Expr(expr value)



---

#class <small>ast.</small>**Expression**None

Expression(expr body)



---

#class <small>ast.</small>**ExtSlice**(dims=(), **kwargs)

Deprecated AST node class. Use ast.Tuple instead.



---

#class <small>ast.</small>**FloorDiv**None

FloorDiv



---

#class <small>ast.</small>**For**None

For(expr target, expr iter, stmt* body, stmt* orelse, string? type_comment)



---

#class <small>ast.</small>**FormattedValue**None

FormattedValue(expr value, int conversion, expr? format_spec)



---

#class <small>ast.</small>**FunctionDef**None

FunctionDef(identifier name, arguments args, stmt* body, expr* decorator_list, expr? returns, string? type_comment)



---

#class <small>ast.</small>**FunctionType**None

FunctionType(expr* argtypes, expr returns)



---

#class <small>ast.</small>**GeneratorExp**None

GeneratorExp(expr elt, comprehension* generators)



---

#class <small>ast.</small>**Global**None

Global(identifier* names)



---

#class <small>ast.</small>**Gt**None

Gt



---

#class <small>ast.</small>**GtE**None

GtE



---

#class <small>ast.</small>**If**None

If(expr test, stmt* body, stmt* orelse)



---

#class <small>ast.</small>**IfExp**None

IfExp(expr test, expr body, expr orelse)



---

#class <small>ast.</small>**Import**None

Import(alias* names)



---

#class <small>ast.</small>**ImportFrom**None

ImportFrom(identifier? module, alias* names, int? level)



---

#class <small>ast.</small>**In**None

In



---

#class <small>ast.</small>**Index**(value, **kwargs)

Deprecated AST node class. Use the index value directly instead.



---

#class <small>ast.</small>**Interactive**None

Interactive(stmt* body)



---

#class <small>ast.</small>**Invert**None

Invert



---

#class <small>ast.</small>**Is**None

Is



---

#class <small>ast.</small>**IsNot**None

IsNot



---

#class <small>ast.</small>**JoinedStr**None

JoinedStr(expr* values)



---

#class <small>ast.</small>**LShift**None

LShift



---

#class <small>ast.</small>**Lambda**None

Lambda(arguments args, expr body)



---

#class <small>ast.</small>**List**None

List(expr* elts, expr_context ctx)



---

#class <small>ast.</small>**ListComp**None

ListComp(expr elt, comprehension* generators)



---

#class <small>ast.</small>**Load**None

Load



---

#class <small>ast.</small>**Lt**None

Lt



---

#class <small>ast.</small>**LtE**None

LtE



---

#class <small>ast.</small>**MatMult**None

MatMult



---

#class <small>ast.</small>**Match**None

Match(expr subject, match_case* cases)



---

#class <small>ast.</small>**MatchAs**None

MatchAs(pattern? pattern, identifier? name)



---

#class <small>ast.</small>**MatchClass**None

MatchClass(expr cls, pattern* patterns, identifier* kwd_attrs, pattern* kwd_patterns)



---

#class <small>ast.</small>**MatchMapping**None

MatchMapping(expr* keys, pattern* patterns, identifier? rest)



---

#class <small>ast.</small>**MatchOr**None

MatchOr(pattern* patterns)



---

#class <small>ast.</small>**MatchSequence**None

MatchSequence(pattern* patterns)



---

#class <small>ast.</small>**MatchSingleton**None

MatchSingleton(constant value)



---

#class <small>ast.</small>**MatchStar**None

MatchStar(identifier? name)



---

#class <small>ast.</small>**MatchValue**None

MatchValue(expr value)



---

#class <small>ast.</small>**Mod**None

Mod



---

#class <small>ast.</small>**Module**None

Module(stmt* body, type_ignore* type_ignores)



---

#class <small>ast.</small>**Mult**None

Mult



---

#class <small>ast.</small>**Name**None

Name(identifier id, expr_context ctx)



---

#class <small>ast.</small>**NameConstant**(*args, **kwargs)

Deprecated AST node class. Use ast.Constant instead



---

#class <small>ast.</small>**NamedExpr**None

NamedExpr(expr target, expr value)



---

#class <small>ast.</small>**NodeTransformer**()

A :class:`NodeVisitor` subclass that walks the abstract syntax tree and
allows modification of nodes.

The `NodeTransformer` will walk the AST and use the return value of the
visitor methods to replace or remove the old node.  If the return value of
the visitor method is ``None``, the node will be removed from its location,
otherwise it is replaced with the return value.  The return value may be the
original node in which case no replacement takes place.

Here is an example transformer that rewrites all occurrences of name lookups
(``foo``) to ``data['foo']``::

   class RewriteName(NodeTransformer):

       def visit_Name(self, node):
           return Subscript(
               value=Name(id='data', ctx=Load()),
               slice=Constant(value=node.id),
               ctx=node.ctx
           )

Keep in mind that if the node you're operating on has child nodes you must
either transform the child nodes yourself or call the :meth:`generic_visit`
method for the node first.

For nodes that were part of a collection of statements (that applies to all
statement nodes), the visitor may also return a list of nodes rather than
just a single node.

Usually you use the transformer like this::

   node = YourTransformer().visit(node)

$\qquad$**generic_visit**(self, node)

<span class="parent_indent">Called if no explicit visitor function exists for a node.</span>

---

#class <small>ast.</small>**NodeVisitor**()

A node visitor base class that walks the abstract syntax tree and calls a
visitor function for every node found.  This function may return a value
which is forwarded by the `visit` method.

This class is meant to be subclassed, with the subclass adding visitor
methods.

Per default the visitor functions for the nodes are ``'visit_'`` +
class name of the node.  So a `TryFinally` node visit function would
be `visit_TryFinally`.  This behavior can be changed by overriding
the `visit` method.  If no visitor function exists for a node
(return value `None`) the `generic_visit` visitor is used instead.

Don't use the `NodeVisitor` if you want to apply changes to nodes during
traversing.  For this a special visitor exists (`NodeTransformer`) that
allows modifications.

$\qquad$**visit**(self, node)

<span class="parent_indent">Visit a node.</span>

$\qquad$**generic_visit**(self, node)

<span class="parent_indent">Called if no explicit visitor function exists for a node.</span>

$\qquad$**visit_Constant**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>ast.</small>**Nonlocal**None

Nonlocal(identifier* names)



---

#class <small>ast.</small>**Not**None

Not



---

#class <small>ast.</small>**NotEq**None

NotEq



---

#class <small>ast.</small>**NotIn**None

NotIn



---

#class <small>ast.</small>**Num**(*args, **kwargs)

Deprecated AST node class. Use ast.Constant instead



---

#class <small>ast.</small>**Or**None

Or



---

#class <small>ast.</small>**Param**None

Deprecated AST node class.  Unused in Python 3.



---

#class <small>ast.</small>**Pass**None

Pass



---

#class <small>ast.</small>**Pow**None

Pow



---

#class <small>ast.</small>**RShift**None

RShift



---

#class <small>ast.</small>**Raise**None

Raise(expr? exc, expr? cause)



---

#class <small>ast.</small>**Return**None

Return(expr? value)



---

#class <small>ast.</small>**Set**None

Set(expr* elts)



---

#class <small>ast.</small>**SetComp**None

SetComp(expr elt, comprehension* generators)



---

#class <small>ast.</small>**Slice**None

Slice(expr? lower, expr? upper, expr? step)



---

#class <small>ast.</small>**Starred**None

Starred(expr value, expr_context ctx)



---

#class <small>ast.</small>**Store**None

Store



---

#class <small>ast.</small>**Str**(*args, **kwargs)

Deprecated AST node class. Use ast.Constant instead



---

#class <small>ast.</small>**Sub**None

Sub



---

#class <small>ast.</small>**Subscript**None

Subscript(expr value, expr slice, expr_context ctx)



---

#class <small>ast.</small>**Suite**None

Deprecated AST node class.  Unused in Python 3.



---

#class <small>ast.</small>**Try**None

Try(stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody)



---

#class <small>ast.</small>**Tuple**None

Tuple(expr* elts, expr_context ctx)



---

#class <small>ast.</small>**TypeIgnore**None

TypeIgnore(int lineno, string tag)



---

#class <small>ast.</small>**UAdd**None

UAdd



---

#class <small>ast.</small>**USub**None

USub



---

#class <small>ast.</small>**UnaryOp**None

UnaryOp(unaryop op, expr operand)



---

#class <small>ast.</small>**While**None

While(expr test, stmt* body, stmt* orelse)



---

#class <small>ast.</small>**With**None

With(withitem* items, stmt* body, string? type_comment)



---

#class <small>ast.</small>**Yield**None

Yield(expr? value)



---

#class <small>ast.</small>**YieldFrom**None

YieldFrom(expr value)



---

#class <small>ast.</small>**_ABC**(*args)

type(object) -> the object's type
type(name, bases, dict, **kwds) -> a new type

$\qquad$**__init__**(cls, *args)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__instancecheck__**(cls, inst)

<span class="parent_indent">Check if an object is an instance.</span>

---

#class <small>ast.</small>**_Precedence**(value, names=None, *, module=None, qualname=None, type=None, start=1)

Precedence table that originated from python grammar.

$\qquad$**_generate_next_value_**(name, start, count, last_values)

<span class="parent_indent">Generate the next value when not given.
name: the name of the member
start: the initial start value or None
count: the number of existing members
last_value: the last value assigned or None</span>

$\qquad$**next**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**int**None

<span class="parent_indent">int([x]) -> integer
int(x, base=10) -> integer
Convert a number or string to an integer, or return 0 if no arguments
are given.If x is a number, return x.__int__().For floating point
numbers, this truncates towards zero.
If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.The literal can be preceded by '+' or '-' and be surrounded
by whitespace.The base defaults to 10.Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4</span>

$\qquad$**__new__**(cls, value)

<span class="parent_indent">Create and return a new object.See help(type) for accurate signature.</span>

---

#class <small>ast.</small>**_Unparser**(*, _avoid_backslashes=False)

Methods in this class recursively traverse an AST and
output source code for the abstract syntax; original formatting
is disregarded.

$\qquad$**__init__**(self, *, _avoid_backslashes=False)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**interleave**(self, inter, f, seq)

<span class="parent_indent">Call f on each item in seq, calling inter() in between.</span>

$\qquad$**items_view**(self, traverser, items)

<span class="parent_indent">Traverse and separate the given *items* with a comma and append it to
the buffer. If *items* is a single item sequence, a trailing comma
will be added.</span>

$\qquad$**maybe_newline**(self)

<span class="parent_indent">Adds a newline if it isn't the start of generated source</span>

$\qquad$**fill**(self, text=)

<span class="parent_indent">Indent a piece of text and append it, according to the current
indentation level</span>

$\qquad$**write**(self, text)

<span class="parent_indent">Append a piece of text</span>

$\qquad$**buffer_writer**(self, text)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**block**(self, *, extra=None)

<span class="parent_indent">A context manager for preparing the source for blocks. It adds
the character':', increases the indentation on enter and decreases
the indentation on exit. If *extra* is given, it will be directly
appended after the colon character.</span>

$\qquad$**delimit**(self, start, end)

<span class="parent_indent">A context manager for preparing the source for expressions. It adds
*start* to the buffer and enters, after exit it adds *end*.</span>

$\qquad$**delimit_if**(self, start, end, condition)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**require_parens**(self, precedence, node)

<span class="parent_indent">Shortcut to adding precedence related parens</span>

$\qquad$**get_precedence**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**set_precedence**(self, precedence, *nodes)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**get_raw_docstring**(self, node)

<span class="parent_indent">If a docstring node is found in the body of the *node* parameter,
return that docstring node, None otherwise.
Logic mirrored from ``_PyAST_GetDocString``.</span>

$\qquad$**get_type_comment**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**traverse**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit**(self, node)

<span class="parent_indent">Outputs a source code string that, if converted back to an ast
(using ast.parse) will generate an AST equivalent to *node*</span>

$\qquad$**_write_docstring_and_traverse_body**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Module**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_FunctionType**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Expr**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_NamedExpr**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Import**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_ImportFrom**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Assign**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_AugAssign**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_AnnAssign**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Return**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Pass**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Break**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Continue**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Delete**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Assert**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Global**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Nonlocal**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Await**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Yield**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_YieldFrom**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Raise**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Try**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_ExceptHandler**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_ClassDef**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_FunctionDef**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_AsyncFunctionDef**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**_function_helper**(self, node, fill_suffix)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_For**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_AsyncFor**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**_for_helper**(self, fill, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_If**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_While**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_With**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_AsyncWith**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**_str_literal_helper**(self, string, *, quote_types=("", ", """, ""), escape_special_whitespace=False)

<span class="parent_indent">Helper for writing string literals, minimizing escapes.
Returns the tuple (string literal to write, possible quote types).</span>

$\qquad$**_write_str_avoiding_backslashes**(self, string, *, quote_types=("", ", """, ""))

<span class="parent_indent">Write string literal value with a best effort attempt to avoid backslashes.</span>

$\qquad$**visit_JoinedStr**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_FormattedValue**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**_fstring_JoinedStr**(self, node, write)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**_fstring_Constant**(self, node, write)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**_fstring_FormattedValue**(self, node, write)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Name**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**_write_docstring**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**_write_constant**(self, value)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Constant**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_List**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_ListComp**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_GeneratorExp**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_SetComp**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_DictComp**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_comprehension**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_IfExp**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Set**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Dict**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Tuple**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_UnaryOp**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_BinOp**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Compare**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_BoolOp**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Attribute**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Call**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Subscript**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Starred**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Ellipsis**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Slice**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Match**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_arg**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_arguments**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_keyword**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_Lambda**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_alias**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_withitem**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_match_case**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_MatchValue**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_MatchSingleton**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_MatchSequence**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_MatchStar**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_MatchMapping**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_MatchClass**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_MatchAs**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**visit_MatchOr**(self, node)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#func <small>ast.</small>**_dims_getter**(self)

Deprecated. Use elts instead.

---

#func <small>ast.</small>**_dims_setter**(self, value)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>ast.</small>**_getter**(self)

Deprecated. Use value instead.

---

#func <small>ast.</small>**_new**(cls, *args, **kwargs)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>ast.</small>**_pad_whitespace**(source)

Replace all chars except '\f\t' in a line with spaces.

---

#func <small>ast.</small>**_setter**(self, value)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>ast.</small>**_splitlines_no_ff**(source)

Split a string into lines ignoring form feed and other chars.

This mimics how the Python parser splits source code.

---

#class <small>ast.</small>**alias**None

alias(identifier name, identifier? asname)



---

#class <small>ast.</small>**arg**None

arg(identifier arg, expr? annotation, string? type_comment)



---

#class <small>ast.</small>**arguments**None

arguments(arg* posonlyargs, arg* args, arg? vararg, arg* kwonlyargs, expr* kw_defaults, arg? kwarg, expr* defaults)



---

#class <small>ast.</small>**boolop**None

boolop = And | Or



---

#class <small>ast.</small>**cmpop**None

cmpop = Eq | NotEq | Lt | LtE | Gt | GtE | Is | IsNot | In | NotIn



---

#class <small>ast.</small>**comprehension**None

comprehension(expr target, expr iter, expr* ifs, int is_async)



---

#func <small>ast.</small>**copy_location**(new_node, old_node)

Copy source location (`lineno`, `col_offset`, `end_lineno`, and `end_col_offset`
attributes) from *old_node* to *new_node* if possible, and return *new_node*.

---

#func <small>ast.</small>**dump**(node, annotate_fields=True, include_attributes=False, *, indent=None)

Return a formatted dump of the tree in node.  This is mainly useful for
debugging purposes.  If annotate_fields is true (by default),
the returned string will show the names and the values for fields.
If annotate_fields is false, the result string will be more compact by
omitting unambiguous field names.  Attributes such as line
numbers and column offsets are not dumped by default.  If this is wanted,
include_attributes can be set to true.  If indent is a non-negative
integer or string, then the tree will be pretty-printed with that indent
level. None (the default) selects the single line representation.

---

#class <small>ast.</small>**excepthandler**None

excepthandler = ExceptHandler(expr? type, identifier? name, stmt* body)



---

#class <small>ast.</small>**expr**None

expr = BoolOp(boolop op, expr* values)
| NamedExpr(expr target, expr value)
| BinOp(expr left, operator op, expr right)
| UnaryOp(unaryop op, expr operand)
| Lambda(arguments args, expr body)
| IfExp(expr test, expr body, expr orelse)
| Dict(expr* keys, expr* values)
| Set(expr* elts)
| ListComp(expr elt, comprehension* generators)
| SetComp(expr elt, comprehension* generators)
| DictComp(expr key, expr value, comprehension* generators)
| GeneratorExp(expr elt, comprehension* generators)
| Await(expr value)
| Yield(expr? value)
| YieldFrom(expr value)
| Compare(expr left, cmpop* ops, expr* comparators)
| Call(expr func, expr* args, keyword* keywords)
| FormattedValue(expr value, int conversion, expr? format_spec)
| JoinedStr(expr* values)
| Constant(constant value, string? kind)
| Attribute(expr value, identifier attr, expr_context ctx)
| Subscript(expr value, expr slice, expr_context ctx)
| Starred(expr value, expr_context ctx)
| Name(identifier id, expr_context ctx)
| List(expr* elts, expr_context ctx)
| Tuple(expr* elts, expr_context ctx)
| Slice(expr? lower, expr? upper, expr? step)



---

#class <small>ast.</small>**expr_context**None

expr_context = Load | Store | Del



---

#func <small>ast.</small>**fix_missing_locations**(node)

When you compile a node tree with compile(), the compiler expects lineno and
col_offset attributes for every node that supports them.  This is rather
tedious to fill in for generated nodes, so this helper adds these attributes
recursively where not already set, by setting them to the values of the
parent node.  It works recursively starting at *node*.

---

#func <small>ast.</small>**get_docstring**(node, clean=True)

Return the docstring for the given node or None if no docstring can
be found.  If the node provided does not have docstrings a TypeError
will be raised.

If *clean* is `True`, all tabs are expanded to spaces and any whitespace
that can be uniformly removed from the second line onwards is removed.

---

#func <small>ast.</small>**get_source_segment**(source, node, *, padded=False)

Get source code segment of the *source* that generated *node*.

If some location information (`lineno`, `end_lineno`, `col_offset`,
or `end_col_offset`) is missing, return None.

If *padded* is `True`, the first line of a multi-line statement will
be padded with spaces to match its original position.

---

#func <small>ast.</small>**increment_lineno**(node, n=1)

Increment the line number and end line number of each node in the tree
starting at *node* by *n*. This is useful to "move code" to a different
location in a file.

---

#func <small>ast.</small>**iter_child_nodes**(node)

Yield all direct child nodes of *node*, that is, all fields that are nodes
and all items of fields that are lists of nodes.

---

#func <small>ast.</small>**iter_fields**(node)

Yield a tuple of ``(fieldname, value)`` for each field in ``node._fields``
that is present on *node*.

---

#class <small>ast.</small>**keyword**None

keyword(identifier? arg, expr value)



---

#func <small>ast.</small>**literal_eval**(node_or_string)

Safely evaluate an expression node or a string containing a Python
expression.  The string or node provided may only consist of the following
Python literal structures: strings, bytes, numbers, tuples, lists, dicts,
sets, booleans, and None.

---

#func <small>ast.</small>**main**()

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#class <small>ast.</small>**match_case**None

match_case(pattern pattern, expr? guard, stmt* body)



---

#class <small>ast.</small>**mod**None

mod = Module(stmt* body, type_ignore* type_ignores)
| Interactive(stmt* body)
| Expression(expr body)
| FunctionType(expr* argtypes, expr returns)



---

#class <small>ast.</small>**operator**None

operator = Add | Sub | Mult | MatMult | Div | Mod | Pow | LShift | RShift | BitOr | BitXor | BitAnd | FloorDiv



---

#func <small>ast.</small>**parse**(source, filename=<unknown>, mode=exec, *, type_comments=False, feature_version=None)

Parse the source into an AST node.
Equivalent to compile(source, filename, mode, PyCF_ONLY_AST).
Pass type_comments=True to get back type comments where the syntax allows.

---

#class <small>ast.</small>**pattern**None

pattern = MatchValue(expr value)
| MatchSingleton(constant value)
| MatchSequence(pattern* patterns)
| MatchMapping(expr* keys, pattern* patterns, identifier? rest)
| MatchClass(expr cls, pattern* patterns, identifier* kwd_attrs, pattern* kwd_patterns)
| MatchStar(identifier? name)
| MatchAs(pattern? pattern, identifier? name)
| MatchOr(pattern* patterns)



---

#class <small>ast.</small>**slice**None

Deprecated AST node class.



---

#class <small>ast.</small>**stmt**None

stmt = FunctionDef(identifier name, arguments args, stmt* body, expr* decorator_list, expr? returns, string? type_comment)
| AsyncFunctionDef(identifier name, arguments args, stmt* body, expr* decorator_list, expr? returns, string? type_comment)
| ClassDef(identifier name, expr* bases, keyword* keywords, stmt* body, expr* decorator_list)
| Return(expr? value)
| Delete(expr* targets)
| Assign(expr* targets, expr value, string? type_comment)
| AugAssign(expr target, operator op, expr value)
| AnnAssign(expr target, expr annotation, expr? value, int simple)
| For(expr target, expr iter, stmt* body, stmt* orelse, string? type_comment)
| AsyncFor(expr target, expr iter, stmt* body, stmt* orelse, string? type_comment)
| While(expr test, stmt* body, stmt* orelse)
| If(expr test, stmt* body, stmt* orelse)
| With(withitem* items, stmt* body, string? type_comment)
| AsyncWith(withitem* items, stmt* body, string? type_comment)
| Match(expr subject, match_case* cases)
| Raise(expr? exc, expr? cause)
| Try(stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody)
| Assert(expr test, expr? msg)
| Import(alias* names)
| ImportFrom(identifier? module, alias* names, int? level)
| Global(identifier* names)
| Nonlocal(identifier* names)
| Expr(expr value)
| Pass
| Break
| Continue



---

#class <small>ast.</small>**type_ignore**None

type_ignore = TypeIgnore(int lineno, string tag)



---

#class <small>ast.</small>**unaryop**None

unaryop = Invert | Not | UAdd | USub



---

#func <small>ast.</small>**unparse**(ast_obj)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>ast.</small>**walk**(node)

Recursively yield all descendant nodes in the tree starting at *node*
(including *node* itself), in no specified order.  This is useful if you
only want to modify nodes in place and don't care about the context.

---

#class <small>ast.</small>**withitem**None

withitem(expr context_expr, expr? optional_vars)



---

#func <small>contextlib.</small>**contextmanager**(func)

@contextmanager decorator.

Typical usage:

    @contextmanager
    def some_generator(<arguments>):
        <setup>
        try:
            yield <value>
        finally:
            <cleanup>

This makes this:

    with some_generator(<arguments>) as <variable>:
        <body>

equivalent to this:

    <setup>
    try:
        <variable> = <value>
        <body>
    finally:
        <cleanup>

---

#class <small>contextlib.</small>**nullcontext**(enter_result=None)

Context manager that does no additional processing.

Used as a stand-in for a normal context manager, when a particular
block of code is only sometimes used with a normal context manager:

cm = optional_cm if condition else nullcontext()
with cm:
    # Perform operation, using optional_cm if condition is True

$\qquad$**__init__**(self, enter_result=None)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__enter__**(self)

<span class="parent_indent">Return `self` upon entering the runtime context.</span>

$\qquad$**__exit__**(self, *excinfo)

<span class="parent_indent">Raise any exception triggered within the runtime context.</span>

$\qquad$**__aenter__**(self)

<span class="parent_indent">Return `self` upon entering the runtime context.</span>

$\qquad$**__aexit__**(self, *excinfo)

<span class="parent_indent">Raise any exception triggered within the runtime context.</span>

---

#class <small>operator.</small>**attrgetter**None

attrgetter(attr, ...) --> attrgetter object

Return a callable object that fetches the given attribute(s) from its operand.
After f = attrgetter('name'), the call f(r) returns r.name.
After g = attrgetter('name', 'date'), the call g(r) returns (r.name, r.date).
After h = attrgetter('name.first', 'name.last'), the call h(r) returns
(r.name.first, r.name.last).



---

#class <small>operator.</small>**itemgetter**None

itemgetter(item, ...) --> itemgetter object

Return a callable object that fetches the given item(s) from its operand.
After f = itemgetter(2), the call f(r) returns r[2].
After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])



---

#class <small>itertools.</small>**chain**None

chain(*iterables) --> chain object

Return a chain object whose .__next__() method returns elements from the
first iterable until it is exhausted, then elements from the next
iterable, until all of the iterables are exhausted.



---

#class <small>itertools.</small>**repeat**None

repeat(object [,times]) -> create an iterator which returns the object
for the specified number of times.  If not specified, returns the object
endlessly.



---

#class <small>itertools.</small>**starmap**(function, iterable, /)

Return an iterator whose values are returned from the function evaluated with an argument tuple taken from the given sequence.



---

#class <small>itertools.</small>**_grouper**None

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>itertools.</small>**_tee**(iterable, /)

Iterator wrapped to make it copyable.



---

#class <small>itertools.</small>**_tee_dataobject**None

teedataobject(iterable, values, next, /)
--

Data container common to multiple tee objects.



---

#class <small>itertools.</small>**accumulate**(iterable, func=None, *, initial=None)

Return series of accumulated sums (or other binary function results).



---

#class <small>itertools.</small>**chain**None

chain(*iterables) --> chain object

Return a chain object whose .__next__() method returns elements from the
first iterable until it is exhausted, then elements from the next
iterable, until all of the iterables are exhausted.



---

#class <small>itertools.</small>**combinations**(iterable, r)

Return successive r-length combinations of elements in the iterable.

combinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)



---

#class <small>itertools.</small>**combinations_with_replacement**(iterable, r)

Return successive r-length combinations of elements in the iterable allowing individual elements to have successive repeats.

combinations_with_replacement('ABC', 2) --> ('A','A'), ('A','B'), ('A','C'), ('B','B'), ('B','C'), ('C','C')



---

#class <small>itertools.</small>**compress**(data, selectors)

Return data elements corresponding to true selector elements.

Forms a shorter iterator from selected data elements using the selectors to
choose the data elements.



---

#class <small>itertools.</small>**count**(start=0, step=1)

Return a count object whose .__next__() method returns consecutive values.

Equivalent to:
    def count(firstval=0, step=1):
        x = firstval
        while 1:
            yield x
            x += step



---

#class <small>itertools.</small>**cycle**(iterable, /)

Return elements from the iterable until it is exhausted. Then repeat the sequence indefinitely.



---

#class <small>itertools.</small>**dropwhile**(predicate, iterable, /)

Drop items from the iterable while predicate(item) is true.

Afterwards, return every element until the iterable is exhausted.



---

#class <small>itertools.</small>**filterfalse**(function, iterable, /)

Return those items of iterable for which function(item) is false.

If function is None, return the items that are false.



---

#class <small>itertools.</small>**groupby**(iterable, key=None)

make an iterator that returns consecutive keys and groups from the iterable

iterable
  Elements to divide into groups according to the key function.
key
  A function for computing the group category for each element.
  If the key function is not specified or is None, the element itself
  is used for grouping.



---

#class <small>itertools.</small>**islice**None

islice(iterable, stop) --> islice object
islice(iterable, start, stop[, step]) --> islice object

Return an iterator whose next() method returns selected values from an
iterable.  If start is specified, will skip all preceding elements;
otherwise, start defaults to zero.  Step defaults to one.  If
specified as another value, step determines how many values are
skipped between successive calls.  Works like a slice() on a list
but returns an iterator.



---

#class <small>itertools.</small>**pairwise**(iterable, /)

Return an iterator of overlapping pairs taken from the input iterator.

s -> (s0,s1), (s1,s2), (s2, s3), ...



---

#class <small>itertools.</small>**permutations**(iterable, r=None)

Return successive r-length permutations of elements in the iterable.

permutations(range(3), 2) --> (0,1), (0,2), (1,0), (1,2), (2,0), (2,1)



---

#class <small>itertools.</small>**product**None

product(*iterables, repeat=1) --> product object

Cartesian product of input iterables.  Equivalent to nested for-loops.

For example, product(A, B) returns the same as:  ((x,y) for x in A for y in B).
The leftmost iterators are in the outermost for-loop, so the output tuples
cycle in a manner similar to an odometer (with the rightmost element changing
on every iteration).

To compute the product of an iterable with itself, specify the number
of repetitions with the optional repeat keyword argument. For example,
product(A, repeat=4) means the same as product(A, A, A, A).

product('ab', range(3)) --> ('a',0) ('a',1) ('a',2) ('b',0) ('b',1) ('b',2)
product((0,1), (0,1), (0,1)) --> (0,0,0) (0,0,1) (0,1,0) (0,1,1) (1,0,0) ...



---

#class <small>itertools.</small>**repeat**None

repeat(object [,times]) -> create an iterator which returns the object
for the specified number of times.  If not specified, returns the object
endlessly.



---

#class <small>itertools.</small>**starmap**(function, iterable, /)

Return an iterator whose values are returned from the function evaluated with an argument tuple taken from the given sequence.



---

#class <small>itertools.</small>**takewhile**(predicate, iterable, /)

Return successive entries from an iterable as long as the predicate evaluates to true for each entry.



---

#class <small>itertools.</small>**zip_longest**None

zip_longest(iter1 [,iter2 [...]], [fillvalue=None]) --> zip_longest object

Return a zip_longest object whose .__next__() method returns a tuple where
the i-th element comes from the i-th iterable argument.  The .__next__()
method continues until the longest iterable in the argument sequence
is exhausted and then it raises StopIteration.  When the shorter iterables
are exhausted, the fillvalue is substituted in their place.  The fillvalue
defaults to None or can be specified by a keyword argument.



---

#class <small>collections.abc.</small>**AsyncGenerator**()

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__anext__**(self)

<span class="parent_indent">Return the next item from the asynchronous generator.
When exhausted, raise StopAsyncIteration.</span>

$\qquad$**asend**(self, value)

<span class="parent_indent">Send a value into the asynchronous generator.
Return next yielded value or raise StopAsyncIteration.</span>

$\qquad$**athrow**(self, typ, val=None, tb=None)

<span class="parent_indent">Raise an exception in the asynchronous generator.
Return next yielded value or raise StopAsyncIteration.</span>

$\qquad$**aclose**(self)

<span class="parent_indent">Raise GeneratorExit inside coroutine.
</span>

$\qquad$**__subclasshook__**(cls, C)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>collections.abc.</small>**AsyncIterable**()

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__aiter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__subclasshook__**(cls, C)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**GenericAlias**None

<span class="parent_indent">Represent a PEP 585 generic type
E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).</span>

---

#class <small>collections.abc.</small>**AsyncIterator**()

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__anext__**(self)

<span class="parent_indent">Return the next item or raise StopAsyncIteration when exhausted.</span>

$\qquad$**__aiter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__subclasshook__**(cls, C)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>collections.abc.</small>**Awaitable**()

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__await__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__subclasshook__**(cls, C)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**GenericAlias**None

<span class="parent_indent">Represent a PEP 585 generic type
E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).</span>

---

#class <small>collections.abc.</small>**ByteString**()

This unifies bytes and bytearray.

XXX Should add all their methods.



---

#class <small>collections.abc.</small>**Callable**()

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__call__**(self, *args, **kwds)

<span class="parent_indent">Call self as a function.</span>

$\qquad$**__subclasshook__**(cls, C)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**_CallableGenericAlias**(origin, args)

<span class="parent_indent">Represent `Callable[argtypes, resulttype]`.
This sets ``__args__`` to a tuple containing the flattened ``argtypes``
followed by ``resulttype``.
Example: ``Callable[[int, str], float]`` sets ``__args__`` to
``(int, str, float)``.</span>

---

#class <small>collections.abc.</small>**Collection**()

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__subclasshook__**(cls, C)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>collections.abc.</small>**Container**()

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__contains__**(self, x)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__subclasshook__**(cls, C)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**GenericAlias**None

<span class="parent_indent">Represent a PEP 585 generic type
E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).</span>

---

#class <small>collections.abc.</small>**Coroutine**()

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**send**(self, value)

<span class="parent_indent">Send a value into the coroutine.
Return next yielded value or raise StopIteration.</span>

$\qquad$**throw**(self, typ, val=None, tb=None)

<span class="parent_indent">Raise an exception in the coroutine.
Return next yielded value or raise StopIteration.</span>

$\qquad$**close**(self)

<span class="parent_indent">Raise GeneratorExit inside coroutine.
</span>

$\qquad$**__subclasshook__**(cls, C)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>collections.abc.</small>**Generator**()

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__next__**(self)

<span class="parent_indent">Return the next item from the generator.
When exhausted, raise StopIteration.</span>

$\qquad$**send**(self, value)

<span class="parent_indent">Send a value into the generator.
Return next yielded value or raise StopIteration.</span>

$\qquad$**throw**(self, typ, val=None, tb=None)

<span class="parent_indent">Raise an exception in the generator.
Return next yielded value or raise StopIteration.</span>

$\qquad$**close**(self)

<span class="parent_indent">Raise GeneratorExit inside generator.
</span>

$\qquad$**__subclasshook__**(cls, C)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>collections.abc.</small>**Hashable**()

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__hash__**(self)

<span class="parent_indent">Return hash(self).</span>

$\qquad$**__subclasshook__**(cls, C)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>collections.abc.</small>**ItemsView**(mapping)

A set is a finite, iterable container.

This class provides concrete generic implementations of all
methods except for __contains__, __iter__ and __len__.

To override the comparisons (presumably for speed, as the
semantics are fixed), redefine __le__ and __ge__,
then the other operations will automatically follow suit.

$\qquad$**_from_iterable**(cls, it)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__contains__**(self, item)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__iter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>collections.abc.</small>**Iterable**()

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__iter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__subclasshook__**(cls, C)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**GenericAlias**None

<span class="parent_indent">Represent a PEP 585 generic type
E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).</span>

---

#class <small>collections.abc.</small>**Iterator**()

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__next__**(self)

<span class="parent_indent">Return the next item from the iterator. When exhausted, raise StopIteration</span>

$\qquad$**__iter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__subclasshook__**(cls, C)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>collections.abc.</small>**KeysView**(mapping)

A set is a finite, iterable container.

This class provides concrete generic implementations of all
methods except for __contains__, __iter__ and __len__.

To override the comparisons (presumably for speed, as the
semantics are fixed), redefine __le__ and __ge__,
then the other operations will automatically follow suit.

$\qquad$**_from_iterable**(cls, it)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__contains__**(self, key)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__iter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>collections.abc.</small>**Mapping**()

A Mapping is a generic container for associating key/value
pairs.

This class provides concrete generic implementations of all
methods except for __getitem__, __iter__, and __len__.

$\qquad$**__getitem__**(self, key)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**get**(self, key, default=None)

<span class="parent_indent">D.get(k[,d]) -> D[k] if k in D, else d.d defaults to None.</span>

$\qquad$**__contains__**(self, key)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**keys**(self)

<span class="parent_indent">D.keys() -> a set-like object providing a view on D's keys</span>

$\qquad$**items**(self)

<span class="parent_indent">D.items() -> a set-like object providing a view on D's items</span>

$\qquad$**values**(self)

<span class="parent_indent">D.values() -> an object providing a view on D's values</span>

$\qquad$**__eq__**(self, other)

<span class="parent_indent">Return self==value.</span>

---

#class <small>collections.abc.</small>**MappingView**(mapping)

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__init__**(self, mapping)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__len__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**GenericAlias**None

<span class="parent_indent">Represent a PEP 585 generic type
E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).</span>

---

#class <small>collections.abc.</small>**MutableMapping**()

A MutableMapping is a generic container for associating
key/value pairs.

This class provides concrete generic implementations of all
methods except for __getitem__, __setitem__, __delitem__,
__iter__, and __len__.

$\qquad$**__setitem__**(self, key, value)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__delitem__**(self, key)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**pop**(self, key, default=<object object at 0x00000177D8974190>)

<span class="parent_indent">D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised.</span>

$\qquad$**popitem**(self)

<span class="parent_indent">D.popitem() -> (k, v), remove and return some (key, value) pair
as a 2-tuple; but raise KeyError if D is empty.</span>

$\qquad$**clear**(self)

<span class="parent_indent">D.clear() -> None.Remove all items from D.</span>

$\qquad$**update**(self, other=(), /, **kwds)

<span class="parent_indent">D.update([E, ]**F) -> None.Update D from mapping/iterable E and F.
If E present and has a .keys() method, does: for k in E: D[k] = E[k]
If E present and lacks .keys() method, does: for (k, v) in E: D[k] = v
In either case, this is followed by: for k, v in F.items(): D[k] = v</span>

$\qquad$**setdefault**(self, key, default=None)

<span class="parent_indent">D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D</span>

---

#class <small>collections.abc.</small>**MutableSequence**()

All the operations on a read-write sequence.

Concrete subclasses must provide __new__ or __init__,
__getitem__, __setitem__, __delitem__, __len__, and insert().

$\qquad$**__setitem__**(self, index, value)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__delitem__**(self, index)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**insert**(self, index, value)

<span class="parent_indent">S.insert(index, value) -- insert value before index</span>

$\qquad$**append**(self, value)

<span class="parent_indent">S.append(value) -- append value to the end of the sequence</span>

$\qquad$**clear**(self)

<span class="parent_indent">S.clear() -> None -- remove all items from S</span>

$\qquad$**reverse**(self)

<span class="parent_indent">S.reverse() -- reverse *IN PLACE*</span>

$\qquad$**extend**(self, values)

<span class="parent_indent">S.extend(iterable) -- extend sequence by appending elements from the iterable</span>

$\qquad$**pop**(self, index=-1)

<span class="parent_indent">S.pop([index]) -> item -- remove and return item at index (default last).
Raise IndexError if list is empty or index is out of range.</span>

$\qquad$**remove**(self, value)

<span class="parent_indent">S.remove(value) -- remove first occurrence of value.
Raise ValueError if the value is not present.</span>

$\qquad$**__iadd__**(self, values)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>collections.abc.</small>**MutableSet**()

A mutable set is a finite, iterable container.

This class provides concrete generic implementations of all
methods except for __contains__, __iter__, __len__,
add(), and discard().

To override the comparisons (presumably for speed, as the
semantics are fixed), all you have to do is redefine __le__ and
then the other operations will automatically follow suit.

$\qquad$**add**(self, value)

<span class="parent_indent">Add an element.</span>

$\qquad$**discard**(self, value)

<span class="parent_indent">Remove an element.Do not raise an exception if absent.</span>

$\qquad$**remove**(self, value)

<span class="parent_indent">Remove an element. If not a member, raise a KeyError.</span>

$\qquad$**pop**(self)

<span class="parent_indent">Return the popped value.Raise KeyError if empty.</span>

$\qquad$**clear**(self)

<span class="parent_indent">This is slow (creates N new iterators!) but effective.</span>

$\qquad$**__ior__**(self, it)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__iand__**(self, it)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__ixor__**(self, it)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__isub__**(self, it)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>collections.abc.</small>**Reversible**()

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__reversed__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__subclasshook__**(cls, C)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>collections.abc.</small>**Sequence**()

All the operations on a read-only sequence.

Concrete subclasses must override __new__ or __init__,
__getitem__, and __len__.

$\qquad$**__getitem__**(self, index)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__iter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__contains__**(self, value)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__reversed__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**index**(self, value, start=0, stop=None)

<span class="parent_indent">S.index(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.
Supporting start and stop arguments is optional, but
recommended.</span>

$\qquad$**count**(self, value)

<span class="parent_indent">S.count(value) -> integer -- return number of occurrences of value</span>

---

#class <small>collections.abc.</small>**Sized**()

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__len__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__subclasshook__**(cls, C)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>collections.abc.</small>**ValuesView**(mapping)

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__contains__**(self, value)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__iter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>collections.abc.</small>**_CallableGenericAlias**(origin, args)

Represent `Callable[argtypes, resulttype]`.

This sets ``__args__`` to a tuple containing the flattened ``argtypes``
followed by ``resulttype``.

Example: ``Callable[[int, str], float]`` sets ``__args__`` to
``(int, str, float)``.

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**__reduce__**(self)

<span class="parent_indent">Helper for pickle.</span>

$\qquad$**__getitem__**(self, item)

<span class="parent_indent">Return self[key].</span>

---

#func <small>collections.abc.</small>**_check_methods**(C, *methods)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>collections.abc.</small>**_is_param_expr**(obj)

Checks if obj matches either a list of types, ``...``, ``ParamSpec`` or
``_ConcatenateGenericAlias`` from typing.py

---

#func <small>collections.abc.</small>**_is_typevarlike**(arg)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>collections.abc.</small>**_type_repr**(obj)

Return the repr() of an object, special-casing types (internal helper).

Copied from :mod:`typing` since collections.abc
shouldn't depend on that module.

---

#class <small>types.</small>**GenericAlias**None

Represent a PEP 585 generic type

E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).



---

#class <small>types.</small>**DynamicClassAttribute**(fget=None, fset=None, fdel=None, doc=None)

Route attribute access on a class to __getattr__.

This is a descriptor, used to define attributes that act differently when
accessed through an instance and through a class.  Instance access remains
normal, but access to an attribute through a class will be routed to the
class's __getattr__ method; this is done by raising AttributeError.

This allows one to have properties active on an instance, and have virtual
attributes on the class with the same name.  (Enum used this between Python
versions 3.4 - 3.9 .)

Subclass from this to use a different method of accessing virtual atributes
and still be treated properly by the inspect module. (Enum uses this since
Python 3.10 .)

$\qquad$**__init__**(self, fget=None, fset=None, fdel=None, doc=None)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__get__**(self, instance, ownerclass=None)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__set__**(self, instance, value)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__delete__**(self, instance)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**getter**(self, fget)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**setter**(self, fset)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**deleter**(self, fdel)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#func <small>reprlib.</small>**recursive_repr**(fillvalue=...)

Decorator to make a repr function return fillvalue for a recursive call

---

#func <small>reprlib.</small>**recursive_repr**(fillvalue=...)

Decorator to make a repr function return fillvalue for a recursive call

---

#class <small>_collections.</small>**_tuplegetter**None

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>dis.</small>**Bytecode**(x, *, first_line=None, current_offset=None)

The bytecode operations of a piece of code

Instantiate this with a function, method, other compiled object, string of
code, or a code object (as returned by compile()).

Iterating over this yields the bytecode operations as Instruction instances.

$\qquad$**__init__**(self, x, *, first_line=None, current_offset=None)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__iter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**from_traceback**(cls, tb)

<span class="parent_indent">Construct a Bytecode from the given traceback </span>

$\qquad$**info**(self)

<span class="parent_indent">Return formatted information about the code object.</span>

$\qquad$**dis**(self)

<span class="parent_indent">Return a formatted view of the bytecode operations.</span>

---

#class <small>dis.</small>**Instruction**(opname, opcode, arg, argval, argrepr, offset, starts_line, is_jump_target)

Details for a bytecode operation

Defined fields:
  opname - human readable name for operation
  opcode - numeric code for operation
  arg - numeric argument to operation (if any), otherwise None
  argval - resolved arg value (if known), otherwise same as arg
  argrepr - human readable description of operation argument
  offset - start index of operation within bytecode sequence
  starts_line - line started by this opcode (if any), otherwise None
  is_jump_target - True if other code jumps to here, otherwise False

$\qquad$**_disassemble**(self, lineno_width=3, mark_as_current=False, offset_width=4)

<span class="parent_indent">Format instruction details for inclusion in disassembly output
*lineno_width* sets the width of the line number field (0 omits it)
*mark_as_current* inserts a '-->' marker arrow as part of the line
*offset_width* sets the width of the instruction offset field</span>

---

#class <small>dis.</small>**_Instruction**(opname, opcode, arg, argval, argrepr, offset, starts_line, is_jump_target)

_Instruction(opname, opcode, arg, argval, argrepr, offset, starts_line, is_jump_target)

$\qquad$**_make**(cls, iterable)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**_replace**(self, /, **kwds)

<span class="parent_indent">Return a new _Instruction object replacing specified fields with new values</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return a nicely formatted representation string</span>

$\qquad$**_asdict**(self)

<span class="parent_indent">Return a new dict which maps field names to their values.</span>

$\qquad$**__getnewargs__**(self)

<span class="parent_indent">Return self as a plain tuple.Used by copy and pickle.</span>

---

#func <small>dis.</small>**_disassemble_bytes**(code, lasti=-1, varnames=None, names=None, constants=None, cells=None, linestarts=None, *, file=None, line_offset=0)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>dis.</small>**_disassemble_recursive**(co, *, file=None, depth=None)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>dis.</small>**_disassemble_str**(source, **kwargs)

Compile the source string, then disassemble the code object.

---

#func <small>dis.</small>**_format_code_info**(co)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>dis.</small>**_get_code_object**(x)

Helper to handle methods, compiled or raw code objects, and strings.

---

#func <small>dis.</small>**_get_const_info**(const_index, const_list)

Helper to get optional details about const references

Returns the dereferenced constant and its repr if the constant
list is defined.
Otherwise returns the constant index and its repr().

---

#func <small>dis.</small>**_get_instructions_bytes**(code, varnames=None, names=None, constants=None, cells=None, linestarts=None, line_offset=0)

Iterate over the instructions in a bytecode string.

Generates a sequence of Instruction namedtuples giving the details of each
opcode.  Additional information about the code's runtime environment
(e.g. variable names, constants) can be specified using optional
arguments.

---

#func <small>dis.</small>**_get_name_info**(name_index, name_list)

Helper to get optional details about named references

Returns the dereferenced name as both value and repr if the name
list is defined.
Otherwise returns the name index and its repr().

---

#func <small>dis.</small>**_test**()

Simple test program to disassemble a file.

---

#func <small>dis.</small>**_try_compile**(source, name)

Attempts to compile the given source, first as an expression and
then as a statement if the first approach fails.

Utility function to accept strings in functions that otherwise
expect code objects

---

#func <small>dis.</small>**_unpack_opargs**(code)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>dis.</small>**code_info**(x)

Formatted details of methods, functions, or code.

---

#func <small>dis.</small>**disassemble**(co, lasti=-1, *, file=None)

Disassemble a code object.

---

#func <small>dis.</small>**disassemble**(co, lasti=-1, *, file=None)

Disassemble a code object.

---

#func <small>dis.</small>**distb**(tb=None, *, file=None)

Disassemble a traceback (default: last traceback).

---

#func <small>dis.</small>**findlabels**(code)

Detect all offsets in a byte code which are jump targets.

Return the list of offsets.

---

#func <small>dis.</small>**findlinestarts**(code)

Find the offsets in a byte code which are start of lines in the source.

Generate pairs (offset, lineno)

---

#func <small>dis.</small>**get_instructions**(x, *, first_line=None)

Iterator for the opcodes in methods, functions or code

Generates a series of Instruction named tuples giving the details of
each operations in the supplied code.

If *first_line* is not None, it indicates the line number that should
be reported for the first source line in the disassembled code.
Otherwise, the source line information (if any) is taken directly from
the disassembled code object.

---

#func <small>dis.</small>**pretty_flags**(flags)

Return pretty representation of code flags.

---

#func <small>dis.</small>**show_code**(co, *, file=None)

Print details of methods, functions, or code to *file*.

If *file* is not provided, the output is printed on stdout.

---

#class <small>io.</small>**BufferedIOBase**None

Base class for buffered IO objects.

The main difference with RawIOBase is that the read() method
supports omitting the size argument, and does not have a default
implementation that defers to readinto().

In addition, read(), readinto() and write() may raise
BlockingIOError if the underlying raw stream is in non-blocking
mode and not ready; unlike their raw counterparts, they will never
return None.

A typical implementation should not inherit from a RawIOBase
implementation, but wrap one.



---

#class <small>io.</small>**BufferedRWPair**(reader, writer, buffer_size=8192, /)

A buffered reader and writer object together.

A buffered reader object and buffered writer object put together to
form a sequential IO object that can read and write. This is typically
used with a socket or two-way pipe.

reader and writer are RawIOBase objects that are readable and
writeable respectively. If the buffer_size is omitted it defaults to
DEFAULT_BUFFER_SIZE.



---

#class <small>io.</small>**BufferedRandom**(raw, buffer_size=8192)

A buffered interface to random access streams.

The constructor creates a reader and writer for a seekable stream,
raw, given in the first argument. If the buffer_size is omitted it
defaults to DEFAULT_BUFFER_SIZE.



---

#class <small>io.</small>**BufferedReader**(raw, buffer_size=8192)

Create a new buffered reader using the given readable raw IO object.



---

#class <small>io.</small>**BufferedWriter**(raw, buffer_size=8192)

A buffer for a writeable sequential RawIO object.

The constructor creates a BufferedWriter for the given writeable raw
stream. If the buffer_size is not given, it defaults to
DEFAULT_BUFFER_SIZE.



---

#class <small>io.</small>**BytesIO**(initial_bytes=b)

Buffered I/O implementation using an in-memory bytes buffer.



---

#class <small>io.</small>**FileIO**(file, mode=r, closefd=True, opener=None)

Open a file.

The mode can be 'r' (default), 'w', 'x' or 'a' for reading,
writing, exclusive creation or appending.  The file will be created if it
doesn't exist when opened for writing or appending; it will be truncated
when opened for writing.  A FileExistsError will be raised if it already
exists when opened for creating. Opening a file for creating implies
writing so this mode behaves in a similar way to 'w'.Add a '+' to the mode
to allow simultaneous reading and writing. A custom opener can be used by
passing a callable as *opener*. The underlying file descriptor for the file
object is then obtained by calling opener with (*name*, *flags*).
*opener* must return an open file descriptor (passing os.open as *opener*
results in functionality similar to passing None).



---

#class <small>io.</small>**IOBase**None

The abstract base class for all I/O classes.

This class provides dummy implementations for many methods that
derived classes can override selectively; the default implementations
represent a file that cannot be read, written or seeked.

Even though IOBase does not declare read, readinto, or write because
their signatures will vary, implementations and clients should
consider those methods part of the interface. Also, implementations
may raise UnsupportedOperation when operations they do not support are
called.

The basic type used for binary data read from or written to a file is
bytes. Other bytes-like objects are accepted as method arguments too.
In some cases (such as readinto), a writable object is required. Text
I/O classes work with str data.

Note that calling any method (except additional calls to close(),
which are ignored) on a closed stream should raise a ValueError.

IOBase (and its subclasses) support the iterator protocol, meaning
that an IOBase object can be iterated over yielding the lines in a
stream.

IOBase also supports the :keyword:`with` statement. In this example,
fp is closed after the suite of the with statement is complete:

with open('spam.txt', 'r') as fp:
    fp.write('Spam and eggs!')



---

#class <small>io.</small>**IncrementalNewlineDecoder**(decoder, translate, errors=strict)

Codec used when reading a file in universal newlines mode.

It wraps another incremental decoder, translating \r\n and \r into \n.
It also records the types of newlines encountered.  When used with
translate=False, it ensures that the newline sequence is returned in
one piece. When used with decoder=None, it expects unicode strings as
decode input and translates newlines without first invoking an external
decoder.



---

#class <small>io.</small>**RawIOBase**None

Base class for raw binary I/O.



---

#class <small>io.</small>**StringIO**(initial_value=, newline=\n)

Text I/O implementation using an in-memory buffer.

The initial_value argument sets the value of object.  The newline
argument is like the one of TextIOWrapper's constructor.



---

#class <small>io.</small>**TextIOBase**None

Base class for text I/O.

This class provides a character and line based interface to stream
I/O. There is no readinto method because Python's character strings
are immutable.



---

#class <small>io.</small>**TextIOWrapper**(buffer, encoding=None, errors=None, newline=None, line_buffering=False, write_through=False)

Character and line based layer over a BufferedIOBase object, buffer.

encoding gives the name of the encoding that the stream will be
decoded or encoded with. It defaults to locale.getpreferredencoding(False).

errors determines the strictness of encoding and decoding (see
help(codecs.Codec) or the documentation for codecs.register) and
defaults to "strict".

newline controls how line endings are handled. It can be None, '',
'\n', '\r', and '\r\n'.  It works as follows:

* On input, if newline is None, universal newlines mode is
  enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
  these are translated into '\n' before being returned to the
  caller. If it is '', universal newline mode is enabled, but line
  endings are returned to the caller untranslated. If it has any of
  the other legal values, input lines are only terminated by the given
  string, and the line ending is returned to the caller untranslated.

* On output, if newline is None, any '\n' characters written are
  translated to the system default line separator, os.linesep. If
  newline is '' or '\n', no translation takes place. If newline is any
  of the other legal values, any '\n' characters written are translated
  to the given string.

If line_buffering is True, a call to flush is implied when a call to
write contains a newline character.



---

#class <small>io.</small>**UnsupportedOperation**None

Base class for I/O related errors.



---

#class <small>io.</small>**_WindowsConsoleIO**(file, mode=r, closefd=True, opener=None)

Open a console buffer by file descriptor.

The mode can be 'rb' (default), or 'wb' for reading or writing bytes. All
other mode characters will be ignored. Mode 'b' will be assumed if it is
omitted. The *opener* parameter is always ignored.



---

#class <small>io.</small>**_BufferedIOBase**None

Base class for buffered IO objects.

The main difference with RawIOBase is that the read() method
supports omitting the size argument, and does not have a default
implementation that defers to readinto().

In addition, read(), readinto() and write() may raise
BlockingIOError if the underlying raw stream is in non-blocking
mode and not ready; unlike their raw counterparts, they will never
return None.

A typical implementation should not inherit from a RawIOBase
implementation, but wrap one.



---

#class <small>io.</small>**_IOBase**None

The abstract base class for all I/O classes.

This class provides dummy implementations for many methods that
derived classes can override selectively; the default implementations
represent a file that cannot be read, written or seeked.

Even though IOBase does not declare read, readinto, or write because
their signatures will vary, implementations and clients should
consider those methods part of the interface. Also, implementations
may raise UnsupportedOperation when operations they do not support are
called.

The basic type used for binary data read from or written to a file is
bytes. Other bytes-like objects are accepted as method arguments too.
In some cases (such as readinto), a writable object is required. Text
I/O classes work with str data.

Note that calling any method (except additional calls to close(),
which are ignored) on a closed stream should raise a ValueError.

IOBase (and its subclasses) support the iterator protocol, meaning
that an IOBase object can be iterated over yielding the lines in a
stream.

IOBase also supports the :keyword:`with` statement. In this example,
fp is closed after the suite of the with statement is complete:

with open('spam.txt', 'r') as fp:
    fp.write('Spam and eggs!')



---

#class <small>io.</small>**_RawIOBase**None

Base class for raw binary I/O.



---

#class <small>io.</small>**_TextIOBase**None

Base class for text I/O.

This class provides a character and line based interface to stream
I/O. There is no readinto method because Python's character strings
are immutable.



---

#class <small>_thread.</small>**RLock**None

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>_thread.</small>**lock**()

A lock object is a synchronization primitive.  To create a lock,
call threading.Lock().  Methods are:

acquire() -- lock the lock, possibly blocking until it can be obtained
release() -- unlock of the lock
locked() -- test whether the lock is currently locked

A lock is not owned by the thread that locked it; another thread may
unlock it.  A thread attempting to lock a lock that it has already locked
will block until another thread unlocks it.  Deadlocks may ensue.



---

#class <small>_thread.</small>**_ExceptHookArgs**(iterable=(), /)

ExceptHookArgs

Type used to pass arguments to threading.excepthook.



---

#class <small>_thread.</small>**_local**None

Thread-local data



---

#class <small>functools.</small>**CacheInfo**(hits, misses, maxsize, currsize)

CacheInfo(hits, misses, maxsize, currsize)

$\qquad$**_make**(cls, iterable)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**_replace**(self, /, **kwds)

<span class="parent_indent">Return a new CacheInfo object replacing specified fields with new values</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return a nicely formatted representation string</span>

$\qquad$**_asdict**(self)

<span class="parent_indent">Return a new dict which maps field names to their values.</span>

$\qquad$**__getnewargs__**(self)

<span class="parent_indent">Return self as a plain tuple.Used by copy and pickle.</span>

---

#class <small>functools.</small>**_HashedSeq**(tup, hash=<built-in function hash>)

This class guarantees that hash() will be called no more than once
per element.  This is important because the lru_cache() will hash
the key multiple times on a cache miss.

$\qquad$**__init__**(self, tup, hash=<built-in function hash>)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__hash__**(self)

<span class="parent_indent">Return hash(self).</span>

---

#func <small>functools.</small>**_c3_merge**(sequences)

Merges MROs in *sequences* to a single MRO using the C3 algorithm.

Adapted from https://www.python.org/download/releases/2.3/mro/.

---

#func <small>functools.</small>**_c3_mro**(cls, abcs=None)

Computes the method resolution order using extended C3 linearization.

If no *abcs* are given, the algorithm works exactly like the built-in C3
linearization used for method resolution.

If given, *abcs* is a list of abstract base classes that should be inserted
into the resulting MRO. Unrelated ABCs are ignored and don't end up in the
result. The algorithm inserts ABCs where their functionality is introduced,
i.e. issubclass(cls, abc) returns True for the class itself but returns
False for all its direct base classes. Implicit ABCs for a given class
(either registered or inferred from the presence of a special method like
__len__) are inserted directly after the last ABC explicitly listed in the
MRO of said class. If two implicit ABCs end up next to each other in the
resulting MRO, their ordering depends on the order of types in *abcs*.

---

#func <small>functools.</small>**_compose_mro**(cls, types)

Calculates the method resolution order for a given class *cls*.

Includes relevant abstract base classes (with their respective bases) from
the *types* iterable. Uses a modified C3 linearization algorithm.

---

#func <small>functools.</small>**_find_impl**(cls, registry)

Returns the best matching implementation from *registry* for type *cls*.

Where there is no registered implementation for a specific type, its method
resolution order is used to find a more generic implementation.

Note: if *registry* does not contain an implementation for the base
*object* type, this function may return None.

---

#func <small>functools.</small>**_ge_from_gt**(self, other, NotImplemented=NotImplemented)

Return a >= b.  Computed by @total_ordering from (a > b) or (a == b).

---

#func <small>functools.</small>**_ge_from_le**(self, other, NotImplemented=NotImplemented)

Return a >= b.  Computed by @total_ordering from (not a <= b) or (a == b).

---

#func <small>functools.</small>**_ge_from_lt**(self, other, NotImplemented=NotImplemented)

Return a >= b.  Computed by @total_ordering from (not a < b).

---

#func <small>functools.</small>**_gt_from_ge**(self, other, NotImplemented=NotImplemented)

Return a > b.  Computed by @total_ordering from (a >= b) and (a != b).

---

#func <small>functools.</small>**_gt_from_le**(self, other, NotImplemented=NotImplemented)

Return a > b.  Computed by @total_ordering from (not a <= b).

---

#func <small>functools.</small>**_gt_from_lt**(self, other, NotImplemented=NotImplemented)

Return a > b.  Computed by @total_ordering from (not a < b) and (a != b).

---

#func <small>functools.</small>**_le_from_ge**(self, other, NotImplemented=NotImplemented)

Return a <= b.  Computed by @total_ordering from (not a >= b) or (a == b).

---

#func <small>functools.</small>**_le_from_gt**(self, other, NotImplemented=NotImplemented)

Return a <= b.  Computed by @total_ordering from (not a > b).

---

#func <small>functools.</small>**_le_from_lt**(self, other, NotImplemented=NotImplemented)

Return a <= b.  Computed by @total_ordering from (a < b) or (a == b).

---

#class <small>functools.</small>**_lru_cache_wrapper**None

Create a cached callable that wraps another function.

user_function:      the function being cached

maxsize:  0         for no caching
          None      for unlimited cache size
          n         for a bounded cache

typed:    False     cache f(3) and f(3.0) as identical calls
          True      cache f(3) and f(3.0) as distinct calls

cache_info_type:    namedtuple class with the fields:
                        hits misses currsize maxsize



---

#func <small>functools.</small>**_lt_from_ge**(self, other, NotImplemented=NotImplemented)

Return a < b.  Computed by @total_ordering from (not a >= b).

---

#func <small>functools.</small>**_lt_from_gt**(self, other, NotImplemented=NotImplemented)

Return a < b.  Computed by @total_ordering from (not a > b) and (a != b).

---

#func <small>functools.</small>**_lt_from_le**(self, other, NotImplemented=NotImplemented)

Return a < b.  Computed by @total_ordering from (a <= b) and (a != b).

---

#func <small>functools.</small>**_make_key**(args, kwds, typed, kwd_mark=(<object object at 0x00000177D89742A0>,), fasttypes={<class str>, <class int>}, tuple=<class tuple>, type=<class type>, len=<built-in function len>)

Make a cache key from optionally typed positional and keyword arguments

The key is constructed in a way that is flat as possible rather than
as a nested structure that would take more memory.

If there is only a single argument and its data type is known to cache
its hash value, then that argument is returned without a wrapper.  This
saves space and improves lookup speed.

---

#func <small>functools.</small>**_unwrap_partial**(func)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>functools.</small>**cache**(user_function, /)

Simple lightweight unbounded cache.  Sometimes called "memoize".

---

#class <small>functools.</small>**cached_property**(func)

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__init__**(self, func)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__set_name__**(self, owner, name)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__get__**(self, instance, owner=None)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**GenericAlias**None

<span class="parent_indent">Represent a PEP 585 generic type
E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).</span>

---

#func <small>functools.</small>**lru_cache**(maxsize=128, typed=False)

Least-recently-used cache decorator.

If *maxsize* is set to None, the LRU features are disabled and the cache
can grow without bound.

If *typed* is True, arguments of different types will be cached separately.
For example, f(3.0) and f(3) will be treated as distinct calls with
distinct results.

Arguments to the cached function must be hashable.

View the cache statistics named tuple (hits, misses, maxsize, currsize)
with f.cache_info().  Clear the cache and statistics with f.cache_clear().
Access the underlying function with f.__wrapped__.

See:  https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)

---

#class <small>functools.</small>**partial**None

partial(func, *args, **keywords) - new function with partial application
of the given arguments and keywords.



---

#class <small>functools.</small>**partialmethod**(func, /, *args, **keywords)

Method descriptor with partial application of the given arguments
and keywords.

Supports wrapping existing descriptors and handles non-descriptor
callables as instance methods.

$\qquad$**__init__**(self, func, /, *args, **keywords)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**_make_unbound_method**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__get__**(self, obj, cls=None)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**GenericAlias**None

<span class="parent_indent">Represent a PEP 585 generic type
E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).</span>

---

#func <small>functools.</small>**singledispatch**(func)

Single-dispatch generic function decorator.

Transforms a function into a generic function, which can have different
behaviours depending upon the type of its first argument. The decorated
function acts as the default implementation, and additional
implementations can be registered using the register() attribute of the
generic function.

---

#class <small>functools.</small>**singledispatchmethod**(func)

Single-dispatch generic method descriptor.

Supports wrapping existing descriptors and handles non-descriptor
callables as instance methods.

$\qquad$**__init__**(self, func)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**register**(self, cls, method=None)

<span class="parent_indent">generic_method.register(cls, func) -> func
Registers a new implementation for the given *cls* on a *generic_method*.</span>

$\qquad$**__get__**(self, obj, cls=None)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#func <small>functools.</small>**total_ordering**(cls)

Class decorator that fills in missing ordering methods

---

#func <small>functools.</small>**update_wrapper**(wrapper, wrapped, assigned=(__module__, __name__, __qualname__, __doc__, __annotations__), updated=(__dict__,))

Update a wrapper function to look like the wrapped function

wrapper is the function to be updated
wrapped is the original function
assigned is a tuple naming the attributes assigned directly
from the wrapped function to the wrapper function (defaults to
functools.WRAPPER_ASSIGNMENTS)
updated is a tuple naming the attributes of the wrapper that
are updated with the corresponding attribute from the wrapped
function (defaults to functools.WRAPPER_UPDATES)

---

#func <small>functools.</small>**wraps**(wrapped, assigned=(__module__, __name__, __qualname__, __doc__, __annotations__), updated=(__dict__,))

Decorator factory to apply update_wrapper() to a wrapper function

Returns a decorator that invokes update_wrapper() with the decorated
function as the wrapper argument and the arguments to wraps() as the
remaining arguments. Default arguments are as for update_wrapper().
This is a convenience function to simplify applying partial() to
update_wrapper().

---

#class <small>importlib._abc.</small>**Loader**()

Abstract base class for import loaders.

$\qquad$**create_module**(self, spec)

<span class="parent_indent">Return a module to initialize and into which to load.
This method should raise ImportError if anything prevents it
from creating a new module.It may return None to indicate
that the spec should create the new module.</span>

$\qquad$**load_module**(self, fullname)

<span class="parent_indent">Return the loaded module.
The module must be added to sys.modules and have import-related
attributes set properly.The fullname is a str.
ImportError is raised on failure.
This method is deprecated in favor of loader.exec_module(). If
exec_module() exists then it is used to provide a backwards-compatible
functionality for this method.</span>

$\qquad$**module_repr**(self, module)

<span class="parent_indent">Return a module's repr.
Used by the module type when the method does not raise
NotImplementedError.
This method is deprecated.</span>

---

#class <small>importlib._bootstrap.</small>**BuiltinImporter**()

Meta path import for built-in modules.

All methods are either class or static methods to avoid the need to
instantiate the class.

$\qquad$**find_spec**(cls, fullname, path=None, target=None)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**find_module**(cls, fullname, path=None)

<span class="parent_indent">Find the built-in module.
If 'path' is ever specified then the search is considered a failure.
This method is deprecated.Use find_spec() instead.</span>

$\qquad$**get_code**(self, fullname)

<span class="parent_indent">Return None as built-in modules do not have code objects.</span>

$\qquad$**get_source**(self, fullname)

<span class="parent_indent">Return None as built-in modules do not have source code.</span>

$\qquad$**is_package**(self, fullname)

<span class="parent_indent">Return False as built-in modules are never packages.</span>

$\qquad$**_load_module_shim**(self, fullname)

<span class="parent_indent">Load the specified module into sys.modules and return it.
This method is deprecated.Use loader.exec_module() instead.</span>

---

#class <small>importlib._bootstrap.</small>**FrozenImporter**()

Meta path import for frozen modules.

All methods are either class or static methods to avoid the need to
instantiate the class.

$\qquad$**find_spec**(cls, fullname, path=None, target=None)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**find_module**(cls, fullname, path=None)

<span class="parent_indent">Find a frozen module.
This method is deprecated.Use find_spec() instead.</span>

$\qquad$**load_module**(cls, fullname)

<span class="parent_indent">Load a frozen module.
This method is deprecated.Use exec_module() instead.</span>

$\qquad$**get_code**(self, fullname)

<span class="parent_indent">Return the code object for the frozen module.</span>

$\qquad$**get_source**(self, fullname)

<span class="parent_indent">Return None as frozen modules do not have source code.</span>

$\qquad$**is_package**(self, fullname)

<span class="parent_indent">Return True if the frozen module is a package.</span>

---

#class <small>importlib._bootstrap.</small>**ModuleSpec**(name, loader, *, origin=None, loader_state=None, is_package=None)

The specification for a module, used for loading.

A module's spec is the source for information about the module.  For
data associated with the module, including source, use the spec's
loader.

`name` is the absolute name of the module.  `loader` is the loader
to use when loading the module.  `parent` is the name of the
package the module is in.  The parent is derived from the name.

`is_package` determines if the module is considered a package or
not.  On modules this is reflected by the `__path__` attribute.

`origin` is the specific location used by the loader from which to
load the module, if that information is available.  When filename is
set, origin will match.

`has_location` indicates that a spec's "origin" reflects a location.
When this is True, `__file__` attribute of the module is set.

`cached` is the location of the cached bytecode file, if any.  It
corresponds to the `__cached__` attribute.

`submodule_search_locations` is the sequence of path entries to
search when importing submodules.  If set, is_package should be
True--and False otherwise.

Packages are simply modules that (may) have submodules.  If a spec
has a non-None value in `submodule_search_locations`, the import
system will consider modules loaded from the spec as packages.

Only finders (see importlib.abc.MetaPathFinder and
importlib.abc.PathEntryFinder) should modify ModuleSpec instances.

$\qquad$**__init__**(self, name, loader, *, origin=None, loader_state=None, is_package=None)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**__eq__**(self, other)

<span class="parent_indent">Return self==value.</span>

---

#class <small>importlib._bootstrap.</small>**_DeadlockError**None

Unspecified run-time error.



---

#class <small>importlib._bootstrap.</small>**_DummyModuleLock**(name)

A simple _ModuleLock equivalent for Python builds without
multi-threading support.

$\qquad$**__init__**(self, name)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**acquire**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**release**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

---

#class <small>importlib._bootstrap.</small>**_ImportLockContext**()

Context manager for the import lock.

$\qquad$**__enter__**(self)

<span class="parent_indent">Acquire the import lock.</span>

$\qquad$**__exit__**(self, exc_type, exc_value, exc_traceback)

<span class="parent_indent">Release the import lock regardless of any raised exceptions.</span>

---

#class <small>importlib._bootstrap.</small>**_ModuleLock**(name)

A recursive lock implementation which is able to detect deadlocks
(e.g. thread 1 trying to take locks A then B, and thread 2 trying to
take locks B then A).

$\qquad$**__init__**(self, name)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**has_deadlock**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**acquire**(self)

<span class="parent_indent">Acquire the module lock.If a potential deadlock is detected,
a _DeadlockError is raised.
Otherwise, the lock is always acquired and True is returned.</span>

$\qquad$**release**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

---

#class <small>importlib._bootstrap.</small>**_ModuleLockManager**(name)

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__init__**(self, name)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__enter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__exit__**(self, *args, **kwargs)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#func <small>importlib._bootstrap.</small>**_builtin_from_name**(name)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>importlib._bootstrap.</small>**_calc___package__**(globals)

Calculate what __package__ should be.

__package__ is not guaranteed to be defined or could be set to None
to represent that its proper value is unknown.

---

#func <small>importlib._bootstrap.</small>**_call_with_frames_removed**(f, *args, **kwds)

remove_importlib_frames in import.c will always remove sequences
of importlib frames that end with a call to this function

Use it instead of a normal call in places where including the importlib
frames introduces unwanted noise into the traceback (e.g. when executing
module code)

---

#func <small>importlib._bootstrap.</small>**_exec**(spec, module)

Execute the spec's specified module in an existing module's namespace.

---

#func <small>importlib._bootstrap.</small>**_find_and_load**(name, import_)

Find and load the module.

---

#func <small>importlib._bootstrap.</small>**_find_and_load_unlocked**(name, import_)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>importlib._bootstrap.</small>**_find_spec**(name, path, target=None)

Find a module's spec.

---

#func <small>importlib._bootstrap.</small>**_find_spec_legacy**(finder, name, path)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>importlib._bootstrap.</small>**_gcd_import**(name, package=None, level=0)

Import and return the module based on its name, the package the call is
being made from, and the level adjustment.

This function represents the greatest common denominator of functionality
between import_module and __import__. This includes setting __package__ if
the loader did not.

---

#func <small>importlib._bootstrap.</small>**_get_module_lock**(name)

Get or create the module lock for a given module name.

Acquire/release internally the global import lock to protect
_module_locks.

---

#func <small>importlib._bootstrap.</small>**_handle_fromlist**(module, fromlist, import_, *, recursive=False)

Figure out what __import__ should return.

The import_ parameter is a callable which takes the name of module to
import. It is required to decouple the function from assuming importlib's
import implementation is desired.

---

#func <small>importlib._bootstrap.</small>**_init_module_attrs**(spec, module, *, override=False)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>importlib._bootstrap.</small>**_install_external_importers**()

Install importers that require external filesystem access

---

#func <small>importlib._bootstrap.</small>**_load**(spec)

Return a new module object, loaded by the spec's loader.

The module is not added to its parent.

If a module is already in sys.modules, that existing module gets
clobbered.

---

#func <small>importlib._bootstrap.</small>**_load_backward_compatible**(spec)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>importlib._bootstrap.</small>**_load_module_shim**(self, fullname)

Load the specified module into sys.modules and return it.

This method is deprecated.  Use loader.exec_module() instead.

---

#func <small>importlib._bootstrap.</small>**_load_unlocked**(spec)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>importlib._bootstrap.</small>**_lock_unlock_module**(name)

Acquires then releases the module lock for a given module name.

This is used to ensure a module is completely initialized, in the
event it is being imported by another thread.

---

#func <small>importlib._bootstrap.</small>**_module_repr**(module)

The implementation of ModuleType.__repr__().

---

#func <small>importlib._bootstrap.</small>**_module_repr_from_spec**(spec)

Return the repr to use for the module.

---

#func <small>importlib._bootstrap.</small>**_new_module**(name)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>importlib._bootstrap.</small>**_object_name**(obj)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>importlib._bootstrap.</small>**_requires_builtin**(fxn)

Decorator to verify the named module is built-in.

---

#func <small>importlib._bootstrap.</small>**_requires_frozen**(fxn)

Decorator to verify the named module is frozen.

---

#func <small>importlib._bootstrap.</small>**_resolve_name**(name, package, level)

Resolve a relative module name to an absolute one.

---

#func <small>importlib._bootstrap.</small>**_sanity_check**(name, package, level)

Verify arguments are "sane".

---

#func <small>importlib._bootstrap.</small>**_setup**(sys_module, _imp_module)

Setup importlib by importing needed built-in modules and injecting them
into the global namespace.

As sys is needed for sys.modules access and _imp is needed to load built-in
modules, those two modules must be explicitly passed in.

---

#func <small>importlib._bootstrap.</small>**_spec_from_module**(module, loader=None, origin=None)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>importlib._bootstrap.</small>**_verbose_message**(message, *args, verbosity=1)

Print the message to stderr if -v/PYTHONVERBOSE is turned on.

---

#func <small>importlib._bootstrap.</small>**_wrap**(new, old)

Simple substitute for functools.update_wrapper.

---

#func <small>importlib._bootstrap.</small>**module_from_spec**(spec)

Create a module based on the provided spec.

---

#func <small>importlib._bootstrap.</small>**spec_from_loader**(name, loader, *, origin=None, is_package=None)

Return a module spec based on various loader methods.

---

#class <small>importlib._bootstrap_external.</small>**ExtensionFileLoader**(name, path)

Loader for extension modules.

The constructor is designed to work with FileFinder.

$\qquad$**__init__**(self, name, path)

<span class="parent_indent">Cache the module name and the path to the file found by the
finder.</span>

$\qquad$**__eq__**(self, other)

<span class="parent_indent">Return self==value.</span>

$\qquad$**__hash__**(self)

<span class="parent_indent">Return hash(self).</span>

$\qquad$**create_module**(self, spec)

<span class="parent_indent">Create an unitialized extension module</span>

$\qquad$**exec_module**(self, module)

<span class="parent_indent">Initialize an extension module</span>

$\qquad$**is_package**(self, fullname)

<span class="parent_indent">Return True if the extension module is a package.</span>

$\qquad$**get_code**(self, fullname)

<span class="parent_indent">Return None as an extension module cannot create a code object.</span>

$\qquad$**get_source**(self, fullname)

<span class="parent_indent">Return None as extension modules have no source code.</span>

$\qquad$**get_filename**(self, name=None, *args, **kwargs)

<span class="parent_indent">Return the path to the source file as found by the finder.</span>

---

#class <small>importlib._bootstrap_external.</small>**FileFinder**(path, *loader_details)

File-based finder.

Interactions with the file system are cached for performance, being
refreshed when the directory the finder is handling has been modified.

$\qquad$**__init__**(self, path, *loader_details)

<span class="parent_indent">Initialize with the path to search on and a variable number of
2-tuples containing the loader and the file suffixes the loader
recognizes.</span>

$\qquad$**invalidate_caches**(self)

<span class="parent_indent">Invalidate the directory mtime.</span>

$\qquad$**_find_module_shim**(self, fullname)

<span class="parent_indent">Try to find a loader for the specified module by delegating to
self.find_loader().
This method is deprecated in favor of finder.find_spec().</span>

$\qquad$**find_loader**(self, fullname)

<span class="parent_indent">Try to find a loader for the specified module, or the namespace
package portions. Returns (loader, list-of-portions).
This method is deprecated.Use find_spec() instead.</span>

$\qquad$**_get_spec**(self, loader_class, fullname, path, smsl, target)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**find_spec**(self, fullname, target=None)

<span class="parent_indent">Try to find a spec for the specified module.
Returns the matching spec, or None if not found.</span>

$\qquad$**_fill_cache**(self)

<span class="parent_indent">Fill the cache of potential modules and packages for this directory.</span>

$\qquad$**path_hook**(cls, *loader_details)

<span class="parent_indent">A class method which returns a closure to use on sys.path_hook
which will return an instance using the specified loaders and the path
called on the closure.
If the path called on the closure is not a directory, ImportError is
raised.</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

---

#class <small>importlib._bootstrap_external.</small>**FileLoader**(fullname, path)

Base file loader class which implements the loader protocol methods that
require file system usage.

$\qquad$**__init__**(self, fullname, path)

<span class="parent_indent">Cache the module name and the path to the file found by the
finder.</span>

$\qquad$**__eq__**(self, other)

<span class="parent_indent">Return self==value.</span>

$\qquad$**__hash__**(self)

<span class="parent_indent">Return hash(self).</span>

$\qquad$**load_module**(self, name=None, *args, **kwargs)

<span class="parent_indent">Load a module from a file.
This method is deprecated.Use exec_module() instead.</span>

$\qquad$**get_filename**(self, name=None, *args, **kwargs)

<span class="parent_indent">Return the path to the source file as found by the finder.</span>

$\qquad$**get_data**(self, path)

<span class="parent_indent">Return the data from path as raw bytes.</span>

$\qquad$**get_resource_reader**(self, name=None, *args, **kwargs)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>importlib._bootstrap_external.</small>**PathFinder**()

Meta path finder for sys.path and package __path__ attributes.

$\qquad$**_path_importer_cache**(cls, path)

<span class="parent_indent">Get the finder for the path entry from sys.path_importer_cache.
If the path entry is not in the cache, find the appropriate finder
and cache it. If no finder is available, store None.</span>

$\qquad$**_legacy_get_spec**(cls, fullname, finder)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**_get_spec**(cls, fullname, path, target=None)

<span class="parent_indent">Find the loader or namespace_path for this module/package name.</span>

$\qquad$**find_spec**(cls, fullname, path=None, target=None)

<span class="parent_indent">Try to find a spec for 'fullname' on sys.path or 'path'.
The search is based on sys.path_hooks and sys.path_importer_cache.</span>

$\qquad$**find_module**(cls, fullname, path=None)

<span class="parent_indent">find the module on sys.path or 'path' based on sys.path_hooks and
sys.path_importer_cache.
This method is deprecated.Use find_spec() instead.</span>

---

#class <small>importlib._bootstrap_external.</small>**SourceFileLoader**(fullname, path)

Concrete implementation of SourceLoader using the file system.

$\qquad$**path_stats**(self, path)

<span class="parent_indent">Return the metadata for the path.</span>

$\qquad$**_cache_bytecode**(self, source_path, bytecode_path, data)

<span class="parent_indent">Optional method which writes data (bytes) to a file path (a str).
Implementing this method allows for the writing of bytecode files.
The source path is needed in order to correctly transfer permissions</span>

$\qquad$**set_data**(self, path, data, *, _mode=438)

<span class="parent_indent">Write bytes data to a file.</span>

---

#class <small>importlib._bootstrap_external.</small>**SourceLoader**()

Base class of common code needed by both SourceLoader and
SourcelessFileLoader.

$\qquad$**path_mtime**(self, path)

<span class="parent_indent">Optional method that returns the modification time (an int) for the
specified path (a str).
Raises OSError when the path cannot be handled.</span>

$\qquad$**path_stats**(self, path)

<span class="parent_indent">Optional method returning a metadata dict for the specified
path (a str).
Possible keys:
- 'mtime' (mandatory) is the numeric timestamp of last source
code modification;
- 'size' (optional) is the size in bytes of the source code.
Implementing this method allows the loader to read bytecode files.
Raises OSError when the path cannot be handled.</span>

$\qquad$**_cache_bytecode**(self, source_path, cache_path, data)

<span class="parent_indent">Optional method which writes data (bytes) to a file path (a str).
Implementing this method allows for the writing of bytecode files.
The source path is needed in order to correctly transfer permissions</span>

$\qquad$**set_data**(self, path, data)

<span class="parent_indent">Optional method which writes data (bytes) to a file path (a str).
Implementing this method allows for the writing of bytecode files.</span>

$\qquad$**get_source**(self, fullname)

<span class="parent_indent">Concrete implementation of InspectLoader.get_source.</span>

$\qquad$**source_to_code**(self, data, path, *, _optimize=-1)

<span class="parent_indent">Return the code object compiled from source.
The 'data' argument can be any object type that compile() supports.</span>

$\qquad$**get_code**(self, fullname)

<span class="parent_indent">Concrete implementation of InspectLoader.get_code.
Reading of bytecode requires path_stats to be implemented. To write
bytecode, set_data must also be implemented.</span>

---

#class <small>importlib._bootstrap_external.</small>**SourcelessFileLoader**(fullname, path)

Loader which handles sourceless file imports.

$\qquad$**get_code**(self, fullname)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**get_source**(self, fullname)

<span class="parent_indent">Return None as there is no source code.</span>

---

#class <small>importlib._bootstrap_external.</small>**WindowsRegistryFinder**()

Meta path finder for modules declared in the Windows registry.

$\qquad$**_search_registry**(cls, fullname)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**find_spec**(cls, fullname, path=None, target=None)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**find_module**(cls, fullname, path=None)

<span class="parent_indent">Find module named in the registry.
This method is deprecated.Use find_spec() instead.</span>

---

#class <small>importlib._bootstrap_external.</small>**_LoaderBasics**()

Base class of common code needed by both SourceLoader and
SourcelessFileLoader.

$\qquad$**is_package**(self, fullname)

<span class="parent_indent">Concrete implementation of InspectLoader.is_package by checking if
the path returned by get_filename has a filename of '__init__.py'.</span>

$\qquad$**create_module**(self, spec)

<span class="parent_indent">Use default semantics for module creation.</span>

$\qquad$**exec_module**(self, module)

<span class="parent_indent">Execute the module.</span>

$\qquad$**load_module**(self, fullname)

<span class="parent_indent">This method is deprecated.</span>

---

#class <small>importlib._bootstrap_external.</small>**_NamespaceLoader**(name, path, path_finder)

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__init__**(self, name, path, path_finder)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**is_package**(self, fullname)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**get_source**(self, fullname)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**get_code**(self, fullname)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**create_module**(self, spec)

<span class="parent_indent">Use default semantics for module creation.</span>

$\qquad$**exec_module**(self, module)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**load_module**(self, fullname)

<span class="parent_indent">Load a namespace module.
This method is deprecated.Use exec_module() instead.</span>

$\qquad$**get_resource_reader**(self, module)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>importlib._bootstrap_external.</small>**_NamespacePath**(name, path, path_finder)

Represents a namespace package's path.  It uses the module name
to find its parent module, and from there it looks up the parent's
__path__.  When this changes, the module's own path is recomputed,
using path_finder.  For top-level modules, the parent module's path
is sys.path.

$\qquad$**__init__**(self, name, path, path_finder)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**_find_parent_path_names**(self)

<span class="parent_indent">Returns a tuple of (parent-module-name, parent-path-attr-name)</span>

$\qquad$**_get_parent_path**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**_recalculate**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__iter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__getitem__**(self, index)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__setitem__**(self, index, path)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__len__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**__contains__**(self, item)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**append**(self, item)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#func <small>importlib._bootstrap_external.</small>**_calc_mode**(path)

Calculate the mode permissions for a bytecode file.

---

#func <small>importlib._bootstrap_external.</small>**_check_name**(method)

Decorator to verify that the module being requested matches the one the
loader can handle.

The first argument (self) must define _name which the second argument is
compared against. If the comparison fails then ImportError is raised.

---

#func <small>importlib._bootstrap_external.</small>**_classify_pyc**(data, name, exc_details)

Perform basic validity checking of a pyc header and return the flags field,
which determines how the pyc should be further validated against the source.

*data* is the contents of the pyc file. (Only the first 16 bytes are
required, though.)

*name* is the name of the module being imported. It is used for logging.

*exc_details* is a dictionary passed to ImportError if it raised for
improved debugging.

ImportError is raised when the magic number is incorrect or when the flags
field is invalid. EOFError is raised when the data is found to be truncated.

---

#func <small>importlib._bootstrap_external.</small>**_code_to_hash_pyc**(code, source_hash, checked=True)

Produce the data for a hash-based pyc.

---

#func <small>importlib._bootstrap_external.</small>**_code_to_timestamp_pyc**(code, mtime=0, source_size=0)

Produce the data for a timestamp-based pyc.

---

#func <small>importlib._bootstrap_external.</small>**_compile_bytecode**(data, name=None, bytecode_path=None, source_path=None)

Compile bytecode as found in a pyc.

---

#func <small>importlib._bootstrap_external.</small>**_find_module_shim**(self, fullname)

Try to find a loader for the specified module by delegating to
self.find_loader().

This method is deprecated in favor of finder.find_spec().

---

#func <small>importlib._bootstrap_external.</small>**_fix_up_module**(ns, name, pathname, cpathname=None)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>importlib._bootstrap_external.</small>**_get_cached**(filename)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>importlib._bootstrap_external.</small>**_get_sourcefile**(bytecode_path)

Convert a bytecode file path to a source path (if possible).

This function exists purely for backwards-compatibility for
PyImport_ExecCodeModuleWithFilenames() in the C API.

---

#func <small>importlib._bootstrap_external.</small>**_get_supported_file_loaders**()

Returns a list of file-based module loaders.

Each item is a tuple (loader, suffixes).

---

#func <small>importlib._bootstrap_external.</small>**_install**(_bootstrap_module)

Install the path-based import components.

---

#func <small>importlib._bootstrap_external.</small>**_make_relax_case**()

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>importlib._bootstrap_external.</small>**_pack_uint32**(x)

Convert a 32-bit integer to little-endian.

---

#func <small>importlib._bootstrap_external.</small>**_path_is_mode_type**(path, mode)

Test whether the path is the specified mode type.

---

#func <small>importlib._bootstrap_external.</small>**_path_isabs**(path)

Replacement for os.path.isabs.

---

#func <small>importlib._bootstrap_external.</small>**_path_isdir**(path)

Replacement for os.path.isdir.

---

#func <small>importlib._bootstrap_external.</small>**_path_isfile**(path)

Replacement for os.path.isfile.

---

#func <small>importlib._bootstrap_external.</small>**_path_join**(*path_parts)

Replacement for os.path.join().

---

#func <small>importlib._bootstrap_external.</small>**_path_split**(path)

Replacement for os.path.split().

---

#func <small>importlib._bootstrap_external.</small>**_path_stat**(path)

Stat the path.

Made a separate function to make it easier to override in experiments
(e.g. cache stat results).

---

#func <small>importlib._bootstrap_external.</small>**_relax_case**()

True if filenames must be checked case-insensitively and ignore environment flags are not set.

---

#func <small>importlib._bootstrap_external.</small>**_set_bootstrap_module**(_bootstrap_module)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>importlib._bootstrap_external.</small>**_unpack_uint16**(data)

Convert 2 bytes in little-endian to an integer.

---

#func <small>importlib._bootstrap_external.</small>**_unpack_uint32**(data)

Convert 4 bytes in little-endian to an integer.

---

#func <small>importlib._bootstrap_external.</small>**_validate_hash_pyc**(data, source_hash, name, exc_details)

Validate a hash-based pyc by checking the real source hash against the one in
the pyc header.

*data* is the contents of the pyc file. (Only the first 16 bytes are
required.)

*source_hash* is the importlib.util.source_hash() of the source file.

*name* is the name of the module being imported. It is used for logging.

*exc_details* is a dictionary passed to ImportError if it raised for
improved debugging.

An ImportError is raised if the bytecode is stale.

---

#func <small>importlib._bootstrap_external.</small>**_validate_timestamp_pyc**(data, source_mtime, source_size, name, exc_details)

Validate a pyc against the source last-modified time.

*data* is the contents of the pyc file. (Only the first 16 bytes are
required.)

*source_mtime* is the last modified timestamp of the source file.

*source_size* is None or the size of the source file in bytes.

*name* is the name of the module being imported. It is used for logging.

*exc_details* is a dictionary passed to ImportError if it raised for
improved debugging.

An ImportError is raised if the bytecode is stale.

---

#func <small>importlib._bootstrap_external.</small>**_write_atomic**(path, data, mode=438)

Best-effort function to write data to a path atomically.
Be prepared to handle a FileExistsError if concurrent writing of the
temporary file is attempted.

---

#func <small>importlib._bootstrap_external.</small>**cache_from_source**(path, debug_override=None, *, optimization=None)

Given the path to a .py file, return the path to its .pyc file.

The .py file does not need to exist; this simply returns the path to the
.pyc file calculated as if the .py file were imported.

The 'optimization' parameter controls the presumed optimization level of
the bytecode file. If 'optimization' is not None, the string representation
of the argument is taken and verified to be alphanumeric (else ValueError
is raised).

The debug_override parameter is deprecated. If debug_override is not None,
a True value is the same as setting 'optimization' to the empty string
while a False value is equivalent to setting 'optimization' to '1'.

If sys.implementation.cache_tag is None then NotImplementedError is raised.

---

#func <small>importlib._bootstrap_external.</small>**decode_source**(source_bytes)

Decode bytes representing source code and return the string.

Universal newline support is used in the decoding.

---

#func <small>importlib._bootstrap_external.</small>**source_from_cache**(path)

Given the path to a .pyc. file, return the path to its .py file.

The .pyc file does not need to exist; this simply returns the path to
the .py file calculated to correspond to the .pyc file.  If path does
not conform to PEP 3147/488 format, ValueError will be raised. If
sys.implementation.cache_tag is None then NotImplementedError is raised.

---

#func <small>importlib._bootstrap_external.</small>**spec_from_file_location**(name, location=None, *, loader=None, submodule_search_locations=<object object at 0x00000177D89740C0>)

Return a module spec based on a file location.

To indicate that the module is a package, set
submodule_search_locations to a list of directory paths.  An
empty list is sufficient, though its not otherwise useful to the
import system.

The loader must take a spec as its only __init__() arg.

---

#class <small>nt.</small>**DirEntry**()

*<span style=color:red>-!- Missing documentation -!-</span>*



---

#class <small>nt.</small>**times_result**(iterable=(), /)

times_result: Result from os.times().

This object may be accessed either as a tuple of
  (user, system, children_user, children_system, elapsed),
or via the attributes user, system, children_user, children_system,
and elapsed.

See os.times for more information.



---

#class <small>nt.</small>**uname_result**(iterable=(), /)

uname_result: Result from os.uname().

This object may be accessed either as a tuple of
  (sysname, nodename, release, version, machine),
or via the attributes sysname, nodename, release, version, and machine.

See os.uname for more information.



---

#class <small>os.</small>**stat_result**(iterable=(), /)

stat_result: Result from stat, fstat, or lstat.

This object may be accessed either as a tuple of
  (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
or via the attributes st_mode, st_ino, st_dev, st_nlink, st_uid, and so on.

Posix/windows: If your platform supports st_blksize, st_blocks, st_rdev,
or st_flags, they are available as attributes only.

See os.stat for more information.



---

#class <small>os.</small>**statvfs_result**(iterable=(), /)

statvfs_result: Result from statvfs or fstatvfs.

This object may be accessed either as a tuple of
  (bsize, frsize, blocks, bfree, bavail, files, ffree, favail, flag, namemax),
or via the attributes f_bsize, f_frsize, f_blocks, f_bfree, and so on.

See os.statvfs for more information.



---

#class <small>os.</small>**terminal_size**(iterable=(), /)

A tuple of (columns, lines) for holding terminal window size



---

#class <small>os.</small>**PathLike**()

Abstract base class for implementing the file system path protocol.

$\qquad$**__fspath__**(self)

<span class="parent_indent">Return the file system path representation of the object.</span>

$\qquad$**__subclasshook__**(cls, subclass)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**GenericAlias**None

<span class="parent_indent">Represent a PEP 585 generic type
E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).</span>

---

#class <small>os.</small>**_AddedDllDirectory**(path, cookie, remove_dll_directory)

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__init__**(self, path, cookie, remove_dll_directory)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**close**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__enter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__exit__**(self, *args)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

---

#class <small>os.</small>**_Environ**(data, encodekey, decodekey, encodevalue, decodevalue)

A MutableMapping is a generic container for associating
key/value pairs.

This class provides concrete generic implementations of all
methods except for __getitem__, __setitem__, __delitem__,
__iter__, and __len__.

$\qquad$**__init__**(self, data, encodekey, decodekey, encodevalue, decodevalue)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__getitem__**(self, key)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__setitem__**(self, key, value)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__delitem__**(self, key)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__iter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__len__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**copy**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**setdefault**(self, key, value)

<span class="parent_indent">D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D</span>

$\qquad$**__ior__**(self, other)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__or__**(self, other)

<span class="parent_indent">Return self|value.</span>

$\qquad$**__ror__**(self, other)

<span class="parent_indent">Return value|self.</span>

---

#func <small>os.</small>**_execvpe**(file, args, env=None)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>os.</small>**_exists**(name)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>os.</small>**_fspath**(path)

Return the path representation of a path-like object.

If str or bytes is passed in, it is returned unchanged. Otherwise the
os.PathLike interface is used to get the path representation. If the
path representation is not str or bytes, TypeError is raised. If the
provided path is not str, bytes, or os.PathLike, TypeError is raised.

---

#func <small>os.</small>**_get_exports_list**(module)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>os.</small>**_walk**(top, topdown, onerror, followlinks)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#class <small>os.</small>**_wrap_close**(stream, proc)

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__init__**(self, stream, proc)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**close**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__enter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__exit__**(self, *args)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__getattr__**(self, name)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__iter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#func <small>os.</small>**add_dll_directory**(path)

Add a path to the DLL search path.

This search path is used when resolving dependencies for imported
extension modules (the module itself is resolved through sys.path),
and also by ctypes.

Remove the directory by calling close() on the returned object or
using it in a with statement.

---

#func <small>os.</small>**execl**(file, *args)

execl(file, *args)

Execute the executable file with argument list args, replacing the
current process. 

---

#func <small>os.</small>**execle**(file, *args)

execle(file, *args, env)

Execute the executable file with argument list args and
environment env, replacing the current process. 

---

#func <small>os.</small>**execlp**(file, *args)

execlp(file, *args)

Execute the executable file (which is searched for along $PATH)
with argument list args, replacing the current process. 

---

#func <small>os.</small>**execlpe**(file, *args)

execlpe(file, *args, env)

Execute the executable file (which is searched for along $PATH)
with argument list args and environment env, replacing the current
process. 

---

#func <small>os.</small>**execvp**(file, args)

execvp(file, args)

Execute the executable file (which is searched for along $PATH)
with argument list args, replacing the current process.
args may be a list or tuple of strings. 

---

#func <small>os.</small>**execvpe**(file, args, env)

execvpe(file, args, env)

Execute the executable file (which is searched for along $PATH)
with argument list args and environment env, replacing the
current process.
args may be a list or tuple of strings. 

---

#func <small>os.</small>**fdopen**(fd, mode=r, buffering=-1, encoding=None, *args, **kwargs)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>os.</small>**fsdecode**(filename)

Decode filename (an os.PathLike, bytes, or str) from the filesystem
encoding with 'surrogateescape' error handler, return str unchanged. On
Windows, use 'strict' error handler if the file system encoding is
'mbcs' (which is the default encoding).

---

#func <small>os.</small>**fsencode**(filename)

Encode filename (an os.PathLike, bytes, or str) to the filesystem
encoding with 'surrogateescape' error handler, return bytes unchanged.
On Windows, use 'strict' error handler if the file system encoding is
'mbcs' (which is the default encoding).

---

#func <small>os.</small>**get_exec_path**(env=None)

Returns the sequence of directories that will be searched for the
named executable (similar to a shell) when launching a process.

*env* must be an environment variable dict or None.  If *env* is None,
os.environ will be used.

---

#func <small>os.</small>**getenv**(key, default=None)

Get an environment variable, return None if it doesn't exist.
The optional second argument can specify an alternate default.
key, default and the result are str.

---

#func <small>os.</small>**makedirs**(name, mode=511, exist_ok=False)

makedirs(name [, mode=0o777][, exist_ok=False])

Super-mkdir; create a leaf directory and all intermediate ones.  Works like
mkdir, except that any intermediate path segment (not just the rightmost)
will be created if it does not exist. If the target directory already
exists, raise an OSError if exist_ok is False. Otherwise no exception is
raised.  This is recursive.

---

#func <small>os.</small>**popen**(cmd, mode=r, buffering=-1)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>os.</small>**removedirs**(name)

removedirs(name)

Super-rmdir; remove a leaf directory and all empty intermediate
ones.  Works like rmdir except that, if the leaf directory is
successfully removed, directories corresponding to rightmost path
segments will be pruned away until either the whole path is
consumed or an error occurs.  Errors during this latter phase are
ignored -- they generally mean that a directory was not empty.

---

#func <small>os.</small>**renames**(old, new)

renames(old, new)

Super-rename; create directories as necessary and delete any left
empty.  Works like rename, except creation of any intermediate
directories needed to make the new pathname good is attempted
first.  After the rename, directories corresponding to rightmost
path segments of the old name will be pruned until either the
whole path is consumed or a nonempty directory is found.

Note: this function can fail with the new directory structure made
if you lack permissions needed to unlink the leaf directory or
file.

---

#func <small>os.</small>**spawnl**(mode, file, *args)

spawnl(mode, file, *args) -> integer

Execute file with arguments from args in a subprocess.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. 

---

#func <small>os.</small>**spawnle**(mode, file, *args)

spawnle(mode, file, *args, env) -> integer

Execute file with arguments from args in a subprocess with the
supplied environment.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. 

---

#class <small>warnings.</small>**WarningMessage**(message, category, filename, lineno, file=None, line=None, source=None)

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__init__**(self, message, category, filename, lineno, file=None, line=None, source=None)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__str__**(self)

<span class="parent_indent">Return str(self).</span>

---

#class <small>warnings.</small>**_OptionError**None

Exception used by option processing helpers.



---

#func <small>warnings.</small>**_add_filter**(*item, append)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>warnings.</small>**formatwarning**(message, category, filename, lineno, line=None)

Function to format a warning the standard way.

---

#func <small>warnings.</small>**_formatwarnmsg**(msg)

Function to format a warning the standard way.

---

#func <small>warnings.</small>**_formatwarnmsg_impl**(msg)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>warnings.</small>**_getaction**(action)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>warnings.</small>**_getcategory**(category)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>warnings.</small>**_is_internal_frame**(frame)

Signal whether the frame is an internal CPython implementation detail.

---

#func <small>warnings.</small>**_next_external_frame**(frame)

Find the next frame that doesn't involve CPython internals.

---

#func <small>warnings.</small>**_processoptions**(args)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>warnings.</small>**_setoption**(arg)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>warnings.</small>**showwarning**(message, category, filename, lineno, file=None, line=None)

Hook to write a warning to a file; replace if you like.

---

#func <small>warnings.</small>**_showwarnmsg**(msg)

Hook to write a warning to a file; replace if you like.

---

#func <small>warnings.</small>**_showwarnmsg_impl**(msg)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>warnings.</small>**_warn_unawaited_coroutine**(coro)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#class <small>warnings.</small>**catch_warnings**(*, record=False, module=None)

A context manager that copies and restores the warnings filter upon
exiting the context.

The 'record' argument specifies whether warnings should be captured by a
custom implementation of warnings.showwarning() and be appended to a list
returned by the context manager. Otherwise None is returned by the context
manager. The objects appended to the list are arguments whose attributes
mirror the arguments to showwarning().

The 'module' argument is to specify an alternative module to the module
named 'warnings' and imported under that name. This argument is only useful
when testing the warnings module itself.

$\qquad$**__init__**(self, *, record=False, module=None)

<span class="parent_indent">Specify whether to record warnings and if an alternative module
should be used other than sys.modules['warnings'].
For compatibility with Python 3.0, please consider all arguments to be
keyword-only.</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**__enter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__exit__**(self, *exc_info)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#func <small>warnings.</small>**filterwarnings**(action, message=, category=<class Warning>, module=, lineno=0, append=False)

Insert an entry into the list of warnings filters (at the front).

'action' -- one of "error", "ignore", "always", "default", "module",
            or "once"
'message' -- a regex that the warning message must match
'category' -- a class that the warning must be a subclass of
'module' -- a regex that the module name must match
'lineno' -- an integer line number, 0 matches all warnings
'append' -- if true, append to the list of filters

---

#func <small>warnings.</small>**formatwarning**(message, category, filename, lineno, line=None)

Function to format a warning the standard way.

---

#func <small>warnings.</small>**resetwarnings**()

Clear the list of warning filters, so that no filters are active.

---

#func <small>warnings.</small>**showwarning**(message, category, filename, lineno, file=None, line=None)

Hook to write a warning to a file; replace if you like.

---

#func <small>warnings.</small>**simplefilter**(action, category=<class Warning>, lineno=0, append=False)

Insert a simple entry into the list of warnings filters (at the front).

A simple filter matches all modules and messages.
'action' -- one of "error", "ignore", "always", "default", "module",
            or "once"
'category' -- a class that the warning must be a subclass of
'lineno' -- an integer line number, 0 matches all warnings
'append' -- if true, append to the list of filters

---

#func <small>importlib.</small>**find_loader**(name, path=None)

Return the loader for the specified module.

This is a backward-compatible wrapper around find_spec().

This function is deprecated in favor of importlib.util.find_spec().

---

#func <small>importlib.</small>**import_module**(name, package=None)

Import a module.

The 'package' argument is required when performing a relative import. It
specifies the package to use as the anchor point from which to resolve the
relative import to an absolute import.

---

#func <small>importlib.</small>**invalidate_caches**()

Call the invalidate_caches() method on all meta path finders stored in
sys.meta_path (where implemented).

---

#func <small>importlib.</small>**reload**(module)

Reload the module and return it.

The module must have been successfully imported before.

---

#func <small>importlib.machinery.</small>**all_suffixes**()

Returns a list of all recognized module suffixes for this process

---

#class <small>importlib.util.</small>**LazyLoader**(loader)

A loader that creates a module which defers loading until attribute access.

$\qquad$**factory**(cls, loader)

<span class="parent_indent">Construct a callable which returns the eager loader made lazy.</span>

$\qquad$**__init__**(self, loader)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**create_module**(self, spec)

<span class="parent_indent">Return a module to initialize and into which to load.
This method should raise ImportError if anything prevents it
from creating a new module.It may return None to indicate
that the spec should create the new module.</span>

$\qquad$**exec_module**(self, module)

<span class="parent_indent">Make the module load lazily.</span>

---

#class <small>importlib.util.</small>**_LazyModule**(name, doc=None)

A subclass of the module type which triggers loading upon attribute access.

$\qquad$**__getattribute__**(self, attr)

<span class="parent_indent">Trigger the load of the module and return the attribute.</span>

$\qquad$**__delattr__**(self, attr)

<span class="parent_indent">Trigger the load and then perform the deletion.</span>

---

#func <small>importlib.util.</small>**_find_spec_from_path**(name, path=None)

Return the spec for the specified module.

First, sys.modules is checked to see if the module was already imported. If
so, then sys.modules[name].__spec__ is returned. If that happens to be
set to None, then ValueError is raised. If the module is not in
sys.modules, then sys.meta_path is searched for a suitable spec with the
value of 'path' given to the finders. None is returned if no spec could
be found.

Dotted names do not have their parent packages implicitly imported. You will
most likely need to explicitly import all parent packages in the proper
order for a submodule to get the correct spec.

---

#func <small>importlib.util.</small>**_module_to_load**(name)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>importlib.util.</small>**find_spec**(name, package=None)

Return the spec for the specified module.

First, sys.modules is checked to see if the module was already imported. If
so, then sys.modules[name].__spec__ is returned. If that happens to be
set to None, then ValueError is raised. If the module is not in
sys.modules, then sys.meta_path is searched for a suitable spec with the
value of 'path' given to the finders. None is returned if no spec could
be found.

If the name is for submodule (contains a dot), the parent module is
automatically imported.

The name and package arguments work the same as importlib.import_module().
In other words, relative module names (with leading dots) work.

---

#func <small>importlib.util.</small>**module_for_loader**(fxn)

Decorator to handle selecting the proper module for loaders.

The decorated function is passed the module to use instead of the module
name. The module passed in to the function is either from sys.modules if
it already exists or is a new module. If the module is new, then __name__
is set the first argument to the method, __loader__ is set to self, and
__package__ is set accordingly (if self.is_package() is defined) will be set
before it is passed to the decorated function (if self.is_package() does
not work for the module it will be set post-load).

If an exception is raised and the decorator created the module it is
subsequently removed from sys.modules.

The decorator assumes that the decorated function takes the module name as
the second argument.

---

#func <small>importlib.util.</small>**resolve_name**(name, package)

Resolve a relative module name to an absolute one.

---

#func <small>importlib.util.</small>**set_loader**(fxn)

Set __loader__ on the returned module.

This function is deprecated.

---

#func <small>importlib.util.</small>**set_package**(fxn)

Set __package__ on the returned module.

This function is deprecated.

---

#func <small>linecache.</small>**checkcache**(filename=None)

Discard cache entries that are out of date.
(This is not checked upon each call!)

---

#func <small>linecache.</small>**clearcache**()

Clear the cache entirely.

---

#func <small>linecache.</small>**getline**(filename, lineno, module_globals=None)

Get a line for a Python source file from the cache.
Update the cache if it doesn't contain an entry for this file already.

---

#func <small>linecache.</small>**getlines**(filename, module_globals=None)

Get the lines for a Python source file from the cache.
Update the cache if it doesn't contain an entry for this file already.

---

#func <small>linecache.</small>**lazycache**(filename, module_globals)

Seed the cache for filename with module_globals.

The module loader will be asked for the source only when getlines is
called, not immediately.

If there is an entry in the cache already, it is not altered.

:return: True if a lazy load is registered in the cache,
    otherwise False. To register such a load a module loader with a
    get_source method must be found, the filename must be a cacheable
    filename, and the filename must not be already cached.

---

#func <small>linecache.</small>**updatecache**(filename, module_globals=None)

Update a cache entry and return its list of lines.
If something's wrong, print a message, discard the cache entry,
and return an empty list.

---

#func <small>token.</small>**ISEOF**(x)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>token.</small>**ISNONTERMINAL**(x)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>token.</small>**ISTERMINAL**(x)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#class <small>tokenize.</small>**StopTokenizing**None

Common base class for all non-exit exceptions.



---

#class <small>tokenize.</small>**TokenError**None

Common base class for all non-exit exceptions.



---

#class <small>tokenize.</small>**TokenInfo**(type, string, start, end, line)

TokenInfo(type, string, start, end, line)

$\qquad$**__repr__**(self)

<span class="parent_indent">Return a nicely formatted representation string</span>

---

#class <small>tokenize.</small>**Untokenizer**()

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__init__**(self)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**add_whitespace**(self, start)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**untokenize**(self, iterable)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**compat**(self, token, iterable)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#func <small>tokenize.</small>**_all_string_prefixes**()

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>tokenize.</small>**_get_normal_name**(orig_enc)

Imitates get_normal_name in tokenizer.c.

---

#func <small>tokenize.</small>**_tokenize**(readline, encoding)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>tokenize.</small>**detect_encoding**(readline)

The detect_encoding() function is used to detect the encoding that should
be used to decode a Python source file.  It requires one argument, readline,
in the same way as the tokenize() generator.

It will call readline a maximum of twice, and return the encoding used
(as a string) and a list of any lines (left as bytes) it has read in.

It detects the encoding from the presence of a utf-8 bom or an encoding
cookie as specified in pep-0263.  If both a bom and a cookie are present,
but disagree, a SyntaxError will be raised.  If the encoding cookie is an
invalid charset, raise a SyntaxError.  Note that if a utf-8 bom is found,
'utf-8-sig' is returned.

If no encoding is specified, then the default of 'utf-8' will be returned.

---

#func <small>tokenize.</small>**generate_tokens**(readline)

Tokenize a source reading Python code as unicode strings.

This has the same API as tokenize(), except that it expects the *readline*
callable to return str objects instead of bytes.

---

#func <small>tokenize.</small>**group**(*choices)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>tokenize.</small>**maybe**(*choices)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>tokenize.</small>**untokenize**(iterable)

Transform tokens back into Python source code.
It returns a bytes object, encoded using the ENCODING
token, which is the first token sequence output by tokenize.

Each element returned by the iterable must be a token sequence
with at least two elements, a token number and token value.  If
only two tokens are passed, the resulting output is poor.

Round-trip invariant for full input:
    Untokenized source will match input source exactly

Round-trip invariant for limited input:
    # Output bytes will tokenize back to the input
    t1 = [tok[:2] for tok in tokenize(f.readline)]
    newcode = untokenize(t1)
    readline = BytesIO(newcode).readline
    t2 = [tok[:2] for tok in tokenize(readline)]
    assert t1 == t2

---

#class <small>re.</small>**Pattern**()

Compiled regular expression object.



---

#class <small>re.</small>**RegexFlag**(value, names=None, *, module=None, qualname=None, type=None, start=1)

An enumeration.

$\qquad$**_generate_next_value_**(name, start, count, last_values)

<span class="parent_indent">Generate the next value when not given.
name: the name of the member
start: the initial start value or None
count: the number of existing members
last_value: the last value assigned or None</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**int**None

<span class="parent_indent">int([x]) -> integer
int(x, base=10) -> integer
Convert a number or string to an integer, or return 0 if no arguments
are given.If x is a number, return x.__int__().For floating point
numbers, this truncates towards zero.
If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.The literal can be preceded by '+' or '-' and be surrounded
by whitespace.The base defaults to 10.Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4</span>

$\qquad$**__new__**(cls, value)

<span class="parent_indent">Create and return a new object.See help(type) for accurate signature.</span>

---

#class <small>re.</small>**Scanner**(lexicon, flags=0)

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__init__**(self, lexicon, flags=0)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**scan**(self, string)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#func <small>re.</small>**_expand**(pattern, match, template)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>re.</small>**_pickle**(p)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>re.</small>**_subx**(pattern, template)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>re.</small>**escape**(pattern)

Escape special characters in a string.

---

#func <small>re.</small>**findall**(pattern, string, flags=0)

Return a list of all non-overlapping matches in the string.

If one or more capturing groups are present in the pattern, return
a list of groups; this will be a list of tuples if the pattern
has more than one group.

Empty matches are included in the result.

---

#func <small>re.</small>**finditer**(pattern, string, flags=0)

Return an iterator over all non-overlapping matches in the
string.  For each match, the iterator returns a Match object.

Empty matches are included in the result.

---

#func <small>re.</small>**fullmatch**(pattern, string, flags=0)

Try to apply the pattern to all of the string, returning
a Match object, or None if no match was found.

---

#func <small>re.</small>**match**(pattern, string, flags=0)

Try to apply the pattern at the start of the string, returning
a Match object, or None if no match was found.

---

#func <small>re.</small>**purge**()

Clear the regular expression caches

---

#func <small>re.</small>**search**(pattern, string, flags=0)

Scan through string looking for a match to the pattern, returning
a Match object, or None if no match was found.

---

#func <small>re.</small>**split**(pattern, string, maxsplit=0, flags=0)

Split the source string by the occurrences of the pattern,
returning a list containing the resulting substrings.  If
capturing parentheses are used in pattern, then the text of all
groups in the pattern are also returned as part of the resulting
list.  If maxsplit is nonzero, at most maxsplit splits occur,
and the remainder of the string is returned as the final element
of the list.

---

#func <small>re.</small>**sub**(pattern, repl, string, count=0, flags=0)

Return the string obtained by replacing the leftmost
non-overlapping occurrences of the pattern in string by the
replacement repl.  repl can be either a string or a callable;
if a string, backslash escapes in it are processed.  If it is
a callable, it's passed the Match object and must return
a replacement string to be used.

---

#func <small>re.</small>**subn**(pattern, repl, string, count=0, flags=0)

Return a 2-tuple containing (new_string, number).
new_string is the string obtained by replacing the leftmost
non-overlapping occurrences of the pattern in the source
string by the replacement repl.  number is the number of
substitutions that were made. repl can be either a string or a
callable; if a string, backslash escapes in it are processed.
If it is a callable, it's passed the Match object and must
return a replacement string to be used.

---

#func <small>re.</small>**template**(pattern, flags=0)

Compile a template pattern, returning a Pattern object

---

#func <small>copyreg.</small>**_reconstructor**(cls, base, state)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>copyreg.</small>**_reduce_ex**(self, proto)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>copyreg.</small>**_slotnames**(cls)

Return a list of slot names for a given class.

This needs to find slots defined by the class and its bases, so we
can't simply return the __slots__ attribute.  We must walk down
the Method Resolution Order and concatenate the __slots__ of each
class found there.  (This assumes classes don't modify their
__slots__ attribute to misrepresent their slots after the class is
defined.)

---

#func <small>copyreg.</small>**add_extension**(module, name, code)

Register an extension code.

---

#func <small>copyreg.</small>**clear_extension_cache**()

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>copyreg.</small>**constructor**(object)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>copyreg.</small>**pickle**(ob_type, pickle_function, constructor_ob=None)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>copyreg.</small>**pickle_complex**(c)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>copyreg.</small>**pickle_union**(obj)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>copyreg.</small>**remove_extension**(module, name, code)

Unregister an extension code.  For testing only.

---

#func <small>sre_compile.</small>**_bytes_to_codes**(b)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>sre_compile.</small>**_code**(p, flags)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>sre_compile.</small>**_combine_flags**(flags, add_flags, del_flags, TYPE_FLAGS=292)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>sre_compile.</small>**_compile_charset**(charset, flags, code)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>sre_compile.</small>**_compile_info**(code, pattern, flags)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>sre_compile.</small>**_generate_overlap_table**(prefix)

Generate an overlap table for the following prefix.
An overlap table is a table of the same size as the prefix which
informs about the potential self-overlap for each index in the prefix:
- if overlap[i] == 0, prefix[i:] can't overlap prefix[0:...]
- if overlap[i] == k with 0 < k <= i, prefix[i-k+1:i+1] overlaps with
  prefix[0:k]

---

#func <small>sre_compile.</small>**_get_charset_prefix**(pattern, flags)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>sre_compile.</small>**_get_iscased**(flags)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>sre_compile.</small>**_get_literal_prefix**(pattern, flags)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>sre_compile.</small>**_hex_code**(code)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>sre_compile.</small>**_mk_bitmap**(bits, _CODEBITS=32, _int=<class int>)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>sre_compile.</small>**_optimize_charset**(charset, iscased=None, fixup=None, fixes=None)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>sre_compile.</small>**_simple**(p)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>sre_compile.</small>**isstring**(obj)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#class <small>sre_parse.</small>**State**()

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__init__**(self)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**opengroup**(self, name=None)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**closegroup**(self, gid, p)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**checkgroup**(self, gid)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**checklookbehindgroup**(self, gid, source)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>sre_parse.</small>**SubPattern**(state, data=None)

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__init__**(self, state, data=None)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**dump**(self, level=0)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**__len__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__delitem__**(self, index)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__getitem__**(self, index)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__setitem__**(self, index, code)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**insert**(self, index, code)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**append**(self, code)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**getwidth**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>sre_parse.</small>**Tokenizer**(string)

*<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__init__**(self, string)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__next**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**match**(self, char)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**get**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**getwhile**(self, n, charset)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**getuntil**(self, terminator, name)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**tell**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**seek**(self, index)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**error**(self, msg, offset=0)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>sre_parse.</small>**Verbose**None

Common base class for all non-exit exceptions.



---

#func <small>sre_parse.</small>**_class_escape**(source, escape)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>sre_parse.</small>**_escape**(source, escape, state)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>sre_parse.</small>**_parse**(source, state, verbose, nested, first=False)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>sre_parse.</small>**_parse_flags**(source, state, char)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>sre_parse.</small>**_parse_sub**(source, state, verbose, nested)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>sre_parse.</small>**_uniq**(items)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>sre_parse.</small>**expand_template**(template, match)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>sre_parse.</small>**fix_flags**(src, flags)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>sre_parse.</small>**parse_template**(source, state)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>copy.</small>**_copy_immutable**(x)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>copy.</small>**_deepcopy_atomic**(x, memo)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>copy.</small>**_deepcopy_dict**(x, memo, deepcopy=<function deepcopy at 0x00000177D8F4F7F0>)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>copy.</small>**_deepcopy_list**(x, memo, deepcopy=<function deepcopy at 0x00000177D8F4F7F0>)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>copy.</small>**_deepcopy_method**(x, memo)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>copy.</small>**_deepcopy_tuple**(x, memo, deepcopy=<function deepcopy at 0x00000177D8F4F7F0>)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>copy.</small>**_keep_alive**(x, memo)

Keeps a reference to the object x in the memo.

Because we remember objects by their id, we have
to assure that possibly temporary objects are kept
alive by referencing them.
We store a reference at the id of the memo, which should
normally not be used unless someone tries to deepcopy
the memo itself...

---

#func <small>copy.</small>**_reconstruct**(x, memo, func, args, state=None, listiter=None, dictiter=None, deepcopy=<function deepcopy at 0x00000177D8F4F7F0>)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>copy.</small>**deepcopy**(x, memo=None, _nil=[])

Deep copy operation on arbitrary Python objects.

See the module's __doc__ string for more info.

---

#class <small>json.decoder.</small>**JSONDecodeError**(msg, doc, pos)

Subclass of ValueError with the following additional properties:

msg: The unformatted error message
doc: The JSON document being parsed
pos: The start index of doc where parsing failed
lineno: The line corresponding to pos
colno: The column corresponding to pos

$\qquad$**__init__**(self, msg, doc, pos)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__reduce__**(self)

<span class="parent_indent">Helper for pickle.</span>

---

#class <small>json.decoder.</small>**JSONDecoder**(*, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, strict=True, object_pairs_hook=None)

Simple JSON <http://json.org> decoder

Performs the following translations in decoding by default:

+---------------+-------------------+
| JSON          | Python            |
+===============+===================+
| object        | dict              |
+---------------+-------------------+
| array         | list              |
+---------------+-------------------+
| string        | str               |
+---------------+-------------------+
| number (int)  | int               |
+---------------+-------------------+
| number (real) | float             |
+---------------+-------------------+
| true          | True              |
+---------------+-------------------+
| false         | False             |
+---------------+-------------------+
| null          | None              |
+---------------+-------------------+

It also understands ``NaN``, ``Infinity``, and ``-Infinity`` as
their corresponding ``float`` values, which is outside the JSON spec.

$\qquad$**__init__**(self, *, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, strict=True, object_pairs_hook=None)

<span class="parent_indent">``object_hook``, if specified, will be called with the result
of every JSON object decoded and its return value will be used in
place of the given ``dict``.This can be used to provide custom
deserializations (e.g. to support JSON-RPC class hinting).
``object_pairs_hook``, if specified will be called with the result of
every JSON object decoded with an ordered list of pairs.The return
value of ``object_pairs_hook`` will be used instead of the ``dict``.
This feature can be used to implement custom decoders.
If ``object_hook`` is also defined, the ``object_pairs_hook`` takes
priority.
``parse_float``, if specified, will be called with the string
of every JSON float to be decoded. By default this is equivalent to
float(num_str). This can be used to use another datatype or parser
for JSON floats (e.g. decimal.Decimal).
``parse_int``, if specified, will be called with the string
of every JSON int to be decoded. By default this is equivalent to
int(num_str). This can be used to use another datatype or parser
for JSON integers (e.g. float).
``parse_constant``, if specified, will be called with one of the
following strings: -Infinity, Infinity, NaN.
This can be used to raise an exception if invalid JSON numbers
are encountered.
If ``strict`` is false (true is the default), then control
characters will be allowed inside strings.Control characters in
this context are those with character codes in the 0-31 range,
including ``'\t'`` (tab), ``'\n'``, ``'\r'`` and ``'\0'``.</span>

$\qquad$**decode**(self, s, _w=<built-in method match of re.Pattern object at 0x00000177D8F7C930>)

<span class="parent_indent">Return the Python representation of ``s`` (a ``str`` instance
containing a JSON document).</span>

$\qquad$**raw_decode**(self, s, idx=0)

<span class="parent_indent">Decode a JSON document from ``s`` (a ``str`` beginning with
a JSON document) and return a 2-tuple of the Python
representation and the index in ``s`` where the document ended.
This can be used to decode a JSON document from a string that may
have extraneous data at the end.</span>

---

#func <small>json.decoder.</small>**JSONArray**(s_and_end, scan_once, _w=<built-in method match of re.Pattern object at 0x00000177D8F7C930>, _ws= \t\n\r)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>json.decoder.</small>**JSONObject**(s_and_end, strict, scan_once, object_hook, object_pairs_hook, memo=None, _w=<built-in method match of re.Pattern object at 0x00000177D8F7C930>, _ws= \t\n\r)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>json.decoder.</small>**_decode_uXXXX**(s, pos)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>json.decoder.</small>**py_scanstring**(s, end, strict=True, _b={": ", \\: \\, /: /, b: \x08, f: \x0c, n: \n, r: \r, t: \t}, _m=<built-in method match of re.Pattern object at 0x00000177D8F709A0>)

Scan the string s for a JSON string. End is the index of the
character in s after the quote that started the JSON string.
Unescapes all valid JSON string escape sequences and raises ValueError
on attempt to decode an invalid string. If strict is False then literal
control characters are allowed in the string.

Returns a tuple of the decoded string and the index of the character in s
after the end quote.

---

#class <small>json.encoder.</small>**JSONEncoder**(*, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)

Extensible JSON <http://json.org> encoder for Python data structures.

Supports the following objects and types by default:

+-------------------+---------------+
| Python            | JSON          |
+===================+===============+
| dict              | object        |
+-------------------+---------------+
| list, tuple       | array         |
+-------------------+---------------+
| str               | string        |
+-------------------+---------------+
| int, float        | number        |
+-------------------+---------------+
| True              | true          |
+-------------------+---------------+
| False             | false         |
+-------------------+---------------+
| None              | null          |
+-------------------+---------------+

To extend this to recognize other objects, subclass and implement a
``.default()`` method with another method that returns a serializable
object for ``o`` if possible, otherwise it should call the superclass
implementation (to raise ``TypeError``).

$\qquad$**__init__**(self, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)

<span class="parent_indent">Constructor for JSONEncoder, with sensible defaults.
If skipkeys is false, then it is a TypeError to attempt
encoding of keys that are not str, int, float or None.If
skipkeys is True, such items are simply skipped.
If ensure_ascii is true, the output is guaranteed to be str
objects with all incoming non-ASCII characters escaped.If
ensure_ascii is false, the output can contain non-ASCII characters.
If check_circular is true, then lists, dicts, and custom encoded
objects will be checked for circular references during encoding to
prevent an infinite recursion (which would cause an RecursionError).
Otherwise, no such check takes place.
If allow_nan is true, then NaN, Infinity, and -Infinity will be
encoded as such.This behavior is not JSON specification compliant,
but is consistent with most JavaScript based encoders and decoders.
Otherwise, it will be a ValueError to encode such floats.
If sort_keys is true, then the output of dictionaries will be
sorted by key; this is useful for regression tests to ensure
that JSON serializations can be compared on a day-to-day basis.
If indent is a non-negative integer, then JSON array
elements and object members will be pretty-printed with that
indent level.An indent level of 0 will only insert newlines.
None is the most compact representation.
If specified, separators should be an (item_separator, key_separator)
tuple.The default is (', ', ': ') if *indent* is ``None`` and
(',', ': ') otherwise.To get the most compact JSON representation,
you should specify (',', ':') to eliminate whitespace.
If specified, default is a function that gets called for objects
that can't otherwise be serialized.It should return a JSON encodable
version of the object or raise a ``TypeError``.</span>

$\qquad$**default**(self, o)

<span class="parent_indent">Implement this method in a subclass such that it returns
a serializable object for ``o``, or calls the base implementation
(to raise a ``TypeError``).
For example, to support arbitrary iterators, you could
implement default like this::
def default(self, o):
try:
iterable = iter(o)
except TypeError:
pass
else:
return list(iterable)
# Let the base class default method raise the TypeError
return JSONEncoder.default(self, o)</span>

$\qquad$**encode**(self, o)

<span class="parent_indent">Return a JSON string representation of a Python data structure.
>>> from json.encoder import JSONEncoder
>>> JSONEncoder().encode({"foo": ["bar", "baz"]})
'{"foo": ["bar", "baz"]}'</span>

$\qquad$**iterencode**(self, o, _one_shot=False)

<span class="parent_indent">Encode the given object and yield each string
representation as available.
For example::
for chunk in JSONEncoder().iterencode(bigobject):
mysocket.write(chunk)</span>

---

#func <small>json.encoder.</small>**_make_iterencode**(markers, _default, _encoder, _indent, _floatstr, _key_separator, _item_separator, _sort_keys, _skipkeys, _one_shot, ValueError=<class ValueError>, dict=<class dict>, float=<class float>, id=<built-in function id>, int=<class int>, isinstance=<built-in function isinstance>, list=<class list>, str=<class str>, tuple=<class tuple>, _intstr=<slot wrapper __repr__ of int objects>)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>json.encoder.</small>**py_encode_basestring**(s)

Return a JSON representation of a Python string

    

---

#func <small>json.encoder.</small>**py_encode_basestring_ascii**(s)

Return an ASCII-only JSON representation of a Python string

    

---

#class <small>codecs.</small>**BufferedIncrementalDecoder**(errors=strict)

This subclass of IncrementalDecoder can be used as the baseclass for an
incremental decoder if the decoder must be able to handle incomplete
byte sequences.

$\qquad$**__init__**(self, errors=strict)

<span class="parent_indent">Create an IncrementalDecoder instance.
The IncrementalDecoder may use different error handling schemes by
providing the errors keyword argument. See the module docstring
for a list of possible values.</span>

$\qquad$**_buffer_decode**(self, input, errors, final)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**decode**(self, input, final=False)

<span class="parent_indent">Decode input and returns the resulting object.</span>

$\qquad$**reset**(self)

<span class="parent_indent">Reset the decoder to the initial state.</span>

$\qquad$**getstate**(self)

<span class="parent_indent">Return the current state of the decoder.
This must be a (buffered_input, additional_state_info) tuple.
buffered_input must be a bytes object containing bytes that
were passed to decode() that have not yet been converted.
additional_state_info must be a non-negative integer
representing the state of the decoder WITHOUT yet having
processed the contents of buffered_input.In the initial state
and after reset(), getstate() must return (b"", 0).</span>

$\qquad$**setstate**(self, state)

<span class="parent_indent">Set the current state of the decoder.
state must have been returned by getstate().The effect of
setstate((b"", 0)) must be equivalent to reset().</span>

---

#class <small>codecs.</small>**BufferedIncrementalEncoder**(errors=strict)

This subclass of IncrementalEncoder can be used as the baseclass for an
incremental encoder if the encoder must keep some of the output in a
buffer between calls to encode().

$\qquad$**__init__**(self, errors=strict)

<span class="parent_indent">Creates an IncrementalEncoder instance.
The IncrementalEncoder may use different error handling schemes by
providing the errors keyword argument. See the module docstring
for a list of possible values.</span>

$\qquad$**_buffer_encode**(self, input, errors, final)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**encode**(self, input, final=False)

<span class="parent_indent">Encodes input and returns the resulting object.</span>

$\qquad$**reset**(self)

<span class="parent_indent">Resets the encoder to the initial state.</span>

$\qquad$**getstate**(self)

<span class="parent_indent">Return the current state of the encoder.</span>

$\qquad$**setstate**(self, state)

<span class="parent_indent">Set the current state of the encoder. state must have been
returned by getstate().</span>

---

#class <small>codecs.</small>**Codec**()

Defines the interface for stateless encoders/decoders.

The .encode()/.decode() methods may use different error
handling schemes by providing the errors argument. These
string values are predefined:

 'strict' - raise a ValueError error (or a subclass)
 'ignore' - ignore the character and continue with the next
 'replace' - replace with a suitable replacement character;
            Python will use the official U+FFFD REPLACEMENT
            CHARACTER for the builtin Unicode codecs on
            decoding and '?' on encoding.
 'surrogateescape' - replace with private code points U+DCnn.
 'xmlcharrefreplace' - Replace with the appropriate XML
                       character reference (only for encoding).
 'backslashreplace'  - Replace with backslashed escape sequences.
 'namereplace'       - Replace with \N{...} escape sequences
                       (only for encoding).

The set of allowed values can be extended via register_error.

$\qquad$**encode**(self, input, errors=strict)

<span class="parent_indent">Encodes the object input and returns a tuple (output
object, length consumed).
errors defines the error handling to apply. It defaults to
'strict' handling.
The method may not store state in the Codec instance. Use
StreamWriter for codecs which have to keep state in order to
make encoding efficient.
The encoder must be able to handle zero length input and
return an empty object of the output object type in this
situation.</span>

$\qquad$**decode**(self, input, errors=strict)

<span class="parent_indent">Decodes the object input and returns a tuple (output
object, length consumed).
input must be an object which provides the bf_getreadbuf
buffer slot. Python strings, buffer objects and memory
mapped files are examples of objects providing this slot.
errors defines the error handling to apply. It defaults to
'strict' handling.
The method may not store state in the Codec instance. Use
StreamReader for codecs which have to keep state in order to
make decoding efficient.
The decoder must be able to handle zero length input and
return an empty object of the output object type in this
situation.</span>

---

#class <small>codecs.</small>**CodecInfo**(encode, decode, streamreader=None, streamwriter=None, incrementalencoder=None, incrementaldecoder=None, name=None, *, _is_text_encoding=None)

Codec details when looking up the codec registry

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

---

#func <small>codecs.</small>**EncodedFile**(file, data_encoding, file_encoding=None, errors=strict)

Return a wrapped version of file which provides transparent
encoding translation.

Data written to the wrapped file is decoded according
to the given data_encoding and then encoded to the underlying
file using file_encoding. The intermediate data type
will usually be Unicode but depends on the specified codecs.

Bytes read from the file are decoded using file_encoding and then
passed back to the caller encoded using data_encoding.

If file_encoding is not given, it defaults to data_encoding.

errors may be given to define the error handling. It defaults
to 'strict' which causes ValueErrors to be raised in case an
encoding error occurs.

The returned wrapped file object provides two extra attributes
.data_encoding and .file_encoding which reflect the given
parameters of the same name. The attributes can be used for
introspection by Python programs.

---

#class <small>codecs.</small>**IncrementalDecoder**(errors=strict)

An IncrementalDecoder decodes an input in multiple steps. The input can
be passed piece by piece to the decode() method. The IncrementalDecoder
remembers the state of the decoding process between calls to decode().

$\qquad$**__init__**(self, errors=strict)

<span class="parent_indent">Create an IncrementalDecoder instance.
The IncrementalDecoder may use different error handling schemes by
providing the errors keyword argument. See the module docstring
for a list of possible values.</span>

$\qquad$**decode**(self, input, final=False)

<span class="parent_indent">Decode input and returns the resulting object.</span>

$\qquad$**reset**(self)

<span class="parent_indent">Reset the decoder to the initial state.</span>

$\qquad$**getstate**(self)

<span class="parent_indent">Return the current state of the decoder.
This must be a (buffered_input, additional_state_info) tuple.
buffered_input must be a bytes object containing bytes that
were passed to decode() that have not yet been converted.
additional_state_info must be a non-negative integer
representing the state of the decoder WITHOUT yet having
processed the contents of buffered_input.In the initial state
and after reset(), getstate() must return (b"", 0).</span>

$\qquad$**setstate**(self, state)

<span class="parent_indent">Set the current state of the decoder.
state must have been returned by getstate().The effect of
setstate((b"", 0)) must be equivalent to reset().</span>

---

#class <small>codecs.</small>**IncrementalEncoder**(errors=strict)

An IncrementalEncoder encodes an input in multiple steps. The input can
be passed piece by piece to the encode() method. The IncrementalEncoder
remembers the state of the encoding process between calls to encode().

$\qquad$**__init__**(self, errors=strict)

<span class="parent_indent">Creates an IncrementalEncoder instance.
The IncrementalEncoder may use different error handling schemes by
providing the errors keyword argument. See the module docstring
for a list of possible values.</span>

$\qquad$**encode**(self, input, final=False)

<span class="parent_indent">Encodes input and returns the resulting object.</span>

$\qquad$**reset**(self)

<span class="parent_indent">Resets the encoder to the initial state.</span>

$\qquad$**getstate**(self)

<span class="parent_indent">Return the current state of the encoder.</span>

$\qquad$**setstate**(self, state)

<span class="parent_indent">Set the current state of the encoder. state must have been
returned by getstate().</span>

---

#class <small>codecs.</small>**StreamReader**(stream, errors=strict)

Defines the interface for stateless encoders/decoders.

The .encode()/.decode() methods may use different error
handling schemes by providing the errors argument. These
string values are predefined:

 'strict' - raise a ValueError error (or a subclass)
 'ignore' - ignore the character and continue with the next
 'replace' - replace with a suitable replacement character;
            Python will use the official U+FFFD REPLACEMENT
            CHARACTER for the builtin Unicode codecs on
            decoding and '?' on encoding.
 'surrogateescape' - replace with private code points U+DCnn.
 'xmlcharrefreplace' - Replace with the appropriate XML
                       character reference (only for encoding).
 'backslashreplace'  - Replace with backslashed escape sequences.
 'namereplace'       - Replace with \N{...} escape sequences
                       (only for encoding).

The set of allowed values can be extended via register_error.

$\qquad$**str**None

<span class="parent_indent">str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str
Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.</span>

$\qquad$**__init__**(self, stream, errors=strict)

<span class="parent_indent">Creates a StreamReader instance.
stream must be a file-like object open for reading.
The StreamReader may use different error handling
schemes by providing the errors keyword argument. These
parameters are predefined:
 'strict' - raise a ValueError (or a subclass)
 'ignore' - ignore the character and continue with the next
 'replace'- replace with a suitable replacement character
 'backslashreplace' - Replace with backslashed escape sequences;
The set of allowed parameter values can be extended via
register_error.</span>

$\qquad$**decode**(self, input, errors=strict)

<span class="parent_indent">Decodes the object input and returns a tuple (output
object, length consumed).
input must be an object which provides the bf_getreadbuf
buffer slot. Python strings, buffer objects and memory
mapped files are examples of objects providing this slot.
errors defines the error handling to apply. It defaults to
'strict' handling.
The method may not store state in the Codec instance. Use
StreamReader for codecs which have to keep state in order to
make decoding efficient.
The decoder must be able to handle zero length input and
return an empty object of the output object type in this
situation.</span>

$\qquad$**read**(self, size=-1, chars=-1, firstline=False)

<span class="parent_indent">Decodes data from the stream self.stream and returns the
resulting object.
chars indicates the number of decoded code points or bytes to
return. read() will never return more data than requested,
but it might return less, if there is not enough available.
size indicates the approximate maximum number of decoded
bytes or code points to read for decoding. The decoder
can modify this setting as appropriate. The default value
-1 indicates to read and decode as much as possible.size
is intended to prevent having to decode huge files in one
step.
If firstline is true, and a UnicodeDecodeError happens
after the first line terminator in the input only the first line
will be returned, the rest of the input will be kept until the
next call to read().
The method should use a greedy read strategy, meaning that
it should read as much data as is allowed within the
definition of the encoding and the given size, e.g.if
optional encoding endings or state markers are available
on the stream, these should be read too.</span>

$\qquad$**readline**(self, size=None, keepends=True)

<span class="parent_indent">Read one line from the input stream and return the
decoded data.
size, if given, is passed as size argument to the
read() method.</span>

$\qquad$**readlines**(self, sizehint=None, keepends=True)

<span class="parent_indent">Read all lines available on the input stream
and return them as a list.
Line breaks are implemented using the codec's decoder
method and are included in the list entries.
sizehint, if given, is ignored since there is no efficient
way to finding the true end-of-line.</span>

$\qquad$**reset**(self)

<span class="parent_indent">Resets the codec buffers used for keeping internal state.
Note that no stream repositioning should take place.
This method is primarily intended to be able to recover
from decoding errors.</span>

$\qquad$**seek**(self, offset, whence=0)

<span class="parent_indent">Set the input stream's current position.
Resets the codec buffers used for keeping state.</span>

$\qquad$**__next__**(self)

<span class="parent_indent">Return the next decoded line from the input stream.</span>

$\qquad$**__iter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__getattr__**(self, name, getattr=<built-in function getattr>)

<span class="parent_indent">Inherit all other methods from the underlying stream.
</span>

$\qquad$**__enter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__exit__**(self, type, value, tb)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>codecs.</small>**StreamReaderWriter**(stream, Reader, Writer, errors=strict)

StreamReaderWriter instances allow wrapping streams which
work in both read and write modes.

The design is such that one can use the factory functions
returned by the codec.lookup() function to construct the
instance.

$\qquad$**__init__**(self, stream, Reader, Writer, errors=strict)

<span class="parent_indent">Creates a StreamReaderWriter instance.
stream must be a Stream-like object.
Reader, Writer must be factory functions or classes
providing the StreamReader, StreamWriter interface resp.
Error handling is done in the same way as defined for the
StreamWriter/Readers.</span>

$\qquad$**read**(self, size=-1)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**readline**(self, size=None)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**readlines**(self, sizehint=None)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__next__**(self)

<span class="parent_indent">Return the next decoded line from the input stream.</span>

$\qquad$**__iter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**write**(self, data)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**writelines**(self, list)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**reset**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**seek**(self, offset, whence=0)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__getattr__**(self, name, getattr=<built-in function getattr>)

<span class="parent_indent">Inherit all other methods from the underlying stream.
</span>

$\qquad$**__enter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__exit__**(self, type, value, tb)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>codecs.</small>**StreamRecoder**(stream, encode, decode, Reader, Writer, errors=strict)

StreamRecoder instances translate data from one encoding to another.

They use the complete set of APIs returned by the
codecs.lookup() function to implement their task.

Data written to the StreamRecoder is first decoded into an
intermediate format (depending on the "decode" codec) and then
written to the underlying stream using an instance of the provided
Writer class.

In the other direction, data is read from the underlying stream using
a Reader instance and then encoded and returned to the caller.

$\qquad$**__init__**(self, stream, encode, decode, Reader, Writer, errors=strict)

<span class="parent_indent">Creates a StreamRecoder instance which implements a two-way
conversion: encode and decode work on the frontend (the
data visible to .read() and .write()) while Reader and Writer
work on the backend (the data in stream).
You can use these objects to do transparent
transcodings from e.g. latin-1 to utf-8 and back.
stream must be a file-like object.
encode and decode must adhere to the Codec interface; Reader and
Writer must be factory functions or classes providing the
StreamReader and StreamWriter interfaces resp.
Error handling is done in the same way as defined for the
StreamWriter/Readers.</span>

$\qquad$**read**(self, size=-1)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**readline**(self, size=None)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**readlines**(self, sizehint=None)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__next__**(self)

<span class="parent_indent">Return the next decoded line from the input stream.</span>

$\qquad$**__iter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**write**(self, data)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**writelines**(self, list)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**reset**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**seek**(self, offset, whence=0)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__getattr__**(self, name, getattr=<built-in function getattr>)

<span class="parent_indent">Inherit all other methods from the underlying stream.
</span>

$\qquad$**__enter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__exit__**(self, type, value, tb)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#class <small>codecs.</small>**StreamWriter**(stream, errors=strict)

Defines the interface for stateless encoders/decoders.

The .encode()/.decode() methods may use different error
handling schemes by providing the errors argument. These
string values are predefined:

 'strict' - raise a ValueError error (or a subclass)
 'ignore' - ignore the character and continue with the next
 'replace' - replace with a suitable replacement character;
            Python will use the official U+FFFD REPLACEMENT
            CHARACTER for the builtin Unicode codecs on
            decoding and '?' on encoding.
 'surrogateescape' - replace with private code points U+DCnn.
 'xmlcharrefreplace' - Replace with the appropriate XML
                       character reference (only for encoding).
 'backslashreplace'  - Replace with backslashed escape sequences.
 'namereplace'       - Replace with \N{...} escape sequences
                       (only for encoding).

The set of allowed values can be extended via register_error.

$\qquad$**__init__**(self, stream, errors=strict)

<span class="parent_indent">Creates a StreamWriter instance.
stream must be a file-like object open for writing.
The StreamWriter may use different error handling
schemes by providing the errors keyword argument. These
parameters are predefined:
 'strict' - raise a ValueError (or a subclass)
 'ignore' - ignore the character and continue with the next
 'replace'- replace with a suitable replacement character
 'xmlcharrefreplace' - Replace with the appropriate XML
 character reference.
 'backslashreplace'- Replace with backslashed escape
 sequences.
 'namereplace' - Replace with \N{...} escape sequences.
The set of allowed parameter values can be extended via
register_error.</span>

$\qquad$**write**(self, object)

<span class="parent_indent">Writes the object's contents encoded to self.stream.
</span>

$\qquad$**writelines**(self, list)

<span class="parent_indent">Writes the concatenated list of strings to the stream
using .write().</span>

$\qquad$**reset**(self)

<span class="parent_indent">Resets the codec buffers used for keeping internal state.
Calling this method should ensure that the data on the
output is put into a clean state, that allows appending
of new fresh data without having to rescan the whole
stream to recover state.</span>

$\qquad$**seek**(self, offset, whence=0)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__getattr__**(self, name, getattr=<built-in function getattr>)

<span class="parent_indent">Inherit all other methods from the underlying stream.
</span>

$\qquad$**__enter__**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__exit__**(self, type, value, tb)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

---

#func <small>codecs.</small>**getdecoder**(encoding)

Lookup up the codec for the given encoding and return
its decoder function.

Raises a LookupError in case the encoding cannot be found.

---

#func <small>codecs.</small>**getencoder**(encoding)

Lookup up the codec for the given encoding and return
its encoder function.

Raises a LookupError in case the encoding cannot be found.

---

#func <small>codecs.</small>**getincrementaldecoder**(encoding)

Lookup up the codec for the given encoding and return
its IncrementalDecoder class or factory function.

Raises a LookupError in case the encoding cannot be found
or the codecs doesn't provide an incremental decoder.

---

#func <small>codecs.</small>**getincrementalencoder**(encoding)

Lookup up the codec for the given encoding and return
its IncrementalEncoder class or factory function.

Raises a LookupError in case the encoding cannot be found
or the codecs doesn't provide an incremental encoder.

---

#func <small>codecs.</small>**getreader**(encoding)

Lookup up the codec for the given encoding and return
its StreamReader class or factory function.

Raises a LookupError in case the encoding cannot be found.

---

#func <small>codecs.</small>**getwriter**(encoding)

Lookup up the codec for the given encoding and return
its StreamWriter class or factory function.

Raises a LookupError in case the encoding cannot be found.

---

#func <small>codecs.</small>**iterdecode**(iterator, encoding, errors=strict, **kwargs)

Decoding iterator.

Decodes the input strings from the iterator using an IncrementalDecoder.

errors and kwargs are passed through to the IncrementalDecoder
constructor.

---

#func <small>codecs.</small>**iterencode**(iterator, encoding, errors=strict, **kwargs)

Encoding iterator.

Encodes the input strings from the iterator using an IncrementalEncoder.

errors and kwargs are passed through to the IncrementalEncoder
constructor.

---

#func <small>codecs.</small>**make_encoding_map**(decoding_map)

Creates an encoding map from a decoding map.

If a target mapping in the decoding map occurs multiple
times, then that target is mapped to None (undefined mapping),
causing an exception when encountered by the charmap codec
during translation.

One example where this happens is cp875.py which decodes
multiple character to \u001a.

---

#func <small>codecs.</small>**make_identity_dict**(rng)

make_identity_dict(rng) -> dict

Return a dictionary where elements of the rng sequence are
mapped to themselves.

---

#class <small>_json.</small>**Scanner**None

JSON scanner object



---

#class <small>_json.</small>**Scanner**None

JSON scanner object



---

#class <small>_json.</small>**Encoder**None

_iterencode(obj, _current_indent_level) -> iterable



---

#func <small>json.scanner.</small>**py_make_scanner**(context)

*<span style=color:red>-!- Missing documentation -!-</span>*

---

