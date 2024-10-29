import pygame
import constants

def Initialise_Window():
    window = pygame.display.set_mode(constants.DISPLAY_SIZE)
    pygame.display.set_caption(constants.DISPLAY_CAPTION)

    display_icon = pygame.image.load(constants.DISPLAY_ICON_PATH)
    pygame.display.set_icon(display_icon)

    return window

def Create_Grid(surface):
    pygame.draw.rect(surface,color=constants.GRID_BORDER_COLOR,
                     rect=[constants.GRID_POS[0]-constants.GRID_BORDER_THICKNESS,constants.GRID_POS[1]-constants.GRID_BORDER_THICKNESS,
                           constants.GRID_SIZE+2*constants.GRID_BORDER_THICKNESS,constants.GRID_SIZE+2*constants.GRID_BORDER_THICKNESS],
                     border_radius=constants.GRID_BORDER_RADIUS)
    
    
    pygame.draw.rect(surface,color=constants.GRID_COLOR,
                     rect=[constants.GRID_POS[0],constants.GRID_POS[1],constants.GRID_SIZE,constants.GRID_SIZE],
                     border_radius=constants.GRID_BORDER_RADIUS)