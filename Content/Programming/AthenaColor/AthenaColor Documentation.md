---
cssclass: athenacolor
---

# AthenaColor Documentation
This file supports the full documentation of the [[AthenaColor]] package.

Currently supported Python versions: **3.7**, **3.8**, **3.9**, **3.10**
Other, older, versions are not currently supported. These older versions will probably not be supported by Andreas Sas himself, but if you want to contribute to the project and make this package compatible with older versions of Python, Pull requests are always welcome.
```python
help
azeaze
```

**Source Code:** [GitHub Repository]()

 ## Color Objects
 Each color object has full support for math and comparison dunders.
 
 ### Color systems
 *class* AthenaColor.**RGB(** *r : int, g : int, b : int* **)**^rgb
 <div class="inset">
An RGB object can hold three integer values (r,g,b) each ranging between 0 to 255. Any inserted
</div>

```python
from AthenaColor import RGB

color = RGB(255,255,255)
```

<div class="inset">
	RGB.<b>r</b>
	<div class="inset">
		The property 
	</div>
</div>

<div class="inset">
	RGB.<b>export()</b>
	<div class="inset">
		Exports the various color elements which make up the color system to a tuple. In the case of the RGB object, this is a tuple in the order of 
		r,g,b.
	</div>
</div>

```python
>>> from AthenaColor import RGB
>>> RGB(64,128,255).export()
(64, 128, 255)
```

<div class="inset">
	RGB.<b>__str__()</b>
	<div class="inset">
		Returns a string object with all the color elements separated by a <code>;</code>
	</div>
</div>

```python
>>> from AthenaColor import RGB
>>> str(RGB(64,128,255))
'64;128;255'
```

---
 *class* AthenaColor.**HEX** ^hex
<div class="inset">

</div>

---
*class* AthenaColor.**HSL** ^hsl
<div class="inset">

</div>

---
*class* AthenaColor.**HSV** ^hsv
<div class="inset">

</div>

---
*class* AthenaColor.**CMYK** ^cmyk
<div class="inset">

</div>

---
*class* AthenaColor.**RGBA** ^rgba
<div class="inset">

</div>

---
*class* AthenaColor.**HEXA** ^hexa
<div class="inset">

</div>

## Console Styling
 ### Nested
### Inline