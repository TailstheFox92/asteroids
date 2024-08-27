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
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


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

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, updatable, drawable)
    player = Player(x, y)

    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for sprite in updatable:
            sprite.update(dt)  # update rotation

        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game Over!")
                exit(0)
            for shot in shots:
                if shot.is_colliding(asteroid):
                    asteroid.split()
                    shot.kill()

        screen.fill("black")  # fill screen with black

        for sprite in drawable:
            sprite.draw(screen)  # draw player on screen

        pygame.display.flip()

        dt = clock.tick(FRAMES_PER_SECOND) / 1000


if __name__ == "__main__":
    main()
