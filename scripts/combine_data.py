#!/usr/bin/env python

import json
from os import walk

json_path = "/Users/xiaoli/Desktop/literatures/json/"
pyscholar_json_path = "/Users/xiaoli/Desktop/literatures/pyscholar_results/res.json"

json_names = []
for (dirpath, dirnames, filenames) in walk(json_path):
    json_names.extend(filenames)
    break

# load pyscholar json result
with open(pyscholar_json_path) as f:
    pyscholar_data = json.load(f)

#combine pyscholar data with alchemy data
for json_file in json_names:
    if json_file[-4:] == "json":
        with open(json_path + json_file) as f:
            alchemy_data = json.load(f)
            for pyscholar_paper in pyscholar_data:
                if pyscholar_paper['title'] == json_file[0:-5]:
                    alchemy_data['pyscholar'] = pyscholar_paper   

        with open(json_path + json_file, 'wb') as f:
            json.dump(alchemy_data, f, indent=4)