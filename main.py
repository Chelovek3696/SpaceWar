import pygame, sys

from meteor import Meteor
from settings import FPS, HEIGHT, WIDTH, PLAYER_SIZE, METEOR_SIZE
from assets import load_image
from player import Player

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space War')
clock = pygame.time.Clock()

player_image = load_image('assets/player.png', PLAYER_SIZE)
player = Player(player_image)

meteor_image = load_image('assets/meteor.png', METEOR_SIZE)
meteor = Meteor(meteor_image)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not running:
        break

    keys = pygame.key.get_pressed()
    player.move(keys)
    meteor.update()

    screen.fill((15, 15, 30))
    player.draw(screen)
    meteor.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()