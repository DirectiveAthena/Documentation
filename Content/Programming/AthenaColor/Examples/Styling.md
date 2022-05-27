---
copyright: "Andreas Sas 2022"
created: "2022-04-26 03:36"
cssclass: metaDataHide athenacolor
aliases: [AthenaColor Styling]
---
# AthenaColor Styling
## Easy Examples
### Inline Styling
- General Example
    >[!tldr]+ Python Code
    >```python
    >from AthenaColor import Fore, Style
    >
    >    print(  
    >f"""  
    >{Style.Italic}{Fore.SlateGray}AthenaColor Example:{Style.NoForeground}
    >{Fore.Red}This is an of {Style.Bold}EXAMPLE{Style.NoBold} nested styling{Style.NoForeground}    
    >{Fore.SlateGray}As you can see, the color needs to be manually returned here{Style.NoForeground}{Style.NoItalic}
    >"""  
    )
    >```

    >[!example]- Console Output
    ><i><span style="color: SlateGray">AthenaColor Example:</span>
    ><span class="red">This is an <b>EXAMPLE</b> of nested Styling</span>
    ><span style="color: SlateGray">As you can see, the color needs to be manually returned here</span></i>

### Nested Styling

- General Example
    >[!tldr]+ Python Code
    >```python
    >from AthenaColor import ForeNest, StyleNest
    >
    >print(  
    >    StyleNest.Italic(ForeNest.SlateGray(  
    >        "AthenaColor Example:",  
    >        ForeNest.Red(  
    >            "This is an",  
    >            StyleNest.Bold("EXAMPLE"),  
    >            "of nested styling"  
    >        ),    
    >        "As you can see, the correct color returns here by itself",
    >        sep="\n"  
    >    ))  
    >)
    >```

    >[!Example]- Console Output
    ><i><span style="color: SlateGray">AthenaColor Example:</span>
    ><span class="red">This is an <b>EXAMPLE</b> of nested Styling</span>
    ><span style="color: SlateGray">As you can see, the correct color returns here by itself</span></i>
  