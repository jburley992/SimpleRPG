import pygame,menu
from animation import Character_Animation as CA
import HelperFunctions as HF
from pygame import *
# When accessing files be sure to make it so that the files can be accessed on both
# windows and unix environments

class Hero(pygame.sprite.Sprite):
    def __init__(self, image,r,l,u,d):
        # General Stuff
        pygame.sprite.Sprite.__init__(self)
        self.movespeed = 7
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = 800, 450
        # Movement Stuff
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False
        #Animation Stuff
        self.animation = CA()
        self.animation.loadAnimation(r,l,u,d)
        self.currentAnimlength = 0
        self.maxAnimLength = len(self.animation.walkRight)
        self.changeAnim = pygame.USEREVENT + 1
        pygame.time.set_timer(self.changeAnim, 125)
        self.damage = 5
        #Menu
        self.menu = menu.Menu()
        self.battleMenu =menu.battleMenu()

    def move_hero(self):
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


    def menuController(self,event):
            self.menu.change_child(event)


    #Implement these functions
    def interactWithBattleMenu(self):
        subMenu = self.battleMenu.children[self.battleMenu.selectedChild]
        if subMenu.title == "Attack":
            self.attack()
        elif subMenu.title == "Inventory":
            self.useItem()
        elif subMenu.title == "Spells":
            self.cast()
        elif subMenu.title == "Run":
            if HF.runchance():
                self.returnToLevel()
        elif subMenu.title == "Exit":
                HF.exitAction()

    def attack(self):
        #Implement Battle Animation
        subMenu = self.battleMenu.children[self.battleMenu.selectedChild]
        subMenu.items[subMenu.index].health -= self.damage
        if(subMenu.items[subMenu.index].health ) <= 0:
            subMenu.items.remove(subMenu.items[subMenu.index])
            subMenu.index = len(subMenu.items) - 1











