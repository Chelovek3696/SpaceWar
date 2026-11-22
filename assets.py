from  pathlib import Path

import pygame

def load_image(filename, size):
    path = Path(__file__).resolve().parent / filename
    image = pygame.image.load(str(path)).convert_alpha()
    return pygame.transform.scale(image, size)