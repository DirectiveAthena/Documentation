# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import itertools

# Custom Library
from AthenaCSS.models.generator import CSSGenerator

# Custom Packages
from functions.headers import header_default, header_pages, header_pages_special
from functions.clean_embed import clean_embed
from functions.hide_metadata import hide_metadata
from functions.markers import markers
from functions.header_border_colors import header_border_colors

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
PATH_PUBLISH = "D:\Directive Athena\Programs\Veritas\Storage\Documentation\publish.css"
PATH_SNIPPET = "D:\Directive Athena\Programs\Veritas\Storage\Documentation\.obsidian\snippets\publish.css"
PATH_DUMP = "D:\Directive Athena\Programs\Veritas\Storage\Documentation\Assets\.css\DocumentationCSS\dump.css"

def main():
    # assemble components into the generator
    generator = CSSGenerator(
        content=list(itertools.chain(
            header_default(),
            header_pages(),
            header_pages_special(),
            clean_embed(),
            hide_metadata(),
            markers(),
            header_border_colors()
        ))
    )

    # write output to file
    with (
        open(PATH_DUMP, "w+") as file_dump,
        open(PATH_PUBLISH, "w+") as file_publish,
        open(PATH_SNIPPET, "w+") as file_snippet
    ):
        text = generator.to_text()
        file_dump.write(text)
        file_publish.write(text)
        file_snippet.write(text)

    pass

if __name__ == '__main__':
    main()
