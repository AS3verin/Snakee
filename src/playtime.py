import pygame
import constants

class TimePlay:
    """ Compute the time played while playing Snakee
    
    Attributes:
        pygame.clock: pygame function to create a clock
        t0: initial time when the a run is launched
        t: current time
        TOP: Time of play
        tdeath: time for the death
    """
    def __init__(self):
        """ Initialize the instane of the clock, and the initial time. """
        self.clock = pygame.time.Clock()
        self.t = pygame.time.get_ticks()
        self.t0 = 0
        self.tdeath = 0
        self.TOP = 0
        self.time_display = 0
    
    def reset(self):
        self.t0 = self.t
        self.tdeath = 0
        self.TOP = 0
        self.time_display = 0

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
    
    def Convert_Time_To_Display(self, time):
        """ Get the time of play in the format hh:mm:ss.msms . """
        return TimeConverter(time).to_str_timer()

    def set_time_display(self, time):
        self.time_display = time

    def display_TOP(self, window):
        """ Display the time of play around the grid. """      
        time_to_display = self.Convert_Time_To_Display(self.time_display)

        font = pygame.font.SysFont(constants.CLOCK_FONT,
                                   constants.CLOCK_FONT_SIZE)
        time_render = font.render(time_to_display, True, 
                                  constants.CLOCK_FONT_COLOR)
        time_rect = time_render.get_rect(center=constants.CLOCK_FONT_POS)
        
        window.blit(time_render, time_rect.topleft)

    def update(self, gameover):
        """ Update the TOP and the number of FPS of the clock. """
        self.clock.tick(constants.FPS) # Game run at max FPS frames per second
        _ = self.get_TOP()
        if self.tdeath == 0 and gameover:
            self.tdeath = self.TOP

class TimeConverter:
    """ Convert the time from ms (int) to string in the format hh:mm:ss.ss. """
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
