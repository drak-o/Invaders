import pygame
from modules.Bullet import Bullet
from modules.Entity import Entity


class Player(Entity):
    def __init__(self, *args, screen=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.screen = screen
        self.velocity_x = 0
        self.shoot_cooldown = 300
        self.last_shot = 0

    def shoot(self):
        """generate a bullet and updates it"""
        bullet = Bullet(
            self.x, self.y, "./media/bullet.png", 32, 64, self.group, 10, self.screen
        )
        bullet.update()

    def update(self):
        """moves player on the x axis
        only update self.x if newX is within the range of the screen width
        """
        newX = self.x + self.velocity_x  # store the potential new x coordinate

        if 0 < newX < pygame.display.get_surface().get_width() - self.w:
            self.x = newX

        self.rect.x = self.x

    def eventHandler(self, event):
        """This is the main event handler for the player

        Args:
            event (pygame.event.Event): an event such as KEYDOWN passed from the main event loop
        """

        # KEYDOWN handlers
        if event.type == pygame.KEYDOWN:
            # throttled shooting
            if event.key == pygame.K_SPACE:
                now = pygame.time.get_ticks()  # current time

                # checks if enough time has passed since the last shot
                if now - self.last_shot >= self.shoot_cooldown:
                    self.shoot()
                    self.last_shot = now

            # decrease velocity_x by one when holding K_LEFT
            if event.key == pygame.K_LEFT:
                self.velocity_x = -1

            # increase velocity_x by one when holding K_RIGHT
            elif event.key == pygame.K_RIGHT:
                self.velocity_x = 1

        # KEYUP handlers
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.velocity_x = 0
            elif event.key == pygame.K_RIGHT:
                self.velocity_x = 0

        self.update()
