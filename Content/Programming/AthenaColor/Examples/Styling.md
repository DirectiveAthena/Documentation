---
copyright: "Andreas Sas 2022"
created: "2022-04-26 03:36"
cssclass: 
aliases: [AthenaColor Styling]
---
# AthenaColor Styling
## Inline Styling
- General Example
    >[!code]- Python Code
    >```python
    >from AthenaColor import ForeNest, StyleNest
    >
    >    print(  
    >f"""  
    >{Fore.SlateGray}AthenaColor Example:{Style.NoForeground}  
    >{Fore.Red}This is an of {Style.Bold}EXAMPLE{Style.NoBold} nested styling{Style.NoForeground}    
    >{Fore.SlateGray}As you can see, the color needs to be manually returned here{Style.NoForeground}
    >"""  
    )
    >```

    >[!Example]- Console Output
    ><span style="color: SlateGray">AthenaColor Example:</span>
    ><span class="red">This is an <b>EXAMPLE</b> of nested Styling</span>
    ><span style="color: SlateGray">As you can see, the correct color returns here by itself</span>

## Nested Styling

- General Example
    >[!code]- Python Code
    >```python
    >from AthenaColor import ForeNest, StyleNest
    >
    >print(  
    >    ForeNest.SlateGray(StyleNest.Italic(  
    >        "AthenaColor Example:",  
    >        ForeNest.Red(  
    >            "This is an",  
    >            StyleNest.Bold("EXAMPLE"),  
    >            "of nested styling"  
    >        ),  
    >        sep="\n"  
    >    ))  
    >)
    >```

    >[!Example]- Console Output
    ><span style="color: SlateGray">AthenaColor Example:</span>
    ><span class="red">This is an <b>EXAMPLE</b> of nested Styling</span>
    ><span style="color: SlateGray">As you can see, the correct color returns here by itself</span>
  