import pygame
from modules.Entity import Entity


class Player(Entity):
    def __init__(self, x, y, entity_img, bullet_img, w, h, screen, health=3, score=0):
        super().__init__(x, y, entity_img, bullet_img, w, h, score, health)
        self.screen = screen
        self.velocity_x = 0

    def draw(self):
        """
        redraws the background and the player
        """

        self.screen.fill([0, 0, 0])
        self.screen.blit(self.entity_img, (self.x, self.y))

    def shoot(self):
        print("shoot() ran!")
        return

    def eventHandler(self, event):
        """This is the main event handler for the player

        Args:
            event (pygame.event.Event): an event such as KEYDOWN passed from the main event loop
        """

        # KEYDOWN adds or subtracts 1 to self.velocity_x
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.velocity_x = -1
            elif event.key == pygame.K_RIGHT:
                self.velocity_x = 1
            elif event.key == pygame.K_SPACE:
                self.shoot()

        # KEYUP sets the self.velocity_x to 0
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.velocity_x = 0
            elif event.key == pygame.K_RIGHT:
                self.velocity_x = 0

        newX = self.x + self.velocity_x  # store the potential new x coordinate

        # only update self.x if newX is within the range of the screen width
        w = pygame.display.get_surface().get_width()

        if 0 < newX < w - self.w:
            self.x = newX

        self.draw()  # redraw
