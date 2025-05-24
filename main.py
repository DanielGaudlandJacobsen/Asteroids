import sys
import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    group_asteroids = pygame.sprite.Group()
    group_shots = pygame.sprite.Group()

    AsteroidField.containers = (group_updatable,)
    Asteroid.containers = (group_updatable, group_drawable, group_asteroids)
    Player.containers = (group_updatable, group_drawable)
    Shot.containers = (group_shots, group_updatable, group_drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        group_updatable.update(dt)
        for asteroid in group_asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")
        for drawable in group_drawable:
            drawable.draw(screen)
        pygame.display.flip()

        # Set framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()