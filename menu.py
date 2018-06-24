import pygame
import HelperFunctions as HF
from pygame import *


class MenuItem(object):
    def __init__(self,title):
        self.title = title
        self.items = []

    def display_items(self):
        pass

    def selectItem(self):
        pass





class Menu(object):
    def __init__(self):
        self.children = [
            MenuItem("Inventory"),
            MenuItem("Spells"),
            MenuItem("Quests"),
            MenuItem("Stats"),
            MenuItem("Exit")
        ]

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




    def renderChildren(self,window):

        window.blit(self.menu, self.menu_Rect)
        window.blit(self.cursor, self.cursor_Rect)
        for item in self.children:
            HF.draw_text(item.title, window, x=self.menu_Rect.left + 185, y=self.offset, size=40, font="Typewriter.ttf")
            self.offset += 60
        self.offset = self.menu_Rect.top + 130



