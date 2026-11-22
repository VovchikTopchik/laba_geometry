import pygame

import state
import rasterfill

pygame.init()

state.screen = pygame.display.set_mode((state.SCREEN_WIDTH, state.SCREEN_HEIGHT))
state.clock = pygame.time.Clock()

start_x, start_y, end_x, end_y = 0, 0, 0, 0
flag = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                for row in state.matrix:
                    for i in range(len(row)):
                        row[i] = 0
            elif event.key == pygame.K_b:
                rasterfill.draw_line(start_x, start_y, end_x, end_y)
            elif event.key == pygame.K_d:
                rasterfill.draw_line_dda(start_x, start_y, end_x, end_y)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            col = x // state.STEP
            row = y // state.STEP
            if 0 <= col < state.GRID_WIDTH and 0 <= row < state.GRID_HEIGHT:
                if event.button == pygame.BUTTON_RIGHT:
                    rasterfill.fill(col, row, 1)
                elif event.button == pygame.BUTTON_MIDDLE:
                    rasterfill.fill(col, row, 0)
                else:
                    state.matrix[row][col] ^= 1
                    if not flag:
                        start_x, start_y = col, row
                        flag = 1
                    else:
                        end_x, end_y = col, row
                        flag = 0

    state.screen.fill(state.BLACK)

    rasterfill.draw_matrix()

    for i in range(state.GRID_WIDTH + 1):
        x = i * state.STEP
        pygame.draw.line(state.screen, state.RED, (x, 0), (x, state.SCREEN_HEIGHT))
    for j in range(state.GRID_HEIGHT + 1):
        y = j * state.STEP
        pygame.draw.line(state.screen, state.RED, (0, y), (state.SCREEN_WIDTH, y))

    pygame.draw.line(
        state.screen,
        state.GREEN,
        (start_x * state.STEP + state.CELL // 2, start_y * state.STEP + state.CELL // 2),
        (end_x * state.STEP + state.CELL // 2, end_y * state.STEP + state.CELL // 2),
    )

    pygame.display.flip()

pygame.quit()
