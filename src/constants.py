import pathlib

### window settings
DISPLAY_SIZE = WIDTH, HEIGHT = 1280, 720
DISPLAY_CAPTION = "Snakee"
DISPLAY_ICON_PATH = pathlib.Path("./assets/Snakee_icon.png")

### grid
# display
GRID_SIZE = 600 # px
GRID_POS = (WIDTH//2-GRID_SIZE//2,HEIGHT//2-GRID_SIZE//2) # position of the top left corner (px, px)
GRID_COLOR = (0,0,0) # rgb
GRID_BORDER_COLOR = (255,255,255) # rgb
GRID_BORDER_RADIUS = 2 # px
GRID_BORDER_THICKNESS = 2 # px

# array
ARR_GRID_RES = 10 # px

### snake
# display
SNAKE_HEAD_COLOUR = (0,255,0)
SNAKE_BODY_COLOUR = (222,208,16)
# initialisation

### Clock
FPS = 60
MS_TO_S = 1000
S_TO_M = 60
M_TO_H = 60
S_TO_H = 3600
