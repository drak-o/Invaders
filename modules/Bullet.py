from modules.Entity import Entity
import pygame


class Bullet(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed = 10

    def update(self):
        self.y -= self.speed

        # sync rect
        self.rect.y = self.y

        # remove bullet when off-screen
        if self.rect.top > pygame.display.get_surface().get_height():
            self.kill()
