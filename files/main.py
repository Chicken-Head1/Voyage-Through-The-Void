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
    loading_text = FONT.render("Loading...",
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



if __name__ == '__main__':
    import pygame



pygame.init()
WINDOW = pygame.display.set_mode(flags=pygame.RESIZABLE)
loading_screen()



import requests
import os, stat, sys
from json import load, dump
from typing import NoReturn
from threading import Thread
import subprocess



DIRPATH: str = os.path.dirname(os.path.abspath(__file__))
FILEPATH: str = f'{os.path.abspath(__file__)}'

VERSION_URL = "https://chicken-head1.github.io/Space-Simulator/version.md"
VERSION_PATH = f"/{os.path.join(DIRPATH, "data", "version.txt")}"
MENU_BG_PATH = f"/{os.path.join(DIRPATH, "images", "menu_bg.jpeg")}"
CURSOR_PATH = f"/{os.path.join(DIRPATH, "images", "cursor.svg")}"
MAIN_MENU_MUSIC_PATH = f"/{os.path.join(DIRPATH, "sound", "main_menu.mp3")}"
MUSIC_ON_PATH = f"/{os.path.join(DIRPATH, "images", "music_on.svg")}"
MUSIC_OFF_PATH = f"/{os.path.join(DIRPATH, "images", "music_off.svg")}"
CLICK_SFX_PATH = f"/{os.path.join(DIRPATH, "sound", "click_sfx.mp3")}"
RETURN_PATH = f"/{os.path.join(DIRPATH, "images", "return.svg")}"
UPDATE_FILE_PATH = f"{os.path.join(DIRPATH, "update", "main.py")}"

CURSOR_SIZE: tuple[int, int] = (15, 15)
music_img_size: tuple[int, int] = (50, 50)
return_img_size: tuple[int, int] = (30, 30)

win_width = WINDOW.get_width()
win_height = WINDOW.get_height()
win_right = win_width
win_bottom = win_height
win_left = 0
win_top = 0
win_centrex = win_width/2
win_centrey = win_height/2

ver_font_div = 43.6
norm_font_div = 21.8
spacing_div = 5
return_img_div = 5

FONT = pygame.font.SysFont(name="Courier", size=int(win_height/norm_font_div), bold=True)
VER_FONT = pygame.font.SysFont(name="Comic-Sans", size=int(win_height/ver_font_div), bold=True)
DOWNLOADING_FONT = pygame.font.SysFont(name='Courier', size=int(win_height/10.9))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HOVER_COLOUR = (187, 211, 255)
MENU_GREY = (130, 130, 130)

settings_font_colour = WHITE
start_game_font_colour = WHITE
exit_game_font_colour = WHITE
version_update_font_colour = WHITE


web_version: str = str()
current_version: str = str()
up_to_date: bool = True

screen: int = 0

max_fps: int = 240
fps_limit: float = 60

music_volume: float = 0.15
click_sfx_volume: float = 1

music_button_div: float = 17.44

# Menu button rects
settings_box_menu = pygame.Rect
version_box_menu = pygame.Rect
start_box_menu = pygame.Rect
exit_box_menu = pygame.Rect
music_on_box_menu_settings = pygame.Rect
music_off_box_menu_settings = pygame.Rect
update_button_rect = pygame.Rect
update_button = pygame.font


# Settings button rects

return_img_box = pygame.Rect


def get_local_version() -> str:
    """
    Gets the current local game version.

    :return str: A string containing version information.
    """

    with open(VERSION_PATH, 'r') as version:
        ver = list(version.read())
        ver.pop()

    vers = str()

    for i in ver:
        vers += i

    return vers


def get_web_version() -> str:
    """
    Gets the current website game version.

    :return str: A string containing version information.
    """

    try:
        version = requests.get(url=VERSION_URL)
        version = str(version.content).removeprefix("b'").removesuffix("\\n'")

    except:
        print("Failed to access server.")
        version = ""

    return version


def check_update() -> bool:
    """
    Check for a new game version.

    :return: bool: True if the server could not be accessed or the current version is the most up to date version and False if the version is not up to date.
    """
    
    if web_version == current_version or web_version == "":
        return True

    return False


def update_mouse(window: pygame.Surface, 
                 cursor_img_rect: pygame.Rect, 
                 cursor_img: pygame.Surface,
                 ) -> NoReturn:
    """
    Updates the mouse image and position.

    :param window: a Surface for the mouse to be updated upon.
    :param cursor_img_rect: The pygame rect from the cursor image.
    :param cursor_img: The pygame loaded image of the cursor.

    :return NoReturn: This is intended to be a threadded function. Has no return due to infinite loop. Thread is meant to be daemon.
    """

    while True:
        cursor_img_rect.topleft = pygame.mouse.get_pos() # get pos of the mouse
        window.blit(pygame.transform.smoothscale(cursor_img, CURSOR_SIZE), cursor_img_rect) # change the mouse image to the custom one


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

    version_text = VER_FONT.render(f"{current_version}", True, WHITE)
    new_update = VER_FONT.render(f"A new update is available -> {web_version}", True, WHITE) 
    update_button = VER_FONT.render(f"Update Now", True, version_update_font_colour) # upon pressing "update now", do a get request for the updated files on git
    update_button_rect = update_button.get_rect()
    version_box_menu = pygame.Rect(int(win_width/72),          # Xpos
                                   int(win_height/9.2588),     # Ypos
                                   update_button_rect.width,   # width
                                   update_button_rect.height,  # height
                                   )

    start_text = FONT.render("Enter the VAB", True, start_game_font_colour)
    start_text_rect = start_text.get_rect()
    start_box_menu = pygame.Rect(win_centrex-int(start_text_rect.width/2), # Xpos
                                 win_centrey-int(win_height/spacing_div),  # Ypos
                                 start_text_rect.width,                    # width
                                 start_text_rect.height,                   # height
                                 )

    settings_text = FONT.render("Settings", True, settings_font_colour)
    settings_text_rect = settings_text.get_rect()
    settings_box_menu = pygame.Rect(win_centrex-int(settings_text_rect.width/2), # Xpos
                                    win_centrey,                                 # Ypos
                                    settings_text_rect.width,                    # width
                                    settings_text_rect.height,                   # height
                                    )

    exit_game = FONT.render("Exit Game", True, exit_game_font_colour)
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
           return_img_box

    if screen != 2:
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

    version_text = VER_FONT.render(f"{current_version}", True, WHITE)
    new_update = VER_FONT.render(f"A new update is available -> {web_version}", True, WHITE) 
    update_button = VER_FONT.render(f"Update Now", True, version_update_font_colour) # upon pressing "update now", do a get request for the updated files on git
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

    return_img = pygame.image.load(RETURN_PATH)
    return_img = pygame.transform.smoothscale(return_img, 
                                              return_img_size,
                                              )
    return_img_rect = return_img.get_rect()
    return_img_pos: tuple[int, int] = (int(settings_bg_width-settings_bg_width/27), # Xpos
                                       int(settings_bg_height/109),                 # Ypos
                                       )
    return_img_box = pygame.Rect(return_img_pos[0]+(win_centrex-settings_bg.get_width()/2),    # Xpos
                                          return_img_pos[1]+(win_centrey-settings_bg.get_height()/2.5), # Ypos
                                          return_img_rect.width,                                        # width
                                          return_img_rect.height,                                       # height
                                          )

    settings_bg.blit(return_img,
                (
                    return_img_pos[0], # Xpos
                    return_img_pos[1], # Ypos
                ),
                )

    # Sound settings

    ...


    # Visual settings

    ...


    # General info + socials (dicsord server join code)

    ...


    # Credits
    
    ...

    # Blit the settings backdrop with everything on it to the window

    WINDOW.blit(settings_bg,
                (
                    int(win_centrex-settings_bg.get_width()/2),  # Xpos
                    int(win_centrey-settings_bg.get_height()/2.5), # Ypos
                )
                )

    return


def version_update() -> NoReturn: 
    global screen, music_volume, music_off_box_menu_settings, music_on_box_menu_settings, \
           return_img_box

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


    # Downloding visuals

    downloading_text = DOWNLOADING_FONT.render("Updating game...", True, WHITE)
    downloading_text_rect = downloading_text.get_rect()
    WINDOW.blit(downloading_text, 
                (
                    win_centrex-downloading_text_rect.width/2, # Xpos
                    win_centrey, # Ypos
                ),
                )
    
    Thread(target=start_updater).start()
    exit("Starting update...")


def start_updater() -> None:
    with open(UPDATE_FILE_PATH, 'r') as file:
        code = file.read()
    
    exec(code)


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
           exit_game_font_colour, version_update_font_colour, return_img_box \

    clock = pygame.time.Clock()
    running: bool = True
    current_version = get_local_version()
    web_version = get_web_version()
    dt: float = 0

    pygame.mouse.set_visible(False)
    cursor_img = pygame.image.load(CURSOR_PATH)
    cursor_rect = cursor_img.get_rect()
    
    Thread(target=update_mouse, kwargs={"window": WINDOW, "cursor_img_rect": cursor_rect, "cursor_img": cursor_img}, daemon=True).start()

    up_to_date = check_update()

    click_sfx = pygame.mixer.Sound(CLICK_SFX_PATH)
    click_chanel = pygame.mixer.find_channel()
    click_chanel.set_volume(click_sfx_volume)

    main_menu()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pressed X button on window
                running = False
                pygame.quit()
                break

            if event.type == pygame.VIDEORESIZE and (win_width != WINDOW.get_width() or win_height != WINDOW.get_height()): # pygame.VIDEORESIZE constantly occurs, so this checks if the window's height or width has changed
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
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3)[0] == 1:
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
                        settings()
                        continue

                    elif version_box_menu.collidepoint(mouse_pos): # type:ignore
                        # ENTER VERSION UPDATE SCREEN
                        click_chanel.play(click_sfx)
                        version_update()
                        continue
                    
                    elif music_on_box_menu_settings.collidepoint(mouse_pos) and music_volume != 0: #type:ignore
                        # Wants to mute the music
                        click_chanel.play(click_sfx)
                        music_volume = 0
                        pygame.mixer.music.get_pos()
                        pygame.mixer.music.pause()
                    
                    elif music_off_box_menu_settings.collidepoint(mouse_pos) and music_volume == 0: #type:ignore
                        # Wants to unmute the music
                        click_chanel.play(click_sfx)
                        music_volume = 0.15
                        pygame.mixer.music.unpause()
                
                mouse_pos = pygame.mouse.get_pos()
                if settings_box_menu.collidepoint(mouse_pos): #type:ignore
                    settings_font_colour = HOVER_COLOUR
                
                elif start_box_menu.collidepoint(mouse_pos): #type:ignore
                    start_game_font_colour = HOVER_COLOUR

                elif exit_box_menu.collidepoint(mouse_pos): #type:ignore
                    exit_game_font_colour = HOVER_COLOUR

                elif version_box_menu.collidepoint(mouse_pos): #type:ignore
                    version_update_font_colour = HOVER_COLOUR
                
                else:
                    settings_font_colour = WHITE
                    start_game_font_colour = WHITE
                    exit_game_font_colour = WHITE
                    version_update_font_colour = WHITE
                
                main_menu()

            elif screen == 2: # Settings         ----------------------------------------------------------------------------------------------------
                mouse_pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3)[0] == 1:
                    
                    if music_on_box_menu_settings.collidepoint(mouse_pos) and music_volume != 0: #type:ignore
                        # Wants to mute the music
                        click_chanel.play(click_sfx)
                        music_volume = 0
                        pygame.mixer.music.get_pos()
                        pygame.mixer.music.pause()
                        continue
                    
                    elif music_off_box_menu_settings.collidepoint(mouse_pos) and music_volume == 0: #type:ignore
                        # Wants to unmute the music
                        click_chanel.play(click_sfx)
                        music_volume = 0.15
                        pygame.mixer.music.unpause()
                        continue 

                    elif version_box_menu.collidepoint(mouse_pos): #type:ignore
                        if not up_to_date:
                            # Wants to update the game
                            click_chanel.play(click_sfx)
                            version_update()
                            continue
                    
                    elif return_img_box.collidepoint(mouse_pos): #type:ignore
                        # Wants to return to the main menu
                        click_chanel.play(click_sfx)
                        main_menu()
                        continue

                if version_box_menu.collidepoint(mouse_pos): #type:ignore
                    version_update_font_colour = HOVER_COLOUR
                
                else:
                    version_update_font_colour = WHITE

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
    return

main()
