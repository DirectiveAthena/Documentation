#class AthenaDocumentor.**Output**()

Standardized way of outputting correctly parsed objects into string objects.
Used by the parser `output_...` methods to correctly form the wanted text version

The base Output class is an abstract class, which means the classes that inherit from it,
must implement all following methods.

**format_documentation**(cls, parsed_object: Parsed) -> str

Formats the `parsed_object.doc` into a correct string.

Parameters:
- parsed_object:Parsed

Returns: str

**format_type**(cls, parsed_object: Parsed) -> str

Formats the `parsed_object.type` into a correct string.

Parameters:
- parsed_object:Parsed

Returns: str

**format_module_name**(cls, parsed_object: Parsed) -> str

Formats the `parsed_object.module_name` into a correct string.

Parameters:
- parsed_object:Parsed

Returns: str

**format_object_name**(cls, parsed_object: Parsed) -> str

Formats the `parsed_object.name` into a correct string.

Parameters:
- parsed_object:Parsed

Returns: str

**format_signature**(cls, parsed_object: Parsed) -> str

Formats the `parsed_object.signature` into a correct string.

Parameters:
- parsed_object:Parsed

Returns: str

**format_header**(cls, parsed_object: Parsed) -> str

Formats multiple components of `parsed_object` together.
This forms the piece of documentation that display the name, signature, type and other similar components.

Parameters:
- parsed_object:Parsed

Returns: str

**format_footer**(cls, parsed_object: Parsed) -> str

Formats multiple components of `parsed_object` together.
This forms the piece of documentation that display the end of the piece of documentation for that `parsed_object`

Parameters:
- parsed_object:Parsed

Returns: str

**structure_function**(cls, parsed_object: Parsed) -> str

Calls on other `Output` methods to export a sensible string for a function object

Parameters:
- parsed_object:Parsed

Returns: str

**structure_class**(cls, parsed_object: Parsed) -> str

Calls on other `Output` methods to export a sensible string for a class object

Parameters:
- parsed_object:Parsed

Returns: str

**structure_method**(cls, parsed_object: Parsed) -> str

Calls on other `Output` methods to export a sensible string for a method object

Parameters:
- parsed_object:Parsed

Returns: str

---

#class AthenaDocumentor.**OutputMarkdown**()

Standardized way of outputting correctly parsed objects into string objects,
which can be interpreted as Markdown text
Used by the parser `output_...` methods to correctly form the wanted text version

**format_documentation**(cls, parsed_object: Parsed) -> str

*`-!- Missing documentation -!-`*

**format_type**(cls, parsed_object: Parsed) -> str

*`-!- Missing documentation -!-`*

**format_module_name**(cls, parsed_object: Parsed) -> str

*`-!- Missing documentation -!-`*

**format_object_name**(cls, parsed_object: Parsed) -> str

*`-!- Missing documentation -!-`*

**format_signature**(cls, parsed_object: ParsedFunction | ParsedMethod | ParsedClass) -> str

*`-!- Missing documentation -!-`*

**format_header**(cls, parsed_object: ParsedFunction | ParsedMethod | ParsedClass) -> str

*`-!- Missing documentation -!-`*

**format_footer**(cls, parsed_object: Parsed) -> str

*`-!- Missing documentation -!-`*

**structure_function**(cls, parsed_object: ParsedFunction | ParsedMethod) -> str

*`-!- Missing documentation -!-`*

**structure_class**(cls, parsed_object: ParsedClass) -> str

*`-!- Missing documentation -!-`*

**structure_method**(cls, parsed_object: ParsedFunction | ParsedMethod) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaDocumentor.**Parser**(*, root_module: types.ModuleType, markdown_structure: type[Output] = <class AthenaDocumentor.models.outputs.output_markdown.OutputMarkdown>, parse_items_with_underscore: bool = True) -> None

Object to control the correct handling of parsing through a Python package

**__post_init__**(self)

*`-!- Missing documentation -!-`*

**parse**(self) -> Parser

Main method of the Parser object.
Running this will start the pared and populate the 'parsed_items' slot of the Parser object

**_parse_recursive**(self, module_to_parse: Any)

*`-!- Missing documentation -!-`*

**output_to_dict**(self, *, flat: bool = False) -> dict[str:list[dict]]

Output the 'parsed_items' dictionary as is, or with custom parameters.

**output_to_json_file**(self, filepath: str)

Output the 'parsed_items' dictionary to a json file.
This method calls the `self.output_to_dict` method with the 'flat' parameter set to `True`

**output_to_json_string**(self) -> str

Output the 'parsed_items' dictionary to a json formatted string.
This method calls the `self.output_to_dict` method with the 'flat' parameter set to `True`

**_output_to_markdown**(self)

*`-!- Missing documentation -!-`*

**output_to_markdown_file**(self, *filepath: str)

Output the 'parsed_items' to a structured MarkDown file.

**output_to_markdown_string**(self) -> str

Output the 'parsed_items' to string, formatted in MarkDown

**__init__**(self, *, root_module: types.ModuleType, markdown_structure: type[Output] = <class AthenaDocumentor.models.outputs.output_markdown.OutputMarkdown>, parse_items_with_underscore: bool = True) -> None

Initialize self.  See help(type(self)) for accurate signature.

**__repr__**(self)

Return repr(self).

---

#class AthenaDocumentor.data.types.**Types**(value, names=None, *, module=None, qualname=None, type=None, start=1)

A simple data storage class to hold all tags meant to precede the object title.

**_generate_next_value_**(name, start, count, last_values)

Generate the next value when not given.

name: the name of the member
start: the initial start value or None
count: the number of existing members
last_value: the last value assigned or None

**object**()

The base class of the class hierarchy.

When called, it accepts no arguments and returns a new featureless
instance that has no instance attributes and cannot be given any.

**__new__**(cls, value)

Create and return a new object.  See help(type) for accurate signature.

---

#class AthenaDocumentor.models.parsed.parsed.**Parsed**(obj, parent_module)

The base Parsed class is an abstract class, which means the classes that inherit from it,
must implement all following methods.

**__init__**(self, obj, parent_module)

Initialize self.  See help(type(self)) for accurate signature.

**to_dict**(self) -> dict

Cast the object attributes to a dictionary format

**__repr__**(self)

Return repr(self).

---

#class AthenaDocumentor.models.parsed.parsed_class.**ParsedClass**(obj, parent_module)

A dataclass for storage of class object components.
Does not hold the documentation by itself, as this can often lead to memory overloads with large documentation strings

Parameters:
- obj: the class in question which must be stored
- parent_module: the module where the class in located in. This is a `types.ModuleType`

**__init__**(self, obj, parent_module)

Initialize self.  See help(type(self)) for accurate signature.

**to_dict**(self) -> dict

Cast the object attributes to a dictionary format

**__repr__**(self)

Return repr(self).

---

#class AthenaDocumentor.models.parsed.parsed_function.**ParsedFunction**(obj, parent_module)

A dataclass for storage of a function object components.
Does not hold the documentation by itself, as this can often lead to memory overloads with large documentation strings

Parameters:
- obj: the function in question which must be stored
- parent_module: the module where the class in located in. This is a `types.ModuleType`

**__init__**(self, obj, parent_module)

Initialize self.  See help(type(self)) for accurate signature.

**to_dict**(self) -> dict

Cast the object attributes to a dictionary format

**__repr__**(self)

Return repr(self).

---

#class AthenaDocumentor.models.parsed.parsed_method.**ParsedMethod**(obj, parent_module)

A dataclass for storage of method object components.
Does not hold the documentation by itself, as this can often lead to memory overloads with large documentation strings

Parameters:
- obj: the method in question which must be stored
- parent_module: the module where the class which holds the method in located in. This is a `types.ModuleType`

**__init__**(self, obj, parent_module)

Initialize self.  See help(type(self)) for accurate signature.

**to_dict**(self) -> dict

Cast the object attributes to a dictionary format

**__repr__**(self)

Return repr(self).

---

#class AthenaDocumentor.models.parsed.parsed_module.**ParsedModule**(obj, parent_module)

A dataclass for storage of module object components.
Does not hold the documentation by itself, as this can often lead to memory overloads with large documentation strings

Parameters:
- obj: the module in question which must be stored
- parent_module: the module where the class in located in. This is a `types.ModuleType`

**__repr__**(self)

Return repr(self).

---

