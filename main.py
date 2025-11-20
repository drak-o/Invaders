import pygame
import sys
from modules.Player import Player


class Game:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.screen = pygame.display.set_mode([w, h])
        self.clock = pygame.time.Clock()
        pygame.init()
        pygame.key.set_repeat(True)

    def generateInvaders(self):
        for row in range(1, 5):
            for col in range(1, len(self.board) - 1):
                self.board[row, col] = "O"

    def main(self):
        player = Player(
            self.w / 2, self.h - 100, "./media/256px-square.png", "./media/bullet.png" 75, 50, self.screen
        )
        player.draw()
        running = True

        # main event loop
        while running:
            self.clock.tick(100)
            self.screen.fill([0, 0, 0])

            for event in pygame.event.get():
                # print("event: ", event)
                if event.type == pygame.QUIT:
                    running = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()

                player.eventHandler(event)

                pygame.display.flip()


object = Game(500, 500)
object.main()
