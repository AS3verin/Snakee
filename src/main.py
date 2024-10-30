import pygame
from pygame.locals import *
import game, display, playtime, items

from constants import TIME_TO_PLAY, START_KEY, RESTART_KEY

def main():
    pygame.init()
    window = display.Initialise_Window()
    
    # Initialization
    grid = display.Grid(window)
    snake = items.Snake(grid)
    
    # Create a clock for the time of play measurement
    Clock_time = playtime.TimePlay()
    
    # Initialisation of the session
    session = game.Session(grid,snake,Clock_time)
    
    pygame.time.set_timer(USEREVENT,TIME_TO_PLAY)

    running = True
    while running:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False
            """
            Event Managment
            """
            if session.gameover and keys[RESTART_KEY]:
                session.restart(window)
            else:
                if not session.running and keys[START_KEY]:
                    session.start()
                snake.move(keys,session)
                if event.type == USEREVENT:
                    snake.update_pos(session,grid)


        window.fill((0, 0, 0)) # Remove the previous assets
        """
        Assets displaying managment
        """
        grid.display_grid_border()
        grid.display_snake(snake)
        if session.gameover:
            if Clock_time.tdeath==0:
                Clock_time.tdeath = Clock_time.TOP
            grid.display_deathscreen(window)
        
        Clock_time.display_TOP(window,session)
        """
        End of displaying
        """

        pygame.display.update()
        Clock_time.update()
        





if __name__ == "__main__":
    main()
