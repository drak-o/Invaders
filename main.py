import pygame
import sys
from modules.Player import Player
from modules.Barrier import Barrier

class Game:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        # Initialize a window or screen for display
        self.screen = pygame.display.set_mode([w, h])
        # Initialize a Clock
        self.clock = pygame.time.Clock()
        # add a sprite or sequence of sprites to a group
        self.group = pygame.sprite.LayeredUpdates()
        # initialize all pygame modules
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

        barrier = Barrier(
            self.w / 2,
            self.h - 200,
            "media\256px-square.png"
            
        )
         
        running = True

        # main event loop
        while running:
            pygame.display.flip()  # Update the full display Surface to the screen
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
