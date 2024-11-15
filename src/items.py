import pygame, numpy as np
from pygame.locals import *
import constants

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
        """ Initializes the instance of the snake.
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

    ### Movement test ###
    def move_up(self):
        self.delta_x, self.delta_y = 0, -1
    
    def move_down(self):
        self.delta_x, self.delta_y = 0, 1

    def move_left(self):
        self.delta_x, self.delta_y = -1, 0
    
    def move_right(self):
        self.delta_x, self.delta_y = 1, 0

    ### Update position ###
    def border_collision(self,head_pos):
        h_collision = head_pos[0]<0 or head_pos[0]>constants.GRID_NCELL-1
        v_collision = head_pos[1]<0 or head_pos[1]>constants.GRID_NCELL-1
        return h_collision or v_collision
    
    def snake_collision(self,head_pos):
        return head_pos in self.pos

    def update_pos(self):
        """ Updates the position of the snake.
        """
        current_pos = self.pos.copy()
        current_head_pos = current_pos[0]
        new_head_pos = (current_head_pos[0]+self.delta_x,
                        current_head_pos[1]+self.delta_y)
        if self.border_collision(new_head_pos) or self.snake_collision(new_head_pos):
            self.death = True
        else:
            self.pos.insert(0,new_head_pos)
            self.pos.pop()

    ### Growing ###
    def growing(self,is_there_consumable,new_tail):
        eat_consumable = False
        if is_there_consumable:
            self.pos.insert(-1,new_tail)
            self.len += 1
            eat_consumable = True
        return eat_consumable
        
            


class Consumable:
    def __init__(self, taken_cells):
        self.name = constants.CONSUMABLE_NAME
        self.colour = constants.CONSUMABLE_DISPLAY["colour"]
        self.eaten = False
        self.pos = self.search_empty_cell(taken_cells)

    def reset(self, taken_cells):
        self.eaten = False
        self.pos = self.search_empty_cell(taken_cells)

    def search_empty_cell(self,taken_cells):
        potential_new_pos = tuple(np.random.randint(0,constants.GRID_NCELL-1,2))
        while potential_new_pos in taken_cells:
            potential_new_pos = tuple(np.random.randint(0,constants.GRID_NCELL-1,2))
        return potential_new_pos

# init image, manage position (random, not on snake), give point when eaten