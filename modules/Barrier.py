from modules.Entity import Entity
import pygame

class Barrier(Entity):
    """
    A barrier entity that extends `Entity`.

    Inherits position, size, image loading, collision rect,
    and group/layer handling. 
    Args:
        x (int): X position.
        y (int): Y position.
        entity_img (str): Path to the bullet image.
        w (int): Width.
        h (int): Height.
        group: Sprite group to add this entity to.
        layer (int): Render layer.
        score (int, optional): Unused for barriers.
        health (int, optional): sprite index .
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
        
    def Barriercollision(self): 
        self.health -= 1 
        self.image = pygame.image.load(f"./media/Barrier{self.health}.png").convert_alpha()
        




