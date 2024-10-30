import pathlib, pygame

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
ARR_GRID_SIZE = GRID_SIZE//ARR_GRID_RES # px

### snake
# display
SNAKE_HEAD_COLOUR = (0,255,0)
SNAKE_BODY_COLOUR = (222,208,16)
# movement
SNAKE_SPEED = 1 # grid cell/t

### Clock
# Display
FPS = 10
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

### Movements
INITIALISE_MOV = pygame.K_SPACE
ACCEPTABLE_MOV_KEYS = [pygame.K_UP, pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT]