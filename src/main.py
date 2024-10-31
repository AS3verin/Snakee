import pygame
import game, menu, constants

if __name__ == "__main__":
    global main_menu

    game = game.Game()
    game.initialize()

    
    main_menu = menu.initialize_menu()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

            # Main menu
            if main_menu.is_enabled():
                main_menu.mainloop(game.window, fps_limit=constants.FPS)
            

            # Flip surface
            pygame.display.flip()

