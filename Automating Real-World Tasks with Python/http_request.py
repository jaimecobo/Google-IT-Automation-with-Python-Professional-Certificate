#! /usr/bin/env python3

import os
import requests

# Path to the data
path = "/data/feedback/"

keys = ["title", "name", "date", "feedback"]

folder = os.listdir(path)
for file in folder:
    keycount = 0
    fb = {}
    with open(path + file) as fl:
        for line in fl:
            value = line.strip()
            fb[keys[keycount]] = value
            keycount += 1
    print(fb)
    response = requests.post("http://<IP Address>/feedback/",
    json=fb)
print(response.request.body)
print(response.status_code)

#=================================================================
#=================================================================

#! /usr/bin/env python3
import os
import requests

list_of_files = os.listdir('/data/feedback')
for file in list_of_files:
        fp = open('/data/feedback/'+file)
        #data = fp.read()
        #data = data.split('\n')
		data = fp.read().split('\n')
        dic = {"title":data[0], "name":data[1], "date":data[2], "feedback":data[3]}
        response = requests.post('http://104.197.6.205/feedback/', json=dic)
        print(response.status_code)


#=================================================================
#=================================================================


feedback_dir = "/data/feedback/"
website_dir = "/projects/corpweb/"
url = "http://34.68.197.162/feedback/"
feedback_dic = {}

for feedback_file in os.listdir(feedback_dir):
    with open(feedback_dir + feedback_file,"r") as f:
        lines = f.readlines()
        feedback_dic["title"] = lines[0]
        feedback_dic["name"] = lines[1]
        feedback_dic["date"] = lines[2]
        feedback_dic["feedback"] = lines[3]
        response = requests.post(url, data=feedback_dic)
        print(response.status_code)
        print(response.ok)