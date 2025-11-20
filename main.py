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

    def main(self):
        player = Player(
            self.w / 2,
            self.h - 100,
            "./media/256px-square.png",
            75,
            50,
            self.group,
            1,
        )
        running = True

        # main event loop
        while running:
            pygame.display.flip()
            self.screen.fill([0, 0, 0])
            self.clock.tick(100)

            # run event handler for player
            player.eventHandler()

            self.group.update()  # run update functions of each class in group
            self.group.draw(self.screen)

            # handle quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()


object = Game(500, 500)
object.main()
