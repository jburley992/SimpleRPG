# Design enemy so that it Can be part of a sprite Group
import pygame

class NPC(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()



class Enemy(NPC):

    def __init__(self,image):
        NPC.__init__(image)
