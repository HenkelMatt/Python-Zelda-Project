import os
import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        image_path = os.path.join(os.path.dirname(__file__), '..', 'graphics', 'test', 'rock.png')
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)