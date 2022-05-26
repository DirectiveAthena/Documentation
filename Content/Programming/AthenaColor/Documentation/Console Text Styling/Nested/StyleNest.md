---
copyright: "Andreas Sas 2022"
created: "2022-05-26 13:03"
cssclass: metaDataHide athenacolor
aliases: [AthenaColor StyleNest]
---

# AthenaColor Console Text Styling: StyleNest

*class* AthenaColor.**StyleNest()**
- AthenaColor.*StyleNest* is a class which holds all methods pertaining to the 
style transformation of given objects.
- A method of the class is always a static method and any method used by this class always has two arguments
    - `*obj` : Holds all the elements needed to be enclosed by the ANSI styling codes.
    - `sep` : A keyword only argument which allows you defined a specific separation string between the various objects in `*obj`. 
        By default this is a empty space.

--

*method* AthenaColor.StyleNest.**Reset(**`*obj,sep=sep_`**)**  
- Returns a 
*method* AthenaColor.StyleNest.**Bold(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**NoBold(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**Dim(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**NoDim(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**Italic(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**NoItalic(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**Underline(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**NoUnderline(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**BlinkSlow(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**NoBlinkSlow(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**BlinkRapid(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**NoBlinkRapid(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**Reversed(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**NoReversed(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**Conceal(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**NoConceal(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**Crossed(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**NoCrossed(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**FontPrimary(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**FontSecond1(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**FontSecond2(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**FontSecond3(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**FontSecond4(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**FontSecond5(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**FontSecond6(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**FontSecond8(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**FontSecond9(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**FontSecond10(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**NoFont(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**Fraktur(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**UnderlineDouble(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**NoUnderlineDouble(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**PropSpacing(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**NoPropSpacing(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**NoForeground(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**NoBackground(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**Frame(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**NoFrame(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**Circle(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**NoCircle(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**OverLine(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**NoOverLine(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**UnderColourDefault(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**IdeogramUnderLine(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**IdeogramUnderLineDouble(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**IdeogramOverLine(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**IdeogramOverLineDouble(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**IdeogramStress(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**NoIdeogram(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**SuperScript(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**SubScript(**`*obj,sep=sep_`**)**  
*method* AthenaColor.StyleNest.**NoScript(**`*obj,sep=sep_`**)**