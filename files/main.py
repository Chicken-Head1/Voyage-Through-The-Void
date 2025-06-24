#!/usr/bin/env python3
"""
A game about space craft and interplanertary and interstellar flight.
Inspiration from the game `Spaceflight Simulator`.
"""

def loading_screen() -> None:
    win_centrex = WINDOW.get_width()/2
    win_centrey = WINDOW.get_height() /2
    win_height = WINDOW.get_height()
    WHITE = (255, 255, 255)
    norm_font_div = 21.8
    FONT = pygame.font.SysFont(name="Courier", size=int(win_height/norm_font_div), bold=True)

    WINDOW.fill("black")
    loading_text = FONT.render("Loading game...",
                               False, # anti-ailiasing
                               WHITE,
                               )
    loading_text_rect = loading_text.get_rect()
    WINDOW.blit(loading_text,
                (
                    win_centrex-int(loading_text_rect.width/2), # Xpos
                    win_centrey,                               # Ypos
                )
                )
    pygame.display.set_caption("Space Simulator")
    pygame.display.flip()
    return



import pygame

pygame.init()
WINDOW = pygame.display.set_mode(flags=pygame.RESIZABLE)
loading_screen()


import requests
import os
import sys
from json import load, dump
from typing import NoReturn
import subprocess
import time
from pygame.font import Font
from threading import Timer



def save_data(data: dict,
              path: str,
              ) -> None:
    with open(path, 'w') as file:
        dump(data, file, indent = 2)
    
    return


def get_data(path: str,
              ) -> dict:
    with open(path, 'r') as file:
        data: dict = load(file)

    return data



DIRPATH: str = os.path.dirname(os.path.abspath(__file__))
FILEPATH: str = f'{os.path.abspath(__file__)}'

VERSION_URL = "https://chicken-head1.github.io/Space-Simulator/version.md"

VERSION_PATH = f"/{os.path.join(DIRPATH, "data", "version.txt")}"
SETTINGS_DATA_PATH = f"{os.path.join(DIRPATH, "data", "settings_data.json")}"
MENU_BG_PATH = f"/{os.path.join(DIRPATH, "images", "menu_bg.jpeg")}"
CURSOR_PATH = f"/{os.path.join(DIRPATH, "images", "cursor.svg")}"
MAIN_MENU_MUSIC_PATH = f"/{os.path.join(DIRPATH, "sound", "main_menu.mp3")}"
MUSIC_ON_PATH = f"/{os.path.join(DIRPATH, "images", "music_on.svg")}"
MUSIC_OFF_PATH = f"/{os.path.join(DIRPATH, "images", "music_off.svg")}"
CLICK_SFX_PATH = f"/{os.path.join(DIRPATH, "sound", "click_sfx.mp3")}"
RETURN_PATH = f"/{os.path.join(DIRPATH, "images", "return.svg")}"
UPDATE_FILE_PATH = f"{os.path.join(DIRPATH, "updater.py")}"
INFO_PATH = f"{os.path.join(DIRPATH, "images", "info.svg")}"
CREDITS_PATH = f"{os.path.join(DIRPATH, "images", "credits.svg")}"
VISUALS_PATH = f"{os.path.join(DIRPATH, "images", "eye.svg")}"
VOLUME_PATH = f"{os.path.join(DIRPATH, "images", "volume.svg")}"

INFORMATION = 'information'
CLICKABLE = 'clickable'

win_width: float = WINDOW.get_width()
win_height: float = WINDOW.get_height()
win_right: float = win_width
win_bottom: float = win_height
win_left: int = 0
win_top: int = 0
win_centrex: float = win_width/2
win_centrey: float = win_height/2

print("win_width", win_width)
print("win_height", win_height)
print("win_centrex", win_centrex)
print("win_centrey", win_centrey)

music_img_size: tuple = (
                                   int(win_width/28.8),   # width
                                   int(win_height/17.44), # height
                                   )
return_img_size: tuple = (
                                    int(win_width/48),      # width
                                    int(win_height/29.066), # height
                                    )
info_img_size: tuple = (
                                  int(win_width/57.6),    # width
                                  int(win_height/14.533), # height
                                  )
credits_img_size: tuple = (
                                     int(win_width/20.571),  # width
                                     int(win_height/12.457), # height
                                     )
visual_img_size: tuple = (
                   int(win_width/20.571),  # width
                   int(win_height/12.457), # height
                   )
sound_img_size: tuple = (
                  int(win_width/20.571),  # width
                  int(win_height/12.457), # height
                  )


SETTINGS_DATA: dict = get_data(SETTINGS_DATA_PATH)

# Fonts and global colours

ver_font_div: float = 43.6
norm_font_div: float = 31.8
spacing_div: float = 5.0
return_img_div: float = 5.0
settings_font_div: float = 21.8
title_spacing_div: float = 13

FONT: Font = pygame.font.SysFont(name="Courier", size=int(win_height/norm_font_div), bold=True)
VER_FONT: Font = pygame.font.SysFont(name="Comic-Sans", size=int(win_height/ver_font_div), bold=True)
SETTINGS_FONT: Font = pygame.font.SysFont(name="Courier", size=int(win_height/settings_font_div), bold=True)

WHITE: tuple = (255, 255, 255)
GREY: tuple = (200, 200, 200)
BLACK: tuple = (0, 0, 0)
HOVER_COLOUR: tuple = (187, 211, 255)
PURPLE: tuple = (150, 0, 200)
MENU_GREY: tuple = (130, 130, 130)
DEBUG_HIGHLIGHT_COLOUR = (0, 211, 0)
global_font_colour: tuple = SETTINGS_DATA["global_font_colour"]
global_hover_colour: tuple = SETTINGS_DATA["global_hover_colour"]
global_textbox_active_colour: tuple = SETTINGS_DATA["global_textbox_active_colour"]
global_textbox_inactive_colour: tuple = SETTINGS_DATA["global_textbox_inactive_colour"]

PYGAME_DIGIT: list = [
                      pygame.K_0,
                      pygame.K_1,
                      pygame.K_2, 
                      pygame.K_3,
                      pygame.K_4,
                      pygame.K_5,
                      pygame.K_6,
                      pygame.K_7,
                      pygame.K_8,
                      pygame.K_9,
                      ]

web_version: str = str()
current_version: str = str()
up_to_date: bool = True

screen: int = 0
settings_screen: int = 0

max_fps: int = 240
fps_limit: float = SETTINGS_DATA["fps_limit"]

music_volume: float = SETTINGS_DATA["music_volume"]
click_sfx_volume: float = SETTINGS_DATA["click_sfx_volume"]
previous_volume: float = SETTINGS_DATA["previous_volume"]

music_button_div: float = 17.44

click_sfx = pygame.mixer.Sound(CLICK_SFX_PATH)
click_chanel = pygame.mixer.find_channel()
click_chanel.set_volume(click_sfx_volume)

save_timer_delay: int = 60
updating: bool = False

# Menu(?) stuff

settings_font_colour: tuple = global_font_colour
start_game_font_colour: tuple = global_font_colour
exit_game_font_colour: tuple = global_font_colour
version_update_font_colour: tuple = global_font_colour

settings_box_menu = pygame.Rect
version_box_menu = pygame.Rect
start_box_menu = pygame.Rect
exit_box_menu = pygame.Rect
music_on_box_menu_settings = pygame.Rect
music_off_box_menu_settings = pygame.Rect
update_button_rect = pygame.Rect
info_img_settings_box = pygame.Rect
info_text_settings_box = pygame.Rect
credits_text_settings_box = pygame.Rect
visual_text_settings_box = pygame.Rect
sound_text_settings_box = pygame.Rect
return_text_settings_box = pygame.Rect
settings_bg = pygame.Surface
update_button = pygame.font

class SaveTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

class Button:
    def __init__(self, 
                 x: int,
                 y: int,
                 width: float,
                 height: float,
                 win_y_gap: int,
                 win_x_gap: int,
                 active: bool,
                 text: str,
                 font_colour: tuple[int, int, int] = global_font_colour,
                 ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.col_rect = pygame.Rect(x+win_x_gap, y+win_y_gap, width, height)
        self.active = active
        self.text = text
        self.font_colour = font_colour
        self.text_surface = FONT.render(self.text, True, self.font_colour)
        self.type = CLICKABLE

    def draw_to(self, 
                screen: pygame.Surface,
                ) -> None:
        screen.blit(self.text_surface, (self.rect.x+int(win_width/288), self.rect.y+int(win_height/174.4)))
        return
    
    def debug(self,
              screen: pygame.Surface,
              ) -> None:
        pygame.draw.rect(screen, DEBUG_HIGHLIGHT_COLOUR, self.col_rect, int(win_width/480))
        print("self.x: ", self.x)
        print("self.y: ", self.y)
        print("self.text: ", self.text)
        print("self.rect: ", self.rect)
        print("self.col_rect: ", self.col_rect)
        print("self.type: ", self.type)
        print("self.active: ", self.active)
        print("self.height: ", self.height)
        print("self.width: ", self.width)
        return

class InputBox:
    def __init__(self, 
                 x: int,
                 y: int,
                 width: float,
                 height: float,
                 win_y_gap: int,
                 win_x_gap: int,
                 active: bool,
                 text: str,
                 max_int: int,
                 pre_box_text: str,
                 suff_box_text: str,
                 ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_int = max_int
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.pre_box_text = pre_box_text
        self.suff_box_text = suff_box_text
        self.txt_surface = FONT.render(f'{self.pre_box_text}{self.text}{self.suff_box_text}', True, global_font_colour)
        self.active = active
        self.text_colour = global_font_colour
        self.col_rect = pygame.Rect(x + win_x_gap, 
                                    y + win_y_gap, 
                                    width, 
                                    height,
                                    )
        self.colour = global_textbox_active_colour if self.active else global_textbox_inactive_colour
        self.type = CLICKABLE

    def handle_event(self,
                     event: pygame.event.Event,
                     screen: pygame.Surface,
                     ) -> None:
        mouse_pos = pygame.mouse.get_pos()

        if self.active:
            self.colour = global_textbox_active_colour
        
        else:
            self.colour = global_textbox_inactive_colour

        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3)[0]: # if left clicking
            
            if self.active:
                if not self.col_rect.collidepoint(mouse_pos):
                    self.active = False
                    click_chanel.play(click_sfx)
                
            else:
                if self.col_rect.collidepoint(mouse_pos):
                    self.active = True
                    click_chanel.play(click_sfx)

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE: # remove last digit from the activated box
                self.text = self.text[:-2]

            elif event.key == 13: # keep the data of the activated box upon 'enter' or 'return' keypress
                self.active = False

            elif event.mod == 0: # no key modification (shift, ctrl, alt, opt, cmd, win, e.t.c.)
                self.text += event.unicode

        self.draw_to(screen)
    
    def draw_to(self, 
                screen: pygame.Surface,
                ) -> None:
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+int(win_width/288), self.rect.y+int(win_height/174.4)))
        # Blit the rect.
        pygame.draw.rect(screen, self.colour, self.rect, int(win_width/480)) 
        return

    def debug(self,
              screen: pygame.Surface,
              ) -> None:
        pygame.draw.rect(screen, DEBUG_HIGHLIGHT_COLOUR, self.col_rect, int(win_width/480))
        print("self.x: ", self.x)
        print("self.y: ", self.y)
        print("self.text_colour: ", self.text_colour)
        print("self.text: ", self.text)
        print("self.rect: ", self.rect)
        print("self.col_rect: ", self.col_rect)
        print("self.type: ", self.type)
        print("self.active: ", self.active)
        print("self.pre_box_text: ", self.pre_box_text)
        print("self.suff_box_text: ", self.suff_box_text)
        print("self.txt_surface: ", self.txt_surface)
        print("self.colour: ", self.colour)
        print("self.height: ", self.height)
        print("self.width: ", self.width)
        print("self.max_int: ", self.max_int)
        return

class TitleText:

    def __init__(self,
                 text: str,
                 x: int,
                 y: int,
                 win_x_gap: int,
                 win_y_gap: int,
                 font_colour: tuple,
                 ) -> None:
        self.x = x
        self.y = y
        self.colour = font_colour
        self.text = text
        self.text_surface = FONT.render(self.text, True, self.colour)
        self.rect = self.text_surface.get_rect()
        self.col_rect = pygame.Rect(x+win_x_gap, y+win_y_gap, self.rect.width, self.rect.height)
        self.type = INFORMATION

    def draw_to(self, 
                screen: pygame.Surface,
                ) -> None:
        screen.blit(self.text_surface, (self.x+int(win_width/288), self.y+int(win_height/174.4)))
        return
    
    def debug(self,
              screen: pygame.Surface,
              ) -> None:
        pygame.draw.rect(screen, DEBUG_HIGHLIGHT_COLOUR, self.col_rect, int(win_width/480))
        print("self.x: ", self.x)
        print("self.y: ", self.y)
        print("self.colour: ", self.colour)
        print("self.text: ", self.text)
        print("self.rect: ", self.rect)
        print("self.col_rect: ", self.col_rect)
        print("self.type: ", self.type)
        return


class RGBInputBox(InputBox):

    def __init__(self, 
                 x: int, 
                 y: int, 
                 width: float, 
                 height: float, 
                 win_y_gap: int, 
                 win_x_gap: int, 
                 active: bool, 
                 text: str, 
                 pre_box_text: str = "", 
                 suff_box_text: str = "",
                 ) -> None:
        self.max_int = 255
        super().__init__(x, 
                         y, 
                         width, 
                         height, 
                         win_y_gap, 
                         win_x_gap, 
                         active, 
                         text, 
                         self.max_int, 
                         pre_box_text, 
                         suff_box_text, 
                         )
        return

    def handle_event(self, 
                     event: pygame.event.Event,
                     screen: pygame.Surface,
                     ) -> None:

        mouse_pos = pygame.mouse.get_pos()

        if self.active:
            self.colour = global_textbox_active_colour
        
        else:
            self.colour = global_textbox_inactive_colour

        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3)[0]: # if left clicking
            
            if self.active:
                if not self.col_rect.collidepoint(mouse_pos):
                    self.active = False
                    click_chanel.play(click_sfx)
                
            else:
                if self.col_rect.collidepoint(mouse_pos):
                    self.active = True
                    click_chanel.play(click_sfx)

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE: # remove last digit from the activated box
                self.text = self.text[:-1]

            elif event.key == 13: # keep the data of the activated box upon 'enter' or 'return' keypress
                self.active = False

            elif event.mod == 0:
                if event.key in PYGAME_DIGIT and len(self.text) < 3: # if the key is a digit AND if the total length of the text is digits 2 or less
                    try:
                        if int(self.text + event.unicode) <= self.max_int: # text value cannot be more than 255
                            self.text += event.unicode # add the digit to the current text
                    except ValueError: # self.text == ''
                        self.text += event.unicode # add the digit to the current text

        self.draw_to(screen)
        return

class NumberInputBox(InputBox):

    def __init__(self, 
                 x: int, 
                 y: int, 
                 width: float, 
                 height: float, 
                 win_y_gap: int, 
                 win_x_gap: int,
                 active: bool, 
                 text: str, 
                 max_int: int,
                 pre_box_text: str = "",
                 suff_box_text: str = "",
                 ) -> None:
        super().__init__(x=x, 
                         y=y, 
                         width=width, 
                         height=height, 
                         win_x_gap=win_x_gap, 
                         win_y_gap=win_y_gap, 
                         active=active, 
                         text=text, 
                         max_int=max_int, 
                         pre_box_text=pre_box_text, 
                         suff_box_text=suff_box_text,
                         )
        self.max_int = max_int
        self.type = CLICKABLE
        return
    
    def handle_event(self, 
                     event: pygame.event.Event,
                     screen: pygame.Surface,
                     ) -> None:

        mouse_pos = pygame.mouse.get_pos()

        if self.active:
            self.colour = global_textbox_active_colour
        
        else:
            self.colour = global_textbox_inactive_colour

        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3)[0]: # if left clicking
            
            if self.active: # if the box is active
                if not self.col_rect.collidepoint(mouse_pos): # if not clicking on the box
                    self.active = False
                    click_chanel.play(click_sfx)
                
            else:
                if self.col_rect.collidepoint(mouse_pos): # if clicking on the box
                    self.active = True
                    click_chanel.play(click_sfx)

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE: # remove last digit from the activated box
                self.text = self.text[:-1]

            elif event.key == 13: # keep the data of the activated box upon 'enter' or 'return' keypress
                self.active = False

            elif event.mod == 0:
                if event.key in PYGAME_DIGIT and len(self.text) <3: # if the key is a digit AND if the total length of the text is digits 2 or less
                    try:
                        if int(self.text + event.unicode) <= self.max_int: # text value cannot be more than 100
                            self.text += event.unicode # add the digit to the current text
                    except ValueError: # self.text == ''
                        self.text += event.unicode # add the digit to the current text

        self.draw_to(screen)
        return


# Settings stuff

info_text_font_colour: tuple = global_font_colour
credits_font_colour: tuple = global_font_colour
visuals_font_colour: tuple = global_font_colour
sound_font_colour: tuple = global_font_colour
return_font_colour: tuple = global_font_colour
RGB_TEXT_BOX_OFFSET_DIV: int = 96

return_img_box = pygame.Rect

settings_objects: dict = {
                          "font_colour_input_box_R": RGBInputBox(1, 1, 1, 1, 1, 1, False, str(global_font_colour[0]), 'R:'),
                          "font_colour_input_box_G": RGBInputBox(1, 1, 1, 1, 1, 1, False, str(global_font_colour[1]), 'G:'),
                          "font_colour_input_box_B": RGBInputBox(1, 1, 1, 1, 1, 1, False, str(global_font_colour[2]), 'B:'),
                          "font_colour_text": TitleText("", 1, 1, 1, 1, global_font_colour),

                          "hover_colour_input_box_R": RGBInputBox(1, 1, 1, 1, 1, 1, False, str(global_hover_colour[0]), 'R:'),
                          "hover_colour_input_box_G": RGBInputBox(1, 1, 1, 1, 1, 1, False, str(global_hover_colour[1]), 'G:'),
                          "hover_colour_input_box_B": RGBInputBox(1, 1, 1, 1, 1, 1, False, str(global_hover_colour[2]), 'B:'),
                          "hover_colour_text": TitleText("", 1, 1, 1, 1, global_font_colour),

                          "textbox_active_colour_input_box_R": RGBInputBox(1, 1, 1, 1, 1, 1, False, str(global_textbox_active_colour[0]), 'R:'),
                          "textbox_active_colour_input_box_G": RGBInputBox(1, 1, 1, 1, 1, 1, False, str(global_textbox_active_colour[1]), 'G:'),
                          "textbox_active_colour_input_box_B": RGBInputBox(1, 1, 1, 1, 1, 1, False, str(global_textbox_active_colour[2]), 'B:'),
                          "textbox_active_colour_text": TitleText("", 1, 1, 1, 1, global_font_colour),

                          "textbox_inactive_colour_input_box_R": RGBInputBox(1, 1, 1, 1, 1, 1, False, str(global_textbox_inactive_colour[0]), 'R:'),
                          "textbox_inactive_colour_input_box_G": RGBInputBox(1, 1, 1, 1, 1, 1, False, str(global_textbox_inactive_colour[1]), 'G:'),
                          "textbox_inactive_colour_input_box_B": RGBInputBox(1, 1, 1, 1, 1, 1, False, str(global_textbox_inactive_colour[2]), 'B:'),
                          "textbox_inactive_colour_text": TitleText("", 1, 1, 1, 1, global_font_colour),

                          "fps_limit_input_box": NumberInputBox(1, 1, 1, 1, 1, 1, False, str(fps_limit), max_fps),
                          "fps_limit_text": TitleText("", 1, 1, 1, 1, global_font_colour),

                          "music_volume_input_box": NumberInputBox(1, 1, 1, 1, 1, 1, False, str(int(music_volume*100)), 100, suff_box_text="%"),
                          "music_volume_text": TitleText("", 1, 1, 1, 1, global_font_colour),

                          "click_sfx_volume_input_box": NumberInputBox(1, 1, 1, 1, 1, 1, False, str(int(click_sfx_volume*100)), 100, suff_box_text="%"),
                          "click_sfx_volume_text": TitleText("", 1, 1, 1, 1, global_font_colour),
                          }


def save_timer() -> None:
    save_data(data=SETTINGS_DATA, path=SETTINGS_DATA_PATH)
    return


def get_local_version() -> str:
    """
    Gets the current local game version.

    :return str: A string containing version information.
    """

    with open(VERSION_PATH, 'r') as version:
        local_version = version.read()

    return local_version


def get_web_version() -> str:
    """
    Gets the current website game version.

    :return str: A string containing version information.
    """

    try:
        version = requests.get(url=VERSION_URL)
        version = str(version.content).removeprefix("b'").removesuffix("\\n'")

    except:
        version = ""

    return version


def check_update() -> bool:
    """
    Check for a new game version.

    :return bool: True if the server could not be accessed or the current version is the most up to date version and False if the version is not up to date.
    """
    
    if web_version == current_version or web_version == "":
        return True

    return False


def clear_screen() -> None:
    """
    Clear the screen of all visuals.
    """

    WINDOW.fill(BLACK)

    return


def main_menu() -> None:
    """
    Dislpays the main menu.
    """

    global screen, version_box_menu, start_box_menu, settings_box_menu, \
           exit_box_menu, music_volume, music_off_box_menu_settings, music_on_box_menu_settings, \
           update_button_rect, update_button, version_update_font_colour, \
           settings_font_colour, exit_game_font_colour, start_game_font_colour
    
    if screen != 1:
        clear_screen()

    if screen != 1 and screen != 2 and screen != 3:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(MAIN_MENU_MUSIC_PATH)
        pygame.mixer.music.play(loops=-1)

    screen = 1

    pygame.mixer.music.set_volume(music_volume)

    WINDOW.fill('black')

    bg = pygame.image.load(MENU_BG_PATH)
    bg = pygame.transform.scale(bg, (WINDOW.get_width(), WINDOW.get_height()))
    WINDOW.blit(bg, (0, 0))

    version_text = VER_FONT.render(f"{current_version}", True, global_font_colour)
    new_update = VER_FONT.render(f"A new update is available -> {web_version}", True, global_font_colour) 
    update_button = VER_FONT.render(f"Update Now", True, version_update_font_colour) # upon pressing "update now", do a get request for the updated files on git
    update_button_rect = update_button.get_rect()
    version_box_menu = pygame.Rect(int(win_width/72),          # Xpos
                                   int(win_height/9.2588),     # Ypos
                                   update_button_rect.width,   # width
                                   update_button_rect.height,  # height
                                   )

    start_text = SETTINGS_FONT.render("Enter the VAB", True, start_game_font_colour)
    start_text_rect = start_text.get_rect()
    start_box_menu = pygame.Rect(win_centrex-int(start_text_rect.width/2), # Xpos
                                 win_centrey-int(win_height/spacing_div),  # Ypos
                                 start_text_rect.width,                    # width
                                 start_text_rect.height,                   # height
                                 )

    settings_text = SETTINGS_FONT.render("Settings", True, settings_font_colour)
    settings_text_rect = settings_text.get_rect()
    settings_box_menu = pygame.Rect(win_centrex-int(settings_text_rect.width/2), # Xpos
                                    win_centrey,                                 # Ypos
                                    settings_text_rect.width,                    # width
                                    settings_text_rect.height,                   # height
                                    )

    exit_game = SETTINGS_FONT.render("Exit Game", True, exit_game_font_colour)
    exit_game_rect = exit_game.get_rect()
    exit_box_menu = pygame.Rect(win_centrex-int(exit_game_rect.width/2), # Xpos
                                win_centrey+int(win_height/spacing_div), # Ypos
                                exit_game_rect.width,                    # width
                                exit_game_rect.height,                   # height
                                )
    
    music_on_img = pygame.image.load(MUSIC_ON_PATH)
    music_on_img = pygame.transform.smoothscale(music_on_img, 
                                          music_img_size,
                                          )
    music_on_rect = music_on_img.get_rect()
    music_on_box_menu_settings = pygame.Rect(int(win_width-win_width/music_button_div), # Xpos
                                    int(win_height/music_button_div),          # Ypos
                                    music_on_rect.width,                       # width
                                    music_on_rect.height,                      # width
                                    )
    
    music_off_img = pygame.image.load(MUSIC_OFF_PATH)
    music_off_img = pygame.transform.smoothscale(music_off_img, 
                                           music_img_size,
                                           )
    music_off_rect = music_off_img.get_rect()
    music_off_box_menu_settings = pygame.Rect(int(win_width-win_width/music_button_div), # Xpos
                                     int(win_height/music_button_div),          # Ypos
                                     music_off_rect.width,                      # width
                                     music_off_rect.height,                     # width
                                     )

    if pygame.mixer.music.get_busy():
        WINDOW.blit(music_on_img,
                    (
                        int(win_width-win_width/music_button_div), # Xpos
                        int(win_height/music_button_div),          # Ypos
                    ),
                    )
    else:
        WINDOW.blit(music_off_img,
                    (
                        int(win_width-win_width/music_button_div), # Xpos
                        int(win_height/music_button_div),          # Ypos
                    ),
                    )

    WINDOW.blit(version_text, 
                (
                    int(win_width/72),    # Xpos
                    int(win_height/43.6), # Ypos
                ),
                )
    WINDOW.blit(start_text, 
                (
                    win_centrex-int(start_text_rect.width/2), # Xpos
                    win_centrey-int(win_height/spacing_div),  # Ypos
                ),
                )
    WINDOW.blit(settings_text, 
                (
                    win_centrex-int(settings_text_rect.width/2), # Xpos
                    win_centrey,                                 # Ypos
                ),
                )
    WINDOW.blit(exit_game, 
                ( 
                    win_centrex-int(exit_game_rect.width/2), # Xpos
                    win_centrey+int(win_height/spacing_div), # Ypos
                ),
                )

    if not up_to_date:
        WINDOW.blit(new_update, 
                    (
                        int(win_width/72),  # Xpos
                        int(win_height/16), # Ypos 
                    ),
                    )
        WINDOW.blit(update_button, 
                    (
                        version_box_menu.x, # Xpos
                        version_box_menu.y, # Ypos
                    ),
                    )

    return


def settings() -> None: 
    """
    Displays the settings page.
    """
    global screen, music_volume, music_off_box_menu_settings, music_on_box_menu_settings, \
           update_button_rect, update_button, version_update_font_colour, \
           return_img_box, info_img_settings_box, info_text_settings_box, info_img_tint_colour, \
           info_text_font_colour, settings_bg, credits_text_settings_box, credits_font_colour, \
           settings_screen, visual_text_settings_box, sound_font_colour, visuals_font_colour, \
           sound_text_settings_box, return_text_settings_box, return_font_colour, \
           global_textbox_inactive_colour, global_textbox_active_colour, settings_objects, \
           title_spacing_div, global_font_colour, global_hover_colour, fps_limit, click_sfx_volume

    if screen != 2 and settings_screen != 0:
        clear_screen()

    if screen != 1 and screen != 2 and screen != 3:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(MAIN_MENU_MUSIC_PATH)
        pygame.mixer.music.play(loops=-1)

    screen = 2

    pygame.mixer.music.set_volume(music_volume)

    bg = pygame.image.load(MENU_BG_PATH)
    bg = pygame.transform.scale(bg, (WINDOW.get_width(), WINDOW.get_height()))
    WINDOW.blit(bg, (0, 0))


    # Music mute button

    music_on_img = pygame.image.load(MUSIC_ON_PATH)
    music_on_img = pygame.transform.smoothscale(music_on_img, 
                                          music_img_size,
                                          )
    music_on_rect = music_on_img.get_rect()
    music_on_box_menu_settings = pygame.Rect(int(win_width-win_width/music_button_div), # Xpos
                                    int(win_height/music_button_div),          # Ypos
                                    music_on_rect.width,                       # width
                                    music_on_rect.height,                      # width
                                    )
    
    music_off_img = pygame.image.load(MUSIC_OFF_PATH)
    music_off_img = pygame.transform.smoothscale(music_off_img, 
                                           music_img_size,
                                           )
    music_off_rect = music_off_img.get_rect()
    music_off_box_menu_settings = pygame.Rect(int(win_width-win_width/music_button_div), # Xpos
                                     int(win_height/music_button_div),          # Ypos
                                     music_off_rect.width,                      # width
                                     music_off_rect.height,                     # width
                                     )

    if pygame.mixer.music.get_busy():
        WINDOW.blit(music_on_img,
                    (
                        int(win_width-win_width/music_button_div), # Xpos
                        int(win_height/music_button_div),          # Ypos
                    ),
                    )
    else:
        WINDOW.blit(music_off_img,
                    (
                        int(win_width-win_width/music_button_div), # Xpos
                        int(win_height/music_button_div),          # Ypos
                    ),
                    )


    # Version data + button

    version_text = VER_FONT.render(f"{current_version}", True, global_font_colour)
    new_update = VER_FONT.render(f"A new update is available -> {web_version}", True, global_font_colour) 
    update_button = VER_FONT.render(f"Update Now", True, version_update_font_colour)
    update_button_rect = update_button.get_rect()
    version_box_menu_settings = pygame.Rect(int(win_width/72), # Xpos
                                   int(win_height/9.2588),     # Ypos
                                   update_button_rect.width,   # width
                                   update_button_rect.height,  # height
                                   )

    WINDOW.blit(version_text, 
                (
                    int(win_width/72),    # Xpos
                    int(win_height/43.6), # Ypos
                ),
                )
    
    if not up_to_date:
        WINDOW.blit(new_update, 
                    (
                        int(win_width/72),  # Xpos
                        int(win_height/16), # Ypos 
                    ),
                    )
        WINDOW.blit(update_button, 
                    (
                        version_box_menu_settings.x, # Xpos
                        version_box_menu_settings.y, # Ypos
                    ),
                    )


    # Backdrop for settings buttons

    settings_bg = pygame.Surface(
                        (
                            win_centrex + win_centrex/2, # Horizontal size 
                            win_centrey + win_centrey/4, # Vertical size 
                        ),
                        )
    
    settings_bg.fill(MENU_GREY)

    settings_bg_rect = settings_bg.get_rect()
    settings_bg_rect = pygame.Rect(int(win_centrex-settings_bg.get_width()/2),    # Xpos
                                   int(win_centrey-settings_bg.get_height()/2.5), # Ypos
                                   settings_bg_rect.width,                        # width
                                   settings_bg_rect.height,                       # height
                                   )
    
    settings_bg_width = settings_bg_rect.width
    settings_bg_height = settings_bg_rect.height
    win_x_gap = int(win_centrex-settings_bg.get_width()/2)
    win_y_gap = int(win_centrey-settings_bg.get_height()/2.5)


    # Return button (menu)

    return_text = SETTINGS_FONT.render("RETURN", True, return_font_colour)
    return_text_rect = return_text.get_rect()
    return_text_pos: tuple[int, int] = (
                                        int(settings_bg_width-settings_bg_width/27)-return_text_rect.width, # Xpos
                                        int(settings_bg_height/109),                                        # Ypos
                                        )
    return_text_settings_box = pygame.Rect(return_text_pos[0]+win_x_gap, # Xpos
                                          return_text_pos[1]+win_y_gap,  # Ypos
                                          return_text_rect.width,        # width
                                          return_text_rect.height,       # height
                                          )
    settings_bg.blit(
                     return_text,
                     (
                         return_text_pos[0], # Xpos
                         return_text_pos[1], # Ypos
                     )
                     )

    return_img = pygame.image.load(RETURN_PATH)
    return_img = pygame.transform.smoothscale(return_img, 
                                            return_img_size,
                                            )
    return_img_rect = return_img.get_rect()
    return_img_pos: tuple[int, int] = (
                                      int(return_text_pos[0]-return_text_rect.width/2.5),     # Xpos
                                      int(settings_bg_height/109+return_text_rect.height/10), # Ypos
                                      )
    return_img_box = pygame.Rect(
                                 return_img_pos[0]+win_x_gap, # Xpos
                                 return_img_pos[1]+win_y_gap, # Ypos
                                 return_img_rect.width,       # width
                                 return_img_rect.height,      # height
                                )
    settings_bg.blit(return_img,
                (
                    return_img_pos[0], # Xpos
                    return_img_pos[1], # Ypos
                ),
                )

    base_box_pos = (
                    int(settings_bg_width/10),   # Xpos
                    int(settings_bg_height/5.7), # Ypos
                    )
    title_x_offset = int(base_box_pos[0]/1.5)
    title_y_offset = int(win_height/title_spacing_div)
    box_offset = win_width/RGB_TEXT_BOX_OFFSET_DIV
    title_box_y_offset = int(settings_bg_height/title_spacing_div)
    box_width: float = win_width/14.4
    box_height = win_height/norm_font_div + 10
    
    if settings_screen == 0: # Main settings area
        # Sound settings

        sound_text = SETTINGS_FONT.render("SOUND", True, sound_font_colour)
        sound_text_rect = sound_text.get_rect()
        sound_text_pos = (
                           int(settings_bg_width-settings_bg_width/3.5), # Xpos
                           int(settings_bg_height/4),                  # Ypos
                           )
        sound_text_settings_box = pygame.Rect(
                                               sound_text_pos[0]+win_x_gap, # Xpos
                                               sound_text_pos[1]+win_y_gap, # Ypos
                                               sound_text_rect.width,       # width
                                               sound_text_rect.height,      # height
                                               )
        settings_bg.blit(
                         sound_text,
                         (
                             sound_text_pos[0], # Xpos
                             sound_text_pos[1], # Ypos
                         ),
                         )

        sound_img = pygame.transform.smoothscale(pygame.image.load(VOLUME_PATH), sound_img_size)
        sound_img_rect = sound_img.get_rect()
        sound_img_pos = (
                          int(sound_text_pos[0]-1.5*sound_img_rect.width),  # Xpos
                          int(sound_text_pos[1]-sound_img_rect.height/3.5), # Ypos
                          )
        settings_bg.blit(
                         sound_img,
                         (
                             sound_img_pos[0], # Xpos
                             sound_img_pos[1], # Ypos
                         ),
                         )


        # Visual settings

        visual_text = SETTINGS_FONT.render("VISUALS", True, visuals_font_colour)
        visual_text_rect = visual_text.get_rect()
        visual_text_pos = (
                           int(settings_bg_width/6),  # Xpos
                           int(settings_bg_height/4), # Ypos
                           )
        visual_text_settings_box = pygame.Rect(
                                               visual_text_pos[0]+win_x_gap, # Xpos
                                               visual_text_pos[1]+win_y_gap, # Ypos
                                               visual_text_rect.width,       # width
                                               visual_text_rect.height,      # height
                                               )
        settings_bg.blit(
                         visual_text,
                         (
                             visual_text_pos[0], # Xpos
                             visual_text_pos[1], # Ypos
                         ),
                         )

        visual_img = pygame.transform.smoothscale(pygame.image.load(VISUALS_PATH), visual_img_size)
        visual_img_rect = visual_img.get_rect()
        visual_img_pos = (
                          int(visual_text_pos[0]-visual_text_rect.width/2),   # Xpos
                          int(visual_text_pos[1]-visual_img_rect.height/3.5), # Ypos
                          )
        settings_bg.blit(
                         visual_img,
                         (
                             visual_img_pos[0], # Xpos
                             visual_img_pos[1], # Ypos
                         ),
                         )


        # General info + socials (dicsord server join code)
        
        info_text = SETTINGS_FONT.render("INFO", True, info_text_font_colour)
        info_text_rect = info_text.get_rect()
        info_text_pos = (
                        int(settings_bg_width/6),                       # Xpos
                        int(settings_bg_height-settings_bg_height/3.5), # Ypos
                        )
        info_text_settings_box = pygame.Rect(info_text_pos[0]+win_x_gap, # Xpos
                                            info_text_pos[1]+win_y_gap,  # Ypos
                                            info_text_rect.width,        # width
                                            info_text_rect.height,       # height
                                            )
        settings_bg.blit(info_text,
                        (
                        info_text_pos[0], # Xpos
                        info_text_pos[1], # Ypos
                        ),
                        )

        info_img = pygame.image.load(INFO_PATH)
        info_img = pygame.transform.smoothscale(info_img, 
                                                info_img_size,
                                                )
        info_img_rect = info_img.get_rect()
        info_img_pos = (int(info_text_pos[0]-(info_text_rect.width/2)), # Xpos
                        int(info_text_pos[1]-(info_img_rect.height/3.5)), # Ypos
                        )
        info_img_settings_box = pygame.Rect(info_img_pos[0]+win_x_gap, # Xpos
                                            info_img_pos[1]+win_y_gap, # Ypos
                                            info_img_rect.width,       # width
                                            info_img_rect.height,      # height
                                            )
        
        settings_bg.blit(info_img,
                        (
                        info_img_pos[0], # Xpos
                        info_img_pos[1], # Ypos
                        ),
                        )


        # Credits
        
        credits_text = SETTINGS_FONT.render("CREDITS", True, credits_font_colour)
        credits_text_rect = credits_text.get_rect()
        credits_text_pos = (int(settings_bg_width-settings_bg_width/3.5),   # Xpos
                            int(settings_bg_height-settings_bg_height/3.5), # Ypos
                            )
        credits_text_settings_box = pygame.Rect(credits_text_pos[0] + win_x_gap, # Xpos
                                                credits_text_pos[1] + win_y_gap, # Ypos
                                                credits_text_rect.width,         # width
                                                credits_text_rect.height,        # height
                                                )
        settings_bg.blit(credits_text,       # Surface
                        (
                        credits_text_pos[0], # Xpos
                        credits_text_pos[1], # Ypos
                        ),
                        )

        credits_img = pygame.transform.smoothscale(pygame.image.load(CREDITS_PATH), credits_img_size)
        credits_img_rect = credits_img.get_rect()
        credits_img_pos = (
                        int(credits_text_pos[0] - (credits_text_rect.width/1.5)), # Xpos
                        int(credits_text_pos[1] - (credits_img_rect.height/3.5)), # Ypos
                        )
        settings_bg.blit(credits_img,       # Surface
                        (
                        credits_img_pos[0], # Xpos
                        credits_img_pos[1], # Ypos
                        ),
                        )

    elif settings_screen == 1: # Credits
        # Menu music credits
        menu_music_credit_text = FONT.render('Menu music by "Ivymusic" on pixabay.com', True, global_font_colour)
        menu_music_credit_text_pos = (
                                      int(settings_bg_width/10), # Xpos
                                      int(settings_bg_height/6), # Ypos
                                      )
        settings_bg.blit(
                         menu_music_credit_text,
                         (
                             menu_music_credit_text_pos[0], # Xpos
                             menu_music_credit_text_pos[1], # Ypos
                         ),
                         )

        # Click sfx credits
        click_sfx_credit_text = FONT.render('Click sfx by "MatthewVakaliuk73627" on pixabay.com', True, global_font_colour)
        click_sfx_credit_text_pos = (
                                     int(menu_music_credit_text_pos[0]),   # Xpos
                                     int(2*menu_music_credit_text_pos[1]), # Ypos
                                     )
        settings_bg.blit(
                         click_sfx_credit_text,
                         click_sfx_credit_text_pos,
                         )

    elif settings_screen == 2: # General info + socials
        discord_link_text = FONT.render("Official Discord: 'discord.gg/JymnDDbK9c'", True, global_font_colour)
        discord_link_text_pos = (
                                 int(settings_bg_height/10), # Xpos
                                 int(settings_bg_height/6),  # Ypos
                                 )
        settings_bg.blit(discord_link_text, discord_link_text_pos)
    
    elif settings_screen == 3: # Visual settings - e.g. fps, text colour, hover colour

        if True: # global font colour
        
            font_colour_input_box_R = settings_objects["font_colour_input_box_R"]
            font_colour_input_box_G = settings_objects["font_colour_input_box_G"]
            font_colour_input_box_B = settings_objects["font_colour_input_box_B"]
            font_colour_text = settings_objects["font_colour_text"]

            font_colour_text = TitleText(text="Text colour:",
                                        font_colour=global_font_colour,
                                        win_x_gap=win_x_gap,
                                        win_y_gap=win_y_gap,
                                        x=base_box_pos[0]-title_x_offset,
                                        y=base_box_pos[1]-int(0.5*title_y_offset),
                                        )

            font_colour_input_box_R = RGBInputBox(base_box_pos[0],                                                   # Xpos
                                                  font_colour_text.y+title_box_y_offset,                             # Ypos
                                                  win_width/14.4,                                                    # width
                                                  win_height/norm_font_div + 10,                                     # height (font height)
                                                  win_y_gap,                                                         # settings bg win gap
                                                  win_x_gap,                                                         # settings bg win gap
                                                  active=False if font_colour_input_box_R.active == False else True, # Active or not
                                                  text=font_colour_input_box_R.text,                                 # Text
                                                  pre_box_text=font_colour_input_box_R.pre_box_text,                 # Colour value change
                                                  suff_box_text=font_colour_input_box_R.suff_box_text,               # Colour value change
                                                  )
            font_colour_input_box_G = RGBInputBox(x=int(font_colour_input_box_R.rect.x + font_colour_input_box_R.rect.width + box_offset),
                                                  y=int(font_colour_input_box_R.rect.y),
                                                  width=win_width/14.4,
                                                  height=win_height/norm_font_div + 10,
                                                  win_x_gap=win_x_gap,
                                                  win_y_gap=win_y_gap,
                                                  active=False if font_colour_input_box_G.active == False else True,
                                                  text=font_colour_input_box_G.text,
                                                  pre_box_text=font_colour_input_box_G.pre_box_text,
                                                  )
            font_colour_input_box_B = RGBInputBox(x=int(font_colour_input_box_G.rect.x + font_colour_input_box_G.rect.width + box_offset),
                                                  y=int(font_colour_input_box_R.rect.y),
                                                  width=win_width/14.4,
                                                  height=win_height/norm_font_div + 10,
                                                  win_x_gap=win_x_gap,
                                                  win_y_gap=win_y_gap,
                                                  active=False if font_colour_input_box_B.active == False else True,
                                                  text=font_colour_input_box_B.text,
                                                  pre_box_text=font_colour_input_box_B.pre_box_text,
                                                  )

            settings_objects["font_colour_input_box_R"] = font_colour_input_box_R
            settings_objects["font_colour_input_box_G"] = font_colour_input_box_G
            settings_objects["font_colour_input_box_B"] = font_colour_input_box_B
            settings_objects["font_colour_text"] = font_colour_text
            
            font_colour_input_box_R.draw_to(settings_bg)
            font_colour_input_box_G.draw_to(settings_bg)
            font_colour_input_box_B.draw_to(settings_bg)
            font_colour_text.draw_to(settings_bg)

            if font_colour_input_box_R.text == '':
                font_colour_input_box_R.pre_box_text = 'R:0'
            else:
                font_colour_input_box_R.pre_box_text = 'R:'

            if font_colour_input_box_G.text == '':
                font_colour_input_box_G.pre_box_text = 'G:0'
            else:
                font_colour_input_box_G.pre_box_text = 'G:'

            if font_colour_input_box_B.text == '':
                font_colour_input_box_B.pre_box_text = 'B:0'
            else:
                font_colour_input_box_B.pre_box_text = 'B:'

            global_font_colour = (
                                int(font_colour_input_box_R.text) if font_colour_input_box_R.text != '' else 0,
                                int(font_colour_input_box_G.text) if font_colour_input_box_G.text != '' else 0,
                                int(font_colour_input_box_B.text) if font_colour_input_box_B.text != '' else 0,
                                )

            SETTINGS_DATA["global_font_colour"] = [value for value in global_font_colour]


        if True: # global hover colour
        
            hover_colour_input_box_R = settings_objects["hover_colour_input_box_R"]
            hover_colour_input_box_G = settings_objects["hover_colour_input_box_G"]
            hover_colour_input_box_B = settings_objects["hover_colour_input_box_B"]
            hover_colour_text = settings_objects["hover_colour_text"]

            hover_colour_text = TitleText(text="Text hover colour:",
                                          font_colour=global_hover_colour,
                                          win_x_gap=win_x_gap,
                                          win_y_gap=win_y_gap,
                                          x=font_colour_text.x,
                                          y=font_colour_input_box_R.y+title_y_offset,
                                          )

            hover_colour_input_box_R = RGBInputBox(x=base_box_pos[0],
                                                   y=hover_colour_text.y+title_box_y_offset,
                                                   width=box_width,
                                                   height=box_height,
                                                   win_x_gap=win_x_gap,
                                                   win_y_gap=win_y_gap,
                                                   active=hover_colour_input_box_R.active,
                                                   text=hover_colour_input_box_R.text,
                                                   pre_box_text=hover_colour_input_box_R.pre_box_text,
                                                   )
            hover_colour_input_box_G = RGBInputBox(x=font_colour_input_box_G.x,
                                                y=hover_colour_input_box_R.y,
                                                width=win_width/14.4,
                                                height=win_height/norm_font_div + 10,
                                                win_x_gap=win_x_gap,
                                                win_y_gap=win_y_gap,
                                                active=hover_colour_input_box_G.active,
                                                text=hover_colour_input_box_G.text,
                                                pre_box_text=hover_colour_input_box_G.pre_box_text,
                                                )
            hover_colour_input_box_B = RGBInputBox(x=font_colour_input_box_B.x,
                                                y=hover_colour_input_box_R.y,
                                                width=win_width/14.4,
                                                height=win_height/norm_font_div + 10,
                                                win_x_gap=win_x_gap,
                                                win_y_gap=win_y_gap,
                                                active=hover_colour_input_box_B.active,
                                                text=hover_colour_input_box_B.text,
                                                pre_box_text=hover_colour_input_box_B.pre_box_text,
                                                )

            hover_colour_input_box_R.draw_to(settings_bg)
            hover_colour_input_box_G.draw_to(settings_bg)
            hover_colour_input_box_B.draw_to(settings_bg)
            hover_colour_text.draw_to(settings_bg)

            settings_objects["hover_colour_input_box_R"] = hover_colour_input_box_R
            settings_objects["hover_colour_input_box_G"] = hover_colour_input_box_G
            settings_objects["hover_colour_input_box_B"] = hover_colour_input_box_B
            settings_objects["hover_colour_text"] = hover_colour_text

            if hover_colour_input_box_R.text == '':
                hover_colour_input_box_R.pre_box_text = 'R:0'
            else:
                hover_colour_input_box_R.pre_box_text = 'R:'

            if hover_colour_input_box_G.text == '':
                hover_colour_input_box_G.pre_box_text = 'G:0'
            else:
                hover_colour_input_box_G.pre_box_text = 'G:'

            if hover_colour_input_box_B.text == '':
                hover_colour_input_box_B.pre_box_text = 'B:0'
            else:
                hover_colour_input_box_B.pre_box_text = 'B:'

            global_hover_colour = (
                              int(hover_colour_input_box_R.text) if hover_colour_input_box_R.text != '' else 0,
                              int(hover_colour_input_box_G.text) if hover_colour_input_box_G.text != '' else 0,
                              int(hover_colour_input_box_B.text) if hover_colour_input_box_B.text != '' else 0,
                              )

            SETTINGS_DATA["global_hover_colour"] = [value for value in global_hover_colour]


        if True: # textbox bg active colour (clicked on and typing in)
        
            textbox_active_colour_input_box_R = settings_objects["textbox_active_colour_input_box_R"]
            textbox_active_colour_input_box_G = settings_objects["textbox_active_colour_input_box_G"]
            textbox_active_colour_input_box_B = settings_objects["textbox_active_colour_input_box_B"]
            textbox_active_colour_text = settings_objects["textbox_active_colour_text"]

            textbox_active_colour_text = TitleText(text="Border colour (active):",
                                                font_colour=global_textbox_active_colour,
                                                win_x_gap=win_x_gap,
                                                win_y_gap=win_y_gap,
                                                x=hover_colour_text.x,
                                                y=hover_colour_input_box_R.y+title_y_offset,
                                                )

            textbox_active_colour_input_box_R = RGBInputBox(x=base_box_pos[0],
                                                            y=textbox_active_colour_text.y+title_box_y_offset,
                                                            width=win_width/14.4,
                                                            height=win_height/norm_font_div + 10,
                                                            win_x_gap=win_x_gap,
                                                            win_y_gap=win_y_gap,
                                                            active=textbox_active_colour_input_box_R.active,
                                                            text=textbox_active_colour_input_box_R.text,
                                                            pre_box_text=textbox_active_colour_input_box_R.pre_box_text,
                                                            )
            textbox_active_colour_input_box_G = RGBInputBox(x=hover_colour_input_box_G.x,
                                                            y=textbox_active_colour_input_box_R.y,
                                                            width=win_width/14.4,
                                                            height=win_height/norm_font_div + 10,
                                                            win_x_gap=win_x_gap,
                                                            win_y_gap=win_y_gap,
                                                            active=textbox_active_colour_input_box_G.active,
                                                            text=textbox_active_colour_input_box_G.text,
                                                            pre_box_text=textbox_active_colour_input_box_G.pre_box_text,
                                                            )
            textbox_active_colour_input_box_B = RGBInputBox(x=hover_colour_input_box_B.x,
                                                            y=textbox_active_colour_input_box_R.y,
                                                            width=win_width/14.4,
                                                            height=win_height/norm_font_div + 10,
                                                            win_x_gap=win_x_gap,
                                                            win_y_gap=win_y_gap,
                                                            active=textbox_active_colour_input_box_B.active,
                                                            text=textbox_active_colour_input_box_B.text,
                                                            pre_box_text=textbox_active_colour_input_box_B.pre_box_text,
                                                            )

            textbox_active_colour_input_box_R.draw_to(settings_bg)
            textbox_active_colour_input_box_G.draw_to(settings_bg)
            textbox_active_colour_input_box_B.draw_to(settings_bg)
            textbox_active_colour_text.draw_to(settings_bg)

            settings_objects["textbox_active_colour_input_box_R"] = textbox_active_colour_input_box_R
            settings_objects["textbox_active_colour_input_box_G"] = textbox_active_colour_input_box_G
            settings_objects["textbox_active_colour_input_box_B"] = textbox_active_colour_input_box_B
            settings_objects["textbox_active_colour_text"] = textbox_active_colour_text

            if textbox_active_colour_input_box_R.text == '':
                textbox_active_colour_input_box_R.pre_box_text = 'R:0'
            else:
                textbox_active_colour_input_box_R.pre_box_text = 'R:'

            if textbox_active_colour_input_box_G.text == '':
                textbox_active_colour_input_box_G.pre_box_text = 'G:0'
            else:
                textbox_active_colour_input_box_G.pre_box_text = 'G:'

            if textbox_active_colour_input_box_B.text == '':
                textbox_active_colour_input_box_B.pre_box_text = 'B:0'
            else:
                textbox_active_colour_input_box_B.pre_box_text = 'B:'

            global_textbox_active_colour = (
                                        int(textbox_active_colour_input_box_R.text) if textbox_active_colour_input_box_R.text != '' else 0,
                                        int(textbox_active_colour_input_box_G.text) if textbox_active_colour_input_box_G.text != '' else 0,
                                        int(textbox_active_colour_input_box_B.text) if textbox_active_colour_input_box_B.text != '' else 0,
                                        )

            SETTINGS_DATA["global_textbox_active_colour"] = [value for value in global_textbox_active_colour]


        if True: # textbox bg inactive colour (not clicked on or typable)
        
            textbox_inactive_colour_input_box_R = settings_objects["textbox_inactive_colour_input_box_R"]
            textbox_inactive_colour_input_box_G = settings_objects["textbox_inactive_colour_input_box_G"]
            textbox_inactive_colour_input_box_B = settings_objects["textbox_inactive_colour_input_box_B"]
            textbox_inactive_colour_text = settings_objects["textbox_inactive_colour_text"]

            textbox_inactive_colour_text = TitleText(text="Border colour (inactive):",
                                                    font_colour=global_textbox_inactive_colour,
                                                    win_x_gap=win_x_gap,
                                                    win_y_gap=win_y_gap,
                                                    x=hover_colour_text.x,
                                                    y=textbox_active_colour_input_box_R.y+title_y_offset,
                                                    )
            textbox_inactive_colour_input_box_R = RGBInputBox(x=base_box_pos[0],
                                                            y=textbox_inactive_colour_text.y+title_box_y_offset,
                                                            width=win_width/14.4,
                                                            height=win_height/norm_font_div + 10,
                                                            win_x_gap=win_x_gap,
                                                            win_y_gap=win_y_gap,
                                                            active=textbox_inactive_colour_input_box_R.active,
                                                            text=textbox_inactive_colour_input_box_R.text,
                                                            pre_box_text=textbox_inactive_colour_input_box_R.pre_box_text,
                                                            )
            textbox_inactive_colour_input_box_G = RGBInputBox(x=textbox_active_colour_input_box_G.x,
                                                            y=textbox_inactive_colour_input_box_R.y,
                                                            width=win_width/14.4,
                                                            height=win_height/norm_font_div + 10,
                                                            win_x_gap=win_x_gap,
                                                            win_y_gap=win_y_gap,
                                                            active=textbox_inactive_colour_input_box_G.active,
                                                            text=textbox_inactive_colour_input_box_G.text,
                                                            pre_box_text=textbox_inactive_colour_input_box_G.pre_box_text,
                                                            )
            textbox_inactive_colour_input_box_B = RGBInputBox(x=textbox_active_colour_input_box_B.x,
                                                            y=textbox_inactive_colour_input_box_R.y,
                                                            width=win_width/14.4,
                                                            height=win_height/norm_font_div + 10,
                                                            win_x_gap=win_x_gap,
                                                            win_y_gap=win_y_gap,
                                                            active=textbox_inactive_colour_input_box_B.active,
                                                            text=textbox_inactive_colour_input_box_B.text,
                                                            pre_box_text=textbox_inactive_colour_input_box_B.pre_box_text,
                                                            )

            textbox_inactive_colour_input_box_R.draw_to(settings_bg)
            textbox_inactive_colour_input_box_G.draw_to(settings_bg)
            textbox_inactive_colour_input_box_B.draw_to(settings_bg)
            textbox_inactive_colour_text.draw_to(settings_bg)

            settings_objects["textbox_inactive_colour_input_box_R"] = textbox_inactive_colour_input_box_R
            settings_objects["textbox_inactive_colour_input_box_G"] = textbox_inactive_colour_input_box_G
            settings_objects["textbox_inactive_colour_input_box_B"] = textbox_inactive_colour_input_box_B
            settings_objects["textbox_inactive_colour_text"] = textbox_inactive_colour_text

            if textbox_inactive_colour_input_box_R.text == '':
                textbox_inactive_colour_input_box_R.pre_box_text = 'R:0'
            else:
                textbox_inactive_colour_input_box_R.pre_box_text = 'R:'

            if textbox_inactive_colour_input_box_G.text == '':
                textbox_inactive_colour_input_box_G.pre_box_text = 'G:0'
            else:
                textbox_inactive_colour_input_box_G.pre_box_text = 'G:'

            if textbox_inactive_colour_input_box_B.text == '':
                textbox_inactive_colour_input_box_B.pre_box_text = 'B:0'
            else:
                textbox_inactive_colour_input_box_B.pre_box_text = 'B:'

            global_textbox_inactive_colour = (
                                            int(textbox_inactive_colour_input_box_R.text) if textbox_inactive_colour_input_box_R.text != '' else 0,
                                            int(textbox_inactive_colour_input_box_G.text) if textbox_inactive_colour_input_box_G.text != '' else 0,
                                            int(textbox_inactive_colour_input_box_B.text) if textbox_inactive_colour_input_box_B.text != '' else 0,
                                            )

            SETTINGS_DATA["global_textbox_inactive_colour"] = [value for value in global_textbox_inactive_colour]


        if True: # fps limiter
            
            fps_limit_input_box = settings_objects["fps_limit_input_box"]
            fps_limit_text = settings_objects["fps_limit_text"]

            fps_limit_text = TitleText(text="FPS limit:",
                                    x=int(font_colour_text.x+font_colour_input_box_B.x+1.2*title_x_offset),
                                    y=font_colour_text.y,
                                    win_x_gap=win_x_gap,
                                    win_y_gap=win_y_gap,
                                    font_colour=global_font_colour
                                    )
            fps_limit_input_box = NumberInputBox(x=fps_limit_text.x+title_x_offset,
                                                y=fps_limit_text.y+title_box_y_offset,
                                                width=win_width/14.4,
                                                height=win_height/norm_font_div + 10,
                                                win_x_gap=win_x_gap,
                                                win_y_gap=win_y_gap,
                                                active=fps_limit_input_box.active,
                                                text=fps_limit_input_box.text,
                                                max_int=max_fps,
                                                pre_box_text=fps_limit_input_box.pre_box_text,
                                                suff_box_text=fps_limit_input_box.suff_box_text,
                                                )

            fps_limit_text.draw_to(settings_bg)
            fps_limit_input_box.draw_to(settings_bg)

            settings_objects["fps_limit_input_box"] = fps_limit_input_box
            settings_objects["fps_limit_text"] = fps_limit_text
            SETTINGS_DATA["fps_limit"] = fps_limit_text

            if fps_limit_input_box.text == '':
                fps_limit = 0
                fps_limit_input_box.pre_box_text = '0'
            
            else:
                fps_limit = int(fps_limit_input_box.text)
                fps_limit_input_box.pre_box_text = ''

    elif settings_screen == 4: # Sound settings

        if True: # music volume
            music_volume_text = settings_objects["music_volume_text"]
            music_volume_input_box = settings_objects["music_volume_input_box"]

            music_volume_text = TitleText(text="Music Volume:",
                                        x=base_box_pos[0]-title_x_offset,
                                        y=base_box_pos[1]-int(0.5*title_y_offset),
                                        win_x_gap=win_x_gap,
                                        win_y_gap=win_y_gap,
                                        font_colour=global_font_colour
                                        )
            music_volume_input_box = NumberInputBox(x=base_box_pos[0],
                                                    y=base_box_pos[1],
                                                    width=win_width/14.4,
                                                    height=win_height/norm_font_div + 10,
                                                    win_x_gap=win_x_gap,
                                                    win_y_gap=win_y_gap,
                                                    active=music_volume_input_box.active,
                                                    text=music_volume_input_box.text,
                                                    max_int=100,
                                                    pre_box_text=music_volume_input_box.pre_box_text,
                                                    suff_box_text=music_volume_input_box.suff_box_text,
                                                    )

            music_volume_text.draw_to(settings_bg)
            music_volume_input_box.draw_to(settings_bg)

            if music_volume_input_box.text == '':
                music_volume_input_box.pre_box_text = '0'
            
            else:
                music_volume_input_box.pre_box_text = ''

            music_volume = int(music_volume_input_box.text)/100 if music_volume_input_box.text != '' else 0
            settings_objects["music_volume_text"] = music_volume_text
            settings_objects["music_volume_input_box"] = music_volume_input_box
            SETTINGS_DATA["music_volume"] = music_volume

            if music_volume == 0:
                pygame.mixer.music.pause()
            
            else:
                pygame.mixer.music.unpause()

        if True: # click sfx volume
            click_sfx_volume_text = settings_objects["click_sfx_volume_text"]
            click_sfx_volume_input_box = settings_objects["click_sfx_volume_input_box"]
            
            click_sfx_volume_text = TitleText(x=music_volume_text.x,
                                              y=music_volume_input_box.y+title_y_offset,
                                              win_x_gap=win_x_gap,
                                              win_y_gap=win_y_gap,
                                              font_colour=global_font_colour,
                                              text="Click SFX volume:",
                                              )
            click_sfx_volume_input_box = NumberInputBox(x=base_box_pos[0],
                                                        y=click_sfx_volume_text.y+title_box_y_offset,
                                                        width=box_width,
                                                        height=box_height,
                                                        win_x_gap=win_x_gap,
                                                        win_y_gap=win_y_gap,
                                                        active=click_sfx_volume_input_box.active,
                                                        text=click_sfx_volume_input_box.text,
                                                        max_int=100,
                                                        pre_box_text=click_sfx_volume_input_box.pre_box_text,
                                                        suff_box_text=click_sfx_volume_input_box.suff_box_text,
                                                        )
            
            if click_sfx_volume_input_box.text == '':
                click_sfx_volume_input_box.pre_box_text = '0'
            
            else:
                click_sfx_volume_input_box.pre_box_text = ''

            click_sfx_volume_text.draw_to(settings_bg)
            click_sfx_volume_input_box.draw_to(settings_bg)

            click_sfx_volume = int(click_sfx_volume_input_box.text)/100 if click_sfx_volume_input_box.text != '' else 0
            click_chanel.set_volume(click_sfx_volume)

            settings_objects["click_sfx_volume_text"] = click_sfx_volume_text
            settings_objects["click_sfx_volume_input_box"] = click_sfx_volume_input_box
            SETTINGS_DATA["click_sfx_volume"] = click_sfx_volume

    # Blit the settings backdrop with everything on it to the window

    WINDOW.blit(settings_bg,
                (
                    int(win_centrex-settings_bg.get_width()/2),    # Xpos
                    int(win_centrey-settings_bg.get_height()/2.5), # Ypos
                ),
                )

    return


def version_update() -> NoReturn: 
    global screen, music_volume, music_off_box_menu_settings, music_on_box_menu_settings, \
           return_img_box
    
    save_timer_timer.cancel()
    save_timer()

    if screen != 3:
        clear_screen()

    pygame.mixer.music.stop()

    screen = 3

    bg = pygame.image.load(MENU_BG_PATH)
    bg = pygame.transform.scale(bg, (win_width, win_height))
    WINDOW.blit(bg, (0, 0))
    
    # Return to menu screen

    return_img = pygame.image.load(RETURN_PATH)
    return_img = pygame.transform.smoothscale(return_img, 
                                              return_img_size,
                                              )
    return_img_rect = return_img.get_rect()
    return_img_pos: tuple[int, int] = (int(win_height/music_button_div),          # Xpos
                                       int(win_width-win_width/music_button_div), # Ypos
                                       )
    return_img_box = pygame.Rect(return_img_pos[0],      # Xpos
                                 return_img_pos[1],      # Ypos
                                 return_img_rect.width,  # width
                                 return_img_rect.height, # height
                                 )

    WINDOW.blit(return_img,
                (
                    return_img_pos[0], # Xpos
                    return_img_pos[1], # Ypos
                ),
                )
    
    time.sleep(0.1)

    start_updater()


def start_updater() -> NoReturn:
    
    args = [sys.executable, UPDATE_FILE_PATH]
    subprocess.Popen(args, start_new_session=True)
    pygame.quit()
    exit(0)


def enter_vab() -> None: 
    global screen
    screen = 4

    return


def start_simulation() -> None: 
    global screen
    screen = 5

    return


def main() -> None:

    global current_version, web_version, up_to_date, win_width, win_height, win_right, win_bottom, \
           win_centrex, win_centrey, VER_FONT, FONT, music_volume, settings_text, start_text, \
           update_button, exit_game, settings_font_colour, start_game_font_colour, \
           exit_game_font_colour, version_update_font_colour, return_img_box, info_text_settings_box, \
           info_text_font_colour, credits_text_settings_box, credits_font_colour, settings_screen, \
           visual_text_settings_box, sound_text_settings_box, sound_font_colour, visuals_font_colour,\
           return_text_settings_box, return_font_colour, settings_objects, previous_volume


    clock = pygame.time.Clock()
    running: bool = True
    current_version = get_local_version()
    web_version = get_web_version()
    dt: float = 0
    up_to_date = check_update()

    main_menu()
    
    while running:
        for pyevent in pygame.event.get():
            if pyevent.type == pygame.QUIT: # pressed X button on window
                running = False
                pygame.quit()
                save_timer_timer.cancel()
                save_timer()
                break

            if pyevent.type == pygame.VIDEORESIZE and (win_width != WINDOW.get_width() or win_height != WINDOW.get_height()): # pygame.VIDEORESIZE constantly occurs, so this checks if the window's height or width has changed
                win_width = WINDOW.get_width()
                win_height = WINDOW.get_height()
                win_right = win_width
                win_bottom = win_height
                win_centrex = win_width/2
                win_centrey = win_height/2

                FONT = pygame.font.SysFont(name="Courier", size=int(win_height/norm_font_div), bold=True)
                VER_FONT = pygame.font.SysFont(name="Comic-Sans", size=int(win_height/ver_font_div), bold=True)

                if screen == 1:
                    main_menu()
                elif screen == 2:
                    settings()
                elif screen == 3:
                    version_update()
                elif screen == 4:
                    enter_vab()
                elif screen == 5:
                    start_simulation()

            if screen == 1: # Main Menu          ----------------------------------------------------------------------------------------------------
                if pyevent.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3)[0] == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if exit_box_menu.collidepoint(mouse_pos): # type:ignore
                        # Exit the game
                        click_chanel.play(click_sfx)
                        running = False
                        # last save
                        continue

                    elif start_box_menu.collidepoint(mouse_pos): # type:ignore
                        # ENTER THE VAB
                        click_chanel.play(click_sfx)
                        enter_vab()
                        continue

                    elif settings_box_menu.collidepoint(mouse_pos): # type:ignore
                        # ENTER SETTINGS SCREEN
                        click_chanel.play(click_sfx)
                        settings_screen = 0
                        settings()
                        continue

                    elif version_box_menu.collidepoint(mouse_pos): # type:ignore
                        # ENTER VERSION UPDATE SCREEN
                        if not up_to_date:
                            click_chanel.play(click_sfx)
                            version_update()
                            continue
                    
                    elif music_on_box_menu_settings.collidepoint(mouse_pos) and music_volume != 0: #type:ignore
                        # Wants to mute the music
                        click_chanel.play(click_sfx)
                        pygame.mixer.music.pause()
                        previous_volume = int(settings_objects["music_volume_input_box"].text)/100 if settings_objects["music_volume_input_box"].text != '' else 0
                        settings_objects["music_volume_input_box"].text = ''
                        settings_objects["music_volume_input_box"].pre_box_text = '0'
                        continue
                    
                    elif music_off_box_menu_settings.collidepoint(mouse_pos) and music_volume == 0: #type:ignore
                        # Wants to unmute the music
                        click_chanel.play(click_sfx)
                        settings_objects["music_volume_input_box"].text = str(int(previous_volume*100))
                        settings_objects["music_volume_input_box"].pre_box_text = ''
                        pygame.mixer.music.unpause()
                        continue 
                
                mouse_pos = pygame.mouse.get_pos()
                if settings_box_menu.collidepoint(mouse_pos): #type:ignore
                    settings_font_colour = global_hover_colour
                
                elif start_box_menu.collidepoint(mouse_pos): #type:ignore
                    start_game_font_colour = global_hover_colour

                elif exit_box_menu.collidepoint(mouse_pos): #type:ignore
                    exit_game_font_colour = global_hover_colour

                elif version_box_menu.collidepoint(mouse_pos): #type:ignore
                    version_update_font_colour = global_hover_colour
                
                else:
                    settings_font_colour = global_font_colour
                    start_game_font_colour = global_font_colour
                    exit_game_font_colour = global_font_colour
                    version_update_font_colour = global_font_colour
                
                main_menu()

            elif screen == 2: # Settings         ----------------------------------------------------------------------------------------------------
                mouse_pos = pygame.mouse.get_pos()

                if pyevent.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3)[0] == 1:
                    
                    if music_on_box_menu_settings.collidepoint(mouse_pos) and music_volume != 0: #type:ignore
                        # Wants to mute the music
                        click_chanel.play(click_sfx)
                        pygame.mixer.music.pause()
                        previous_volume = int(settings_objects["music_volume_input_box"].text)/100 if settings_objects["music_volume_input_box"].text != '' else 0
                        settings_objects["music_volume_input_box"].text = ''
                        settings_objects["music_volume_input_box"].pre_box_text = '0'
                        continue
                    
                    elif music_off_box_menu_settings.collidepoint(mouse_pos) and music_volume == 0: #type:ignore
                        # Wants to unmute the music
                        click_chanel.play(click_sfx)
                        settings_objects["music_volume_input_box"].text = str(int(previous_volume*100))
                        settings_objects["music_volume_input_box"].pre_box_text = ''
                        pygame.mixer.music.unpause()
                        continue 

                    elif version_box_menu.collidepoint(mouse_pos): #type:ignore
                        if not up_to_date:
                            # Wants to update the game
                            click_chanel.play(click_sfx)
                            version_update()
                            continue
                    
                    elif return_text_settings_box.collidepoint(mouse_pos): #type:ignore
                        if settings_screen == 0: # In the main settings screen
                            # Wants to return to the main menu
                            click_chanel.play(click_sfx)
                            main_menu() # Display the main menu
                            continue
                        
                        else: # Not in the main settings screen
                            # Wants to return to the main settings screen
                            click_chanel.play(click_sfx)
                            settings_screen = 0 # Change to main settings

                            for obj in settings_objects.values():
                                if obj.type == CLICKABLE: # If the object can be coloured
                                    obj.active = False # Reset it's activity to default

                            settings() # Display the settings page
                            continue

                    elif settings_screen == 0: # Main settings zone
                        if credits_text_settings_box.collidepoint(mouse_pos): #type:ignore
                            click_chanel.play(click_sfx)
                            settings_screen = 1
                            continue

                        elif info_text_settings_box.collidepoint(mouse_pos): #type:ignore
                            click_chanel.play(click_sfx)
                            settings_screen = 2
                            continue

                        elif visual_text_settings_box.collidepoint(mouse_pos): #type:ignore
                            click_chanel.play(click_sfx)
                            settings_screen = 3
                            continue

                        elif sound_text_settings_box.collidepoint(mouse_pos): #type:ignore
                            click_chanel.play(click_sfx)
                            settings_screen = 4
                            continue

                for obj in settings_objects.values():
                    if not obj.type == INFORMATION:
                        obj.handle_event(pyevent, settings_bg)

                if version_box_menu.collidepoint(mouse_pos): #type:ignore
                    version_update_font_colour = global_hover_colour
                
                elif info_text_settings_box.collidepoint(mouse_pos): #type:ignore
                    info_text_font_colour = global_hover_colour
                
                elif credits_text_settings_box.collidepoint(mouse_pos): #type:ignore
                    credits_font_colour = global_hover_colour
                
                elif visual_text_settings_box.collidepoint(mouse_pos): #type:ignore
                    visuals_font_colour = global_hover_colour
                
                elif sound_text_settings_box.collidepoint(mouse_pos): #type:ignore
                    sound_font_colour = global_hover_colour
                
                elif return_text_settings_box.collidepoint(mouse_pos): #type:ignore
                    return_font_colour = global_hover_colour
                
                else:
                    info_text_font_colour = global_font_colour
                    version_update_font_colour = global_font_colour
                    credits_font_colour = global_font_colour
                    visuals_font_colour = global_font_colour
                    sound_font_colour = global_font_colour
                    return_font_colour = global_font_colour

                settings()

            elif screen == 3: # Version Update   ----------------------------------------------------------------------------------------------------
                version_update()
                continue

            elif screen == 4: # VAB              ----------------------------------------------------------------------------------------------------
                enter_vab()
                continue
            
            elif screen == 5: # Game             ----------------------------------------------------------------------------------------------------
                start_simulation()
                continue

        pygame.display.flip()
        dt = clock.tick(fps_limit) / 100
    
    pygame.quit()
    save_timer_timer.cancel()
    save_timer()
    return


if __name__ == '__main__':
    save_timer_timer = SaveTimer(save_timer_delay, save_timer)
    save_timer_timer.start()
    main()
