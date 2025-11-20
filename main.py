import pygame
import sys
from modules.Player import Player


class Game:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.screen = pygame.display.set_mode([w, h])
        self.clock = pygame.time.Clock()
        self.group = pygame.sprite.LayeredUpdates()
        pygame.init()
        pygame.key.set_repeat(True)

    def main(self):
        player = Player(
            self.w / 2,
            self.h - 100,
            "./media/256px-square.png",
            75,
            50,
            self.group,
            1,
            self.screen,
        )
        running = True

        # main event loop
        while running:
            pygame.display.flip()
            self.screen.fill([0, 0, 0])
            self.clock.tick(100)
            self.group.update()
            self.group.draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()

                player.eventHandler(event)


object = Game(500, 500)
object.main()
