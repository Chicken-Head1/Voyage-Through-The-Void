#!/usr/bin/env python

import requests
import os
import subprocess
import sys
import pygame
import time



pygame.init()
WINDOW = pygame.display.set_mode(flags=pygame.RESIZABLE)
pygame.display.set_caption("Space Simulator Updater")
win_height = WINDOW.get_height()
win_centrex = WINDOW.get_width()/2
win_centrey = WINDOW.get_height()/2


DOWNLOADING_FONT = pygame.font.SysFont(name='Courier', size=int(win_height/10.9))


WINDOW.fill((0, 0, 0))

downloading_text = DOWNLOADING_FONT.render("Updating game...", True, (255, 255, 255))
downloading_text_rect = downloading_text.get_rect()
WINDOW.blit(downloading_text, 
            (
                win_centrex-downloading_text_rect.width/2, # Xpos
                win_centrey, # Ypos
            ),
            )

pygame.display.flip()


NEW_DATA_URL = "https://chicken-head1.github.io/Space-Simulator/files/update/new_data.txt"
BASE_FILE_URL = "https://chicken-head1.github.io/Space-Simulator/files"
DIRPATH: str = os.path.dirname(os.path.abspath(__file__))

try:
    data = requests.get(url=NEW_DATA_URL)
    data = str(data.content).removeprefix("b'").removesuffix("\\n'")
    data_list = data.split(";")
    data_list = [i.split(":") for i in data_list]

except requests.exceptions.SSLError:
    print("Could not access webserver... unable to update game")
    data_list = []

for command_set in data_list:
    try:
        command = command_set[0]
        file = command_set[1]
    except IndexError: # No commands for the updater to use
        break # Just reopen the game, this only occurs during development :3
    url = BASE_FILE_URL+file.replace('"', '')
    new_data = str(requests.get(url).content).removeprefix("b'").removesuffix("\\n'")
    file = file.removeprefix('"').removesuffix('"')
    file_path = DIRPATH+file

    if command == 'add': # add directory
        file = file.removeprefix('/')
        try:
            os.mkdir(file)
        except: # suppress errors from exiting the script
            ...

    elif command == 'adf' or command == 'edi': # add & edit file
        with open(file_path, 'w') as file:
            file.write(new_data)
    
    elif command == 'rmf': # remove file)
        try:
            os.remove(file_path)
        except: # suppress errors from exiting the script
            ...
    
    elif command == 'rmd': # remove directory
        file = file.removeprefix('/')
        try:
            os.rmdir(file)
        except: # suppress errors from exiting the script
            ...

def get_file_data(url: str) -> str:
    """
    Gets the data of a specified file from the webserver through its URL, returning the data given.
    """

    data = str(requests.get(url).content).removeprefix("b'").removesuffix("\\n'")

    return data


WINDOW.fill((0, 0, 0))
updated_text = DOWNLOADING_FONT.render("Relaunching game...", True, (255, 255, 255))
updated_text_rect = updated_text.get_rect()
WINDOW.blit(updated_text, 
            (
                win_centrex-updated_text_rect.width/2, # Xpos
                win_centrey, # Ypos
            ),
            )

pygame.display.flip()

time.sleep(2)


pygame.quit()
args = [sys.executable, f"{os.path.join(DIRPATH, 'main.py')}"]
subprocess.Popen(args, start_new_session=True)
exit(0)
