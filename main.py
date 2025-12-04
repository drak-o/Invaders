import pygame
import sys
from modules.Player import Player
from modules.Barrier import Barrier
from modules.Invaders import Octopus

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

    def barrier_collision_handler(self, bullet, barrier):
        print("bullet hit barrier:", barrier)

        # remove bullet
        self.player.bullets.remove(bullet)
        bullet.kill()

        # apply damage
        barrier.health -= 1

        # remove barrier if dead
        if barrier.health <= 0 and barrier in self.barriers:
            self.barriers.remove(barrier)
            barrier.kill()

    def invader_collision_handler(self, bullet, invader):
        print("bullet hit invader:", invader)

        # remove bullet
        self.player.bullets.remove(bullet)
        bullet.kill()

        # apply damage
        invader.health -= 1

        # remove invader if dead
        if invader.health <= 0 and invader in self.invaders:
            self.invaders.remove(invader)
            invader.kill()

    def player_collision_handler(self, bullet, invader):
        print("bullet hit player:", self.player)

        # remove bullets
        invader.bullets.remove(bullet)
        bullet.kill()

        # apply damage
        self.player.health -= 1

        # kill self.player if dead
        if self.player.health <= 0:
            self.player.kill()

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
            self.player.eventHandler()

            self.group.update()  # run update functions of each class in group
            self.group.draw(self.screen)

            # if the player dies you want to draw black
            if self.player.health <= 0:
                running = False

            # loop which detects collision of player bullets with various entities
            for bullet in self.player.bullets:

                # listen for barrier collision and handle it
                for barrier in self.barriers:
                    if bullet.rect.colliderect(barrier.rect):
                        self.barrier_collision_handler(bullet, barrier)
                        break

                # listen for invader collision and handle it
                for invader in self.invaders:
                    if bullet.rect.colliderect(invader.rect):
                        self.invader_collision_handler(bullet, invader)
                        break

            # loop which detects collision of Invader bullets with the player
            for bullet in octopus.bullets:
                if bullet.rect.colliderect(self.player.rect):
                    self.player_collision_handler(bullet, octopus)
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
