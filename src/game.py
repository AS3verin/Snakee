import pygame
from pygame.locals import *
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
