# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library
from time import sleep
from AthenaCSSstitcher import CssStitcher


# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def main():
    root = r"D:\Directive Athena\Programs\Veritas\Storage\Documentation\Assets"
    stitcher = CssStitcher(
        CssLibraryPath=rf"{root}\CSS\CssLib",
        ResultFilePath=rf"D:\Directive Athena\Programs\Veritas\Storage\Documentation\publish.css",
        ResultJsonPath=rf"{root}\CSS\CssLib.json",
        Overwrite=True
    )
    while True:
        stitcher.run()
        sleep(1)

if __name__ == '__main__':
    main()