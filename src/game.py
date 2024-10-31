import pygame
from pygame.locals import *
import game, display, playtime, items

import constants

class Session:
    def __init__(self, grid, snake):
        # all classes
        self.grid = grid
        self.snake = snake
        self.Clock_time = playtime.TimePlay()
        # properties
        self.running = False # Running of the session
        self.gameover = False

    def start(self):
        self.running = True
        self.Clock_time.reset()

    def reset(self,window):
        self.grid.__init__(window)
        self.snake.__init__(self.grid)
        self.running = False
        self.gameover = False

    def session_time(self):
        if self.gameover:
            self.Clock_time.set_time_display(self.Clock_time.tdeath)
        elif not self.running:
            self.Clock_time.set_time_display(0)
        else:
            self.Clock_time.set_time_display(self.Clock_time.TOP)


class Game:
    def __init__(self):
        self.running = True
        self.session = None

        self.window = None
        self.grid = None

        self.snake = None #TODO Remove grid at init then init items.snake()
        self.consumable = None

### Initialize ###
    def initialize(self):
        pygame.init()
        self.window = self.initialise_Window()  
        self.grid = display.Grid(self.window)
        self.snake = items.Snake(self.grid)
        # Initialisation of the session
        self.session = game.Session(self.grid, self.snake)
    
        pygame.time.set_timer(USEREVENT,constants.TIME_TO_PLAY)
    
    def initialise_Window(self):
        window = pygame.display.set_mode(constants.DISPLAY_SIZE)
        pygame.display.set_caption(constants.DISPLAY_CAPTION)

        display_icon = pygame.image.load(constants.DISPLAY_ICON_PATH)
        pygame.display.set_icon(display_icon)

        return window

### Render ###
    def render_playground(self):
        self.window.fill((0, 0, 0)) # fill the entire screen
        self.grid.display_grid_border()
        self.grid.display_snake(self.snake)
    
    def render_clock(self):  
        self.session.Clock_time.display_TOP(self.window)

    def render(self):
        self.render_playground()                 
        if self.session.gameover:
            self.grid.display_deathscreen(self.window)        
        self.render_clock()

### Event ###
    def moving(self, event):
        keys = pygame.key.get_pressed()
        if self.session.running and not self.session.gameover:
            self.snake.move(keys,self.session)
        if event.type == USEREVENT:
            self.snake.update_pos(self.session, self.grid)


    def start_session(self, event):
        if event.type == pygame.KEYDOWN:
            if not self.session.running and (event.key == constants.START_KEY):
                self.session.start()
            elif self.session.gameover and (event.key == constants.RESET_KEY):
                self.session.reset(self.window)

### Update ###
    def update(self):
        pygame.display.update()
        self.session.Clock_time.update(self.session.gameover)
        self.session.session_time()


### Execute ###
    def execute(self):    
        self.initialize()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.start_session(event)
                self.moving(event)

            self.render()
            self.update()
