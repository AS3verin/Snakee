import pygame
from pygame.locals import *
import constants

class Consumable:
    def __init__(self, name):
        self.name = name
        self.eaten = False
# init image, manage position (random, not on snake), give point when eaten

class Snake:
    """ Class taking care of the snake.

    This class initialises the snake, allows it to move according the rule of 
    the snake game, and makes it eat and grow.

    Attributes:
        colours: dictionary for the colours of the snake (keys: head, body)
        pos: list containing tuples stating the position of each part of the 
             body, the first element being the head
        head_pos: tuple of the position of the head of the body
    """
    def __init__(self):
        """ Initializes the instance of the snake within the grid.
        """
        # display
        self.colours = {"head":constants.SNAKE_HEAD_COLOUR, 
                        "body":constants.SNAKE_BODY_COLOUR}

        # initialisation
        self.pos = [(constants.GRID_NCELL//2,constants.GRID_NCELL//2)]
        self.delta_x, self.delta_y = 0, 0
        self.len = len(self.pos)
        self.death = False

    def reset(self):
        self.pos = [(constants.GRID_NCELL//2,constants.GRID_NCELL//2)]
        self.delta_x, self.delta_y = 0, 0
        self.len = len(self.pos)
        self.death = False


    def initialise_mov(self):
        self.delta_x = 1

    def move_up(self):
        self.delta_x, self.delta_y = 0, -1
    
    def move_down(self):
        self.delta_x, self.delta_y = 0, 1

    def move_left(self):
        self.delta_x, self.delta_y = -1, 0
    
    def move_right(self):
        self.delta_x, self.delta_y = 1, 0



    def border_collision(self,head_pos):
        h_collision = head_pos[0]<0 or head_pos[0]>constants.GRID_NCELL-1
        v_collision = head_pos[1]<0 or head_pos[1]>constants.GRID_NCELL-1
        return h_collision or v_collision

    def update_pos(self):
        """ Updates the attribute of the position of the snake,
        and how he moves in the grid.
        """
        current_pos = self.pos.copy()
        current_head_pos = current_pos[0]
        new_head_pos = (current_head_pos[0]+self.delta_x,
                        current_head_pos[1]+self.delta_y)
        if self.border_collision(new_head_pos):
            self.death = True
        else:
            # update the snake position
            self.pos.insert(0,new_head_pos)
            self.pos.pop()
            
