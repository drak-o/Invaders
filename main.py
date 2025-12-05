import pygame
import sys
from modules.Player import Player
from modules.Barrier import Barrier
from modules.Invaders import Invader
from events.Events import MainEvents

# initialize all pygame modules
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

        # the main instance of the player class
        self.player = Player(
            self.w / 2 - 37.5,
            self.h - 100,
            "./media/256px-square.png",
            100,
            50,
            self.group,
            1,
            None,
            3,
        )

        # arrays to store entity types
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
        invader = Invader(
            self.w / 2 - 50,
            self.h / 2 - 100,
            "./media/Barrier3.png",
            100,
            100,
            self.group,
            1,
            None,
            25,
        )
        self.invaders.append(invader)

        # create an instance of MainEvents
        # so that we can call handle_events()
        main_events = MainEvents(
            self.player,
            self.barriers,
            self.invaders,
            self.screen,
        )

        # render an inital piece of text
        font = pygame.font.Font(None, 36)

        # main event loop
        while True:
            # run handle_events() which calls all functions linked with event listening
            if not main_events.handle_events():
                break

            # run update functions of each class in group
            self.group.update()

            self.screen.fill([0, 0, 0])
            self.group.draw(self.screen)

            # draw the player health
            player_health_txt = font.render(
                "health: " + str(self.player.health), True, (255, 255, 255)
            )
            self.screen.blit(player_health_txt, (10, self.h - 36))

            # draw the health of invader
            if self.invaders:
                invader_health = self.invaders[0].health
            else:
                invader_health = 0

            invader_health_txt = font.render(
                "invader health: " + str(invader_health), True, (255, 255, 255)
            )
            invader_text_width = invader_health_txt.get_size()[0]

            self.screen.blit(
                invader_health_txt,
                (self.w - invader_text_width - 10, 18),
            )

            game_over_text = font.render("Game Over :(", True, (255, 255, 255))
            game_over_text_width = game_over_text.get_size()[0]
            game_over_text_height = game_over_text.get_size()[1]

            self.screen.blit(
                game_over_text,
                (
                    self.w / 2 - game_over_text_width / 2,
                    self.h / 2 - game_over_text_height / 2,
                ),
            )

            # Update the full display Surface to the screen
            pygame.display.flip()

            self.clock.tick(100)

        # cleanup
        pygame.display.quit()
        pygame.quit()
        sys.exit()


game = Game(500, 500)
game.main()
