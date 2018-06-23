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



def main():
    scene = SB.MenuScene()

    while True:
        mainClock.tick(100)
        for event in pygame.event.get():
            scene.processEvents(event)
        scene.updateScene()
        scene.renderScene(windowSurface)
        pygame.display.update()
        scene = scene.next


main()
