import pygame
import constants

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
        self.t = pygame.time.get_ticks()
        self.t0 = 0
        self.tdeath = 0
        self.TOP = 0
    
    def set_time(self):
        """ Set the current time.   """
        self.t = pygame.time.get_ticks()

    def get_TOP(self):
        """ Get the current time of play (TOP) in ms since the game launch.
        
        TOP = current_time - initial time
        """
        self.set_time()
        self.TOP = self.t - self.t0
        return self.TOP
    
    def Get_Time_To_Display(self, time):
        """ Get the time of play in the format hh:mm:ss.msms """
        return TimeConverter(time).to_str_timer()
    
    def display_TOP(self, window, session):
        """ Display the time of play around the grid
        """
        if session.gameover:
            time = self.tdeath
        elif not session.running:
            time = 0
        else:
            time = self.TOP
        
        time_to_display = self.Get_Time_To_Display(time)

        font = pygame.font.SysFont(constants.CLOCK_FONT,
                                   constants.CLOCK_FONT_SIZE)
        time_render = font.render(time_to_display, True, 
                                  constants.CLOCK_FONT_COLOR)
        time_rect = time_render.get_rect(center=constants.CLOCK_FONT_POS)
        
        window.blit(time_render, time_rect.topleft)

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
        seconds = self.milliseconds / constants.MS_TO_S
        return seconds

    def to_str_seconds(self):
        seconds = self.milliseconds / constants.MS_TO_S
        return f"{seconds:05.2f}"

    def to_minutes_seconds(self):
        total_seconds = self.to_seconds()
        minutes = total_seconds // constants.M_TO_H
        seconds = total_seconds % constants.S_TO_M
        return f"{int(minutes):02}:{seconds:05.2f}"

    def to_hours_minutes_seconds(self):
        total_seconds = self.to_seconds()
        hours = total_seconds // constants.S_TO_H
        minutes = (total_seconds % constants.S_TO_H) // constants.M_TO_H
        seconds = total_seconds % constants.S_TO_M
        return f"{int(hours):02}:{int(minutes):02}:{seconds:05.2f}"
    
    def to_str_timer(self):
        if self.milliseconds >= 3600000:
            return self.to_hours_minutes_seconds()
        elif self.milliseconds >= 60000:
            return self.to_minutes_seconds()
        else:
            return self.to_str_seconds()
