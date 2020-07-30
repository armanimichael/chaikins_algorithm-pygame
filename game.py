"Game entry point"

import pygame
from pygame.math import Vector2
from chaikin_algorithm import chaikin_algorithm

SCREEN_SIZE = 800


def main():
    "Game Main"

    pygame.init()
    pygame.display.set_caption("Chaikin's Algorithm")

    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    running = True

    points = (
        Vector2(0, 400),
        Vector2(200, 100),
        Vector2(400, 700),
        Vector2(600, 600),
        Vector2(700, 50),
        Vector2(800, 0)
    )
    pygame.draw.lines(screen, (255, 0, 0), False, points)

    new_points = chaikin_algorithm(points, 6)
    pygame.draw.lines(screen, (0, 255, 0), False, new_points)

    pygame.display.update()
    # Game Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
