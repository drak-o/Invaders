from modules.Entity import Entity
import pygame


class Bullet(Entity):
    """
    A projectile entity that extends `Entity`.

    Inherits position, size, image loading, collision rect,
    and group/layer handling. Adds vertical movement and
    automatic removal when leaving the screen.

    Args:
        speed (int): the speed of the bullet.
        owner (string): describes which entity owns the bullet.
        x (int): X position.
        y (int): Y position.
        entity_img (str): Path to the bullet image.
        w (int): Width.
        h (int): Height.
        group: Sprite group to add this entity to.
        layer (int): Render layer.
        score (int, optional): Unused for bullets.
        health (int, optional): Unused for bullets.
    """

    def __init__(self, speed, owner, *args, **kwargs):
        self.speed = speed
        self.owner = owner
        super().__init__(*args, **kwargs)

    def update(self):
        self.y -= self.speed

        # sync rect
        self.rect.y = self.y
