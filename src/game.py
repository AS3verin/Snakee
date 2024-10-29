import pygame
import constants

 
class Snake:
    """ Description of the snake.

    Exhaustive description

    Attributes:
        colours:
        pos:
        snake_len:
    """
    def __init__(self,grid):
        # display
        self.colours = {"head":constants.SNAKE_HEAD_COLOUR, "body":constants.SNAKE_BODY_COLOUR}

        # initialisation
        self.pos = [(grid.arr_grid_size//2,grid.arr_grid_size//2)]
        self.snake_len = len(self.pos)

