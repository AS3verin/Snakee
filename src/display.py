import pygame
import constants

def Initialise_Window():
    """ Initialize the window of play

    Return:
        window: pygame.Surface where to watch the game    
    """
    window = pygame.display.set_mode(constants.DISPLAY_SIZE)
    pygame.display.set_caption(constants.DISPLAY_CAPTION)

    display_icon = pygame.image.load(constants.DISPLAY_ICON_PATH)
    pygame.display.set_icon(display_icon)

    return window


class Grid:
    """ Class displaying grid of play and all elements inside.

    This class enables the initialization of a square grid where the game 
    take place. This grid is described by a number of cell and the size of
    the cells. All of the elements seen on the grid are displayed by this
    class.

    Attributes:
        window: pygame.Surface where the grid is displayed.
        arr_grid_res: Number of pixel per length of grid cell.
        arr_grid_size: Size of the grid in pixel. 
    """
    def __init__(self,window):
        """ Initializes the instance of the grid based on the window.

        Args:
            window: pygame.Surface where the grid is displayed
        """
        # display attribution
        self.window = window
        # initialisation of the grid size in pixel
        self.arr_grid_res = constants.ARR_GRID_RES
        self.arr_grid_size = constants.GRID_SIZE//self.arr_grid_res

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
        pos_in_px = ( constants.GRID_POS[0] + self.arr_grid_res*pos[0] ,
                      constants.GRID_POS[1] + self.arr_grid_res*pos[1])
        return pos_in_px
    
    def display_snake(self,snake):
        """Display the snake on the grid
        
        Args:
            snake: ...
        """
        head_pos_in_px = self.from_arrel_to_px(snake.pos[0])
        pygame.draw.rect(self.window,color=snake.colours["head"],
                        rect=[head_pos_in_px[0],head_pos_in_px[1],self.arr_grid_res,self.arr_grid_res])
