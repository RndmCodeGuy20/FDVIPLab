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
**Date** : _12/4/2023_<br>

---

### AIM - To study and perform line and edge detection using OpenCV

1. Vertical and Horizontal Line Detection
2. Hough Line Detection
3. Canny Edge Detection

---

## Importing Dependencies

```python
import cv2
import matplotlib.pyplot as plt
import numpy as np
```

## Reading Image

```python
image = cv2.imread('images/lines.jpg', 0)
```

## Vertical and Horizontal Line Detection

### 1. Vertical Line Detection

```python
kernel = np.ones((11, 3), np.uint8)

verticalLines = cv2.erode(img, kernel, iterations=1)
```

### 2. Horizontal Line Detection

```python
kernel = np.ones((2, 19), np.uint8)

horizontalLines = cv2.erode(img, kernel, iterations=1)
```

### Output

| ![horizontalLines.png](..%2Fdata%2FhorizontalLines.png) | ![verticalLines.png](..%2Fdata%2FverticalLines.png) |
|:-------------------------------------------------------:|:---------------------------------------------------:|
|                  **Horizontal Lines**                   |                 **Vertical Lines**                  |

## Hough Line Detection

```python
edges = cv2.Canny(img, 100, 150)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 30, maxLineGap=50)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 128), 1)
```

### Output

| ![lineDetected.png](..%2Fdata%2FlineDetected.png) | ![lineEdges.png](..%2Fdata%2FlineEdges.png) |
|:-------------------------------------------------:|:-------------------------------------------:|
|                     **Lines**                     |                  **Edges**                  |

## Canny Edge Detection

```python
edges = cv2.Canny(img, 100, 150)
```

### Output

| ![edges.png](..%2Fdata%2Fedges.png) |
|:-----------------------------------:|
|           **Canny Edges**           |