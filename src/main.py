import pygame
import game

def main():
    pygame.init()
    window = game.Initialise_Window()
    grid = game.Grid(window)
    snake = game.Snake(grid)
    grid.display_snake(snake)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        


        pygame.display.update()




if __name__ == "__main__":
    main()
