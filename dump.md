>
>#class AthenaDocumentor.data.types.**Types**(value, names=None, *, module=None, qualname=None, type=None, start=1)
>
>    An enumeration.
>
>    >
>    >#func enum.**_generate_next_value_**(name, start, count, last_values)
>    >
>    >    Generate the next value when not given.
>    >    
>    >    name: the name of the member
>    >    start: the initial start value or None
>    >    count: the number of existing members
>    >    last_value: the last value assigned or None
>    
>    ---
>    
>    >
>    >#func enum.**__new__**(cls, value)
>    >
>    >    Create and return a new object.  See help(type) for accurate signature.
>    
>    ---

--->
>#func AthenaDocumentor.functions.markdown_string_manipulations.**indent_all_lines**(text: 'str', indent: 'int') -> 'str'
>
>    Indents all lines in a string with a defined amount of indentation
>    
>    Parameters:
>        - text: str -> to be indented string.
>            Where every new line is accompanied by a whitespace the length of `indent`
>        - indent: int -> The amount of whitespace preceding a line of text
>    
>    Returns:
>        str

--->
>#func AthenaDocumentor.functions.markdown_string_manipulations.**quote_all_lines**(text: 'str') -> 'str'
>
>    Places a quote prefix in front of all lines in a string
>    
>    Parameters:
>        - text: str -> to be indented string.
>            Where every new line is accompanied by a whitespace the length of `indent`
>        - indent: int -> The amount of whitespace preceding a line of text
>    
>    Returns:
>        str

--->
>#func AthenaDocumentor.functions.type_finder.**find_type**(obj) -> 'Types'
>
>

--->
>#class AthenaDocumentor.models.markdown_structure.**MarkdownStructure**()
>
>    The MarkdownStructure supports the `Parser` in formatting `ParsedObject` objects to the defined format.
>
>

--->
>#class AthenaDocumentor.models.parsed_data.**ParsedObject**(obj)
>
>    ParsedObject(obj)
>
>    >
>    >#func AthenaDocumentor.models.parsed_data.**__init__**(self, obj)
>    >
>    >    Initialize self.  See help(type(self)) for accurate signature.
>    
>    ---
>    
>    >
>    >#func AthenaDocumentor.models.parsed_data.**to_dict**(self) -> 'dict'
>    >
>    >
>    
>    ---
>    
>    >
>    >#func AthenaDocumentor.models.parsed_data.**__repr__**(self)
>    >
>    >    Return repr(self).
>    
>    ---
>    
>    >
>    >#func AthenaDocumentor.models.parsed_data.**__eq__**(self, other)
>    >
>    >    Return self==value.
>    
>    ---

--->
>#class AthenaDocumentor.models.parser.**Parser**(*, root_module: 'Any', markdown_structure: 'type[MarkdownStructure]' = <class 'AthenaDocumentor.models.markdown_structure.MarkdownStructure'>) -> None
>
>    Object to control the correct handling of parsing through a Python package
>    
>    Parameters:
>        - root_module: Defines the base package it must parse through
>        - markdown_structure: Defines the markdown structure used in the `self.output_to_markdown_file` method
>
>    >
>    >#func AthenaDocumentor.models.parser.**parse**(self) -> 'Parser'
>    >
>    >    Main method of the Parser object.
>    >    Running this will start the pared and populate the 'parsed_items' slot of the Parser object
>    >    
>    >    Returns:
>    >        self : Done for chaining methods
>    
>    ---
>    
>    >
>    >#func AthenaDocumentor.models.parser.**_parse_recursive**(self, module_to_parse: 'Any')
>    >
>    >
>    
>    ---
>    
>    >
>    >#func AthenaDocumentor.models.parser.**output_to_dict**(self, *, flat: 'bool' = False) -> 'dict[str:list[dict]]'
>    >
>    >    Output the 'parsed_items' dictionary as is, or with custom parameters.
>    >    
>    >    Parameters:
>    >        - flat: Outputs the dictionary in base types only (string, integers, booleans, etc...)
>    >    
>    >    Returns:
>    >        dict
>    
>    ---
>    
>    >
>    >#func AthenaDocumentor.models.parser.**output_to_json_file**(self, filepath: 'str')
>    >
>    >    Output the 'parsed_items' dictionary to a json file.
>    >    This method calls the `self.output_to_dict` method with the 'flat' parameter set to `True`
>    >    
>    >    Parameters:
>    >        - filepath: Defines the output file location
>    
>    ---
>    
>    >
>    >#func AthenaDocumentor.models.parser.**output_to_markdown_file**(self, filepath: 'str')
>    >
>    >    Output the 'parsed_items' to a structured markdown file.
>    >    
>    >    Parameters:
>    >        - filepath: Defines the output file location
>    
>    ---
>    
>    >
>    >#func AthenaDocumentor.models.parser.**__init__**(self, *, root_module: 'Any', markdown_structure: 'type[MarkdownStructure]' = <class 'AthenaDocumentor.models.markdown_structure.MarkdownStructure'>) -> None
>    >
>    >    Initialize self.  See help(type(self)) for accurate signature.
>    
>    ---
>    
>    >
>    >#func AthenaDocumentor.models.parser.**__repr__**(self)
>    >
>    >    Return repr(self).
>    
>    ---

---