import pygame, glob, Camera
from pygame import *
# When accessing files be sure to make it so that the files can be accessed on both
# windows and unix environments



class Animation(object):
    def __init__(self):
        self.walkRight = 0
        self.walkLeft = 0
        self.walkUp = 0
        self.walkDown = 0

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


class Hero(pygame.sprite.Sprite):
    def __init__(self, image,r,l,u,d):
        # General Stuff
        pygame.sprite.Sprite.__init__(self)
        self.movespeed = 7
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.bottom, self.rect.left = 800, 0
        # Movement Stuff
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False
        #Animation Stuff
        self.animation = Animation()
        self.animation.loadAnimation(r,l,u,d)
        self.currentAnimlength = 0
        self.maxAnimLength = len(self.animation.walkRight)
        self.changeAnim = pygame.USEREVENT + 1
        pygame.time.set_timer(self.changeAnim, 125)

    def draw_hero(self):
        if self.moveDown:
            self.rect.top += self.movespeed
        if self.moveUp:
            self.rect.top -= self.movespeed
        if self.moveLeft:
            self.rect.left -= self.movespeed
        if self.moveRight:
            self.rect.right += self.movespeed



    def animationController(self):
        self.currentAnimlength += 1
        if(self.currentAnimlength >= self.maxAnimLength):
            self.currentAnimlength = 0
        if(self.moveRight):
            self.image = self.animation.walkRight[self.currentAnimlength]
        elif(self.moveLeft):
            self.image = self.animation.walkLeft[self.currentAnimlength]
        elif(self.moveUp):
            self.image = self.animation.walkUp[self.currentAnimlength]
        elif(self.moveDown):
            self.image = self.animation.walkDown[self.currentAnimlength ]


    def movementController(self, event):
        if event.type == KEYDOWN:
            if event.key == ord("a"):
                self.moveLeft = True
                self.moveRight = False
            if event.key == ord("d"):
                self.moveLeft = False
                self.moveRight = True
            if event.key == ord("w"):
                self.moveDown = False
                self.moveUp = True
                self.moveDown = False
            if event.key == ord("s"):
                self.moveUp = False
                self.moveDown = True

        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == ord("a"):
                self.moveLeft = False
            if event.key == ord("d"):
                self.moveRight = False
            if event.key == ord("w"):
                self.moveUp = False
            if event.key == ord("s"):
                self.moveDown = False


