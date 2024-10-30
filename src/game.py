import pygame, matplotlib.pyplot as plt, numpy as np
import constants

 
class Snake:
    """ Description of the snake.

    Exhaustive description

    Attributes:
        colours: dictionary for the colours of the snake (keys: head, body)
        pos: list containing tuples stating the position of each part of the 
             body, the first element being the head
        head_pos: tuple of the position of the head of the body
    """
    def __init__(self,grid):
        # display
        self.colours = {"head":constants.SNAKE_HEAD_COLOUR, 
                        "body":constants.SNAKE_BODY_COLOUR}

        # initialisation
        self.pos = [(constants.ARR_GRID_SIZE//2,constants.ARR_GRID_SIZE//2)]
        self.delta_x, self.delta_y = 0, 0
        self.snake_len = len(self.pos)
        grid.arr_grid[*self.pos[0]] = 1
    
    def update_pos1(self,key):
        has_moved = True
        current_pos = self.pos.copy()
        current_head_pos = current_pos[0]
        # if the movement is possible: move the head of the snake
        if current_head_pos[1]>0 and key==pygame.K_UP:
            self.pos.insert(0,(current_head_pos[0],current_head_pos[1]-1))
        elif current_head_pos[1]<constants.ARR_GRID_SIZE-1 and key==pygame.K_DOWN:
            self.pos.insert(0,(current_head_pos[0],current_head_pos[1]+1))
        elif current_head_pos[0]>0 and key==pygame.K_LEFT:
            self.pos.insert(0,(current_head_pos[0]-1,current_head_pos[1]))
        elif current_head_pos[0]<constants.ARR_GRID_SIZE-1 and key==pygame.K_RIGHT:
            self.pos.insert(0,(current_head_pos[0]+1,current_head_pos[1]))
        else:
            has_moved = False
        # if there is a movement: move all the body
        if has_moved:
            self.pos.pop()
        return has_moved
    
    def update_pos(self,grid):
        current_pos = self.pos.copy()
        current_head_pos = current_pos[0]
        # update the snake position
        self.pos.insert(0,(current_head_pos[0]+self.delta_x,
                           current_head_pos[1]+self.delta_y))
        self.pos.pop()
        # update the grid
        grid.arr_grid[*self.pos[0]] = 1
        grid.arr_grid[*current_pos[-1]] = 0
        #print(self.pos,np.where(grid.arr_grid==1))


    def move(self,event,grid):
        if event.type==pygame.KEYDOWN and event.key==constants.INITIALISE_MOV and self.delta_x==0 and self.delta_y==0:
            self.delta_x = constants.SNAKE_SPEED

        if event.type==pygame.KEYDOWN and (event.key in constants.ACCEPTABLE_MOV_KEYS):
            if self.delta_x and event.key==pygame.K_UP:
                self.delta_x, self.delta_y = 0, -1
            elif self.delta_x and event.key==pygame.K_DOWN:
                self.delta_x, self.delta_y = 0, 1
            elif self.delta_y and event.key==pygame.K_LEFT:
                self.delta_x, self.delta_y = -1, 0
            elif self.delta_y and event.key==pygame.K_RIGHT:
                self.delta_x, self.delta_y = 1, 0
            
