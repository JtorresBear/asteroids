from constants import *
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    #dt is delta
    dt = 0
    
    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Shot.containers = (shots_group,updateable_group,drawable_group)
    
    
    Asteroid.containers = (asteroids,updateable_group,drawable_group)
    AsteroidField.containers = updateable_group
    asteroid_field = AsteroidField()

    Player.containers = (updateable_group,drawable_group)
    player1 = Player(SCREEN_WIDTH/ 2,SCREEN_HEIGHT / 2)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return     
             
        updateable_group.update(dt)
        for asteroid in asteroids:
           for shot in shots_group:
               if asteroid.collided(shot):
                   asteroid.split()
                   shot.kill()
           if asteroid.collided(player1):
               print("Game over!")
               sys.exit()
               #raise SystemExit("Game over!")
        screen.fill("black")
        for thing in drawable_group:
            thing.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
