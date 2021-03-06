import pygame,enemies
from pygame.locals import *
import HelperFunctions as HF
from interactables import Weapons as w
from pygame import *


class MenuItem(object):
    def __init__(self,title,func):
        self.title = title
        self.items = []
        self.index = 0
        self.action = func
        self.cursor = pygame.image.load("null.png")
        self.cursorRect = self.cursor.get_rect()

    def display_items(self,window):
        #implement scrolling through Menu

        #Menu Scaling
        rect = pygame.Rect((HF.WINDOWWIDTH/2 - 350, 130), HF.ICONSIZE)
        textRect = pygame.Rect((HF.WINDOWWIDTH/2 - 350, 130), HF.ICONSIZE)
        textRect.left += 225
        scale = HF.selectScale()
        for item in self.items:
            if item.image != None:
                if type(item) != type(enemies.spider):
                    window.blit(item.image,rect)
                window.blit(self.cursor,self.cursorRect)
                if item.description != None:
                    HF.draw_text(item.description[:25],window,textRect.centerx,textRect.centery,size=HF.selectTextSize(),font="Typewriter.ttf")
                rect.top += 60
                textRect.top += 60
        


    def addItem(self,item):
        self.items.append(item)

    def chooseEnemyToAttack(self,event,enemies=None):
        amount = len(enemies)
        if(amount == 0):
            #End battle
            return
        self.items = enemies
        self.cursorRect.centerx = enemies[self.index].rect.centerx - 100
        self.cursorRect.centery = enemies[self.index].rect.centery
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == KEYDOWN:
            if event.key == K_UP and self.index < (amount -1):
                self.index += 1
                print(self.index)
            elif event.key == K_DOWN and self.index > 0:
                self.index -= 1





class Menu(object):
    def __init__(self):
        self.children = [
            MenuItem("Inventory",None),
            MenuItem("Spells",None),
            MenuItem("Quests",None),
            MenuItem("Stats",None),
            MenuItem("Exit",HF.exitAction)
        ]
        #Fix Naming Conventions
        self.children[0].addItem(w("null.png",5))
        self.selectedChild = 0
        self.menu = pygame.image.load("menu.png")
        self.menu = pygame.transform.scale(self.menu,(int(HF.WINDOWWIDTH*0.9),int(HF.WINDOWHEIGHT*0.9)))
        self.menu_Rect = self.menu.get_rect()
        #Implement UI Scaling At some point
        self.menu_Rect.centerx = HF.WINDOWWIDTH/2
        self.menu_Rect.centery = HF.WINDOWHEIGHT/2
        self.offset = self.menu_Rect.top
        self.cursor = pygame.image.load("null.png")
        self.cursor_Rect = self.cursor.get_rect()
        scale = HF.selectScale()
        self.cursor = pygame.transform.scale(self.cursor,(int(self.cursor_Rect.width*scale),int(self.cursor_Rect.height*scale)))
        self.cursor_Rect.bottom = self.menu_Rect.top + 65
        self.cursor_Rect.left = self.menu_Rect.left - 20


    def add_child(self,item):
        self.children.append(item)

    def change_child(self,event,enemies=[]):

            if event.type == KEYDOWN:

                if event.key == ord("w"):
                    if self.selectedChild == 0:
                        pass
                    else:
                        self.selectedChild -= 1
                        self.cursor_Rect.top -= 60
                elif event.key == ord("s"):
                    if self.selectedChild == len(self.children) - 1:
                        pass
                    else:
                        self.selectedChild += 1
                        self.cursor_Rect.top += 60
            # Menu Children events Called here
            if  self.children[self.selectedChild].action != None:
                self.children[self.selectedChild].action(self.children[self.selectedChild],event,enemies)
                #Will return what object is selected in the list
                return self.children.index


    def renderChildren(self,window):

        window.blit(self.menu, self.menu_Rect)
        window.blit(self.cursor, self.cursor_Rect)
        for item in self.children:
            HF.draw_text(item.title, window, x=self.menu_Rect.left + 155, y=self.offset, size=40, font="Typewriter.ttf")
            self.offset += 60
        self.offset = self.menu_Rect.top + 65
        self.children[self.selectedChild].display_items(window)


class battleMenu(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.menu = pygame.image.load("battleMenu.png")
        self.menu = pygame.transform.scale(self.menu,(300,400))
        self.menu_Rect.left = 0
        self.menu_Rect.centery = HF.WINDOWHEIGHT/2
        self.children = [
            MenuItem("Inventory",None),
            MenuItem("Attack", MenuItem.chooseEnemyToAttack),
            MenuItem("Spells",None),
            MenuItem("Run",None),
            MenuItem("Exit",None)
        ]
        self.cursor_Rect.left = 0
        self.cursor_Rect.top = self.offset + 55
        #Modify Where Cursor and Menu Items Load


