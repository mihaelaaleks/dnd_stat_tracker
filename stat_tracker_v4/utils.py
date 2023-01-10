import json

#   this is a general utilities script
    #it contains functions that read the json character sheet
    #can modify and save it
    

def load_json_sheet(file_string):
    json_as_dict = {}
    with open(file_string, "r") as f: 
        json_as_dict = json.load(f)
    
    return json_as_dict