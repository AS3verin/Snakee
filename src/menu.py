from typing import Tuple, Any, Optional, List

import pygame
import pygame_menu

import constants

class Menu:

    def __init__(self):
        self.menus = {}
        # Dict of the menu. Organized like a tree with unique number for each
        # node represented as the key
        #                                1
        #           ---------------------|-------------------- 
        #           |                    |                   |
        #           2                    3                   4
        #           |                                        |
        #           |---------------------                   |
        #           |                    |                   |
        #           21                    22                 41
        # 
        self.list_game = constants.GAMES
        self.game_selector = self.select_game_tuple()
        self.game_chosen = self.list_game[0]
        self.menu_theme = self.initialize_theme()
        self.initialize_menu()
        
    
    def select_game_tuple(self):
        return [(str(1+i) + ' - ' + game, game) for i, game in enumerate(self.list_game)]

    def initialize_menu(self):

        # --------------------------------------------------------------------------
        # Create Play Menu
        # --------------------------------------------------------------------------
        play_menu = pygame_menu.Menu(height = constants.GRID_NPX,
                                        width = constants.GRID_NPX,
                                        theme = self.menu_theme,
                                        title='Play Menu',
                                    )
        self.menus["2"] = play_menu
        play_menu.add.button('Start',  # When pressing return -> play_game()
                            self.play_game,
                            )
        print(self.game_selector)
        play_menu.add.selector('Select Game ', self.game_selector, # select game displayed
                            onchange= self.change_game,
                            selector_id='select_game')
        play_menu.add.button('Return to main menu', pygame_menu.events.BACK)
        # --------------------------------------------------------------------------
        # Create About Menu
        # --------------------------------------------------------------------------
        about_menu = pygame_menu.Menu(height = constants.GRID_NPX,
                                        width = constants.GRID_NPX,
                                        theme = self.menu_theme,
                                        title='About Menu',
                                    )
        self.menus["3"] = about_menu

        for m in constants.ABOUT:
            about_menu.add.label(m, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
        about_menu.add.vertical_margin(30)
        about_menu.add.button('Return to menu', pygame_menu.events.BACK)
        # --------------------------------------------------------------------------
        # Create Main Menu
        # --------------------------------------------------------------------------
        main_menu = pygame_menu.Menu(height = constants.GRID_NPX,
                                    width = constants.GRID_NPX,
                                    theme = self.menu_theme,
                                    title='Main Menu',
                                    )
        self.menus["1"] = main_menu
        main_menu.add.button('Play', play_menu)
        main_menu.add.button('About', about_menu)
        main_menu.add.button('Quit', pygame_menu.events.EXIT)


    def initialize_theme(self):
        """     Modification of the theme common for all menu and submenu  """
        menu_theme = pygame_menu.themes.THEME_GREEN.copy()
        menu_theme.widget_font_size = 40
        # ...
        return menu_theme

    def change_game(self, value, game_selector):
        ### value: Tuple(str display in the selector, index of the selected)
        selected, index = value
        print("game selector: ", self.game_selector)
        print("value (selected, index): ", value)
        print("previous game_chosen ", self.game_chosen)
        self.game_chosen = selected[1]
        print(f'Selected game: ({selected[0]}) at index ({index})')


    def play_game(self):
        self.menus["1"].disable()
        self.menus["1"].full_reset()


        

