import pygame
from modules.Bullet import Bullet
from modules.Entity import Entity


class Player(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocity_x = 0
        self.shoot_cooldown = 300
        self.last_shot = 0

    def shoot(self):
        """generate a bullet"""
        bullet = Bullet(
            self.x + self.w / 2 - 16,
            self.y - self.h / 2,
            "./media/bullet.png",
            32,
            64,
            self.group,
            10,
        )

    def update(self):
        """moves player on the x axis
        only update self.x if newX is within the range of the screen width with offset of 10
        """
        newX = self.x + self.velocity_x  # store the potential new x coordinate

        if 10 < newX < pygame.display.get_surface().get_width() - self.w - 10:
            self.x = newX

        self.rect.x = self.x

    def eventHandler(self):
        """This is the main event handler for the player class"""

        keys = pygame.key.get_pressed()

        # movement
        if keys[pygame.K_LEFT]:
            self.velocity_x = -5
        elif keys[pygame.K_RIGHT]:
            self.velocity_x = 5
        else:
            self.velocity_x = 0

        # continuous shooting
        if keys[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
            if now - self.last_shot >= self.shoot_cooldown:
                self.shoot()
                self.last_shot = now
