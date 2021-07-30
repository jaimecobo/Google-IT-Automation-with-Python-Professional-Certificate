#! /usr/bin/env python3
import os
import requests

txt_files = os.listdir('/data/feedback')
for file in txt_files:
  doc = open('/data/feedback/'+file)
  data = doc.read().split('\n')
  dict = {"title":data[0], "name":data[1], "date":data[2], "feedback":data[3]}
  response = requests.post('http://34.121.88.186/feedback/', json=dict)
  print(response.status_code)
