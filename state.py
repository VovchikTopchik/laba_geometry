import pygame

GRID_WIDTH = 40
GRID_HEIGHT = 30
CELL = 20
SPEED = 75

LINE = 1
STEP = CELL + LINE
SCREEN_WIDTH = GRID_WIDTH * STEP + LINE
SCREEN_HEIGHT = GRID_HEIGHT * STEP + LINE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)
COLORS = (WHITE, GREY)


screen: pygame.Surface = None
clock: pygame.time.Clock = None

matrix = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
