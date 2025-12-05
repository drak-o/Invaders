import pygame


class Text:
    """
    Handles game text rendering and stores references to game objects.

    Args:
        player (Player): The player object, used for displaying player-related info.
        invaders (list[Invader]): A List of Invader objects.
        screen (pygame.Surface): The main display surface.
        font: Optional path to a .ttf font file. Uses default font if None.

    Notes:
        font.render() is frequently used as part of this file because it:
        creates a new surface
        draws the letters onto that surface
        returns something compatible with the blit function
    """

    def __init__(self, player, invaders, screen, font=None):
        self.player = player
        self.invaders = invaders
        self.screen = screen
        self.font = pygame.font.Font(font, 36)
        self.screen_w, self.screen_h = pygame.display.get_surface().get_size()

    # run most functions from file
    def draw_text(self):
        self.draw_player_health()
        self.draw_invader_health()
        # self.draw_game_over()

    # draw the player health
    def draw_player_health(self):
        player_health_txt = self.font.render(
            "health: " + str(self.player.health), True, (255, 255, 255)
        )

        # blit 10 px from the left of the screen at screen height - text height
        self.screen.blit(player_health_txt, (10, self.screen_h - 36))

    # draw the health of invader
    def draw_invader_health(self):
        # draw 0 if invader health does not exist
        if self.invaders:
            invader_health = self.invaders[0].health
        else:
            invader_health = 0

        invader_health_txt = self.font.render(
            "invader health: " + str(invader_health), True, (255, 255, 255)
        )
        invader_text_width = invader_health_txt.get_size()[0]

        # blit 10 px from the right of screen half a text height down
        self.screen.blit(
            invader_health_txt,
            (self.screen_w - invader_text_width - 10, 18),
        )

    def draw_centered_text(self, text):
        surface_text = self.font.render(text, True, (255, 255, 255))
        surface_text_width = surface_text.get_size()[0]
        surface_text_height = surface_text.get_size()[1]

        self.screen.fill([0, 0, 0])

        # blit in middle of screen
        self.screen.blit(
            surface_text,
            (
                self.screen_w / 2 - surface_text_width / 2,
                self.screen_h / 2 - surface_text_height / 2,
            ),
        )
