import random

from game_object import GameObject
from settings import METEOR_SPEED, WIDTH


class Meteor(GameObject):
    def __init__(self, image):
        super().__init__(image)
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.bottom = 0
        self.speed = METEOR_SPEED

    def update(self):
        self.rect.y += self.speed