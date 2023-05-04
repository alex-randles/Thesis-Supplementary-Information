import os
import sys
from rdflib import *
import time
import json
directory = "/home/alex/Desktop/Evaluation-1 (Validation Reports)/"
for file in os.listdir(directory):
    mapping_directory = os.fsdecode(file)
    mapping_id = mapping_directory.split("(")[0]
    mapping_project = mapping_directory.split("(")[-1].split(")")[0]
    print(directory + str(file))
    if os.path.isdir(directory + str(file)):
        sub_directory = os.fsencode(directory + str(file))
        str_sub_directory = sub_directory.decode('utf-8')
        # print(str_sub_directory)
        files = os.listdir(str_sub_directory)
        if "validation_report_1.ttl" in files and "validation_report.ttl" in files:
            g1 = Graph().parse(directory + str(file) + "/validation_report.ttl", format="ttl")
            g2 = Graph().parse(directory + str(file) + "/validation_report_1.ttl", format="ttl")
            g3 = g1 + g2
            g3.serialize(directory + str(file) + "/validation_report_3.ttl", format="ttl")