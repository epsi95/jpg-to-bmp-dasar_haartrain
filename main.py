#!/usr/bin/env python
from PIL import Image
import glob

images_jpg = glob.glob("*.jpg")
counter = 1

for i in images_jpg:
    filename = "bmp\\a"+str(counter)+".bmp"
    print(filename)
    Image.open(i).save(filename)
    counter += 1


