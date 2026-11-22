import pygame
from game_object import GameObject
from settings import WIDTH, HEIGHT, PLAYER_SPEED


class Player(GameObject):
    def __init__(self, image):
        super().__init__(image)
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH