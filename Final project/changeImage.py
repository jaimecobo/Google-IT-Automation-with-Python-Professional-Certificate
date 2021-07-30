#!/usr/bin/env python3
from PIL import Image
import os
import sys

path = "supplier-data/images/"
images = os.listdir(path)

for im in images:
  if 'tiff' in im:
    file_name = os.path.splitext(im)[0]
    outfile = "supplier-data/images/" + file_name + ".jpeg"
    Image.open(path + im).convert("RGB").resize((600,400)).save(outfile,"JPEG")
	  
	  
#######################################################################
#######################################################################

#!/usr/bin/env python3
#from PIL import Image
#import os, sys

#path = "supplier-data/images/"
#pictures = os.listdir(path)

#for pic in pictures:
#  if 'tiff' in pic:
    #grab the picture name without the .tiff extension
#    file_name = os.path.splitext(pic)[0]
#    outfile = "supplier-data/images/" + file_name + ".jpeg"
#    try:
#      Image.open(path + pic).convert("RGB").resize((600,400)).save(outfile,"JPEG")
#    except IOError:
#     print("cannot convert", pic)