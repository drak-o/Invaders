import pygame
from modules.Text import Text


class MainEvents:
    """
    This class handles all misc events, collision events, and input events.

    Args:
        player (Player): The main instance of Player.
        barriers (list[Barrier]): A List of Barrier objects.
        invaders (list[Invader]): A List of Invader objects.
        screen (pygame.Surface): The main display surface.
    """

    def __init__(self, player, barriers, invaders, screen):
        self.player = player
        self.barriers = barriers
        self.invaders = invaders
        self.screen = screen
        self.text = Text(player, invaders, screen)

    def handle_events(self):
        """
        Function that centralizes all handlers, for simplicity in main
        """
        # if the player dies draw Game Over and quit
        if self.player.health <= 0:
            self.text.draw_centered_text("Game Over :(")
            return False

        # else if the invaders are dead draw you won and quit
        elif not self.invaders:
            self.text.draw_centered_text("You Won! :)")
            return False

        # handle quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        self.player_key_handler()
        self.bullet_offscreen_listener()
        self.barrier_collision_listener()
        self.invader_collision_listener()
        self.player_invader_collision_listener()

        return True

    """
        Event Handlers
    """

    def player_key_handler(self):
        # function is too small so decided to merge handler and listener
        player = self.player

        # do nothing if player is dead or hidden to fix issue
        if player.health <= 0 or player.hidden_until > 0:
            return

        keys = pygame.key.get_pressed()

        # movement
        if keys[pygame.K_LEFT]:
            player.velocity_x = -5
        elif keys[pygame.K_RIGHT]:
            player.velocity_x = 5
        else:
            player.velocity_x = 0

        # continuous shooting
        if keys[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
            if now - player.last_shot >= player.shoot_cooldown:
                player.shoot()
                player.last_shot = now

    def barrier_collision_handler(self, bullet, barrier):
        print("bullet hit barrier:", barrier)

        # remove bullet from correct list
        if bullet.owner == "Player":
            self.player.bullets.remove(bullet)
        elif bullet.owner == "Invader" and self.invaders:
            self.invaders[0].bullets.remove(bullet)

        # remove from screen
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

    def player_collision_handler(self, bullet, player):
        print("bullet hit player:", player)

        # remove bullets
        if self.invaders:
            self.invaders[0].bullets.remove(bullet)

        # remove bullet from screen
        bullet.kill()

        # apply damage
        player.health -= 1

        # kill self.player if dead
        if player.health <= 0:
            player.kill()

        # respawn animation
        player.hide()

    """
        Event Listeners
    """

    def barrier_collision_listener(self):
        # create one unioned list from player bullets and invaders bullets
        if self.invaders:
            bullets = self.player.bullets + self.invaders[0].bullets
        else:
            bullets = self.player.bullets

        for bullet in bullets:
            # listen for barrier collision and handle it
            for barrier in self.barriers:
                if bullet.rect.colliderect(barrier.rect):
                    self.barrier_collision_handler(bullet, barrier)
                    break

    def invader_collision_listener(self):
        bullets = self.player.bullets

        for bullet in bullets:
            # listen for invader collision and handle it
            for invader in self.invaders:
                if bullet.rect.colliderect(invader.rect):
                    self.invader_collision_handler(bullet, invader)
                    break

    # this was rewritten to fix indexing error
    def player_invader_collision_listener(self):

        player = self.player

        # nested loop which detects collision of invader bullets with the player
        for invader in self.invaders:
            bullets = invader.bullets

            for bullet in bullets:
                if bullet.rect.colliderect(player.rect):
                    self.player_collision_handler(bullet, player)
                    break

    def bullet_offscreen_listener(self):
        screen_bottom = pygame.display.get_surface().get_height()
        # create one unioned list from player bullets and invaders bullets
        if self.invaders:
            bullets = self.player.bullets + self.invaders[0].bullets
        else:
            bullets = self.player.bullets

        # loop over bullets and decide if it should be deleted or not
        for bullet in bullets:
            if bullet.owner == "Player" and bullet.rect.top < 0 - bullet.h:
                self.player.bullets.remove(bullet)
                bullet.kill()
                break
            elif (
                bullet.owner == "Invader"
                and bullet.rect.bottom > screen_bottom + bullet.h
            ):
                if self.invaders:
                    self.invaders[0].bullets.remove(bullet)

                bullet.kill()
                break
