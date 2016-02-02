#! /usr/bin/env python

#import PyScholar.src.pyscholar
import json
from pattern.web import URL
import pdf2txt

k = 'o'
path_to_pyscholar_json = "/Users/xiaoli/Desktop/literatures/pyscholar_results/res.json"
path_to_pdf_download = "/Users/xiaoli/Desktop/literatures/pdf1/"
out_txt_path = "/Users/xiaoli/Desktop/literatures/text/"
json_path = "/Users/xiaoli/Desktop/literatures/json/"

with open(path_to_pyscholar_json) as f:
    pyscholar_data = json.load(f)

    for paper in pyscholar_data:
        url_pdf = paper['url_pdf']
        pdf_title = paper['title'] + '.pdf'
        if url_pdf and url_pdf[-4:] == ".pdf":
            url = URL(url_pdf)
            f = open(path_to_pdf_download + pdf_title, 'wb')
            f.write(url.download(cached = False))
            f.close()
