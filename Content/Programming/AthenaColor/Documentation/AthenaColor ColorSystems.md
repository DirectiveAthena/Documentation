---
cssclass: athenacolor
---
# AthenaColor ColorSystems
## Color Objects
Each color object has full support for math and comparison dunders.
 
 Currently implemented color systems are:
 - [[#^rgb|RGB]]
 - [[#^rgba|RGBA]]
 - [[#^hex|HEX]]
 - [[#^hexa|HEXA]]
 - [[#^hsl|HSL]]
 - [[#^hsv|HSV]]
 - [[#^cmyk|CMYK]]
 
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
>>> HEX("#123456").export()
(18, 52, 120)
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
*dunder* HEX.**____repr____()**
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
- The property `h` holds the **HUE** value. The property accepts an integer or a float value. The amount of rounded to decimals is stored in the  [[AthenaColor InitClass#^decimalPlaces|init.decimalPlaces]] property.

---
*property* HSL.**s**
- The property `s` holds the **SATURATION** value. The property accepts an integer or a float value. The amount of rounded to decimals is stored in the  [[AthenaColor InitClass#^decimalPlaces|init.decimalPlaces]] property.

---
*property* HSL.**l**
- The property `l` holds the **LUMINOSITY** value. The property accepts an integer or a float value. The amount of rounded to decimals is stored in the  [[AthenaColor InitClass#^decimalPlaces|init.decimalPlaces]] property.

---
*method* HSL.**export()**
- Exports the various color elements which make up the color system to a tuple. In the case of the HSL object, this is a tuple in the order of h,s,l.

```python
>>> from AthenaColor import HSL
>>> HSL(180,0.5,0.5).export()
(180,0.5,0.5)
```

---
*dunder* HSL.**____str____()**
- Returns a string object with all the color elements separated by a `;`

```python
>>> from AthenaColor import HSL
>>> str(HSL(180,0.5,0.5))
'180;0.5;0.5'
```

---
*dunder* HSL.**____repr____()**
- Returns a string object, consisting of a literal presentation of the object with name, and color element properties.

```python
>>> from AthenaColor import HSL
>>> repr(HSL(180,0.5,0.5))
'HSL(h=180,s=0.5,l=0.5)'
```

### Color system: HSV 
^hsv

*class* AthenaColor.**HSV(**`h:int|float=0`,`s:int|float=0`,`v:int|float=0`**)**
- An HSL object consists out of three values. Hue, which ranges between 0 and 360 degrees, Saturation and Value which both range between 0 and 1.

```python
from AthenaColor import HSV

color = HSV(180,0.5,0.5)
```

---
*property* HSV.**h**
- The property `h` holds the **HUE** value. The property accepts an integer or a float value. The amount of rounded to decimals is stored in the  [[AthenaColor InitClass#^decimalPlaces|init.decimalPlaces]] property.

---
*property* HSV.**s**
- The property `s` holds the **SATURATION** value. The property accepts an integer or a float value. The amount of rounded to decimals is stored in the  [[AthenaColor InitClass#^decimalPlaces|init.decimalPlaces]] property.

---
*property* HSV.**v**
- The property `v` holds the **VALUE** value. The property accepts an integer or a float value. The amount of rounded to decimals is stored in the  [[AthenaColor InitClass#^decimalPlaces|init.decimalPlaces]] property.

---
*method* HVL.**export()**
- Exports the various color elements which make up the color system to a tuple. In the case of the HSV object, this is a tuple in the order of h,s,v.

```python
>>> from AthenaColor import HSV
>>> HSV(180,0.5,0.5).export()
(180,0.5,0.5)
```

---
*dunder* HSV.**____str____()**
- Returns a string object with all the color elements separated by a `;`

```python
>>> from AthenaColor import HSV
>>> str(HSV(180,0.5,0.5))
'180;0.5;0.5'
```

---
*dunder* HSV.**____repr____()**
- Returns a string object, consisting of a literal presentation of the object with name, and color element properties.

```python
>>> from AthenaColor import HSV
>>> repr(HSV(180,0.5,0.5))
'HSL(h=180,s=0.5,l=0.5)'
```


### Color system: CMYK 
^cmyk
 
*class* AthenaColor.**CMYK(**`c:int|float=0`, `m:int|float=0`, `y:int|float=0`,`k:int|float=0`**)**
- A CMYK object can hold four float values, ranging between 0 and 1.

```python
from AthenaColor import CMYK

color = CMYK(.25,.5,.75,1)
```

---
*property* CMYK.**c**
- The property `c` holds the **CYAN** value. The property accepts an integer or a float value. The amount of rounded to decimals is stored in the  [[AthenaColor InitClass#^decimalPlaces|init.decimalPlaces]] property.

---
*property* CMYK.**m**
- The property `m` holds the **MAGENTA** value. The property accepts an integer or a float value. The amount of rounded to decimals is stored in the  [[AthenaColor InitClass#^decimalPlaces|init.decimalPlaces]] property.

---
*property* CMYK.**y**
- The property `y` holds the **YELLOW** value. The property accepts an integer or a float value. The amount of rounded to decimals is stored in the  [[AthenaColor InitClass#^decimalPlaces|init.decimalPlaces]] property.

---
*property* CMYK.**k**
- The property `k` holds the **BLACK** value. The property accepts an integer or a float value. The amount of rounded to decimals is stored in the  [[AthenaColor InitClass#^decimalPlaces|init.decimalPlaces]] property.

---
*method* CMYK.**export()**
- Exports the various color elements which make up the color system to a tuple. In the case of the CMYK object, this is a tuple in the order of c,m,y,k.

```python
>>> from AthenaColor import CMYK
>>> CMYK(.25,.5,.75,1).export()
(0.25, 0.5, 0.75, 1)
```

---
*dunder* CMYK.**____str____()**
- Returns a string object with all the color elements separated by a `;`

```python
>>> from AthenaColor import CMYK
>>> str(CMYK(.25,.5,.75,1))
'0.25;0.5;0.75;1'
```

---
*dunder* CMYK.**____repr____()**
- Returns a string object, consisting of a literal presentation of the object with name, and color element properties.

```python
>>> from AthenaColor import CMYK
>>> repr(CMYK(.25,.5,.75,1))
'CMYK(c=0.25,m=0.5,y=0.75,k=1)'
```

### Color system: RGBA 
^rgba

*class* AthenaColor.**RGBA(**`r:int=0`, `g:int=0`, `b:int=0`, `a:int=0`**)**
- An RGBA object can hold four integer values (r,g,b,a) each ranging between 0 to 255.

```python
from AthenaColor import RGBA

color = RGBA(255,255,255,255)
```

---
*property* RGBA.**r**
- The property `r` holds the **RED** value. The property accepts an integer or a float value, but float values will always be rounded back to an integer. The rounding function depends on the [[AthenaColor InitClass#^roundUp|init.roundUp]] property.

---
*property* RGBA.**g**
- The property `g` holds the **GREEN** value. The property accepts an integer or a float value, but float values will always be rounded back to an integer. The rounding function depends on the [[AthenaColor InitClass#^roundUp|init.roundUp]] property.

---
*property* RGBA.**b**
- The property `b` holds the **BLUE** value. The property accepts an integer or a float value, but float values will always be rounded back to an integer. The rounding function depends on the [[AthenaColor InitClass#^roundUp|init.roundUp]] property..

---
*property* RGBA.**a**
- The property `a` holds the **TRANSPARENCY** value. The property accepts an integer or a float value, but float values will always be rounded back to an integer. The rounding function depends on the [[AthenaColor InitClass#^roundUp|init.roundUp]] property.

---
*method* RGBA.**export()**
- Exports the various color elements which make up the color system to a tuple. In the case of the RGBA object, this is a tuple in the order of r,g,b,a.

```python
>>> from AthenaColor import RGB
>>> RGB(32,64,128,255).export()
(32, 64, 128, 255)
```

---
*dunder* RGBA.**____str____()**
- Returns a string object with all the color elements separated by a `;`

```python
>>> from AthenaColor import RGBA
>>> str(RGBA(32,64,128,255))
'32;64;128;255'
```

---
*dunder* RGBA.**____repr____()**
- Returns a string object, consisting of a literal presentation of the object with name, and color element properties.

```python
>>> from AthenaColor import RGBA
>>> repr(RGB(32,64,128,255))
'RGBA(r=32,g=64,b=128,a=255)'
```

### Color system: HEXA 
^hexa
 
*class* AthenaColor.**HEXA(**`hex_value:str="#00000000"`**)**
- An HEXA object directly inherits from the [[#Color system RGBA|RGBA]] class. On initialization, a true HEXA string can be used to defined the r,g,b,a values. These three integer values (r,g,b,a) each range between 0 to 255.

```python
from AthenaColor import HEXA

color = HEXA("#12345678")
```

---
*property* HEXA.**r**
- The property `r` holds the **RED** value. The property accepts an integer or a float value, but float values will always be rounded back to an integer. The rounding function depends on the [[AthenaColor InitClass#^roundUp|init.roundUp]] property.

---
*property* HEXA.**g**
- The property `g` holds the **GREEN** value. The property accepts an integer or a float value, but float values will always be rounded back to an integer. The rounding function depends on the [[AthenaColor InitClass#^roundUp|init.roundUp]] property.

---
*property* HEXA.**b**
- The property `r` holds the **BLUE** value. The property accepts an integer or a float value, but float values will always be rounded back to an integer. The rounding function depends on the [[AthenaColor InitClass#^roundUp|init.roundUp]] property.

---
*property* HEXA.**a**
- The property `a` holds the **TRANSPARENCY** value. The property accepts an integer or a float value, but float values will always be rounded back to an integer. The rounding function depends on the [[AthenaColor InitClass#^roundUp|init.roundUp]] property.

---
*method* HEXA.**export()**
- Exports the various color elements which make up the color system to a tuple. In the case of the HEXA object, this is a tuple in the order of r,g,b,a.

```python
>>> from AthenaColor import HEXA
>>> HEXA("#12345678").export()
(18,52,86,120)
```

---
*dunder* HEX.**____str____()**
- Returns a string object with the r,g,b,a format changed to a hexadecimal format.

```python
>>> from AthenaColor import HEXA
>>> str(HEXA("#12345678"))
'#12345678'
```

---
*dunder* HEX.**____repr____()**
- Returns a string object, consisting of a literal presentation of the object with name, and color element properties.

```python
>>> from AthenaColor import HEXA
>>> repr(HEXA("#12345678"))
HEXA(r=18,g=52,b=86,a=120)
```
