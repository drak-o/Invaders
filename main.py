import pygame
import sys
from modules.Player import Player
from modules.Barrier import Barrier
from modules.Invaders import Octopus
from events.Events import MainEvents

pygame.init()


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
        self.player = Player(
            self.w / 2 - 37.5,
            self.h - 100,
            "./media/256px-square.png",
            75,
            50,
            self.group,
            1,
            None,
            3,
        )
        self.barriers = []
        self.invaders = []

    def main(self):
        # create 4 barriers and append them to the barriers list
        for i in range(4):
            barrier = Barrier(
                75 + (i * 100),
                self.h - 200,
                "./media/Barrier3.png",
                50,
                50,
                self.group,
                1,
                None,
                3,
            )
            self.barriers.append(barrier)

        # create one invader and apped it to invaders list
        invader = Octopus(
            self.w / 2 - 50,
            self.h / 2 - 100,
            "./media/Barrier3.png",
            100,
            100,
            self.group,
            1,
            None,
            1,
        )
        self.invaders.append(invader)

        main_events = MainEvents(self.player, self.barriers, self.invaders)

        running = True

        # main event loop
        while running:
            pygame.display.flip()  # Update the full display Surface to the screen
            self.screen.fill([0, 0, 0])
            self.clock.tick(100)

            # run events
            main_events.handle_events()

            self.group.update()  # run update functions of each class in group
            self.group.draw(self.screen)

            # if the player dies you want to draw black and quit
            if self.player.health <= 0:
                self.screen.fill([0, 0, 0])
                pygame.display.flip()  # update the whole screen
                pygame.time.wait(1000)
                running = False
                pygame.display.quit()
                pygame.quit()
                sys.exit()

            # handle quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()


game = Game(500, 500)
game.main()
