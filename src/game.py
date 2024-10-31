import pygame
from pygame.locals import *
import game, display, playtime, items

import constants

class Session:
    def __init__(self, window):
        # initialisation
        self.display_session = display.display_session(window)
        self.snake = items.Snake()
        self.consumable = None #items.Consumable() to do!
        self.Clock_time = playtime.TimePlay()
        # properties
        self.running = False # Running of the session
        self.gameover = False

    def start(self):
        self.running = True
        self.Clock_time.reset()

    def reset(self):
        self.snake.reset()
        self.running = False
        self.gameover = False

    ### Renders ###
    def render_playground(self, window):
        self.display_session.display_grid_border()
        self.display_session.display_snake(self.snake)
        if self.gameover:
            self.display_session.display_deathscreen(window)  
    
    def render_clock(self, window):  
        self.Clock_time.display_TOP(window)


    ### Update snake and consumables ###
    def snake_moving(self, keys):
        delta_x, delta_y = self.snake.delta_x, self.snake.delta_y
        # initialise movement
        if self.running and delta_x==0 and delta_y==0:
            self.snake.initialise_mov()
        # which movement
        if delta_x and keys[K_UP]:
            self.snake.move_up()
        elif delta_x and keys[K_DOWN]:
            self.snake.move_down()
        elif delta_y and keys[K_LEFT]:
            self.snake.move_left()
        elif delta_y and keys[K_RIGHT]:
            self.snake.move_right()

    def update_session(self, event, keys):
        if not self.running:
            if (event.type == pygame.KEYDOWN) and (event.key == constants.START_KEY):
                self.start()
        else:
            if self.gameover:
                if (event.type == pygame.KEYDOWN) and (event.key == constants.RESET_KEY):
                    self.reset()
            else:
                if self.snake.death:
                    self.gameover = True
                else:
                    self.snake_moving(keys)
                    if event.type == USEREVENT: # controls the speed of the snake
                        self.snake.update_pos()

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



class Game:
    def __init__(self):
        self.running = True
        self.session = None
        self.window = None

    ### Initialize ###
    def initialize(self):
        pygame.init()
        self.window = self.initialise_Window()
        self.session = game.Session(self.window)
        pygame.time.set_timer(USEREVENT,constants.TIME_TO_PLAY)
    
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
        self.initialize()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.update_frame(event)

            self.render()
            self.update()
