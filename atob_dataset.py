import sys
from PIL import Image
import os
import glob
import numpy as np

size = 600, 600
path1 = 'test/dsm'
path2 = 'test/dtm'
input1_paths = glob.glob(os.path.join(os.getcwd(), path1, "*.jpg"))
input2_paths = glob.glob(os.path.join(os.getcwd(), path2, "*.jpg"))

images1 = [Image.open(d).resize(size,  Image.ANTIALIAS) for d in input1_paths]
images2 = [Image.open(d).resize(size,  Image.ANTIALIAS) for d in input2_paths]

for i in range(len(images1)):
    new_im = Image.new('RGB', (size[0]*2, size[1]))
    x_offset = 0
    new_im.paste(images1[i], (x_offset,0)) 
    x_offset += size[0]
    new_im.paste(images2[i], (x_offset,0)) 
    new_im.save(os.path.join(os.getcwd(), 'test/atob', str(i+1)+'.jpg'))
    
    
