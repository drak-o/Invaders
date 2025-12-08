import pygame
import sys
from modules.Player import Player
from modules.Barrier import Barrier
from modules.Invaders import Invader
from modules.Text import Text
from events.Events import MainEvents

# initialize all pygame modules
pygame.init()


class Game:
    def __init__(self, w, h, bg_image):
        self.w = w
        self.h = h
        # Initialize a window or screen for display
        self.screen = pygame.display.set_mode([w, h])
        # Initialize a Clock
        self.clock = pygame.time.Clock()
        # add a sprite or sequence of sprites to a group
        self.group = pygame.sprite.LayeredUpdates()

        self.bg_img = pygame.image.load(bg_image)
        self.bg_img = pygame.transform.scale(
            self.bg_img, (self.w, self.h)
        )  # scale to fit screen

        # the main instance of the player class
        self.player = Player(
            x=self.w / 2 - 37.5,
            y=self.h - 100,
            entity_img="./media/Boat.png",
            w=150,
            h=100,
            group=self.group,
            layer=1,
            score=None,
            health=3,
        )

        # arrays to store entity types
        self.barriers = []
        self.invaders = []

    def main(self):
        # create 4 barriers and append them to the barriers list
        for i in range(4):
            barrier = Barrier(
                x=25 + i * (75 + 50),  # start_x + i * (width + gap)
                y=self.h - 200,
                entity_img="./media/Barrier3.png",
                w=75,
                h=75,
                group=self.group,
                layer=1,
                score=None,
                health=3,
            )
            self.barriers.append(barrier)

        # create one invader and apped it to invaders list
        invader = Invader(
            x=self.w / 2 - 96,
            y=self.h / 2 - 192,
            entity_img="./media/Barrier3.png",
            w=192,
            h=192,
            group=self.group,
            layer=1,
            score=None,
            health=25,
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

        # create an instance of the text class
        text = Text(self.player, self.invaders, self.screen, None)

        # main event loop
        while True:
            # run handle_events() which calls all functions linked with event listening
            if not main_events.handle_events():
                break

            # run update functions of each class in group
            self.group.update()

            self.screen.blit(self.bg_img, (0, 0))
            self.group.draw(self.screen)

            text.draw_text()
            # Update the full display Surface to the screen
            pygame.display.flip()

            self.clock.tick(100)

            # check status of bullet arrays
            # print(
            #     "main() self.invaders[0].bullets: ",
            #     self.invaders[0].bullets,
            # )
            # print("main() self.player.bullets: ", self.player.bullets)

            # print(self.barriers)

        # cleanup
        pygame.display.quit()
        pygame.quit()
        sys.exit()


game = Game(500, 500, "./media/Background.jpg")
game.main()
