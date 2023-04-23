<style>
h1, h2, h3
{
font-family: "Inria Serif", Times, serif;
    font-variant-ligatures: common-ligatures;
}

body{
    font-family: "IBM Plex Sans", sans-serif;
    font-variant-ligatures: common-ligatures;
}
</style>

# <center>Shri Ramdeobaba College of Engineering and Management<br>Nagpur, 440013</center>

## <center>Department of Computer Science Engineering</center>

### <center>FDVIP Lab</center>

---

**Name** : _Shantanu Mane_<br>
**Roll No.** : _E63_<br>
**Batch** : _CSE-AIML_<br>
**Date** : _5/4/2023_<br>

---

### AIM - To study and perform morphological operations on an image.

1. Erosion
2. Dilation
3. Opening
4. Closing

---

## Importing Dependencies

```python
import cv2
import matplotlib.pyplot as plt
import numpy as np
```

## Reading the images

```python
image = cv2.imread("../data/mri_2.png", 0)
```

## 1. Erosion

### Creating Kernel

```python
kernel = np.ones((5, 5), np.uint8)
```

### Applying Erosion

```python
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

invert = cv2.bitwise_not(binr)

erosion = cv2.erode(invert, kernel, iterations=1)
```

### Output

| ![eroded.png](..%2Fdata%2Feroded.png) |
|:-------------------------------------:|
|           **Eroded Image**            |

## 2. Dilation

### Creating Kernel

```python
kernel = np.ones((5, 5), np.uint8)
```

### Applying Dilation

```python
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

invert = cv2.bitwise_not(binr)

dilation = cv2.dilate(invert, kernel, iterations=1)
```

### Output

| ![dilated.png](..%2Fdata%2Fdilated.png) |
|:---------------------------------------:|
|            **Dilated Image**            |

## 3. Opening

### Creating Kernel

```python
kernel = np.ones((5, 5), np.uint8)
```

### Applying Opening

```python
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

invert = cv2.bitwise_not(binr)
for i in range(0, 25, 5):
    opening = cv2.morphologyEx(binr, cv2.MORPH_OPEN, kernel, iterations=i)
    cv2.imwrite(f"../data/opening_{i}.png", opening)
```

### Output

| Iterations | Image                                         |
|------------|-----------------------------------------------|
| 0          | ![opening_0.png](..%2Fdata%2Fopening_0.png)   |
| 5          | ![opening_5.png](..%2Fdata%2Fopening_5.png)   |
| 10         | ![opening_10.png](..%2Fdata%2Fopening_10.png) |
| 15         | ![opening_15.png](..%2Fdata%2Fopening_15.png) |
| 20         | ![opening_20.png](..%2Fdata%2Fopening_20.png) |
| 25         | ![opening_25.png](..%2Fdata%2Fopening_25.png) |

## 4. Closing

### Creating Kernel

```python
kernel = np.ones((5, 5), np.uint8)
```

### Applying Closing

```python
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

invert = cv2.bitwise_not(binr)
for i in range(0, 25, 5):
    closing = cv2.morphologyEx(binr, cv2.MORPH_CLOSE, kernel, iterations=i)
    cv2.imwrite(f"../data/closing_{i}.png", closing)
```

### Output

| Iterations | Image                                         |
|------------|-----------------------------------------------|
| 0          | ![closing_0.png](..%2Fdata%2Fclosing_0.png)   |
| 5          | ![closing_5.png](..%2Fdata%2Fclosing_5.png)   |
| 10         | ![closing_10.png](..%2Fdata%2Fclosing_10.png) |
| 15         | ![closing_15.png](..%2Fdata%2Fclosing_15.png) |
| 20         | ![closing_20.png](..%2Fdata%2Fclosing_20.png) |
| 25         | ![closing_25.png](..%2Fdata%2Fclosing_25.png) |