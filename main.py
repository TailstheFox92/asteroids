# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import (
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        FRAMES_PER_SECOND
    )
from player import Player


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    print(f"Spawning player at {x}, {y}")
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)  # update rotation
        screen.fill("black")  # fill screen with black
        player.draw(screen)  # draw player on screen
        pygame.display.flip()

        dt = clock.tick(FRAMES_PER_SECOND) / 1000


if __name__ == "__main__":
    main()
