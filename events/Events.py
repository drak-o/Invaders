import pygame


class MainEvents:
    def __init__(self, game):
        self.game = game

    """
        Event Handlers
    """

    def player_key_handler(self):
        # function is too small so decided to merge handler and listener
        player = self.game.player

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

    def barrier_collision_handler(self, bullet, barrier, barriers, bullets):
        print("bullet hit barrier:", barrier)

        # remove bullet
        bullets.remove(bullet)
        bullet.kill()

        # apply damage
        barrier.health -= 1

        # remove barrier if dead
        if barrier.health <= 0 and barrier in barriers:
            barriers.remove(barrier)
            barrier.kill()

    def invader_collision_handler(self, bullet, invader, invaders, bullets):
        print("bullet hit invader:", invader)

        # remove bullet
        bullets.remove(bullet)
        bullet.kill()

        # apply damage
        invader.health -= 1

        # remove invader if dead
        if invader.health <= 0 and invader in invaders:
            invaders.remove(invader)
            invader.kill()

    def player_collision_handler(self, bullet, player, bullets):
        print("bullet hit player:", self.game.player)

        # remove bullets
        bullets.remove(bullet)
        bullet.kill()

        # apply damage
        player.health -= 1

        # kill self.player if dead
        if player.health <= 0:
            player.kill()

    """
        Event Listeners
    """

    def barrier_collision_listener(self):

        bullets = self.game.player.bullets
        barriers = self.game.barriers

        for bullet in bullets:
            # listen for barrier collision and handle it
            for barrier in barriers:
                if bullet.rect.colliderect(barrier.rect):
                    self.barrier_collision_handler(bullet, barrier, barriers, bullets)
                    break

    def invader_collision_listener(self):

        bullets = self.game.player.bullets
        invaders = self.game.invaders

        for bullet in bullets:
            # listen for invader collision and handle it
            for invader in invaders:
                if bullet.rect.colliderect(invader.rect):
                    self.invader_collision_handler(bullet, invader, invaders, bullets)
                    break

    def player_invader_collision_listener(self, invader):
        bullets = invader.bullets
        player = self.game.player

        # loop which detects collision of Invader bullets with the player
        for bullet in bullets:
            if bullet.rect.colliderect(player.rect):
                self.player_collision_handler(bullet, player, bullets)
                break
