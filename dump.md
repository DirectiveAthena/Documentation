#class <small>AthenaDocumentor.</small>**MarkdownStructure**()

The MarkdownStructure supports the `Parser` in formatting `ParsedObject` objects to the defined format.



---

#class <small>AthenaDocumentor.</small>**ParsedObject**(obj)

ParsedObject(obj)

$\qquad$**__init__**(self, obj)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**to_dict**(self) -> dict

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**__eq__**(self, other)

<span class="parent_indent">Return self==value.</s

---

#class <small>AthenaDocumentor.</small>**Parser**(*, root_module: Any, markdown_structure: type[MarkdownStructure] = <class AthenaDocumentor.models.markdown_structure.MarkdownStructure>) -> None

Object to control the correct handling of parsing through a Python package

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

$\qquad$**output_to_markdown_file**(self, filepath: str)

<span class="parent_indent">Output the 'parsed_items' to a structured markdown file.</span>

$\qquad$**__init__**(self, *, root_module: Any, markdown_structure: type[MarkdownStructure] = <class AthenaDocumentor.models.markdown_structure.MarkdownStructure>) -> None

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</s

---

#class <small>AthenaDocumentor.data.types.</small>**Types**(value, names=None, *, module=None, qualname=None, type=None, start=1)

An enumeration.

$\qquad$**_generate_next_value_**(name, start, count, last_values)

<span class="parent_indent">Generate the next value when not given.
name: the name of the member
start: the initial start value or None
count: the number of existing members
last_value: the last value assigned or None</span>

$\qquad$**__new__**(cls, value)

<span class="parent_indent">Create and return a new object.See help(type) for accurate signature.</s

---

#func <small>AthenaDocumentor.functions.markdown_string_manipulations.</small>**indent_all_lines**(text: str, indent: int) -> str

Indents all lines in a string with a defined amount of indentation

---

#func <small>AthenaDocumentor.functions.markdown_string_manipulations.</small>**quote_all_lines**(text: str) -> str

Places a quote prefix in front of all lines in a string

---

#func <small>AthenaDocumentor.functions.markdown_string_manipulations.</small>**remove_empty_prefix**(text: str) -> str

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>AthenaDocumentor.functions.type_finder.</small>**find_type**(obj) -> Types

*<span style=color:red>-!- Missing documentation -!-</span>*

---

