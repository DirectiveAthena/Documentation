---
copyright: "Andreas Sas 2022"
created: "2022-04-26 03:36"
cssclass: 
aliases: [AthenaColor Styling]
---
# AthenaColor Styling
## Inline Styling
## Nested Styling

>[!code]- Python Code
>```python
>from AthenaColor import ForeNest
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
><span style="color: SlateGray">AthenaColor Example:
><span class="red">This is an <b>EXAMPLE</b> of nested Styling