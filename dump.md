#class <small>AthenaDocumentor.data.types.</small>.**Types**(value, names=None, *, module=None, qualname=None, type=None, start=1)

An enumeration.

$\qquad$**_generate_next_value_**(name, start, count, last_values)

$\qquad$ $\qquad$ Generate the next value when not given.

name: the name of the member
start: the initial start value or None
count: the number of existing members
last_value: the last value assigned or None

$\qquad$**__new__**(cls, value)

$\qquad$ $\qquad$ Create and return a new object.See help(type) for accurate signat

---

#func <small>AthenaDocumentor.functions.markdown_string_manipulations.</small>.**indent_all_lines**(text: 'str', indent: 'int') -> 'str'

Indents all lines in a string with a defined amount of indentation

Parameters:
- text: str -> to be indented string.
Where every new line is accompanied by a whitespace the length of `indent`
- indent: int -> The amount of whitespace preceding a line of text

Returns:
str

---

#func <small>AthenaDocumentor.functions.markdown_string_manipulations.</small>.**quote_all_lines**(text: 'str') -> 'str'

Places a quote prefix in front of all lines in a string

Parameters:
- text: str -> to be indented string.
Where every new line is accompanied by a whitespace the length of `indent`
- indent: int -> The amount of whitespace preceding a line of text

Returns:
str

---

#func <small>AthenaDocumentor.functions.markdown_string_manipulations.</small>.**remove_empty_prefix**(text: 'str') -> 'str'

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#func <small>AthenaDocumentor.functions.type_finder.</small>.**find_type**(obj) -> 'Types'

*<span style=color:red>-!- Missing documentation -!-</span>*

---

#class <small>AthenaDocumentor.models.markdown_structure.</small>.**MarkdownStructure**()

The MarkdownStructure supports the `Parser` in formatting `ParsedObject` objects to the defined format.



---

#class <small>AthenaDocumentor.models.parsed_data.</small>.**ParsedObject**(obj)

ParsedObject(obj)

$\qquad$**__init__**(self, obj)

$\qquad$ $\qquad$ Initialize self.See help(type(self)) for accurate signature.

$\qquad$**to_dict**(self) -> 'dict'

$\qquad$ $\qquad$ *<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**__repr__**(self)

$\qquad$ $\qquad$ Return repr(self).

$\qquad$**__eq__**(self, other)

$\qquad$ $\qquad$ Return self==va

---

#class <small>AthenaDocumentor.models.parser.</small>.**Parser**(*, root_module: 'Any', markdown_structure: 'type[MarkdownStructure]' = <class 'AthenaDocumentor.models.markdown_structure.MarkdownStructure'>) -> None

Object to control the correct handling of parsing through a Python package

Parameters:
- root_module: Defines the base package it must parse through
- markdown_structure: Defines the markdown structure used in the `self.output_to_markdown_file` method

$\qquad$**parse**(self) -> 'Parser'

$\qquad$ $\qquad$ Main method of the Parser object.
Running this will start the pared and populate the 'parsed_items' slot of the Parser object

Returns:
self : Done for chaining methods

$\qquad$**_parse_recursive**(self, module_to_parse: 'Any')

$\qquad$ $\qquad$ *<span style=color:red>-!- Missing documentation -!-</span>*

$\qquad$**output_to_dict**(self, *, flat: 'bool' = False) -> 'dict[str:list[dict]]'

$\qquad$ $\qquad$ Output the 'parsed_items' dictionary as is, or with custom parameters.

Parameters:
- flat: Outputs the dictionary in base types only (string, integers, booleans, etc...)

Returns:
dict

$\qquad$**output_to_json_file**(self, filepath: 'str')

$\qquad$ $\qquad$ Output the 'parsed_items' dictionary to a json file.
This method calls the `self.output_to_dict` method with the 'flat' parameter set to `True`

Parameters:
- filepath: Defines the output file location

$\qquad$**output_to_markdown_file**(self, filepath: 'str')

$\qquad$ $\qquad$ Output the 'parsed_items' to a structured markdown file.

Parameters:
- filepath: Defines the output file location

$\qquad$**__init__**(self, *, root_module: 'Any', markdown_structure: 'type[MarkdownStructure]' = <class 'AthenaDocumentor.models.markdown_structure.MarkdownStructure'>) -> None

$\qquad$ $\qquad$ Initialize self.See help(type(self)) for accurate signature.

$\qquad$**__repr__**(self)

$\qquad$ $\qquad$ Return repr(se

---

