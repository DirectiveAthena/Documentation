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

#class <small>AthenaDocumentor.</small>**Parser**(*, root_module: Any, markdown_structure: type[Output] = <class AthenaDocumentor.models.outputs.output_markdown.OutputMarkdown>, parse_items_with_underscore: bool = True) -> None

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

$\qquad$**__init__**(self, *, root_module: Any, markdown_structure: type[Output] = <class AthenaDocumentor.models.outputs.output_markdown.OutputMarkdown>, parse_items_with_underscore: bool = True) -> None

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

---

