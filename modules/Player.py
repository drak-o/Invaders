import pygame
from modules.Bullet import Bullet
from modules.Entity import Entity


class Player(Entity):
    """
    A game entity that extends `Entity`.

    Inherits position, size, image loading, collision rect,
    and group/layer handling. Adds basic movement and shooting state.

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
        self.velocity_x = 0
        self.shoot_cooldown = 300
        self.last_shot = 0
        self.bullets = []

    def shoot(self):
        """generate a bullet"""
        bullet = Bullet(
            10,
            self.x + self.w / 2 - 16,
            self.y - self.h / 2,
            "./media/bullet.png",
            32,
            64,
            self.group,
            10,
        )
        self.bullets.append(bullet)

    def update(self):
        """moves player on the x axis
        only update self.x if newX is within the range of the screen width with offset of 10
        """
        newX = self.x + self.velocity_x  # store the potential new x coordinate

        if 10 < newX < pygame.display.get_surface().get_width() - self.w - 10:
            self.x = newX

        self.rect.x = self.x
