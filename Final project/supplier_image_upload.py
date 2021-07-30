#!/usr/bin/env python3
import os
import requests

url = "http://localhost/upload/"
path = "supplier-data/images/"

images = os.listdir(path)

for im in images:
  if im.endswith(".jpeg"):
    with open(path + im, 'rb') as opened:
      r = requests.post(url, files={'file': opened})


###############################################################
###############################################################

#!/usr/bin/env python3
import os, sys
import requests

url = "http://localhost/upload/"
path = "supplier-data/images/"

images = os.listdir(path)

for image in images:
  if image.endswith(".jpeg"):
    with open(path + image, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
