import pygame
import game

def main():
    pygame.init()
    window = game.Initialise_Window()
    game.Create_Grid(window)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()




if __name__ == "__main__":
    main()
