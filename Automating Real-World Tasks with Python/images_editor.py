#!/usr/bin/env python3
import os
from PIL import Image
old_path = os.path.expanduser('~') + '/images/'
new_path = '/opt/icons/'
for image in os.listdir(old_path):
  if image.startswith('.'):
    continue
  im = Image.open(old_path + image)
  im.rotate(-90).resize((128, 128)).convert("RGB").save(new_path + image.split($
  im.close()

