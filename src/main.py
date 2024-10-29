import pygame
import game, display, playtime

from constants import FPS

def main():
    pygame.init()
    window = game.Initialise_Window()
    
    # Initialization
    grid = game.Grid(window)
    snake = game.Snake(grid)
    
    # Create a clock for the time of play measurement
    Clock_time = game.TimePlay()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            """
            Event Managment
            """


        window.fill((0, 0, 0)) # Remove the previous assets
        """
        Assets displaying managment
        """
        grid.display_grid_border()
        grid.display_snake(snake)
        
        Clock_time.display_TOP(window)
        """
        End of displaying
        """

        pygame.display.update()
        Clock_time.update()
        





if __name__ == "__main__":
    main()
