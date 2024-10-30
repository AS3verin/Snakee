import pygame
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
    def __init__(self,grid):
        """ Initializes the instance of the snake within the grid.

        Args:
            grid: np.array containing the grid
        """
        # display
        self.colours = {"head":constants.SNAKE_HEAD_COLOUR, 
                        "body":constants.SNAKE_BODY_COLOUR}

        # initialisation
        self.pos = [(constants.ARR_GRID_SIZE//2,constants.ARR_GRID_SIZE//2)]
        self.delta_x, self.delta_y = 0, 0
        self.len = len(self.pos)
        grid.arr_grid[*self.pos[0]] = 1

    def border_collision(self,head_pos):
        h_collision = head_pos[0]<0 or head_pos[0]>constants.ARR_GRID_SIZE-1
        v_collision = head_pos[1]<0 or head_pos[1]>constants.ARR_GRID_SIZE-1
        return h_collision or v_collision
    
    def update_pos(self,session,grid):
        """ Updates the attribute of the position of the snake,
        and how he moves in the grid.

        Args:
            grid: np.array containing the grid
        """
        current_pos = self.pos.copy()
        current_head_pos = current_pos[0]
        new_head_pos = (current_head_pos[0]+self.delta_x,
                        current_head_pos[1]+self.delta_y)
        if self.border_collision(new_head_pos):
            session.gameover = True
        else:
            # update the snake position
            self.pos.insert(0,new_head_pos)
            self.pos.pop()
            # update the grid
            grid.arr_grid[*self.pos[0]] = 1
            grid.arr_grid[*current_pos[-1]] = 0

    def move(self,keys,session):
        """ Makes the snake move at a constant speed and depending of the 
        player inputs.

        Args:
            keys: list of keys that the player input
            grid: np.array containing the grid
        """
        if session.running and self.delta_x==0 and self.delta_y==0:
            self.delta_x = 1

        if self.delta_x and keys[K_UP]:
            self.delta_x, self.delta_y = 0, -1
        elif self.delta_x and keys[K_DOWN]:
            self.delta_x, self.delta_y = 0, 1
        elif self.delta_y and keys[K_LEFT]:
            self.delta_x, self.delta_y = -1, 0
        elif self.delta_y and keys[K_RIGHT]:
            self.delta_x, self.delta_y = 1, 0
            
