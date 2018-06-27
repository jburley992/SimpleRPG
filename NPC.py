# Design enemy so that it Can be part of a sprite Group
import pygame,random

class NPC(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()



class Enemy(NPC):

    def __init__(self,image,damage,health,*abilities):
        NPC.__init__(image)
        self.base_damage = damage
        self.health = health
        self.abilities = abilities
    #Buff allies, harm foes
    def battle(self,allies=None,foes=None):
        '''Fighting Mechanics will go here
           Devise Algorithm to make attacks seem pseudorandom
           Additionally, attacks with more damage should be used less ofter'''
        tmp = 0
        for atk in self.abilities:
            tmp += atk.damage
        counter = 0
        for atk in self.abilities:
            atk.likelihood = atk.damage/tmp
            if atk.inflictStatus == True:
                counter += 0.1*atk.likelihood
                atk.likelihood -= 0.1*atk.likelihood
            #Basic Attack gets an increase in likelihood
            #Over Strong and Special attacks
            self.abilities[0] += counter
            id = float(random.randint(0,1000))/1000.0
        for index,atk in enumerate(self.abilities):
            if atk.likelihood < id and not (self.abilities[index + 1]  <id):
                return atk




        pass
