import pygame
import game, menu, constants


def main():
    game1 = game.Game()
    game1.initialize()

    menus = menu.Menu()
    main_menu = menus.menus["1"]

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

            # Main menu
            if main_menu.is_enabled():
                main_menu.mainloop(game1.window, fps_limit=constants.FPS)
            else:
                game1.set_session(menus.game_chosen)
                game1.execute()

            # Flip surface
            pygame.display.flip()


if __name__ == "__main__":
    main()
