import sys
import pygame
import game

from constants import FPS

def main():
    pygame.init()
    window = game.Initialise_Window()
    
    # Initialization
    grid = game.Grid(window)
    snake = game.Snake(grid)
    
    # Create a clock for the time managment of the program
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 50)
    start_time = pygame.time.get_ticks()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            """
            Event Managment
            """
        current_time = pygame.time.get_ticks()
        total_time = (current_time - start_time) // 1000 # In second

        window.fill((0, 0, 0)) # Remove the previous assets
        """
        Assets displaying managment
        """
        grid.display_snake(snake)
        window.blit(font.render(str(total_time), True, (255, 255, 255)), (50, 50))
        """
        End of displaying
        """

        pygame.display.update()

        clock.tick(FPS) # Game run at max FPS frames per second





if __name__ == "__main__":
    main()
