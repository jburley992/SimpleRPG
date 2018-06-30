import pygame, glob,copy
from pygame import *

class Animation(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


    def loadAnimation(self,animation):
        pass



class Static_Animation(Animation):
    def __init__(self,starting_image,x=0,y=0):
        Animation.__init__(self)
        self.image = starting_image
        self.animation = []
        self.anim_length = None
        self.keyFrame = 0
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    #Overloaded assignment operators
    def __copy__(self):
        newAnim = type(self)(self.image)
        newAnim.rect = self.rect
        newAnim.__dict__.update(self.__dict__)
        return newAnim

    def __deepcopy__(self, memodict={}):
        newAnim = type(self)(self.image)
        self.rect = copy.deepcopy(self.rect,memodict)
        newAnim.__dict__.update(self.__dict__)
        return newAnim

    def loadAnimation(self,animation):
        self.animation = glob.glob(animation)
        self.animation.sort()
        for index, img in enumerate(self.animation):
            self.animation[index] = pygame.image.load(img)
        self.anim_length = len(self.animation)


    def draw_animation(self):
        if self.keyFrame > self.anim_length - 2:
            self.keyFrame = 0
        else:
            self.keyFrame += 1
        self.image = self.animation[self.keyFrame]


class Character_Animation(Animation):
    def __init__(self):
        Animation.__init__(self)
        self.walkRight = 0
        self.walkLeft = 0
        self.walkUp = 0
        self.walkDown = 0

    #Imlplement Overloaded Deep copy operation

    def loadAnimation(self,animR,animL,animU,animD):
        self.walkRight = glob.glob(animR)
        self.walkRight.sort()
        for index,img in enumerate(self.walkRight):
            self.walkRight[index] = pygame.image.load(img)

        self.walkLeft = glob.glob(animL)
        self.walkLeft.sort()
        for index,img in enumerate(self.walkLeft):
            self.walkLeft[index] = pygame.image.load(img)

        self.walkUp = glob.glob(animU)
        self.walkUp.sort()
        for index,img in enumerate(self.walkUp):
            self.walkUp[index] = pygame.image.load(img)


        self.walkDown = glob.glob(animD)
        self.walkDown.sort()
        for index,img in enumerate(self.walkDown):
            self.walkDown[index] = pygame.image.load(img)

    def battleAnimation(self):
        pass
