---
alias: AthenaColor Documentation ColorSystems
cssclass: athenacolor
---
# AthenaColor ColorSystems
 ## Color Objects
 Each color object has full support for math and comparison dunders.
 
 ### Color system: RGB ^rgb
 *class* AthenaColor.**RGB(** *r :int, g:int, b:int* **)**
 <div class="inset">
	An RGB object can hold three integer values (r,g,b) each ranging between 0 to 255.
</div>

```python
from AthenaColor import RGB

color = RGB(255,255,255)
```

<div class="inset">
	RGB.<b>r</b>
	<div class="inset">
		The property <code>r</code> holds the <b>RED</b> value. The property accepts an integer or a float value, but float values will always be rounded back to an integer. The rounding function depends on the AthenaColor.init.roundUp property.
	</div>
	<br>
</div>

<div class="inset">
	RGB.<b>g</b>
	<div class="inset">
		The property <code>g</code> holds the <b>GREEN</b> value. The property accepts an integer or a float value, but float values will always be rounded back to an integer. The rounding function depends on the AthenaColor.init.roundUp property.
	</div>
	<br>
</div>

<div class="inset">
	RGB.<b>b</b>
	<div class="inset">
		The property <code>b</code> holds the <b>BLUE</b> value. The property accepts an integer or a float value, but float values will always be rounded back to an integer. The rounding function depends on the AthenaColor.init.roundUp property.
	</div>
	<br>
</div>

<div class="inset">
	RGB.<b>export()</b>
	<div class="inset">
		Exports the various color elements which make up the color system to a tuple. In the case of the RGB object, this is a tuple in the order of r,g,b.
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

<div class="inset">
	RGB.<b>__repr__()</b>
	<div class="inset">
		Returns a string object, consisting of a literal presentation of the object with name, and color element properties.
	</div>
</div>

```python
>>> from AthenaColor import RGB
>>> repr(RGB(64,128,255))
'RGB(r=64,g=128,b=255)'
```

 ### Color system: HEX ^hex
*class* AthenaColor.**HEX(** *hex_value:str* **)**
<span class="inset"> An HEX object directly inherits from the [[#^rgb|RGB]] class. can hold three integer values (r,g,b) each ranging between 0 to 255.</span>
 <div class="inset">
	An HEX object directly inherits from the <a href="#^rgb"  class="internal-link" >RGB</a> can hold three integer values (r,g,b) each ranging between 0 to 255.
</div>

```python
from AthenaColor import RGB

color = RGB(255,255,255)
```

<div class="inset">
	RGB.<b>r</b>
	<div class="inset">
		The property <code>r</code> holds the <b>RED</b> value. The property accepts an integer or a float value, but float values will always be rounded back to an integer. The rounding function depends on the AthenaColor.init.roundUp property.
	</div>
	<br>
</div>

<div class="inset">
	RGB.<b>g</b>
	<div class="inset">
		The property <code>g</code> holds the <b>GREEN</b> value. The property accepts an integer or a float value, but float values will always be rounded back to an integer. The rounding function depends on the AthenaColor.init.roundUp property.
	</div>
	<br>
</div>

<div class="inset">
	RGB.<b>b</b>
	<div class="inset">
		The property <code>b</code> holds the <b>BLUE</b> value. The property accepts an integer or a float value, but float values will always be rounded back to an integer. The rounding function depends on the AthenaColor.init.roundUp property.
	</div>
	<br>
</div>

<div class="inset">
	RGB.<b>export()</b>
	<div class="inset">
		Exports the various color elements which make up the color system to a tuple. In the case of the RGB object, this is a tuple in the order of r,g,b.
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

<div class="inset">
	RGB.<b>__repr__()</b>
	<div class="inset">
		Returns a string object, consisting of a literal presentation of the object with name, and color element properties.
	</div>
</div>

```python
>>> from AthenaColor import RGB
>>> repr(RGB(64,128,255))
'RGB(r=64,g=128,b=255)'
```


 ### Color system: HSL ^hsl
*class* AthenaColor.**HSL**
<div class="inset">

</div>

 ### Color system: HSV ^hsv
*class* AthenaColor.**HSV**
<div class="inset">

</div>

 ### Color system: CMYK ^cmyk
*class* AthenaColor.**CMYK**
<div class="inset">

</div>

 ### Color system: RGBA ^rgba
*class* AthenaColor.**RGBA**
<div class="inset">

</div>

 ### Color system: HEXA ^hexa
*class* AthenaColor.**HEXA** 
<div class="inset">

</div>
