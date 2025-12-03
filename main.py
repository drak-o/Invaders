import pygame
import sys
from modules.Player import Player
from modules.Barrier import Barrier
from modules.Invaders import Octopus


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
        self.barriers = []
        self.invaders = []

    def main(self):
        player = Player(
            self.w / 2 - 37.5,
            self.h - 100,
            "./media/256px-square.png",
            75,
            50,
            self.group,
            1,
        )

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

        octopus = Octopus(
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
        self.invaders.append(octopus)

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

            # loop which detects collision of bullets with various entities
            for bullet in player.bullets:

                # handle bullet collision with barriers
                for barrier in self.barriers:
                    if bullet.rect.colliderect(barrier.rect):
                        print("bullet hit barrier:", barrier)

                        # remove bullets
                        player.bullets.remove(bullet)
                        bullet.kill()

                        # apply damage
                        barrier.health -= 1

                        # remove barrier if dead
                        if barrier.health <= 0:
                            self.barriers.remove(barrier)
                            barrier.kill()
                        break

                # handle bullet collision with invaders
                for invader in self.invaders:
                    if bullet.rect.colliderect(invader.rect):
                        print("bullet hit invader:", invader)

                        # remove bullets
                        player.bullets.remove(bullet)
                        bullet.kill()

                        # apply damage
                        invader.health -= 1

                        # remove invader if dead
                        if invader.health <= 0:
                            self.invaders.remove(invader)
                            invader.kill()
                        break

            # handle quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()


object = Game(500, 500)
object.main()
