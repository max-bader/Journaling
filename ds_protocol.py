# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Max Bader
# mibader@uci.edu
# 77466224

import json
from collections import namedtuple

# Namedtuple to hold the values retrieved from json messages.
# TODO: update this named tuple to use DSP protocol keys
DataTuple = namedtuple('Response', ['type', 'token'])

def extract_json(json_msg:str) -> DataTuple:
    '''
    Call the json.loads function on a json string and convert it to a DataTuple object
  
    TODO: replace the pseudo placeholder keys with actual DSP protocol keys
    '''
    try:
        json_obj = json.loads(json_msg)
        token = json_obj['response']['token']
        type = json_obj['response']['type']
    except json.JSONDecodeError:
        print("Json cannot be decoded.")

    return DataTuple(type, token)
