import pygame


class Entity(pygame.sprite.Sprite):
    """
    A game entity base class that extends `pygame.sprite.Sprite`.

    Inherits position, size, image loading, collision rect,
    and group/layer handling. Adds group, layer, score, health.

    Args:
        x (int): X position.
        y (int): Y position.
        entity_img (str): Path to the image.
        w (int): Width.
        h (int): Height.
        group: Sprite group to add this entity to.
        layer (int): Render layer.
        score (int, optional): Score value.
        health (int, optional): Health value.
    """

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
