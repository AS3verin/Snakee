import pygame
from pygame.locals import *
import game, display, playtime, items

import constants

class Session:
    def __init__(self,grid,snake,Clock_time):
        # all classes
        self.grid = grid
        self.snake = snake
        self.Clock_time = Clock_time

        # properties
        self.running = False
        self.gameover = False
        self.score = 0

    def start(self):
        self.running = True
        self.Clock_time.t0 = self.Clock_time.t

    def restart(self,window):
        self.grid.__init__(window)
        self.snake.__init__(self.grid)
        self.Clock_time.__init__()
        self.__init__(self.grid,self.snake,self.Clock_time)


class Game:
    def __init__(self):
        self.running = True
        self.session = None

        self.window = None
        self.grid = None

        self.snake = None #TODO Remove grid at init then init items.snake()
        self.consumable = None

    def initialize(self):
        pygame.init()
        self.window = self.initialise_Window()  
        self.grid = display.Grid(self.window)
        self.snake = items.Snake(self.grid)
        # Create a clock for the time of play measurement
        Clock_time = playtime.TimePlay()
        # Initialisation of the session
        self.session = game.Session(self.grid, self.snake, Clock_time)
    
        pygame.time.set_timer(USEREVENT,constants.TIME_TO_PLAY)
    
    def initialise_Window(self):
        window = pygame.display.set_mode(constants.DISPLAY_SIZE)
        pygame.display.set_caption(constants.DISPLAY_CAPTION)

        display_icon = pygame.image.load(constants.DISPLAY_ICON_PATH)
        pygame.display.set_icon(display_icon)

        return window

    def execute(self):    
        self.initialize()

        while self.running:
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    self.running = False
                """
                Event Managment
                """
                if self.session.gameover and keys[constants.RESTART_KEY]:
                    self.session.restart(self.window)
                else:
                    if not self.session.running and keys[constants.START_KEY]:
                        self.session.start()
                    self.snake.move(keys,self.session)
                    if event.type == USEREVENT:
                        self.snake.update_pos(self.session, self.grid)


            self.window.fill((0, 0, 0)) # Remove the previous assets
            """
            Assets displaying managment
            """
            self.grid.display_grid_border()
            self.grid.display_snake(self.snake)
            if self.session.gameover:
                if self.session.Clock_time.tdeath==0:
                    self.session.Clock_time.tdeath = self.session.Clock_time.TOP
                self.grid.display_deathscreen(self.window)
            
            self.session.Clock_time.display_TOP(self.window, self.session)
            """
            End of displaying
            """

            pygame.display.update()
            self.session.Clock_time.update()
