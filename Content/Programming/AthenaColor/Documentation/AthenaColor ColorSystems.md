---
cssclass: athenacolor
---
# AthenaColor ColorSystems
 ## Color Objects
 Each color object has full support for math and comparison dunders.
 ### Color system: RGB 
 ^rgb
 
 *class* AthenaColor.**RGB(**`r:int=0`, `g:int=0`, `b:int=0`**)**
 - An RGB object can hold three integer values (r,g,b) each ranging between 0 to 255.

```python
from AthenaColor import RGB

color = RGB(255,255,255)
```

---
*property* RGB.**r**

- The property `r` holds the **RED** value. The property accepts an integer or a float value, but float values will always be rounded back to an integer. The rounding function depends on the [[AthenaColor InitClass#^roundUp|init.roundUp]] property.

---
*property* RGB.**g**
- The property `g` holds the **GREEN** value. The property accepts an integer or a float value, but float values will always be rounded back to an integer. The rounding function depends on the [[AthenaColor InitClass#^roundUp|init.roundUp]] property.

---
*property* RGB.**b**
- The property `b` holds the **BLUE** value. The property accepts an integer or a float value, but float values will always be rounded back to an integer. The rounding function depends on the [[AthenaColor InitClass#^roundUp|init.roundUp]] property.

---
*method* RGB.**export()**
- Exports the various color elements which make up the color system to a tuple. In the case of the RGB object, this is a tuple in the order of r,g,b.

```python
>>> from AthenaColor import RGB
>>> RGB(64,128,255).export()
(64, 128, 255)
```

---
*dunder* RGB.**____str____()**
- Returns a string object with all the color elements separated by a `;`

```python
>>> from AthenaColor import RGB
>>> str(RGB(64,128,255))
'64;128;255'
```

---
*dunder* RGB.**____repr____()**
- Returns a string object, consisting of a literal presentation of the object with name, and color element properties.

```python
>>> from AthenaColor import RGB
>>> repr(RGB(64,128,255))
'RGB(r=64,g=128,b=255)'
```

 ### Color system: HEX 
 ^hex
 
*class* AthenaColor.**HEX(**`hex_value:str="#000000"`**)**
- An HEX object directly inherits from the [[#Color system RGB|RGB]] class. On initialization, a true HEX string can be used to defined the r,g,b values. These three integer values (r,g,b) each range between 0 to 255.

```python
from AthenaColor import HEX

color = HEX("#123456")
```

---
*property* HEX.**r**
- The property `r` holds the **RED** value. The property accepts an integer or a float value, but float values will always be rounded back to an integer. The rounding function depends on the [[AthenaColor InitClass#^roundUp|init.roundUp]] property.

---
*property* HEX.**g**
- The property `g` holds the **GREEN** value. The property accepts an integer or a float value, but float values will always be rounded back to an integer. The rounding function depends on the [[AthenaColor InitClass#^roundUp|init.roundUp]] property.

---
*property* HEX.**b**
- The property `r` holds the **BLUE** value. The property accepts an integer or a float value, but float values will always be rounded back to an integer. The rounding function depends on the [[AthenaColor InitClass#^roundUp|init.roundUp]] property.

---
*method* HEX.**export()**
- Exports the various color elements which make up the color system to a tuple. In the case of the HEX object, this is a tuple in the order of r,g,b.

```python
>>> from AthenaColor import HEX
>>> HEX(64,128,255).export()
(64, 128, 255)
```

---
*dunder* HEX.**____str____()**
- Returns a string object with the r,g,b format changed to a hexadecimal format.

```python
>>> from AthenaColor import HEX
>>> str(HEX("#123456"))
'#123456'
```

---
*dunder* RGB.**____repr____()**
- Returns a string object, consisting of a literal presentation of the object with name, and color element properties.

```python
>>> from AthenaColor import HEX
>>> repr(HEX("#123456"))
'HEX(r=18,g=52,b=86)'
```

 ### Color system: HSL 
 ^hsl
 
*class* AthenaColor.**HSL(**`h:int|float=0`,`s:int|float=0`,`l:int|float=0`**)**
- An HSL object consists out of three values. Hue, which ranges between 0 and 360 degrees, Saturation and Luminosity which both range between 0 and 1.

```python
from AthenaColor import HSL

color = HSL(180,0.5,0.5)
```

---
*property* HSL.**h**
- The property `h` holds the **HUE** value. The property accepts an integer or a float value, but float values will always be rounded back to an integer. The rounding function depends on the [[AthenaColor InitClass#^decimalPlaces|init.decimalPlaces]] property.
### Color system: HSV 
^hsv
 
*class* AthenaColor.**HSV**

### Color system: CMYK 
^cmyk
 
*class* AthenaColor.**CMYK**

### Color system: RGBA 
^rgba

*class* AthenaColor.**RGBA**

### Color system: HEXA 
^hexa
 
*class* AthenaColor.**HEXA** 
