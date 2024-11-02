from typing import Tuple, Any, Optional, List

import pygame
import pygame_menu

import constants

def initialize_menu():
    global main_menu
    menu_theme = initialize_theme()

    # --------------------------------------------------------------------------
    # Create Play Menu
    # --------------------------------------------------------------------------
    play_menu = pygame_menu.Menu(height = constants.GRID_NPX,
                                    width = constants.GRID_NPX,
                                    theme = menu_theme,
                                    title='Play Menu',
                                   )
    play_menu.add.button('Start',  # When pressing return -> play(DIFFICULTY[0], font)
                         play_game,
                         GAME,
                        )
    play_menu.add.selector('Select Game ',
                           [('1 - Snakee', 'SNAKEE'),
                            ('2 - Other', 'OTHER')],
                           onchange= change_game,
                           selector_id='select_game')
    play_menu.add.button('Return to main menu', pygame_menu.events.BACK)
    # --------------------------------------------------------------------------
    # Create About Menu
    # --------------------------------------------------------------------------
    about_menu = pygame_menu.Menu(height = constants.GRID_NPX,
                                    width = constants.GRID_NPX,
                                    theme = menu_theme,
                                    title='About Menu',
                                   )
   
    for m in constants.ABOUT:
        about_menu.add.label(m, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
    about_menu.add.vertical_margin(30)
    about_menu.add.button('Return to menu', pygame_menu.events.BACK)
    # --------------------------------------------------------------------------
    # Create Main Menu
    # --------------------------------------------------------------------------
    main_menu = pygame_menu.Menu(height = constants.GRID_NPX,
                                 width = constants.GRID_NPX,
                                 theme = menu_theme,
                                 title='Main Menu',
                                )
    main_menu.add.button('Play', play_menu)
    main_menu.add.button('About', about_menu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)

    return main_menu


def initialize_theme():
    """     Modification of the theme common for all menu and submenu  """
    menu_theme = pygame_menu.themes.THEME_GREEN.copy()
    menu_theme.widget_font_size = 35
    # ...
    return menu_theme

GAME = ['SNAKEE']
def change_game(value: Tuple[Any, int], game: str):
    selected, index = value
    print(f'Selected game: "{selected}" ({game}) at index {index}')
    GAME[0] = game


def play_game(game_type):
    global main_menu
    font = pygame.font.SysFont(constants.CLOCK_FONT, constants.CLOCK_FONT_SIZE)
    if game_type[0] == 'SNAKEE':
        f = font.render('Playing Snakee', True, (255, 255, 255))
    elif game_type[0] == 'OTHER':
        f = font.render('No other game to play', True, (255, 255, 255))  
    else:
        raise ValueError(f'unknown game {game_type}')
    f_esc = font.render('Press ESC to get back to the menu', True, (255, 255, 255))

    main_menu.disable()
    main_menu.full_reset()

    

