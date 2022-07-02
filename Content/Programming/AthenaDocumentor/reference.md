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

