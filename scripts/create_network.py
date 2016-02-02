#!/usr/bin/env python

import json
from os import walk
import networkx as nx
import matplotlib.pyplot as plt


json_path = "/Users/xiaoli/Desktop/literatures/json/"
gexf_path = "/Users/xiaoli/Desktop/literatures/gexf/networkx.gexf"

G = nx.Graph()

json_file_names = []
for (dirpath, dirnames, filenames) in walk(json_path):
    json_file_names.extend(filenames)
    break

json_file_names = json_file_names[1:]

i = 1
for file_name in json_file_names:
    with open(json_path + file_name) as f:
        json_data = json.load(f)

    G.add_node(i)
    G.node[i]['file_name'] = file_name[0:-5]
    i += 1

nx.write_gexf(G, gexf_path, prettyprint=True)

