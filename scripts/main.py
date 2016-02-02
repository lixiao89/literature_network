#!/usr/bin/env python

from alchemyapi import AlchemyAPI
import json
import pdf2txt
from os import walk


k = '-o'
pdf_path = "/Users/xiaoli/Desktop/literatures/pdf1/"
out_txt_path = "/Users/xiaoli/Desktop/literatures/text/"
json_path = "/Users/xiaoli/Desktop/literatures/json/"

# Create the AlchemyAPI Object
alchemyapi = AlchemyAPI()

# ---- Convert pdf to txt (doesn't have to be run if no new pdfs are added) ---

pdf_name = []
# get pdf names
for(dirpath, dirnames,filenames) in walk(pdf_path):
    pdf_name.extend(filenames)
    break

# convert pdf to txt
for f in pdf_name:
    if f[-3:] == "pdf":
        full_pdf_path = pdf_path + f
        full_text_path = out_txt_path + f[0:-3] + "txt"
        pdf2txt.main(full_pdf_path, k , full_text_path)

# ---------------------------------------------------------------------------

txt_name = []
for(dirpath, dirnames,filenames) in walk(out_txt_path):
    txt_name.extend(filenames)
    break

json_data = {}
entity_list = []
keywords_list = []
concept_list = []
for f in txt_name:
    if f[-3:] == "txt":
        full_text_path = out_txt_path + f
        with open(full_text_path, 'r') as current_txt_file:
            txt_data = current_txt_file.read().replace('\n','')
            response_entities = alchemyapi.entities('text', txt_data)
            response_keywords = alchemyapi.keywords('text', txt_data)
            response_concepts = alchemyapi.concepts('text', txt_data)
            if response_entities['status'] == 'OK' and response_keywords['status'] == 'OK':
                print "status OK"
                for entity in response_entities["entities"]:
                    dict_temp = {'entity': entity['text'],
                                 'type': entity['type'],
                                 'relevance': entity['relevance']}
                    entity_list.append(dict_temp)
                for keyword in response_keywords["keywords"]:
                    dict_temp = {'keyword': keyword['text'],
                                 'relevance': keyword['relevance']}
                    keywords_list.append(dict_temp)
                for concept in response_concepts['concepts']:
                    dict_temp = {'concept': concept['text'],
                                 'relevance': concept['relevance']}
                    concept_list.append(dict_temp)
                json_data['entities'] = entity_list
                json_data['keywords'] = keywords_list
                json_data['concepts'] = concept_list
                with open(json_path + f[0:-3] + "json", 'wb') as json_out:
                    #json.dump(response, json_out, indent=4)
                    json.dump(json_data, json_out, indent=4)
            else:
                print('Error in entity extraction call: ', response_entities['statusInfo'])

