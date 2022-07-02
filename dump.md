
#class <small>AthenaDocumentor.data.types.</small>**Types**(value, names=None, *, module=None, qualname=None, type=None, start=1)

> An enumeration.


- #func <small>enum.</small>**_generate_next_value_**(name, start, count, last_values)
    > Generate the next value when not given.
> 
> name: the name of the member
> start: the initial start value or None
> count: the number of existing members
> last_value: the last value assigned or None
    


- #func <small>enum.</small>**__new__**(cls, value)
    > Create and return a new object.  See help(type) for accurate signature.


---


> Indents all lines in a string with a defined amount of indentation
> 
> Parameters:
>     - text: str -> to be indented string.
>         Where every new line is accompanied by a whitespace the length of `indent`
>     - indent: int -> The amount of whitespace preceding a line of text
> 
> Returns:
>     str

---


> Places a quote prefix in front of all lines in a string
> 
> Parameters:
>     - text: str -> to be indented string.
>         Where every new line is accompanied by a whitespace the length of `indent`
>     - indent: int -> The amount of whitespace preceding a line of text
> 
> Returns:
>     str

---


> **<span style={color:red}>-!- Missing documentation -!-</span>**

---

#class <small>AthenaDocumentor.models.markdown_structure.</small>**MarkdownStructure**()

> The MarkdownStructure supports the `Parser` in formatting `ParsedObject` objects to the defined format.



---

#class <small>AthenaDocumentor.models.parsed_data.</small>**ParsedObject**(obj)

> ParsedObject(obj)


- #func <small>AthenaDocumentor.models.parsed_data.</small>**__init__**(self, obj)
    > Initialize self.  See help(type(self)) for accurate signature.
    


- #func <small>AthenaDocumentor.models.parsed_data.</small>**to_dict**(self) -> 'dict'
    > **<span style={color:red}>-!- Missing documentation -!-</span>**
    


- #func <small>AthenaDocumentor.models.parsed_data.</small>**__repr__**(self)
    > Return repr(self).
    


- #func <small>AthenaDocumentor.models.parsed_data.</small>**__eq__**(self, other)
    > Return self==value.


---

#class <small>AthenaDocumentor.models.parser.</small>**Parser**(*, root_module: 'Any', markdown_structure: 'type[MarkdownStructure]' = <class 'AthenaDocumentor.models.markdown_structure.MarkdownStructure'>) -> None

> Object to control the correct handling of parsing through a Python package
> 
> Parameters:
>     - root_module: Defines the base package it must parse through
>     - markdown_structure: Defines the markdown structure used in the `self.output_to_markdown_file` method


- #func <small>AthenaDocumentor.models.parser.</small>**parse**(self) -> 'Parser'
    > Main method of the Parser object.
> Running this will start the pared and populate the 'parsed_items' slot of the Parser object
> 
> Returns:
>     self : Done for chaining methods
    


- #func <small>AthenaDocumentor.models.parser.</small>**_parse_recursive**(self, module_to_parse: 'Any')
    > **<span style={color:red}>-!- Missing documentation -!-</span>**
    


- #func <small>AthenaDocumentor.models.parser.</small>**output_to_dict**(self, *, flat: 'bool' = False) -> 'dict[str:list[dict]]'
    > Output the 'parsed_items' dictionary as is, or with custom parameters.
> 
> Parameters:
>     - flat: Outputs the dictionary in base types only (string, integers, booleans, etc...)
> 
> Returns:
>     dict
    


- #func <small>AthenaDocumentor.models.parser.</small>**output_to_json_file**(self, filepath: 'str')
    > Output the 'parsed_items' dictionary to a json file.
> This method calls the `self.output_to_dict` method with the 'flat' parameter set to `True`
> 
> Parameters:
>     - filepath: Defines the output file location
    


- #func <small>AthenaDocumentor.models.parser.</small>**output_to_markdown_file**(self, filepath: 'str')
    > Output the 'parsed_items' to a structured markdown file.
> 
> Parameters:
>     - filepath: Defines the output file location
    


- #func <small>AthenaDocumentor.models.parser.</small>**__init__**(self, *, root_module: 'Any', markdown_structure: 'type[MarkdownStructure]' = <class 'AthenaDocumentor.models.markdown_structure.MarkdownStructure'>) -> None
    > Initialize self.  See help(type(self)) for accurate signature.
    


- #func <small>AthenaDocumentor.models.parser.</small>**__repr__**(self)
    > Return repr(self).


---
