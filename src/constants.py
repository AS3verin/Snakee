import pathlib, pygame
from pygame.locals import *

### window settings
DISPLAY_SIZE = WIDTH, HEIGHT = 1280, 720
DISPLAY_CAPTION = "Snakee"
DISPLAY_ICON_PATH = pathlib.Path("./assets/Snakee_icon.png")

### grid
# display
GRID_NPX = 600 # px
GRID_POS = (WIDTH//2-GRID_NPX//2,HEIGHT//2-GRID_NPX//2) # position of the top left corner (px, px)
GRID_COLOR = (0,0,0) # rgb
GRID_BORDER_COLOR = (255,255,255) # rgb
GRID_BORDER_RADIUS = 2 # px
GRID_BORDER_THICKNESS = 2 # px
# cutting the grid into cells
GRID_RES = 30 # px
GRID_NCELL = GRID_NPX//GRID_RES # number of cells

### snake
# display
SNAKE_HEAD_COLOUR = (0,255,0)
SNAKE_BODY_COLOUR = (222,255,0)
# movement
START_KEY = [K_UP, K_DOWN, K_LEFT, K_RIGHT]
# death 
DEATH_FONT = "Courier"
DEATH_FONT_SIZE = 100
DEATH_FONT_COLOUR = (255,0,0)
DEATH_FONT_POS = (WIDTH//2, HEIGHT//2)
DEATH_MESSAGE = "YOU DIED!"
RESET_KEY = K_SPACE

### consumable
CONSUMABLE_NAME = "Apple"
CONSUMABLE_DISPLAY = {"colour":(255,0,255)}

### Clock
# Display
FPS = 60
# Convert
MS_TO_S = 1000
S_TO_M = 60
M_TO_H = 60
S_TO_H = 3600
# Font
CLOCK_FONT = "Courier"
CLOCK_FONT_SIZE = 40
CLOCK_FONT_COLOR = (255, 255, 255)
CLOCK_FONT_POS = (WIDTH//2, 25)
# Game clock
TIME_TO_PLAY = 150 # ms
