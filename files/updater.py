#!/usr/bin/env python

import requests
import os
from icecream import ic


NEW_DATA_URL = "https://chicken-head1.github.io/Space-Simulator/files/update/new_data.txt"
BASE_FILE_URL = "https://chicken-head1.github.io/Space-Simulator/files"
DIRPATH: str = os.path.dirname(os.path.abspath(__file__))

data = requests.get(url=NEW_DATA_URL)
data = str(data.content).removeprefix("b'").removesuffix("\\n'")

data_list = data.split(";")
data_list = [i.split(":") for i in data_list]


for command_set in data_list:
    command = command_set[0]
    file = command_set[1]
    url = BASE_FILE_URL+file.replace('"', '')
    new_data = str(requests.get(url).content).removeprefix("b'").removesuffix("\\n'")
    file_path = file.removeprefix('"').removesuffix('"')
    file_path = DIRPATH+file_path

    ic(url)
    ic(new_data)


    if command == 'add': # add directory
        file = file.replace('"','')
        file = file.removeprefix('/')
        try:
            os.mkdir(file)
        except: # suppress errors from exiting the script
            ...

    elif command == 'adf' or command == 'edi': # add & edit file
        with open(file_path, 'w') as file:
            file.write(new_data)
    
    elif command == 'rem': # remove file
        try:
            os.remove(file)
        except: # suppress errors from exiting the script
            ...


def get_file_data(url: str) -> str:
    """
    Gets the data of a specified file from the webserver through its URL, returning the data given.
    """

    data = str(requests.get(url).content).removeprefix("b'").removesuffix("\\n'")

    return data
