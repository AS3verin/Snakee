import pygame, numpy as np
from pygame.locals import *

import game, display, playtime, items, constants

class Snake:
    def __init__(self, window):
        # initialisation
        self.display_session = display.display_session(window)
        self.snake = items.Snake()
        self.consumable = items.Consumable(self.all_taken_cells())
        self.Clock_time = playtime.TimePlay()
        # properties
        self.start_key = None
        self.running = False # Running of the session
        self.gameover = False

    def start(self,key):
        self.start_key = key
        self.running = True
        self.Clock_time.reset()

    def reset(self):
        self.snake.reset()
        self.consumable.reset(self.all_taken_cells())
        self.start_key = None
        self.running = False
        self.gameover = False

    ### Renders ###
    def render_playground(self, window):
        self.display_session.display_grid_border()
        self.display_session.display_snake(self.snake)
        self.display_session.display_consumable(self.consumable)
        if self.gameover:
            self.display_session.display_deathscreen(window)  
    
    def render_clock(self, window):  
        self.Clock_time.display_TOP(window)


    ### Update snake and consumables ###
    def snake_moving(self, keys):
        delta_x, delta_y = self.snake.delta_x, self.snake.delta_y
        # initialise movement
        if self.running and delta_x==0 and delta_y==0:
            if self.start_key == K_UP:
                self.snake.delta_y = -1
            elif self.start_key == K_DOWN:
                self.snake.delta_y = 1
            elif self.start_key == K_LEFT:
                self.snake.delta_x = -1
            elif self.start_key == K_RIGHT:
                self.snake.delta_x = 1
        # which movement
        if delta_x and keys[K_UP]:
            self.snake.move_up()
        elif delta_x and keys[K_DOWN]:
            self.snake.move_down()
        elif delta_y and keys[K_LEFT]:
            self.snake.move_left()
        elif delta_y and keys[K_RIGHT]:
            self.snake.move_right()

    def is_there_consumable(self, cell):
        return (np.array(cell)==self.consumable.pos).all()

    def all_taken_cells(self):
        return self.snake.pos

    def update_session(self, event, keys):
        if not self.running:
            if (event.type == pygame.KEYDOWN) and (event.key in constants.START_KEY):
                self.start(event.key)
        else:
            if self.gameover:
                if (event.type == pygame.KEYDOWN) and (event.key == constants.RESET_KEY):
                    self.reset()
            else:
                if self.snake.death:
                    self.gameover = True
                else:
                    self.snake_moving(keys) #TODO buffer because if going down and inputing right,up, you die!
                    if event.type == USEREVENT: # controls the speed of the snake
                        self.snake.update_pos()
                        self.consumable.eaten = self.snake.growing(self.is_there_consumable(self.snake.pos[0]), self.snake.pos[-1])
                        if self.consumable.eaten:
                            self.consumable.reset(self.all_taken_cells())

    ### Update clock ###
    def session_time(self):
        if self.gameover:
            self.Clock_time.set_time_display(self.Clock_time.tdeath)
        elif not self.running:
            self.Clock_time.set_time_display(0)
        else:
            self.Clock_time.set_time_display(self.Clock_time.TOP)
        
    def update_clock(self):
        self.Clock_time.update(self.gameover)
        self.session_time()


class Other:
    def __init__(self, window):
        # initialisation
        self.window = window
        self.running = False

    ### Renders ###
    def render_playground(self, window):
            self.window.fill((254, 132, 111))

            font_message_principal = pygame.font.SysFont(constants.CLOCK_FONT, constants.DEATH_FONT_SIZE)
            message_soon = font_message_principal.render('New Game Coming Soon', True, (255, 255, 255))
            message_rect = message_soon.get_rect(center=constants.DEATH_FONT_POS)
            window.blit(message_soon, message_rect.topleft)

            font_f = pygame.font.SysFont(constants.CLOCK_FONT, constants.CLOCK_FONT_SIZE)
            f_esc = font_f.render('Press ESC to get back to the menu', True, (255, 255, 255))
            f_rect = f_esc.get_rect(center=(constants.WIDTH//2, 90/100*constants.HEIGHT))
            window.blit(f_esc, f_rect.topleft)

    def render_clock(self, window):  
        return 0
    
    def update_session(self, event, keys):
        if (event.type == pygame.KEYDOWN) and (event.key == K_ESCAPE):
            self.running = False

    def update_clock(self):
        return 0



class Game:
    def __init__(self):
        self.running = True
        self.session = None
        self.window = None

    ### Initialize ###
    def initialize(self):
        pygame.init()
        self.window = self.initialise_Window()
        pygame.time.set_timer(USEREVENT,constants.TIME_TO_PLAY)
    
    def set_session(self, game_name):
        if game_name == constants.GAMES[0]:
            self.session = Snake(self.window)
        else:
            self.session = Other(self.window)

    def initialise_Window(self):
        window = pygame.display.set_mode(constants.DISPLAY_SIZE)
        pygame.display.set_caption(constants.DISPLAY_CAPTION)

        display_icon = pygame.image.load(constants.DISPLAY_ICON_PATH)
        pygame.display.set_icon(display_icon)

        return window

    ### Render ###
    def render(self):
        self.window.fill((0, 0, 0)) # fill the entire screen
        self.session.render_playground(self.window)      
        self.session.render_clock(self.window)

    ### Event ###
    def update_frame(self, event):
        keys = pygame.key.get_pressed()
        self.session.update_session(event,keys)

    ### Update ###
    def update(self):
        pygame.display.update()
        self.session.update_clock()

    ### Execute ###
    def execute(self):   
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                self.update_frame(event)

            self.render()
            self.update()
