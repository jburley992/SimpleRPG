#Python Version == 3.2.5
import pygame,Character,HelperFunctions
import SceneBase as SB
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

windowSurface = pygame.display.set_mode((HelperFunctions.WINDOWWIDTH, HelperFunctions.WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('A Simple RPG')

player = Character.Hero(pygame.image.load("hero/frontwalk/tile018.png"),
        "hero/rightWalk/tile0**.png",
        "hero/leftWalk/tile0**.png",
        "hero/backWalk/tile0**.png",
        "hero/frontwalk/tile0**.png")

def main():
    scene = SB.MenuScene(player)

    while True:
        mainClock.tick(100)
        for event in pygame.event.get():
            scene.processEvents(event)
        scene.renderScene(windowSurface)
        scene.updateScene()
        pygame.display.update()
        scene = scene.next
        print(scene)


main()
