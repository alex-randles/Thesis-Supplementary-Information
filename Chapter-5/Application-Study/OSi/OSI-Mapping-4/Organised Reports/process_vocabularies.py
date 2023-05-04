import os
from rdflib import *
for file in os.listdir("."):
    mapping_directory = os.fsdecode(file)
    mapping_id = mapping_directory.split("(")[0]
    mapping_project = mapping_directory.split("(")[-1].split(")")[0]
    if os.path.isdir(file):
        sub_directory = os.fsencode(file)
        str_sub_directory = sub_directory.decode('utf-8')
        for sub_directory_file in os.listdir(sub_directory):
            if "group" not in str_sub_directory:
                current_file = sub_directory_file.decode('utf-8')
                if current_file.endswith(".ttl") and current_file != "refined_mapping.ttl":
                    RR = Namespace("http://www.w3.org/ns/r2rml#")
                    try:
                        g = Graph().parse(str_sub_directory + "/" + current_file, format="ttl")
                        if len(list(g.triples((None, RR.predicateObjectMap, None)))) > 1:
                            print(current_file, "shshsh")
                    except:
                        pass
