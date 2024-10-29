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
    Clock_time = game.TimePlay()
    font = pygame.font.SysFont("Arial", 50)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            """
            Event Managment
            """
        Clock_time.get_TOP()
        current_TOP = Clock_time.Get_TOP_Minutes()

        window.fill((0, 0, 0)) # Remove the previous assets
        """
        Assets displaying managment
        """
        grid.display_grid_border()
        grid.display_snake(snake)
        window.blit(font.render(str(current_TOP), True, (255, 255, 255)), (50, 50))
        """
        End of displaying
        """

        pygame.display.update()
        print("\n Boucle +1")

        Clock_time.clock.tick(FPS) # Game run at max FPS frames per second





if __name__ == "__main__":
    main()
