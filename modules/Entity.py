import pygame


class Entity:
    def __init__(self, x, y, entity_img, bullet_img, w, h, score=0, health=1):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.entity_img = pygame.image.load(entity_img)
        self.entity_img = pygame.transform.scale(self.entity_img, (self.w, self.h))
        self.bullet_img = pygame.image.load(bullet_img)
        self.bullet_img = pygame.transform.scale(self.bullet_img, (32, 32))
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.score = score
        self.health = health
