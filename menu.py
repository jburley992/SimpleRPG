import pygame
import HelperFunctions as HF
from interactables import Weapons as w
from pygame import *


class MenuItem(object):
    def __init__(self,title,func):
        self.title = title
        self.items = []
        #Pass in a function that will change actions
        self.action = func
        self.index = 0

    def display_items(self,window):
        #implement scrolling through Menu
        rect = pygame.Rect((HF.WINDOWWIDTH/2 - 350, 130), HF.ICONSIZE)
        textRect = pygame.Rect((HF.WINDOWWIDTH/2 - 350, 130), HF.ICONSIZE)
        textRect.left += 225
        for item in self.items:
            if item.img != None:
                window.blit(item.img,rect)
                HF.draw_text(item.description[:25],window,textRect.centerx,textRect.centery,size=24,font="Typewriter.ttf")
                rect.top += 60
                textRect.top += 60




    def addItem(self,item):
        self.items.append(item)





class Menu(object):
    def __init__(self):
        self.children = [
            MenuItem("Inventory",None),
            MenuItem("Spells",None),
            MenuItem("Quests",None),
            MenuItem("Stats",None),
            MenuItem("Exit",HF.exitAction)
        ]
        self.children[0].addItem(w("null.png",5))
        self.selectedChild = 0
        self.menu = pygame.image.load("menu.png")
        self.menu_Rect = self.menu.get_rect()
        self.menu_Rect.top = 0
        self.menu_Rect.left = 0
        self.offset = self.menu_Rect.top + 130
        self.cursor = pygame.image.load("null.png")
        self.cursor_Rect = self.cursor.get_rect()
        self.cursor_Rect.centery = self.offset
        self.cursor_Rect.left = self.menu_Rect.left - 20


    def add_child(self,item):
        self.children.append(item)


    def change_child(self,event):
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

            elif event.key == K_RETURN:
                self.children[self.selectedChild].action()

    def renderChildren(self,window):

        window.blit(self.menu, self.menu_Rect)
        window.blit(self.cursor, self.cursor_Rect)
        for item in self.children:
            HF.draw_text(item.title, window, x=self.menu_Rect.left + 185, y=self.offset, size=40, font="Typewriter.ttf")
            self.offset += 60
        self.offset = self.menu_Rect.top + 130
        self.children[self.selectedChild].display_items(window)



