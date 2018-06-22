#Python Version == 3.2.5
import pygame
import SceneBase as SB
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()


WINDOWWIDTH = 1600
WINDOWHEIGHT = 900
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('A generic RPG')
background5 = pygame.image.load("earth.jpg")


def main():
    scene = SB.Scene_01(background5)

    while True:
        mainClock.tick(60)
        scene.processEvents()
        scene.updateScene()
        scene.renderScene(windowSurface)
        pygame.display.update()


main()
