class GameObject:
    def __init__(self, image):
        self.image = image
        self.rect = image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
