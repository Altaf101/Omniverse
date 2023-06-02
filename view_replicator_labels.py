import numpy as np
from PIL import Image, ImageDraw


a = np.load(f'./ASSET/bounding_box_2d_tight_0100.npy')[0]
shape = [(a[1], a[2]), (a[3], a[4])]
# creating new Image object
img = Image.open(f'./ASSET/rgb_0100.png')
# create rectangle image
img1 = ImageDraw.Draw(img)  
img1.rectangle(shape, fill =None, outline ="limegreen", width = 2)
img.save(f"./ASSET/overlay_0100.png")
