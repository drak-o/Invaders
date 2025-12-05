import pygame
from modules.Entity import Entity
from modules.Bullet import Bullet


class Invader(Entity):
    """
    A Class for the Invader which extends Entity.

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.shoot_cooldown = 1000
        self.last_shot = 0
        self.bullets = []

    def shoot(self):
        # generate a bullet
        bullet = Bullet(
            -10,
            self.x + self.w / 2 - 16,
            self.y + self.h / 2 + 16,
            "./media/bullet.png",
            32,
            64,
            self.group,
            10,
        )
        self.bullets.append(bullet)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot >= self.shoot_cooldown:
            self.shoot()
            self.last_shot = now
