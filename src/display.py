import pygame, numpy as np
import constants

class Grid:
    """ Class defining the grid of play and displaying it and all its elements.

    This class enables the initialization of a square grid where the game 
    take place. This grid is described by a number of cell and the size of
    the cells. All of the elements seen on the grid are displayed by this
    class.

    Attributes:
        window: pygame.Surface where the grid is displayed.
        arr_grid_res: Number of pixel per length of grid cell.
        arr_grid_size: Size of the grid in pixel. 
        arr_grid: Array for the grid. 
            0 is an empty cell. 1 corresponds to the snake. 2 is a consumable.
    """
    def __init__(self,window):
        """ Initializes the instance of the grid based on the window.

        Args:
            window: pygame.Surface where the grid is displayed
        """
        # display attribution
        self.window = window
        # initialisation of the grid
        self.arr_grid = np.zeros((constants.ARR_GRID_SIZE,
                                  constants.ARR_GRID_SIZE))

    def get_grid_border_rect(self):
        """ Get the description [x0, y0, dx, dy]) of the grid borders.

        Get the description [x0, y0, dx, dy]) of the grid borders interior
        and exterior

        Return:
            List of the rectangle int and ext description        
        """
        # rect = [x0, y0, dx, dy] with (x0,y0) most upper left right angle
        rect_int = [constants.GRID_POS[0], constants.GRID_POS[1],
                    constants.GRID_SIZE, constants.GRID_SIZE,]
        # rect_ext offset is 1 border thickness for x0, y0
        # and 2 border thickness for the dx, dy
        ext_offset = [-constants.GRID_BORDER_THICKNESS,
                      -constants.GRID_BORDER_THICKNESS,
                      2*constants.GRID_BORDER_THICKNESS,
                      2*constants.GRID_BORDER_THICKNESS,]
        rect_ext = [sum(x) for x in zip(rect_int, ext_offset)]

        return rect_int, rect_ext

    def display_grid_border(self):
        """ Display the grid border.

        Display the grid border by drawing two rectangles of two
        different colors.
        """
        rect_int, rect_ext = self.get_grid_border_rect()

        pygame.draw.rect(self.window,
                         color=constants.GRID_BORDER_COLOR,
                         rect = rect_ext,
                         border_radius=constants.GRID_BORDER_RADIUS)
        pygame.draw.rect(self.window,
                         color=constants.GRID_COLOR, 
                         rect= rect_int,
                         border_radius=constants.GRID_BORDER_RADIUS)
        
    def from_arrel_to_px(self,pos):
        """ Transform a cell position in a pixel position.

        Args:
            pos: tuple of int (x, y) representing the position in pixel.
        """
        pos_in_px = ( constants.GRID_POS[0] + constants.ARR_GRID_RES*pos[0] ,
                      constants.GRID_POS[1] + constants.ARR_GRID_RES*pos[1])
        return pos_in_px
    
    def display_snake(self,snake):
        """Display the snake on the grid
        
        Args:
            snake: ...
        """
        head_pos_in_px = self.from_arrel_to_px(snake.pos[0])
        pygame.draw.rect(self.window,color=snake.colours["head"],
                         rect=[head_pos_in_px[0],head_pos_in_px[1],
                               constants.ARR_GRID_RES,constants.ARR_GRID_RES])
    
        for k in range(1,snake.len):
            body_part_pos = self.from_arrel_to_px(snake.pos[k])
            pygame.draw.rect(self.window,color=snake.colours["body"],
                             rect=[body_part_pos[0],body_part_pos[1],
                                   constants.ARR_GRID_RES,constants.ARR_GRID_RES])
        
    def display_deathscreen(self,window):
        # Re-initialise the grid
        self.display_grid_border()
        # Display the death statement
        font = pygame.font.SysFont(constants.DEATH_FONT,
                                   constants.DEATH_FONT_SIZE)
        message_render = font.render(constants.DEATH_MESSAGE, True,
                                     constants.DEATH_FONT_COLOUR)
        message_rect = message_render.get_rect(center=constants.DEATH_FONT_POS)
        
        window.blit(message_render, message_rect.topleft)
