#!/usr/bin/env python3
"""
Voyage Through The Void
A game about space craft and interplanertary and interstellar flight.
Inspiration from the game `Spaceflight Simulator` by Stef.

Scripted by Elia Brady.
Music and images credited as needed, otherwise created by Elia Brady.

Special thanks to the pre-alpha testers - James, Aayan, Aaliyah, Agamnoor and Aashna - for waiting through my many, many months of programming, or lack thereov.
Special thanks to James and Aayan for assistance with debugging.
Special thanks to Aashna for helping with layout design.
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
    pygame.display.set_caption("Voyage Through The Void")
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
from random import randint



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

VERSION_URL = "https://chicken-head1.github.io/Voyage-Through-The-Void/version.md"

bg_num: int = randint(1, 3)

VERSION_PATH = f"{os.path.join(DIRPATH, "data", "version.txt")}"
SETTINGS_DATA_PATH = f"{os.path.join(DIRPATH, "data", "settings_data.json")}"
MENU_BG_PATH = f"/{os.path.join(DIRPATH, "images", f"menu_bg{bg_num}.png")}"
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

MODEL_PATH = f"{os.path.join(DIRPATH, "data", "models")}"

FUEL_TANK_PATH = f"{os.path.join(MODEL_PATH, "fuel_tank.svg")}"


MODELS: dict = {
                "liquid_fuel_tank": pygame.image.load(FUEL_TANK_PATH),
                "oxidiser_tank": pygame.image.load(FUEL_TANK_PATH),
                "solid_fuel_tank": pygame.image.load(FUEL_TANK_PATH),
                }

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
FONT_SM: Font = pygame.font.SysFont(name="Courier", size=int(win_height/norm_font_div), bold=True)
VER_FONT_SM: Font = pygame.font.SysFont(name="Comic-Sans", size=int(win_height/ver_font_div), bold=True)
SETTINGS_FONT_SM: Font = pygame.font.SysFont(name="Courier", size=int(win_height/settings_font_div), bold=True)

WHITE: tuple = (255, 255, 255)
GREY: tuple = (200, 200, 200)
BLACK: tuple = (0, 0, 0)
HOVER_COLOUR: tuple = (187, 211, 255)
PURPLE: tuple = (150, 0, 200)
SETTINGS_GREY: tuple = (130, 130, 130)
DEBUG_HIGHLIGHT_COLOUR: tuple = (0, 211, 0)
DEBUG_2_HIGHLIGHT_COLOUR: tuple = (0, 0, 211)
DEBUG_ACTIVE_HIGHLIGHT_COLOUR: tuple = (255, 44, 255)
DEBUG_2_ACTIVE_HIGHLIGHT_COLOUR: tuple = (255, 44, 255)
BLUEPRINT_CELL_WALL_BLUE: tuple = (100, 100, 255)
BLUEPRINT_BG_PURPLE: tuple = (170, 170, 255)
BLUEPRINT_UI_BG_PURPLE: tuple = (190, 190, 255)
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
local_version: str = str()
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

settings_bg = pygame.Surface((1, 1))



class SaveTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

class ImageButton:
    def __init__(self,
                 *, 
                 x: int,
                 y: int,
                 active: bool,
                 win_x_gap: int,
                 win_y_gap: int,
                 image: pygame.Surface,
                 always_visible: bool = False,
                 ) -> None:
        
        if x <= 0:
            raise ValueError("X parameter cannot be less than or equal to 0.")
        if y <= 0:
            raise ValueError("Y parameter cannot be less than or equal to 0.")
        if win_x_gap < 0:
            raise ValueError("win_x_gap parameter cannot be less than 0.")
        if win_y_gap < 0:
            raise ValueError("win_y_gap parameter cannot be less than 0.")

        self.x = x
        self.y = y
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.col_rect = pygame.Rect(x+win_x_gap, y+win_y_gap, self.width, self.height)
        self.type = CLICKABLE
        self.active = active
        self.always_visible = always_visible

        return

    def handle_event(self,
                     event: pygame.event.Event,
                     ) -> None:
        mouse_pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed(3)[0] and event.type == pygame.MOUSEBUTTONDOWN:

            if self.active:
                if not self.col_rect.collidepoint(mouse_pos):
                    self.active = False
                    click_chanel.play(click_sfx)

            else:
                if self.col_rect.collidepoint(mouse_pos):
                    self.active = True
                    click_chanel.play(click_sfx)

        return

    def draw_to(self, 
                screen: pygame.Surface,
                ) -> None:
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return

class InputBox:
    def __init__(self, 
                 *,
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
                 font: pygame.font.Font,
                 always_visible: bool = False,
                 ) -> None:
        
        if x <= 0:
            raise ValueError("X parameter cannot be less than or equal to 0.")
        if y <= 0:
            raise ValueError("Y parameter cannot be less than or equal to 0.")
        if win_x_gap < 0:
            raise ValueError("win_x_gap parameter cannot be less than 0.")
        if win_y_gap < 0:
            raise ValueError("win_y_gap parameter cannot be less than 0.")
        if max_int <= 0:
            raise ValueError("max_int parameter cannot be less than or equal to 0.")

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_int = max_int
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.pre_box_text = pre_box_text
        self.suff_box_text = suff_box_text
        self.txt_surface = font.render(f'{self.pre_box_text}{self.text}{self.suff_box_text}', True, global_font_colour)
        self.active = active
        self.text_colour = global_font_colour
        self.col_rect = pygame.Rect(x + win_x_gap, 
                                    y + win_y_gap, 
                                    width, 
                                    height,
                                    )
        self.colour = global_textbox_active_colour if self.active else global_textbox_inactive_colour
        self.font = font
        self.type = CLICKABLE
        self.always_visible = always_visible

        return

    def handle_event(self,
                     event: pygame.event.Event,
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
    
    def draw_to(self, 
                screen: pygame.Surface,
                ) -> None:
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+int(win_width/288), self.rect.y+int(win_height/174.4)))
        # Blit the rect.
        pygame.draw.rect(screen, self.colour, self.rect, int(win_width/480)) 

        return

class Text:

    def __init__(self,
                 *,
                 text: str,
                 x: int,
                 y: int,
                 win_x_gap: int,
                 win_y_gap: int,
                 font_colour: tuple,
                 font: pygame.font.Font,
                 always_visible: bool = False,
                 ) -> None:
        
        if x < 0:
            raise ValueError("X parameter cannot be less than 0.")
        if y < 0:
            raise ValueError("Y parameter cannot be less than 0.")
        if win_x_gap < 0:
            raise ValueError("win_x_gap parameter cannot be less than 0.")
        if win_y_gap < 0:
            raise ValueError("win_y_gap parameter cannot be less than 0.")

        self.x = x
        self.y = y
        self.font_colour = font_colour
        self.text = text
        self.win_x_gap = win_x_gap
        self.win_y_gap = win_y_gap
        self.text_surface = font.render(self.text, True, self.font_colour)
        self.rect = self.text_surface.get_rect()
        self.col_rect = pygame.Rect(x+win_x_gap, y+win_y_gap, self.rect.width, self.rect.height)
        self.font = font
        self.type = INFORMATION
        self.always_visible = always_visible

        return

    def draw_to(self, 
                screen: pygame.Surface,
                ) -> None:
        self.text_surface = self.font.render(self.text, True, self.font_colour)
        screen.blit(self.text_surface, (self.x+self.win_x_gap, self.y+self.win_y_gap))

        return


class TextButton(Text):
    def __init__(self, 
                 *,
                 x: int,
                 y: int,
                 win_y_gap: int,
                 win_x_gap: int,
                 active: bool,
                 text: str,
                 font_colour: tuple[int, int, int] = global_font_colour,
                 font: pygame.font.Font,
                 screen: pygame.Surface,
                 always_visible: bool = False,
                 ) -> None:

        super().__init__(
                         text=text,
                         font_colour=font_colour,
                         x=x,
                         y=y,
                         font=font,
                         win_x_gap=win_x_gap,
                         win_y_gap=win_y_gap,
                         )

        self.type = CLICKABLE
        self.active = active
        self.always_visible = always_visible
        self.screen=screen

    def draw_to(self, 
                screen: pygame.Surface,
                ) -> None:
        self.text_surface = self.font.render(self.text, True, self.font_colour)
        screen.blit(self.text_surface, (self.x, self.y))

        return

    def handle_event(self,
                     event: pygame.event.Event,
                     ) -> None:
        mouse_pos = pygame.mouse.get_pos()

        if self.col_rect.collidepoint(mouse_pos):
            self.font_colour = global_hover_colour
        
        else:
            self.font_colour = global_font_colour

        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3)[0]: # mouse press and button pressed is left click

            if self.col_rect.collidepoint(mouse_pos):
                self.active = True
            
            else:
                self.active = False

        self.draw_to(self.screen)

        return

class RGBInputBox(InputBox):

    def __init__(self, 
                 *,
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
                 font: pygame.font.Font,
                 always_visible: bool = False,
                 ) -> None:
        self.max_int = 255
        super().__init__(x=x, 
                         y=y, 
                         width=width, 
                         height=height, 
                         win_y_gap=win_y_gap, 
                         win_x_gap=win_x_gap, 
                         active=active, 
                         text=text, 
                         max_int=self.max_int, 
                         pre_box_text=pre_box_text, 
                         suff_box_text=suff_box_text, 
                         font=font,
                         always_visible=always_visible,
                         )
        return

    def handle_event(self,
                     event: pygame.event.Event,
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
        return

class NumberInputBox(InputBox):

    def __init__(self, 
                 *,
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
                 font: pygame.font.Font,
                 always_visible: bool = False,
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
                         font=font,
                         always_visible=always_visible,
                         )
        self.max_int = max_int
        self.type = CLICKABLE
        return
    
    def handle_event(self,
                     event: pygame.event.Event,
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
                if event.key in PYGAME_DIGIT: # if the key is a digit
                    try:
                        if int(self.text + event.unicode) <= self.max_int: # text value cannot be more than max int
                            self.text += event.unicode # add the digit to the current text
                    except ValueError: # self.text == ''
                        self.text += event.unicode # add the digit to the current text
        return



class UiUnderlay():
    def __init__(self,
                 *,
                 colour: tuple[int, int, int],
                 width: int,
                 height: int,
                 coords: tuple[int, int],
                 ) -> None:
        self.colour = colour
        self.dimensions = width, height
        self.coords = coords
        return

    def draw_to(self,
                screen: pygame.Surface,
                ) -> None:
        self.cover = pygame.Surface(self.dimensions)
        self.cover.fill(self.colour)
        screen.blit(self.cover, self.coords)
        return


class BlueprintGrid():
    def __init__(self,
                 *,
                 width: int,
                 height: int,
                 cell_size: int,
                 cell_wall_colour: tuple[int, int, int],
                 background_colour: tuple[int, int, int],
                 comps: dict[tuple[int, int], pygame.Surface | None] = {(0, 0): None},
                 ) -> None:

        if width <= -1:
            print(f"The width must be positive. {width}")
            return

        if height <= -1:
            print(f"The height must be positive. {height}")
            return

        if cell_size <= -1:
            print(f"The grid_size must be positive. {cell_size}")
            return

        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cell_wall_colour = cell_wall_colour
        self.components: dict[tuple[int, int], pygame.Surface | None] = {}
        self.grid = pygame.Surface((width, height))
        self.grid.fill(background_colour)
        self.part_count = self.get_part_count()

        self.add_components(components=list(comps.values()), coords=list(comps.keys()))

        return

    def get_part_count(self) -> int:
        count = 0

        for _, obj in self.components.items():
            if obj != None:
                count += 1

        return count

    def get_rocket_height(self) -> int:
        # go through all the cells backwards, then find the first object that isn't None, and collect the y coord value
        # go through all the cells forwards and find the first object that isn't None, and collect the y coord value
        # find the height based off the 2 y values and return the cell count in metres

        height = 0
        coords: list[tuple[int, int]] = []

        for coord in self.components.keys():
            if self.components[coord] != None:
                coords.append(coord)

        coords = sorted(coords, key=lambda k: [k[1], k[0]])

        try:
            lowest_y_cor = coords[-1][1]
            highest_y_cor = coords[0][1]
        
        except IndexError:
            return 0

        return lowest_y_cor - highest_y_cor + 1

    def draw_to(self,
                *,
                screen: pygame.Surface,
                grid_start_coords: tuple[int, int],
                ) -> None:

        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(self.grid, 
                                 self.cell_wall_colour,
                                 (
                                  x * self.cell_size,
                                  y * self.cell_size,
                                  self.cell_size,
                                  self.cell_size,
                                  ),
                                  width=1
                                 )

        for coord in self.components.keys():
            if self.components[coord] != None:
                self.grid.blit(self.components[coord],                                                                                                                   #type:ignore
                               (
                                coord[0] * self.cell_size,
                                coord[1] * self.cell_size,
                                ),
                               )

        screen.blit(self.grid, grid_start_coords)

        return

    def add_component(self,
                      *,
                      component: pygame.Surface,
                      coord: tuple[int, int],
                      ) -> None:

        try:
            if self.components[coord] == None:
                self.components[coord] = pygame.transform.smoothscale(component, (self.cell_size, self.cell_size))

            else:
                print(f"Unable to add object at ({coord[0]}, {coord[1]}). There is a component there.")
                return

        except KeyError:
            self.components[coord] = pygame.transform.smoothscale(component, (self.cell_size, self.cell_size))

        return

    def remove_component(self,
                         coord: tuple[int, int],
                         ) -> None:

        try:
            self.components[coord] = None

        except KeyError:
            print(f"Unable to remove object at ({coord[0]}, {coord[1]}). There is no component there.")
            return

        return

    def add_components(self,
                       *,
                       components: list[pygame.Surface | None],
                       coords: list[tuple[int, int]],
                       ) -> None:

        if len(components) != len(coords):
            print("You must have the same amount of coordinates as component parts when creating a larger single component.")
            return

        for coord in coords:
            if coord in self.components.keys():
                if self.components[coord] != None:
                    print(f"The component at ({coord[0]}, {coord[1]}) cannot overlap other components.")
                    return

        for index, coord in enumerate(coords):
            if components[index] != None:
                self.components[coord] = components[index]

        return

    def add_bigger_component(self,
                             *,
                             component_parts: list[pygame.Surface | None],
                             coords: list[tuple[int, int]],
                             ) -> None:
        self.add_components(components=component_parts, coords=coords)
        return

    def remove_components(self,
                          coords: list[tuple[int, int]],
                          ) -> None:
        
        for coord in coords:
            self.remove_component(coord)

        return



# Settings stuff

info_text_font_colour: tuple = global_font_colour
credits_font_colour: tuple = global_font_colour
visuals_font_colour: tuple = global_font_colour
sound_font_colour: tuple = global_font_colour
return_font_colour: tuple = global_font_colour
RGB_TEXT_BOX_OFFSET_DIV: int = 96

settings_objects: dict = {
                          # Visual settings page
                          "font_colour_input_box_R": RGBInputBox(x=1, y=1, width=1, height=1, win_x_gap=1, win_y_gap=1, active=False, text=str(global_font_colour[0]), pre_box_text='R:', font=FONT),
                          "font_colour_input_box_G": RGBInputBox(x=1, y=1, width=1, height=1, win_x_gap=1, win_y_gap=1, active=False, text=str(global_font_colour[1]), pre_box_text='G:', font=FONT),
                          "font_colour_input_box_B": RGBInputBox(x=1, y=1, width=1, height=1, win_x_gap=1, win_y_gap=1, active=False, text=str(global_font_colour[2]), pre_box_text='B:', font=FONT),
                          "font_colour_text": Text(text="", x=1, y=1, win_x_gap=1, win_y_gap=1, font_colour=global_font_colour, font=FONT),

                          "hover_colour_input_box_R": RGBInputBox(x=1, y=1, width=1, height=1, win_x_gap=1, win_y_gap=1, active=False, text=str(global_hover_colour[0]), pre_box_text='R:', font=FONT),
                          "hover_colour_input_box_G": RGBInputBox(x=1, y=1, width=1, height=1, win_x_gap=1, win_y_gap=1, active=False, text=str(global_hover_colour[1]), pre_box_text='G:', font=FONT),
                          "hover_colour_input_box_B": RGBInputBox(x=1, y=1, width=1, height=1, win_x_gap=1, win_y_gap=1, active=False, text=str(global_hover_colour[2]), pre_box_text='B:', font=FONT),
                          "hover_colour_text": Text(text="", x=1, y=1, win_x_gap=1, win_y_gap=1, font_colour=global_font_colour, font=FONT),

                          "textbox_active_colour_input_box_R": RGBInputBox(x=1, y=1, width=1, height=1, win_x_gap=1, win_y_gap=1, active=False, text=str(global_textbox_active_colour[0]), pre_box_text='R:', font=FONT),
                          "textbox_active_colour_input_box_G": RGBInputBox(x=1, y=1, width=1, height=1, win_x_gap=1, win_y_gap=1, active=False, text=str(global_textbox_active_colour[1]), pre_box_text='G:', font=FONT),
                          "textbox_active_colour_input_box_B": RGBInputBox(x=1, y=1, width=1, height=1, win_x_gap=1, win_y_gap=1, active=False, text=str(global_textbox_active_colour[2]), pre_box_text='B:', font=FONT),
                          "textbox_active_colour_text": Text(text="", x=1, y=1, win_x_gap=1, win_y_gap=1, font_colour=global_font_colour, font=FONT),

                          "textbox_inactive_colour_input_box_R": RGBInputBox(x=1, y=1, width=1, height=1, win_x_gap=1, win_y_gap=1, active=False, text=str(global_textbox_inactive_colour[0]), pre_box_text='R:', font=FONT),
                          "textbox_inactive_colour_input_box_G": RGBInputBox(x=1, y=1, width=1, height=1, win_x_gap=1, win_y_gap=1, active=False, text=str(global_textbox_inactive_colour[1]), pre_box_text='G:', font=FONT),
                          "textbox_inactive_colour_input_box_B": RGBInputBox(x=1, y=1, width=1, height=1, win_x_gap=1, win_y_gap=1, active=False, text=str(global_textbox_inactive_colour[2]), pre_box_text='B:', font=FONT),
                          "textbox_inactive_colour_text": Text(text="", x=1, y=1, win_x_gap=1, win_y_gap=1, font_colour=global_font_colour, font=FONT),

                          "fps_limit_input_box": NumberInputBox(x=1, y=1, width=1, height=1, win_x_gap=1, win_y_gap=1, active=False, text=str(fps_limit), max_int=max_fps, font=FONT),
                          "fps_limit_text": Text(text="", x=1, y=1, win_x_gap=1, win_y_gap=1, font_colour=global_font_colour, font=FONT),

                          # Sound settings page
                          "music_volume_input_box": NumberInputBox(x=1, y=1, width=1, height=1, win_x_gap=1, win_y_gap=1, active=False, text=str(int(music_volume*100)), max_int=100, suff_box_text="%", font=FONT),
                          "music_volume_text": Text(text="", x=1, y=1, win_x_gap=1, win_y_gap=1, font_colour=global_font_colour, font=FONT),

                          "click_sfx_volume_input_box": NumberInputBox(x=1, y=1, width=1, height=1, win_x_gap=1, win_y_gap=1, active=False, text=str(int(click_sfx_volume*100)), max_int=100, suff_box_text="%", font=FONT),
                          "click_sfx_volume_text": Text(text="", x=1, y=1, win_x_gap=1, win_y_gap=1, font_colour=global_font_colour, font=FONT),

                          # Info settings page
                          "discord_link_text": Text(text="", x=1, y=1, win_x_gap=1, win_y_gap=1, font_colour=global_font_colour, font=FONT),

                          # Credits settings page
                          "menu_music_credit_text": Text(text="", x=1, y=1, win_x_gap=1, win_y_gap=1, font_colour=global_font_colour, font=FONT),
                          "click_sfx_credit_text": Text(text="", x=1, y=1, win_x_gap=1, win_y_gap=1, font_colour=global_font_colour, font=FONT),
                          "menu_bg_credit_text": Text(text="", x=1, y=1, win_x_gap=1, win_y_gap=1, font_colour=global_font_colour, font=FONT),
                          "inspo_text": Text(text="", x=1, y=1, win_x_gap=1, win_y_gap=1, font_colour=global_font_colour, font=FONT),

                          # Main settings zone
                          "sound_text": TextButton(x=1, y=1, win_x_gap=1, win_y_gap=1, active=False, text="", font_colour=global_font_colour, font=FONT, screen=WINDOW),
                          "sound_img_button": ImageButton(x=1, y=1, active=False,  win_x_gap=1, win_y_gap=1, image=pygame.Surface((1, 1))),

                          "visual_text": TextButton(x=1, y=1, win_x_gap=1, win_y_gap=1, active=False, text="", font_colour=global_font_colour, font=FONT, screen=WINDOW),
                          "visual_img_button": ImageButton(x=1, y=1, active=False,  win_x_gap=1, win_y_gap=1, image=pygame.Surface((1, 1))),

                          "credits_text": TextButton(x=1, y=1, win_x_gap=1, win_y_gap=1, active=False, text="", font_colour=global_font_colour, font=FONT, screen=WINDOW),
                          "credits_img_button": ImageButton(x=1, y=1, active=False,  win_x_gap=1, win_y_gap=1, image=pygame.Surface((1, 1))),

                          "info_text": TextButton(x=1, y=1, win_x_gap=1, win_y_gap=1, active=False, text="", font_colour=global_font_colour, font=FONT, screen=WINDOW),
                          "info_img_button": ImageButton(x=1, y=1, active=False,  win_x_gap=1, win_y_gap=1, image=pygame.Surface((1, 1))),

                          "return_text": TextButton(x=1, y=1, win_x_gap=1, win_y_gap=1, active=False, text="", font_colour=global_font_colour, font=FONT, screen=WINDOW),
                          "return_img_button": ImageButton(x=1, y=1, active=False,  win_x_gap=1, win_y_gap=1, image=pygame.Surface((1, 1))),

                          # "Always" visible in settings
                          "music_button": ImageButton(x=1, y=1, active=False,  win_x_gap=1, win_y_gap=1, image=pygame.Surface((1, 1)), always_visible=True),

                          "current_version": Text(text="", x=1, y=1, win_x_gap=1, win_y_gap=1, font_colour=global_font_colour, font=VER_FONT, always_visible=True),
                          "update_text": Text(text="", x=1, y=1, win_x_gap=1, win_y_gap=1, font_colour=global_font_colour, font=VER_FONT, always_visible=True),
                          "update_button": TextButton(x=1, y=1, win_x_gap=1, win_y_gap=1, active=False, text="", font_colour=global_font_colour, font=VER_FONT, always_visible=True, screen=WINDOW),
                          }

menu_objects: dict = {
                      "current_version": Text(text="", x=1, y=1, win_x_gap=1, win_y_gap=1, font_colour=global_font_colour, font=VER_FONT),
                      "update_text": Text(text="", x=1, y=1, win_x_gap=1, win_y_gap=1, font_colour=global_font_colour, font=VER_FONT),
                      "update_button": TextButton(x=1, y=1, win_x_gap=1, win_y_gap=1, active=False, text="", font_colour=global_font_colour, font=VER_FONT, screen=WINDOW),

                      "start_text": TextButton(x=1, y=1, win_x_gap=1, win_y_gap=1, active=False, text="", font_colour=global_font_colour, font=SETTINGS_FONT, screen=WINDOW),
                      "settings_text": TextButton(x=1, y=1, win_x_gap=1, win_y_gap=1, active=False, text="", font_colour=global_font_colour, font=SETTINGS_FONT, screen=WINDOW),
                      "exit_game_text": TextButton(x=1, y=1, win_x_gap=1, win_y_gap=1, active=False, text="", font_colour=global_font_colour, font=SETTINGS_FONT, screen=WINDOW),

                      "music_button": ImageButton(x=1, y=1, active=False,  win_x_gap=1, win_y_gap=1, image=pygame.Surface((1, 1)), always_visible=True),
                      }


VAB_objects: dict = {
                     "grid": BlueprintGrid(width=1, height=1, cell_size=1, cell_wall_colour=BLACK, background_colour=BLACK),

                     # Underlays
                     "underlay_left": UiUnderlay(colour=BLACK, width=0, height=0, coords=(0, 0)),
                     "underlay_bottom": UiUnderlay(colour=BLACK, width=0, height=0, coords=(0, 0)),
                     "underlay_right": UiUnderlay(colour=BLACK, width=0, height=0, coords=(0, 0)),

                     # Rocket info
                     "height_text": Text(text="", x=0, y=0, win_x_gap=0, win_y_gap=0, font_colour=BLACK, font=FONT),
                     "part_count_text": Text(text="", x=0, y=0, win_x_gap=0, win_y_gap=0, font_colour=BLACK, font=FONT),
                     "thrust_weight_ratio_text": Text(text="", x=0, y=0, win_x_gap=0, win_y_gap=0, font_colour=BLACK, font=FONT),
                     "thrust_weight_ratio_text_2": Text(text="", x=0, y=0, win_x_gap=0, win_y_gap=0, font_colour=BLACK, font=FONT),
                     }


def save() -> None:
    save_data(data=SETTINGS_DATA, path=SETTINGS_DATA_PATH)
    return


def get_local_version() -> str:
    """
    Gets the current local game version.

    :return str: A string containing version information.
    """

    with open(VERSION_PATH, 'rb') as version:
        local_version = version.read()
        local_version = str(local_version).removeprefix("b'").removesuffix("\\n'")

    return local_version


def get_web_version() -> str:
    """
    Gets the current website game version.

    :return str: A string containing version information.
    """

    try:
        version = requests.get(url=VERSION_URL)
        web_version = str(version.content).removeprefix("b'").removesuffix("\\n'")

    except:
        web_version = ""

    return web_version


def check_update() -> bool:
    """
    Check for a new game version.

    :return bool: True if the server could not be accessed or the current version is the most up to date version and False if the version is not up to date.
    """

    return True if web_version == local_version or web_version == "" else False


def clear_screen(colour: tuple[int, int, int] = BLACK,
                 ) -> None:
    """
    Fills the screen with the specified colour.

    :param colour: A tuple containing the RGB values for a colour. Defaults to (0, 0, 0) or black.
    
    :return None:
    """

    WINDOW.fill(colour)

    return


def main_menu() -> None:
    """
    Dislpays the main menu.
    """

    global screen, music_volume, menu_objects

    if screen != 1:
        clear_screen()

    if screen != 1 and screen != 2 and screen != 3:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(MAIN_MENU_MUSIC_PATH)
        pygame.mixer.music.play(loops=-1)

    screen = 1

    pygame.mixer.music.set_volume(music_volume)

    bg = pygame.transform.scale(pygame.image.load(MENU_BG_PATH), (WINDOW.get_width(), WINDOW.get_height()))
    WINDOW.blit(bg, (0, 0))

    win_x_gap = 0
    win_y_gap = 0

    if True: # Version data + button

        current_version = menu_objects["current_version"]
        update_text = menu_objects["update_text"]
        update_button = menu_objects["update_button"]

        current_version_pos = (
                               int(win_width/72),
                               int(win_height/43.6),
                               )
        update_text_pos = (
                           int(win_width/72),
                           int(win_height/16),
                           )
        update_button_pos = (
                             int(win_width/72),
                             int(win_height/9.2588),
                             )

        current_version = Text(text=f"v{local_version}", 
                               x=current_version_pos[0], 
                               y=current_version_pos[1], 
                               win_x_gap=win_x_gap, 
                               win_y_gap=win_y_gap, 
                               font_colour=global_font_colour, 
                               font=VER_FONT_SM,
                               )
        update_text = Text(text=f"A new update is available -> v{web_version}", 
                           x=update_text_pos[0], 
                           y=update_text_pos[1], 
                           win_x_gap=win_x_gap, 
                           win_y_gap=win_y_gap, 
                           font_colour=global_font_colour, 
                           font=VER_FONT_SM,
                           )
        update_button = TextButton(text=f"Update Now", 
                                   x=update_button_pos[0], 
                                   y=update_button_pos[1], 
                                   win_x_gap=win_x_gap, 
                                   win_y_gap=win_y_gap, 
                                   font_colour=update_button.font_colour, 
                                   font=VER_FONT_SM,
                                   active=update_button.active,
                                   screen=WINDOW,
                                   )
        current_version_contrast = Text(text=current_version.text, 
                                        x=current_version.x, 
                                        y=current_version.y, 
                                        win_x_gap=current_version.win_x_gap, 
                                        win_y_gap=current_version.win_y_gap, 
                                        font_colour=BLACK, 
                                        font=VER_FONT,
                                        )
        update_text_contrast = Text(text=update_text.text, 
                                    x=update_text.x, 
                                    y=update_text.y, 
                                    win_x_gap=update_text.win_x_gap, 
                                    win_y_gap=update_text.win_y_gap, 
                                    font_colour=BLACK, 
                                    font=VER_FONT,
                                    )
        update_button_contrast = TextButton(text=update_button.text, 
                                            x=update_button.x, 
                                            y=update_button.y, 
                                            win_x_gap=update_button.win_x_gap, 
                                            win_y_gap=update_button.win_y_gap, 
                                            font_colour=BLACK, 
                                            font=VER_FONT,
                                            active=update_button.active,
                                            screen=WINDOW,
                                            )

        current_version_contrast.draw_to(WINDOW)
        current_version.draw_to(WINDOW)

        if not up_to_date:
            update_text_contrast.draw_to(WINDOW)
            update_button_contrast.draw_to(WINDOW)
            update_text.draw_to(WINDOW)
            update_button.draw_to(WINDOW)

        menu_objects["current_version"] = current_version
        menu_objects["update_text"] = update_text
        menu_objects["update_button"] = update_button


    if True: # Enter VAB

        start_text = menu_objects["start_text"]

        start_text_pos = (
                          win_centrex-int(start_text.rect.width/2), # Xpos
                          win_centrey-int(win_height/spacing_div),  # Ypos
                          )
        
        start_text = TextButton(
                                text="Enter the VAB",
                                x=int(start_text_pos[0]),
                                y=int(start_text_pos[1]),
                                win_x_gap=0,
                                win_y_gap=0,
                                font_colour=start_text.font_colour,
                                font=SETTINGS_FONT_SM,
                                active=start_text.active,
                                screen=WINDOW,
                                )
        start_text_contrast = TextButton(
                                         text=start_text.text,
                                         x=start_text.x+1,
                                         y=start_text.y+1,
                                         win_x_gap=start_text.win_x_gap,
                                         win_y_gap=start_text.win_y_gap,
                                         font_colour=BLACK,
                                         font=start_text.font,
                                         active=start_text.active,
                                         screen=WINDOW,
                                         )

        start_text_contrast.draw_to(WINDOW)
        start_text.draw_to(WINDOW)

        menu_objects["start_text"] = start_text


    if True: # Enter settings

        settings_text = menu_objects["settings_text"]

        settings_text_pos = (
                             win_centrex-int(settings_text.rect.width/2), # Xpos
                             win_centrey,                                 # Ypos
                             )

        settings_text = TextButton(
                                   text="Settings",
                                   x=int(settings_text_pos[0]),
                                   y=int(settings_text_pos[1]),
                                   win_x_gap=0,
                                   win_y_gap=0,
                                   font_colour=settings_text.font_colour,
                                   font=SETTINGS_FONT_SM,
                                   active=settings_text.active,
                                   screen=WINDOW,
                                   )
        settings_text_contrast = TextButton(
                                            text=settings_text.text,
                                            x=settings_text.x+1,
                                            y=settings_text.y+1,
                                            win_x_gap=settings_text.win_x_gap,
                                            win_y_gap=settings_text.win_y_gap,
                                            font_colour=BLACK,
                                            font=SETTINGS_FONT,
                                            active=False,
                                            screen=WINDOW,
                                            )

        settings_text_contrast.draw_to(WINDOW)
        settings_text.draw_to(WINDOW)


        menu_objects["settings_text"] = settings_text


    if True: # Exit game

        exit_game_text = menu_objects["exit_game_text"]

        exit_game_text_pos = (
                              win_centrex-int(settings_text.rect.width/2), # Xpos
                              win_centrey+int(win_height/spacing_div),     # Ypos
                              )

        exit_game_text = TextButton(
                                    text="Exit Game",
                                    x=int(exit_game_text_pos[0]),
                                    y=int(exit_game_text_pos[1]),
                                    win_x_gap=0,
                                    win_y_gap=0,
                                    font_colour=exit_game_text.font_colour,
                                    font=SETTINGS_FONT_SM,
                                    active=exit_game_text.active,
                                    screen=WINDOW,
                                    )
        exit_game_text_contrast = TextButton(
                                             text=exit_game_text.text,
                                             x=exit_game_text.x+1,
                                             y=exit_game_text.y+1,
                                             win_x_gap=exit_game_text.win_x_gap,
                                             win_y_gap=exit_game_text.win_y_gap,
                                             font_colour=BLACK,
                                             font=SETTINGS_FONT,
                                             active=False,
                                             screen=WINDOW,
                                             )

        exit_game_text_contrast.draw_to(WINDOW)
        exit_game_text.draw_to(WINDOW)

        menu_objects["exit_game_text"] = exit_game_text


    if True: # Music button
        music_button = menu_objects["music_button"]

        music_button_pos = (
                            int(win_width-win_width/music_button_div),
                            int(win_height/music_button_div),
                            )

        music_on_img = pygame.image.load(MUSIC_ON_PATH)
        music_on_img = pygame.transform.smoothscale(music_on_img, 
                                                    music_img_size,
                                                    )
        music_off_img = pygame.image.load(MUSIC_OFF_PATH)
        music_off_img = pygame.transform.smoothscale(music_off_img, 
                                                     music_img_size,
                                                     )
        
        music_button = ImageButton(x=music_button_pos[0],
                                   y=music_button_pos[1],
                                   win_x_gap=win_x_gap,
                                   win_y_gap=win_y_gap,
                                   active=music_button.active,
                                   image=music_on_img,
                                   )

        if music_volume != 0:
            music_button.image = music_on_img
        else:
            music_button.image = music_off_img

        music_button.draw_to(WINDOW)

        menu_objects["music_button"] = music_button


    return


def settings() -> None: 
    """
    Displays the settings page.
    """
    global screen, music_volume, settings_bg, settings_screen, \
           global_textbox_inactive_colour, global_textbox_active_colour, \
           settings_objects, title_spacing_div, global_font_colour, \
           global_hover_colour, fps_limit, click_sfx_volume \

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


    if True: # Backdrop for settings buttons

        settings_bg = pygame.Surface(
                            (
                                win_centrex + win_centrex/2, # Horizontal size 
                                win_centrey + win_centrey/4, # Vertical size 
                            ),
                            )

        settings_bg.fill(SETTINGS_GREY)

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


    base_box_pos: tuple = (
                           int(settings_bg_width/10),   # Xpos
                           int(settings_bg_height/5.7), # Ypos
                           )
    title_x_offset: int = int(base_box_pos[0]/1.5)
    title_y_offset: int = int(win_height/title_spacing_div)
    box_offset: float = win_width/RGB_TEXT_BOX_OFFSET_DIV
    title_box_y_offset: int = int(settings_bg_height/title_spacing_div)
    box_width: float = win_width/14.4
    box_height: float = win_height/norm_font_div + 10


    if True: # Music button
        music_button = settings_objects["music_button"]

        music_button_pos = (
                            int(win_width-win_width/music_button_div),
                            int(win_height/music_button_div),
                            )

        music_on_img = pygame.image.load(MUSIC_ON_PATH)
        music_on_img = pygame.transform.smoothscale(music_on_img, 
                                                    music_img_size,
                                                    )
        music_off_img = pygame.image.load(MUSIC_OFF_PATH)
        music_off_img = pygame.transform.smoothscale(music_off_img, 
                                                     music_img_size,
                                                     )
        
        music_button = ImageButton(x=music_button_pos[0],
                                   y=music_button_pos[1],
                                   win_x_gap=win_x_gap,
                                   win_y_gap=win_y_gap,
                                   active=music_button.active,
                                   image=music_on_img,
                                   always_visible=True,
                                   )

        if music_volume != 0:
            music_button.image = music_on_img
        else:
            music_button.image = music_off_img

        music_button.draw_to(WINDOW)

        settings_objects["music_button"] = music_button


    if True: # Version data + button

        current_version = settings_objects["current_version"]
        update_text = settings_objects["update_text"]
        update_button = settings_objects["update_button"]

        current_version_pos = (
                               int(win_width/72),
                               int(win_height/43.6),
                               )
        update_text_pos = (
                           int(win_width/72),
                           int(win_height/16),
                           )
        update_button_pos = (
                             int(win_width/72),
                             int(win_height/9.2588),
                             )

        current_version = Text(text=f"v{local_version}", 
                               x=current_version_pos[0], 
                               y=current_version_pos[1], 
                               win_x_gap=0, 
                               win_y_gap=0, 
                               font_colour=global_font_colour, 
                               font=current_version.font,
                               always_visible=True,
                               )
        update_text = Text(text=f"A new update is available -> v{web_version}", 
                           x=update_text_pos[0], 
                           y=update_text_pos[1], 
                           win_x_gap=0, 
                           win_y_gap=0, 
                           font_colour=global_font_colour, 
                           font=update_text.font,
                           always_visible=True,
                           )
        update_button = TextButton(text=f"Update Now", 
                                   x=update_button_pos[0], 
                                   y=update_button_pos[1], 
                                   win_x_gap=0, 
                                   win_y_gap=0, 
                                   font_colour=global_font_colour, 
                                   font=update_button.font,
                                   active=update_button.active,
                                   always_visible=True,
                                   screen=WINDOW,
                                   )

        current_version_contrast = Text(text=current_version.text, 
                                        x=current_version.x, 
                                        y=current_version.y, 
                                        win_x_gap=current_version.win_x_gap, 
                                        win_y_gap=current_version.win_y_gap, 
                                        font_colour=BLACK, 
                                        font=VER_FONT_SM,
                                        )
        update_text_contrast = Text(text=update_text.text, 
                                    x=update_text.x, 
                                    y=update_text.y, 
                                    win_x_gap=update_text.win_x_gap, 
                                    win_y_gap=update_text.win_y_gap, 
                                    font_colour=BLACK, 
                                    font=VER_FONT_SM,
                                    )
        update_button_contrast = TextButton(text=update_button.text, 
                                            x=update_button.x, 
                                            y=update_button.y, 
                                            win_x_gap=update_button.win_x_gap, 
                                            win_y_gap=update_button.win_y_gap, 
                                            font_colour=BLACK, 
                                            font=VER_FONT_SM,
                                            active=False,
                                            always_visible=True,
                                            screen=WINDOW,
                                            )

        current_version_contrast.draw_to(WINDOW)
        current_version.draw_to(WINDOW)

        if not up_to_date:
            update_text_contrast.draw_to(WINDOW)
            update_button_contrast.draw_to(WINDOW)
            update_text.draw_to(WINDOW)
            update_button.draw_to(WINDOW)

        settings_objects["current_version"] = current_version
        settings_objects["update_text"] = update_text
        settings_objects["update_button"] = update_button


    if True: # Return button (menu)

        return_text = settings_objects["return_text"]
        return_img_button = settings_objects["return_img_button"]

        return_text_pos: tuple = (
                                  int(settings_bg_width-settings_bg_width/27)-return_text.rect.width, # Xpos
                                  int(settings_bg_height/109),                                        # Ypos
                                  )
        return_img_pos: tuple = (
                                 int(return_text_pos[0]-return_text.rect.width/2.5),     # Xpos
                                 int(settings_bg_height/109+return_text.rect.height/10), # Ypos
                                 )

        return_img = pygame.image.load(RETURN_PATH)
        return_img = pygame.transform.smoothscale(return_img, return_img_size)

        return_text = TextButton(
                                 text="RETURN",
                                 x=int(return_text_pos[0]),
                                 y=int(return_text_pos[1]),
                                 win_x_gap=win_x_gap,
                                 win_y_gap=win_y_gap,
                                 font_colour=return_text.font_colour,
                                 font=SETTINGS_FONT,
                                 active=return_text.active,
                                 screen=settings_bg,
                                 )
        return_img_button = ImageButton(
                                        x=return_img_pos[0],
                                        y=return_img_pos[1],
                                        active = return_img_button.active,
                                        win_x_gap=win_x_gap,
                                        win_y_gap=win_y_gap,
                                        image=return_img,
                                        )

        return_text.draw_to(settings_bg)
        return_img_button.draw_to(settings_bg)

        settings_objects["return_text"] = return_text
        settings_objects["return_img_button"] = return_img_button


    if settings_screen == 0: # Main settings area

        if True: # Sound settings

            sound_text = settings_objects["sound_text"]
            sound_img_button = settings_objects["sound_img_button"]

            sound_img = pygame.transform.smoothscale(pygame.image.load(VOLUME_PATH), sound_img_size)

            sound_text_pos = (
                              int(settings_bg_width-settings_bg_width/3.5), # Xpos
                              int(settings_bg_height/4),                  # Ypos
                              )
            sound_img_pos = (
                             int(sound_text_pos[0]-1.5*sound_img_button.rect.width),  # Xpos
                             int(sound_text_pos[1]-sound_img_button.rect.height/3.5), # Ypos
                             )

            sound_text = TextButton(
                                    text="SOUND",
                                    x=int(sound_text_pos[0]),
                                    y=int(sound_text_pos[1]),
                                    win_x_gap=win_x_gap,
                                    win_y_gap=win_y_gap,
                                    font_colour=sound_text.font_colour,
                                    font=SETTINGS_FONT,
                                    active=sound_text.active,
                                    screen=settings_bg,
                                    )
            sound_img_button = ImageButton(
                                           x=sound_img_pos[0],
                                           y=sound_img_pos[1],
                                           win_x_gap=win_x_gap,
                                           win_y_gap=win_y_gap,
                                           image=sound_img,
                                           active=sound_img_button.active,
                                           )

            sound_text.draw_to(settings_bg)
            sound_img_button.draw_to(settings_bg)

            settings_objects["sound_text"] = sound_text
            settings_objects["sound_img_button"] = sound_img_button


        if True: # Visual settings

            visual_text = settings_objects["visual_text"]
            visual_img_button = settings_objects["visual_img_button"]

            visual_text_pos = (
                               int(settings_bg_width/6),  # Xpos
                               int(settings_bg_height/4), # Ypos
                               )
            visual_img_pos = (
                              int(visual_text_pos[0]-visual_text.rect.width/2),   # Xpos
                              int(visual_text_pos[1]-visual_img_button.rect.height/3.5), # Ypos
                              )

            visual_img = pygame.transform.smoothscale(pygame.image.load(VISUALS_PATH), visual_img_size)

            visual_text = TextButton(
                                     text="VISUALS",
                                     x=int(visual_text_pos[0]),
                                     y=int(visual_text_pos[1]),
                                     win_x_gap=win_x_gap,
                                     win_y_gap=win_y_gap,
                                     font_colour=visual_text.font_colour,
                                     font=SETTINGS_FONT,
                                     active=visual_text.active,
                                     screen=settings_bg,
                                     )
            visual_img_button = ImageButton(
                                            x=visual_img_pos[0],
                                            y=visual_img_pos[1],
                                            win_x_gap=win_x_gap,
                                            win_y_gap=win_y_gap,
                                            image=visual_img,
                                            active=visual_img_button.active,
                                            )

            visual_text.draw_to(settings_bg)
            visual_img_button.draw_to(settings_bg)

            settings_objects["visual_text"] = visual_text
            settings_objects["visual_img_button"] = visual_img_button


        if True: # General info + socials (dicsord server join code)
        
            info_text = settings_objects["info_text"]
            info_img_button = settings_objects["info_img_button"]

            info_img = pygame.transform.smoothscale(pygame.image.load(INFO_PATH), info_img_size)

            info_text_pos = (
                             int(settings_bg_width/6),                       # Xpos
                             int(settings_bg_height-settings_bg_height/3.5), # Ypos
                             )
            info_img_pos = (
                            int(info_text_pos[0]-(info_text.rect.width/2)), # Xpos
                            int(info_text_pos[1]-(info_img_button.rect.height/3.5)), # Ypos
                            )

            info_text = TextButton(
                                   text="INFO",
                                   x=int(info_text_pos[0]),
                                   y=int(info_text_pos[1]),
                                   win_x_gap=win_x_gap,
                                   win_y_gap=win_y_gap,
                                   font_colour=info_text.font_colour,
                                   font=SETTINGS_FONT,
                                   active=info_text.active,
                                   screen=settings_bg,
                                   )
            info_img_button = ImageButton(
                                          x=info_img_pos[0],
                                          y=info_img_pos[1],
                                          win_x_gap=win_x_gap,
                                          win_y_gap=win_y_gap,
                                          image=info_img,
                                          active=info_img_button.active,
                                          )

            info_text.draw_to(settings_bg)
            info_img_button.draw_to(settings_bg)

            settings_objects["info_text"] = info_text
            settings_objects["info_img_button"] = info_img_button


        if True: # Credits
        
            credits_text = settings_objects["credits_text"]
            credits_img_button = settings_objects["credits_img_button"]

            credits_img = pygame.transform.smoothscale(pygame.image.load(CREDITS_PATH), credits_img_size)

            credits_text_pos = (
                                int(settings_bg_width-settings_bg_width/3.5),   # Xpos
                                int(settings_bg_height-settings_bg_height/3.5), # Ypos
                                )
            credits_img_pos = (
                               int(credits_text_pos[0] - (credits_text.rect.width/1.5)), # Xpos
                               int(credits_text_pos[1] - (credits_img_button.rect.height/3.5)), # Ypos
                               )

            credits_text = TextButton(
                                      text="CREDITS",
                                      x=int(credits_text_pos[0]),
                                      y=int(credits_text_pos[1]),
                                      win_x_gap=win_x_gap,
                                      win_y_gap=win_y_gap,
                                      font_colour=credits_text.font_colour,
                                      font=SETTINGS_FONT,
                                      active=credits_text.active,
                                      screen=settings_bg,
                                      )
            credits_img_button = ImageButton(
                                             x=credits_img_pos[0],
                                             y=credits_img_pos[1],
                                             win_x_gap=win_x_gap,
                                             win_y_gap=win_y_gap,
                                             image=credits_img,
                                             active=credits_img_button.active,
                                             )

            credits_text.draw_to(settings_bg)
            credits_img_button.draw_to(settings_bg)

            settings_objects["credits_text"] = credits_text
            settings_objects["credits_img_button"] = credits_img_button


    elif settings_screen == 1: # Credits
        
        if True: # Menu music credits

            menu_music_credit_text = settings_objects["menu_music_credit_text"]

            menu_music_credit_text_pos = (
                                          int(settings_bg_width/10), # Xpos
                                          int(settings_bg_height/6), # Ypos
                                          )
            menu_music_credit_text = Text(
                                          text='Menu music by "Ivymusic" on pixabay.com',
                                          x=menu_music_credit_text_pos[0],
                                          y=menu_music_credit_text_pos[1],
                                          win_x_gap=0,
                                          win_y_gap=0,
                                          font_colour=global_font_colour,
                                          font=FONT,
                                          )

            menu_music_credit_text.draw_to(settings_bg)

            settings_objects["menu_music_credit_text"] = menu_music_credit_text


        if True: # Click sfx credits

            click_sfx_credit_text = settings_objects["click_sfx_credit_text"]

            click_sfx_credit_text_pos = (
                                         int(menu_music_credit_text_pos[0]),   # Xpos
                                         int(2*menu_music_credit_text_pos[1]), # Ypos
                                         )
            click_sfx_credit_text = Text(
                                          text='Click sfx by "MatthewVakaliuk73627" on pixabay.com',
                                          x=click_sfx_credit_text_pos[0],
                                          y=click_sfx_credit_text_pos[1],
                                          win_x_gap=0,
                                          win_y_gap=0,
                                          font_colour=global_font_colour,
                                          font=FONT,
                                          )

            click_sfx_credit_text.draw_to(settings_bg)

            settings_objects["click_sfx_credit_text"] = click_sfx_credit_text


        if True: # Menu bg credits

            menu_bg_credit_text = settings_objects["menu_bg_credit_text"]

            menu_bg_credit_text_pos = (
                                       int(click_sfx_credit_text_pos[0]),   # Xpos
                                       int(2*click_sfx_credit_text_pos[1]), # Ypos
                                       )
            menu_bg_credit_text = Text(
                                       text="All menu background images captured by NASA, and posted on their instagram.",
                                       x=menu_bg_credit_text_pos[0],
                                       y=menu_bg_credit_text_pos[1],
                                       win_x_gap=0,
                                       win_y_gap=0,
                                       font_colour=global_font_colour,
                                       font=FONT,
                                       )

            menu_bg_credit_text.draw_to(settings_bg)

            settings_objects["menu_bg_credit_text"] = menu_bg_credit_text


        if True: # Inspiration credits
            inspo_text = settings_objects["inspo_text"]

            inspo_text_pos = (
                              int(menu_bg_credit_text_pos[0]),   # Xpos
                              int(2*menu_bg_credit_text_pos[1]), # Ypos
                              )
            inspo_text = Text(
                              text="This game is heavily inspired by Stef's Spaceflight Simulator.",
                              x=inspo_text_pos[0],
                              y=inspo_text_pos[1],
                              win_x_gap=0,
                              win_y_gap=0,
                              font_colour=global_font_colour,
                              font=FONT,
                              )

            inspo_text.draw_to(settings_bg)

            settings_objects["inspo_text"] = inspo_text


    elif settings_screen == 2: # General info + socials

        discord_link_text = settings_objects["discord_link_text"]

        discord_link_text_pos = (
                                 int(settings_bg_width/10),   # Xpos
                                 int(2*(settings_bg_height/6)), # Ypos
                                 )
        discord_link_text = Text(
                                 text="Official Discord: 'discord.gg/JymnDDbK9c'",
                                 x=discord_link_text_pos[0],
                                 y=discord_link_text_pos[1],
                                 win_x_gap=0,
                                 win_y_gap=0,
                                 font_colour=global_font_colour,
                                 font=FONT,
                                 )

        discord_link_text.draw_to(settings_bg)

        settings_objects["discord_link_text"] = discord_link_text


    elif settings_screen == 3: # Visual settings - e.g. fps, text colour, hover colour

        if True: # global font colour

            font_colour_input_box_R = settings_objects["font_colour_input_box_R"]
            font_colour_input_box_G = settings_objects["font_colour_input_box_G"]
            font_colour_input_box_B = settings_objects["font_colour_input_box_B"]
            font_colour_text = settings_objects["font_colour_text"]

            font_colour_text = Text(text="Text colour:",
                                    font_colour=global_font_colour,
                                    win_x_gap=0,
                                    win_y_gap=0,
                                    x=base_box_pos[0]-title_x_offset,
                                    y=base_box_pos[1]-int(0.5*title_y_offset),
                                    font=font_colour_text.font
                                    )
            font_colour_input_box_R = RGBInputBox(x=base_box_pos[0],
                                                  y=font_colour_text.y+title_box_y_offset,
                                                  width=box_width,
                                                  height=box_height,
                                                  win_x_gap=win_x_gap,
                                                  win_y_gap=win_y_gap,
                                                  active=font_colour_input_box_R.active,
                                                  text=font_colour_input_box_R.text,
                                                  pre_box_text=font_colour_input_box_R.pre_box_text,
                                                  suff_box_text=font_colour_input_box_R.suff_box_text,
                                                  font=font_colour_input_box_R.font,
                                                  )
            font_colour_input_box_G = RGBInputBox(x=int(font_colour_input_box_R.rect.x + font_colour_input_box_R.rect.width + box_offset),
                                                  y=int(font_colour_input_box_R.rect.y),
                                                  width=box_width,
                                                  height=box_height,
                                                  win_x_gap=win_x_gap,
                                                  win_y_gap=win_y_gap,
                                                  active=font_colour_input_box_G.active,
                                                  text=font_colour_input_box_G.text,
                                                  pre_box_text=font_colour_input_box_G.pre_box_text,
                                                  font=font_colour_input_box_G.font,
                                                  )
            font_colour_input_box_B = RGBInputBox(x=int(font_colour_input_box_G.rect.x + font_colour_input_box_G.rect.width + box_offset),
                                                  y=int(font_colour_input_box_R.rect.y),
                                                  width=box_width,
                                                  height=box_height,
                                                  win_x_gap=win_x_gap,
                                                  win_y_gap=win_y_gap,
                                                  active=font_colour_input_box_B.active,
                                                  text=font_colour_input_box_B.text,
                                                  pre_box_text=font_colour_input_box_B.pre_box_text,
                                                  font=font_colour_input_box_B.font,
                                                  )

            settings_objects["font_colour_input_box_R"] = font_colour_input_box_R
            settings_objects["font_colour_input_box_G"] = font_colour_input_box_G
            settings_objects["font_colour_input_box_B"] = font_colour_input_box_B
            settings_objects["font_colour_text"] = font_colour_text

            font_colour_input_box_R.draw_to(settings_bg)
            font_colour_input_box_G.draw_to(settings_bg)
            font_colour_input_box_B.draw_to(settings_bg)
            font_colour_text.draw_to(settings_bg)

            if True:
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

            hover_colour_text = Text(text="Text hover colour:",
                                     font_colour=global_hover_colour,
                                     win_x_gap=0,
                                     win_y_gap=0,
                                     x=font_colour_text.x,
                                     y=font_colour_input_box_R.y+title_y_offset,
                                     font=hover_colour_text.font,
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
                                                   font=hover_colour_input_box_R.font,
                                                   )
            hover_colour_input_box_G = RGBInputBox(x=font_colour_input_box_G.x,
                                                   y=hover_colour_input_box_R.y,
                                                   width=box_width,
                                                   height=box_height,
                                                   win_x_gap=win_x_gap,
                                                   win_y_gap=win_y_gap,
                                                   active=hover_colour_input_box_G.active,
                                                   text=hover_colour_input_box_G.text,
                                                   pre_box_text=hover_colour_input_box_G.pre_box_text,
                                                   font=hover_colour_input_box_G.font,
                                                   )
            hover_colour_input_box_B = RGBInputBox(x=font_colour_input_box_B.x,
                                                   y=hover_colour_input_box_R.y,
                                                   width=box_width,
                                                   height=box_height,
                                                   win_x_gap=win_x_gap,
                                                   win_y_gap=win_y_gap,
                                                   active=hover_colour_input_box_B.active,
                                                   text=hover_colour_input_box_B.text,
                                                   pre_box_text=hover_colour_input_box_B.pre_box_text,
                                                   font=hover_colour_input_box_B.font,
                                                   )

            hover_colour_input_box_R.draw_to(settings_bg)
            hover_colour_input_box_G.draw_to(settings_bg)
            hover_colour_input_box_B.draw_to(settings_bg)
            hover_colour_text.draw_to(settings_bg)

            settings_objects["hover_colour_input_box_R"] = hover_colour_input_box_R
            settings_objects["hover_colour_input_box_G"] = hover_colour_input_box_G
            settings_objects["hover_colour_input_box_B"] = hover_colour_input_box_B
            settings_objects["hover_colour_text"] = hover_colour_text

            if True:
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

            textbox_active_colour_text = Text(text="Border colour (active):",
                                              font_colour=global_textbox_active_colour,
                                              win_x_gap=0,
                                              win_y_gap=0,
                                              x=hover_colour_text.x,
                                              y=hover_colour_input_box_R.y+title_y_offset,
                                              font=textbox_active_colour_text.font,
                                              )

            textbox_active_colour_input_box_R = RGBInputBox(x=base_box_pos[0],
                                                            y=textbox_active_colour_text.y+title_box_y_offset,
                                                            width=box_width,
                                                            height=box_height,
                                                            win_x_gap=win_x_gap,
                                                            win_y_gap=win_y_gap,
                                                            active=textbox_active_colour_input_box_R.active,
                                                            text=textbox_active_colour_input_box_R.text,
                                                            pre_box_text=textbox_active_colour_input_box_R.pre_box_text,
                                                            font=textbox_active_colour_input_box_R.font,
                                                            )
            textbox_active_colour_input_box_G = RGBInputBox(x=hover_colour_input_box_G.x,
                                                            y=textbox_active_colour_input_box_R.y,
                                                            width=box_width,
                                                            height=box_height,
                                                            win_x_gap=win_x_gap,
                                                            win_y_gap=win_y_gap,
                                                            active=textbox_active_colour_input_box_G.active,
                                                            text=textbox_active_colour_input_box_G.text,
                                                            pre_box_text=textbox_active_colour_input_box_G.pre_box_text,
                                                            font=textbox_active_colour_input_box_G.font
                                                            )
            textbox_active_colour_input_box_B = RGBInputBox(x=hover_colour_input_box_B.x,
                                                            y=textbox_active_colour_input_box_R.y,
                                                            width=box_width,
                                                            height=box_height,
                                                            win_x_gap=win_x_gap,
                                                            win_y_gap=win_y_gap,
                                                            active=textbox_active_colour_input_box_B.active,
                                                            text=textbox_active_colour_input_box_B.text,
                                                            pre_box_text=textbox_active_colour_input_box_B.pre_box_text,
                                                            font=textbox_active_colour_input_box_B.font,
                                                            )

            textbox_active_colour_input_box_R.draw_to(settings_bg)
            textbox_active_colour_input_box_G.draw_to(settings_bg)
            textbox_active_colour_input_box_B.draw_to(settings_bg)
            textbox_active_colour_text.draw_to(settings_bg)

            settings_objects["textbox_active_colour_input_box_R"] = textbox_active_colour_input_box_R
            settings_objects["textbox_active_colour_input_box_G"] = textbox_active_colour_input_box_G
            settings_objects["textbox_active_colour_input_box_B"] = textbox_active_colour_input_box_B
            settings_objects["textbox_active_colour_text"] = textbox_active_colour_text

            if True:
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

            textbox_inactive_colour_text = Text(text="Border colour (inactive):",
                                                font_colour=global_textbox_inactive_colour,
                                                win_x_gap=0,
                                                win_y_gap=0,
                                                x=hover_colour_text.x,
                                                y=textbox_active_colour_input_box_R.y+title_y_offset,
                                                font=textbox_inactive_colour_text.font,
                                                )
            textbox_inactive_colour_input_box_R = RGBInputBox(x=base_box_pos[0],
                                                              y=textbox_inactive_colour_text.y+title_box_y_offset,
                                                              width=box_width,
                                                              height=box_height,
                                                              win_x_gap=win_x_gap,
                                                              win_y_gap=win_y_gap,
                                                              active=textbox_inactive_colour_input_box_R.active,
                                                              text=textbox_inactive_colour_input_box_R.text,
                                                              pre_box_text=textbox_inactive_colour_input_box_R.pre_box_text,
                                                              font=textbox_inactive_colour_input_box_R.font,
                                                              )
            textbox_inactive_colour_input_box_G = RGBInputBox(x=textbox_active_colour_input_box_G.x,
                                                              y=textbox_inactive_colour_input_box_R.y,
                                                              width=box_width,
                                                              height=box_height,
                                                              win_x_gap=win_x_gap,
                                                              win_y_gap=win_y_gap,
                                                              active=textbox_inactive_colour_input_box_G.active,
                                                              text=textbox_inactive_colour_input_box_G.text,
                                                              pre_box_text=textbox_inactive_colour_input_box_G.pre_box_text,
                                                              font=textbox_inactive_colour_input_box_G.font,
                                                              )
            textbox_inactive_colour_input_box_B = RGBInputBox(x=textbox_active_colour_input_box_B.x,
                                                              y=textbox_inactive_colour_input_box_R.y,
                                                              width=box_width,
                                                              height=box_height,
                                                              win_x_gap=win_x_gap,
                                                              win_y_gap=win_y_gap,
                                                              active=textbox_inactive_colour_input_box_B.active,
                                                              text=textbox_inactive_colour_input_box_B.text,
                                                              pre_box_text=textbox_inactive_colour_input_box_B.pre_box_text,
                                                              font=textbox_inactive_colour_input_box_B.font,
                                                              )

            textbox_inactive_colour_input_box_R.draw_to(settings_bg)
            textbox_inactive_colour_input_box_G.draw_to(settings_bg)
            textbox_inactive_colour_input_box_B.draw_to(settings_bg)
            textbox_inactive_colour_text.draw_to(settings_bg)

            settings_objects["textbox_inactive_colour_input_box_R"] = textbox_inactive_colour_input_box_R
            settings_objects["textbox_inactive_colour_input_box_G"] = textbox_inactive_colour_input_box_G
            settings_objects["textbox_inactive_colour_input_box_B"] = textbox_inactive_colour_input_box_B
            settings_objects["textbox_inactive_colour_text"] = textbox_inactive_colour_text

            if True:
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

            fps_limit_text = Text(text="FPS limit:",
                                  x=int(font_colour_text.x+font_colour_input_box_B.x+1.2*title_x_offset),
                                  y=font_colour_text.y,
                                  win_x_gap=0,
                                  win_y_gap=0,
                                  font_colour=global_font_colour,
                                  font=fps_limit_text.font,
                                  )
            fps_limit_input_box = NumberInputBox(x=fps_limit_text.x+title_x_offset,
                                                 y=fps_limit_text.y+title_box_y_offset,
                                                 width=box_width,
                                                 height=box_height,
                                                 win_x_gap=win_x_gap,
                                                 win_y_gap=win_y_gap,
                                                 active=fps_limit_input_box.active,
                                                 text=fps_limit_input_box.text,
                                                 max_int=max_fps,
                                                 pre_box_text=fps_limit_input_box.pre_box_text,
                                                 suff_box_text=fps_limit_input_box.suff_box_text,
                                                 font=fps_limit_input_box.font,
                                                 )

            fps_limit_text.draw_to(settings_bg)
            fps_limit_input_box.draw_to(settings_bg)

            settings_objects["fps_limit_input_box"] = fps_limit_input_box
            settings_objects["fps_limit_text"] = fps_limit_text

            if fps_limit_input_box.text == '':
                fps_limit = 0
                fps_limit_input_box.pre_box_text = '0'
            
            else:
                fps_limit = int(fps_limit_input_box.text)
                fps_limit_input_box.pre_box_text = ''

            SETTINGS_DATA["fps_limit"] = fps_limit


    elif settings_screen == 4: # Sound settings

        if True: # music volume
            music_volume_text = settings_objects["music_volume_text"]
            music_volume_input_box = settings_objects["music_volume_input_box"]

            music_volume_text = Text(text="Music Volume:",
                                         x=base_box_pos[0]-title_x_offset,
                                         y=base_box_pos[1]-int(0.5*title_y_offset),
                                         win_x_gap=0,
                                         win_y_gap=0,
                                         font_colour=global_font_colour,
                                         font=music_volume_text.font,
                                         )
            music_volume_input_box = NumberInputBox(x=base_box_pos[0],
                                                    y=base_box_pos[1],
                                                    width=box_width,
                                                    height=box_height,
                                                    win_x_gap=win_x_gap,
                                                    win_y_gap=win_y_gap,
                                                    active=music_volume_input_box.active,
                                                    text=music_volume_input_box.text,
                                                    max_int=100,
                                                    pre_box_text=music_volume_input_box.pre_box_text,
                                                    suff_box_text=music_volume_input_box.suff_box_text,
                                                    font=music_volume_input_box.font,
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
            
            click_sfx_volume_text = Text(x=music_volume_text.x,
                                         y=music_volume_input_box.y+title_y_offset,
                                         win_x_gap=0,
                                         win_y_gap=0,
                                         font_colour=global_font_colour,
                                         text="Click SFX volume:",
                                         font=click_sfx_volume_text.font,
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
                                                        font=click_sfx_volume_input_box.font,
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

    save_timer_timer.cancel()
    save()

    time.sleep(0.1)

    start_updater()


def start_updater() -> NoReturn:
    
    args = [sys.executable, UPDATE_FILE_PATH]
    subprocess.Popen(args, start_new_session=True)
    pygame.quit()
    exit(0)


def enter_vab() -> None: 
    global screen, VAB_objects
    screen = 4

    pygame.mixer.music.stop()

    clear_screen(BLUEPRINT_BG_PURPLE)

    if True: # Blueprint

        blueprint = VAB_objects["grid"]

        underlay_left = VAB_objects["underlay_left"]
        underlay_bottom = VAB_objects["underlay_bottom"]
        underlay_right = VAB_objects["underlay_right"]

        blueprint_coords = (
                            int(underlay_left.dimensions[0]),
                            0,
                            )
        blueprint_dimensions = (
                                int(win_width-(underlay_right.dimensions[0]+blueprint_coords[0])),
                                int(win_height-underlay_bottom.dimensions[1]),
                                )

        blueprint = BlueprintGrid(
                                  width=blueprint_dimensions[0],
                                  height=blueprint_dimensions[1],
                                  cell_size=int(win_width/48),
                                  cell_wall_colour=BLUEPRINT_CELL_WALL_BLUE,
                                  comps=blueprint.components,
                                  background_colour=BLUEPRINT_BG_PURPLE,
                                  )
        
        VAB_objects["grid"] = blueprint

        blueprint.draw_to(screen=WINDOW, grid_start_coords=blueprint_coords)


    if True: # UI background

        underlay_left = VAB_objects["underlay_left"]

        underlay_left = UiUnderlay(
                                   colour=BLUEPRINT_UI_BG_PURPLE,
                                   width=int(win_width/5.5),
                                   height=int(win_height),
                                   coords=(0, 0),
                                   )

        underlay_left.draw_to(WINDOW)

        VAB_objects["underlay_left"] = underlay_left



        underlay_bottom = VAB_objects["underlay_bottom"]

        underlay_bottom = UiUnderlay(
                                     colour=BLUEPRINT_UI_BG_PURPLE,
                                     width=int(win_width),
                                     height=int(win_height/6),
                                     coords=(0, int(win_height-win_height/6)),
                                     )

        underlay_bottom.draw_to(WINDOW)

        VAB_objects["underlay_bottom"] = underlay_bottom



        underlay_right = VAB_objects["underlay_right"]

        underlay_right = UiUnderlay(
                                    colour=BLUEPRINT_UI_BG_PURPLE,
                                    width=int(win_width/6.2),
                                    height=int(win_height),
                                    coords=(int(win_width-win_width/6.2), 0),
                                    )

        underlay_right.draw_to(WINDOW)

        VAB_objects["underlay_right"] = underlay_right


    if True: # Activation groups

        pass # complete this after "parts" has been completed


    if True: # Rocket stats (height, part count, thrust/weight ratio, e.t.c.)

        thrust_weight_ratio = 0

        height_text = VAB_objects["height_text"]

        height_text = Text(
                           text=f"Height: {blueprint.get_rocket_height()}m",
                           x=int(win_width-win_width/6.35),
                           y=int(win_height/44),
                           win_x_gap=0,
                           win_y_gap=0,
                           font_colour=global_font_colour,
                           font=FONT,
                           )

        height_text.draw_to(WINDOW)

        VAB_objects["height_text"] = height_text


        part_count_text = VAB_objects["part_count_text"]

        part_count_text = Text(
                               text=f"Parts: {blueprint.get_part_count()}",
                               x=height_text.x,
                               y=3*height_text.y,
                               win_x_gap=0,
                               win_y_gap=0,
                               font_colour=global_font_colour,
                               font=FONT,
                               )

        part_count_text.draw_to(WINDOW)

        VAB_objects["part_count_text"] = part_count_text


        thrust_weight_ratio_text = VAB_objects["thrust_weight_ratio_text"]
        thrust_weight_ratio_text_2 = VAB_objects["thrust_weight_ratio_text_2"]

        thrust_weight_ratio_text = Text(
                                        text="Thrust/Weight:",
                                        x=part_count_text.x,
                                        y=5*height_text.y,
                                        win_x_gap=0,
                                        win_y_gap=0,
                                        font_colour=global_font_colour,
                                        font=FONT,
                                        )
        thrust_weight_ratio_text_2 = Text(
                                          text=f"{thrust_weight_ratio}",
                                          x=thrust_weight_ratio_text.x,
                                          y=int(thrust_weight_ratio_text.y+win_height/35),
                                          win_x_gap=0,
                                          win_y_gap=0,
                                          font_colour=global_font_colour,
                                          font=FONT,
                                          )

        thrust_weight_ratio_text.draw_to(WINDOW)
        thrust_weight_ratio_text_2.draw_to(WINDOW)

        VAB_objects["thrust_weight_ratio_text"] = thrust_weight_ratio_text
        VAB_objects["thrust_weight_ratio_text_2"] = thrust_weight_ratio_text_2


    if True: # Launch button

        ...


    if True: # Save button

        ...


    if True: # Load button

        ...


    if True: # Return to menu button

        ...


    if True: # Colour section

        ...


    if True: # Parts section


        if True: # Parts categories

            ...


        if True: # Structure, Capsules/Probes

            ...


        if True: # Propulsion, Fuel, Aerodynamic

            ...


        if True: # Docking, Landing

            ...


        if True: # Electrics

            ...


        if True: # Other

            ...


    return


def start_simulation() -> None: 
    global screen
    screen = 5

    return


def main() -> None:

    global local_version, web_version, up_to_date, win_width, win_height, \
            win_right, win_bottom, win_centrex, win_centrey, VER_FONT, FONT, \
            music_volume, exit_game, settings_screen, previous_volume, \
            SETTINGS_FONT, VER_FONT_SM, FONT_SM, SETTINGS_FONT_SM, screen, \
            menu_objects, settings_objects, settings_objects

    clock = pygame.time.Clock()
    running: bool = True
    local_version = get_local_version()
    web_version = get_web_version()
    dt: float = 0
    up_to_date = check_update()

    main_menu()

    while running:
        for pyevent in pygame.event.get():
            if pyevent.type == pygame.QUIT: # pressed X button on window
                running = False
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
                SETTINGS_FONT = pygame.font.SysFont(name="Courier", size=int(win_height/settings_font_div), bold=True)
                FONT_SM = pygame.font.SysFont(name="Courier", size=int(win_height/norm_font_div)-2, bold=True)
                VER_FONT_SM = pygame.font.SysFont(name="Comic-Sans", size=int(win_height/ver_font_div)-2, bold=True)
                SETTINGS_FONT_SM = pygame.font.SysFont(name="Courier", size=int(win_height/settings_font_div)-2, bold=True)

            if screen == 1: # Main Menu

                main_menu()

                for obj in menu_objects.values():
                    if obj.type == CLICKABLE:
                        obj.handle_event(pyevent)

                if menu_objects["start_text"].active: # Enter the VAB
                    menu_objects["start_text"].active = False
                    screen = 4

                elif menu_objects["settings_text"].active: # Enter settings
                    menu_objects["settings_text"].active = False
                    screen = 2

                elif menu_objects["exit_game_text"].active: # Exit the game
                    menu_objects["exit_game_text"].active = False
                    running = False
                    break

                elif menu_objects["update_button"].active: # Update game
                    menu_objects["update_button"].active = False
                    version_update()

                elif menu_objects["music_button"].active: # Music swap
                    menu_objects["music_button"].active = False

                    if music_volume != 0:
                        previous_volume = music_volume
                        music_volume = 0

                    else:
                        music_volume = previous_volume
 
            elif screen == 2: # Settings

                settings()

                for obj in settings_objects.values():
                    if obj.type == CLICKABLE:
                        obj.handle_event(pyevent)

                if settings_objects["music_button"].active: # Music swap
                    menu_objects["music_button"].active = False

                    if music_volume != 0:
                        previous_volume = music_volume
                        music_volume = 0

                    else:
                        music_volume = previous_volume

                elif settings_objects["update_button"].active:
                    settings_objects["update_button"].active = False

                    if not up_to_date and web_version != "":
                        # Wants to update the game
                        click_chanel.play(click_sfx)
                        version_update()
                        continue

                elif settings_objects["return_text"].active:
                    settings_objects["return_text"].active = False

                    if settings_screen == 0: # In the main settings screen
                        # Wants to return to the main menu
                        click_chanel.play(click_sfx)
                        screen = 1
                        main_menu() # Display the main menu
                        continue

                    else: # Not in the main settings screen
                        # Wants to return to the main settings screen
                        click_chanel.play(click_sfx)
                        settings_screen = 0 # Change to main settings

                    for obj in settings_objects.values():
                        if obj.type == CLICKABLE: # If the object can be coloured
                            obj.active = False # Reset it's activity to default

                elif settings_screen == 0: # Main settings zone
                    if settings_objects["credits_text"].active: 
                        settings_objects["credits_text"].active = False
                        click_chanel.play(click_sfx)
                        settings_screen = 1
                        continue

                    elif settings_objects["info_text"].active:
                        settings_objects["info_text"].active = False
                        click_chanel.play(click_sfx)
                        settings_screen = 2
                        continue

                    elif settings_objects["visual_text"].active:
                        settings_objects["visual_text"].active = False
                        click_chanel.play(click_sfx)
                        settings_screen = 3
                        continue

                    elif settings_objects["sound_text"].active: 
                        settings_objects["sound_text"].active = False
                        click_chanel.play(click_sfx)
                        settings_screen = 4
                        continue

            elif screen == 4: # VAB
                enter_vab()
                continue

            elif screen == 5: # Game
                start_simulation()
                continue

            # REMOVE FOR DISTRIBUTION
            if pyevent.type == pygame.KEYDOWN:
                if pyevent.key == pygame.K_ESCAPE:
                    version_update()

        pygame.display.flip()
        dt = clock.tick(fps_limit) / 100

    pygame.quit()
    save_timer_timer.cancel()
    save()
    return


if __name__ == '__main__':
    save_timer_timer = SaveTimer(save_timer_delay, save)
    save_timer_timer.start()
    main()
