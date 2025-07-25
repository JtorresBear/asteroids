from constants import *
import pygame
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    #dt is delta
    dt = 0
    
    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()

    Player.containers = (updateable_group,drawable_group)
    player1 = Player(SCREEN_WIDTH/ 2,SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return     
             
        updateable_group.update(dt)
        screen.fill("black")
        for thing in drawable_group:
            thing.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
