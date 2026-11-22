import pygame
from collections import deque

import state


def draw_matrix():
    for row in range(state.GRID_HEIGHT):
        for col in range(state.GRID_WIDTH):
            if state.matrix[row][col]:
                rect = (
                    col * state.STEP + state.LINE,
                    row * state.STEP + state.LINE,
                    state.CELL,
                    state.CELL,
                )
                pygame.draw.rect(
                    state.screen,
                    state.COLORS[(state.matrix[row][col] - 1) % 2],
                    rect,
                )


def draw_line_h(start_x, start_y, end_x, end_y):
    if start_x > end_x:
        start_x, end_x = end_x, start_x
        start_y, end_y = end_y, start_y

    dx = end_x - start_x
    dy = end_y - start_y

    y_dir = -1 if dy < 0 else 1
    dy *= y_dir

    if dx != 0:
        y = start_y
        p = 2 * dy - dx
        for i in range(dx + 1):
            state.matrix[y][start_x + i] = 1
            if p >= 0:
                y += y_dir
                p = p - 2 * dx
            p = p + 2 * dy

            draw_matrix()
            pygame.display.flip()
            state.clock.tick(state.SPEED)


def draw_line_v(start_x, start_y, end_x, end_y):
    if start_y > end_y:
        start_x, end_x = end_x, start_x
        start_y, end_y = end_y, start_y

    dx = end_x - start_x
    dy = end_y - start_y

    x_dir = -1 if dx < 0 else 1
    dx *= x_dir

    if dy != 0:
        x = start_x
        p = 2 * dx - dy
        for i in range(dy + 1):
            state.matrix[start_y + i][x] = 1
            if p >= 0:
                x += x_dir
                p = p - 2 * dy
            p = p + 2 * dx

            draw_matrix()
            pygame.display.flip()
            state.clock.tick(state.SPEED)


def draw_line(start_x, start_y, end_x, end_y):
    if abs(end_x - start_x) > abs(end_y - start_y):
        draw_line_h(start_x, start_y, end_x, end_y)
    else:
        draw_line_v(start_x, start_y, end_x, end_y)


def draw_line_dda(start_x, start_y, end_x, end_y):
    dx = end_x - start_x
    dy = end_y - start_y

    steps = max(abs(dx), abs(dy))

    x_inc = dx / steps
    y_inc = dy / steps

    x = start_x
    y = start_y

    for _ in range(steps + 1):
        ix = round(x)
        iy = round(y)

        if 0 <= ix < state.GRID_WIDTH and 0 <= iy < state.GRID_HEIGHT:
            state.matrix[iy][ix] = 2

        x += x_inc
        y += y_inc

        draw_matrix()
        pygame.display.flip()
        state.clock.tick(state.SPEED)


def fill(start_x, start_y, connected_4=1):
    if state.matrix[start_y][start_x] != 0:
        return

    queue = deque([(start_x, start_y)])
    state.matrix[start_y][start_x] = 2

    if connected_4:
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    else:
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < state.GRID_WIDTH and 0 <= ny < state.GRID_HEIGHT:
                if state.matrix[ny][nx] == 0:
                    state.matrix[ny][nx] = 2
                    queue.append((nx, ny))

                    draw_matrix()
                    pygame.display.flip()
                    state.clock.tick(state.SPEED)
