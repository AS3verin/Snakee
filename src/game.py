import pygame, numpy as np
import constants

def Initialise_Window():
    window = pygame.display.set_mode(constants.DISPLAY_SIZE)
    pygame.display.set_caption(constants.DISPLAY_CAPTION)

    display_icon = pygame.image.load(constants.DISPLAY_ICON_PATH)
    pygame.display.set_icon(display_icon)

    return window


class Grid:
    def __init__(self,window):
        # display
        self.window = window
        self.display_grid()

        # initialisation
        self.arr_grid_res = constants.ARR_GRID_RES
        self.arr_grid_size = constants.GRID_SIZE//self.arr_grid_res
        #self.arr_grid = np.zeros((self.arr_grid_size,self.arr_grid_size))

    def display_grid(self):
        pygame.draw.rect(self.window,color=constants.GRID_BORDER_COLOR,
                        rect=[constants.GRID_POS[0]-constants.GRID_BORDER_THICKNESS,constants.GRID_POS[1]-constants.GRID_BORDER_THICKNESS,
                            constants.GRID_SIZE+2*constants.GRID_BORDER_THICKNESS,constants.GRID_SIZE+2*constants.GRID_BORDER_THICKNESS],
                        border_radius=constants.GRID_BORDER_RADIUS)
        pygame.draw.rect(self.window,color=constants.GRID_COLOR,
                        rect=[constants.GRID_POS[0],constants.GRID_POS[1],constants.GRID_SIZE,constants.GRID_SIZE],
                        border_radius=constants.GRID_BORDER_RADIUS)
        
    def from_arrel_to_px(self,pos):
        pos_in_px = ( constants.GRID_POS[0] + self.arr_grid_res*pos[0] ,
                      constants.GRID_POS[1] + self.arr_grid_res*pos[1])
        return pos_in_px
    
    def display_snake(self,snake):
        head_pos_in_px = self.from_arrel_to_px(snake.pos[0])
        pygame.draw.rect(self.window,color=snake.colours["head"],
                        rect=[head_pos_in_px[0],head_pos_in_px[1],self.arr_grid_res,self.arr_grid_res])

    
class Snake:
    def __init__(self,grid):
        # display
        self.colours = {"head":constants.SNAKE_HEAD_COLOUR, "body":constants.SNAKE_BODY_COLOUR}

        # initialisation
        self.pos = [(grid.arr_grid_size//2,grid.arr_grid_size//2)]
        self.snake_len = len(self.pos)


