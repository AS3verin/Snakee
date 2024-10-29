import pygame, numpy as np
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


class TimePlay:
    """ Compute the time played while playing Snakee
    
    Attributes:
        pygame.clock: pygame function to create a clock
        t0: initial time when the class is created
        t: current time
        TOP: Time of play
    """
    def __init__(self):
        """ Initialize the instane of the clock, and the initial time
        """
        self.clock = pygame.time.Clock()
        self.t0 = pygame.time.get_ticks()
        self.t = pygame.time.get_ticks()
        self.TOP = 0
    
    def set_time(self):
        """ Set the current time.
        """
        self.t = pygame.time.get_ticks()

    def get_TOP(self, format = "s"):
        """ Get the current time of play (TOP) in ms since the game launch.
        
        TOP = current_time - initial time
        """
        self.set_time()
        self.TOP = self.t - self.t0
        return self.TOP
    
    def Get_TOP_Secondes(self):
        """ Get the time of play in seconds
        """
        return TimeConverter(self.TOP).to_seconds()
    
    def Get_TOP_Minutes(self):
        """ Get the time of play in m:s
        """
        return TimeConverter(self.TOP).to_minutes_seconds()
    
    def Get_TOP_Hours(self):
        """ Get the time of play in h:m:s
        """
        return TimeConverter(self.TOP).to_hours_minutes_seconds()

    def display_TOP(self, window, format= "m"):
        """ Display the time of play around the grid
        """
        if format == "h":
            time_to_display = self.Get_TOP_Hours()
        elif format == "m":
            time_to_display = self.Get_TOP_Minutes()
        else:
            time_to_display = self.Get_TOP_Secondes()

        font = pygame.font.SysFont(constants.CLOCK_FONT,
                                   constants.CLOCK_FONT_SIZE)
        
        window.blit(font.render(str(time_to_display), True, 
                                constants.CLOCK_FONT_COLOR),
                                constants.CLOCK_FONT_POS)

    def update(self):
        """ Update the TOP and the number of FPS of the clock
        """
        self.clock.tick(constants.FPS) # Game run at max FPS frames per second
        _ = self.get_TOP()

class TimeConverter:
    """ Convert the time from ms to s, min, or hours.

    Convert the time from a int in ms to string in the format hh:mm:ss

    """
    def __init__(self, milliseconds):
        self.milliseconds = milliseconds

    def to_seconds(self):
        return self.milliseconds / constants.MS_TO_S

    def to_minutes_seconds(self):
        total_seconds = self.to_seconds()
        minutes = total_seconds // constants.M_TO_H
        seconds = total_seconds % constants.S_TO_M
        return f"{int(minutes)}:{seconds:.2f}"

    def to_hours_minutes_seconds(self):
        total_seconds = self.to_seconds()
        hours = total_seconds // constants.S_TO_H
        minutes = (total_seconds % constants.S_TO_H) // constants.M_TO_H
        seconds = total_seconds % constants.S_TO_M
        return f"{int(hours)}:{int(minutes)}:{seconds:.2f}"

