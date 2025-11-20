import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, entity_img, w, h, group, layer, score=None, health=None):

        super().__init__()

        # position and size
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        # image
        self.image = pygame.image.load(entity_img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.w, self.h))

        # collision
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        # layer setup
        self.group = group
        group.add(self, layer=layer)

        # misc states
        self.score = score
        self.health = health
