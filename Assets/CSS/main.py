# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library
from AthenaCSSstitcher import CssStitcher

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def main():
    a =  CssStitcher()

    CssStitcher() is CssStitcher


    CssStitcher(
        CssLibraryPath="D:\Directive Athena\Programs\Veritas\Storage\Documentation\Assets\CSS\CssLib",
        ResultFilePath="D:\Directive Athena\Programs\Veritas\Storage\Documentation\Assets\publish.css",
        Overwrite=True
    ).run()

if __name__ == '__main__':
    main()