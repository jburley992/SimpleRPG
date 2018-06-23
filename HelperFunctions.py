import pygame, sys, random
from math import ceil as roundUp
from pygame.locals import *

def draw_text(text, window, x=0, y = 0, color1 = (255,255,255),color2 = None, font="Arial",size = 60):
    Font = pygame.font.Font(font, size)
    Display_text = Font.render(text, True, color1)
    Display_text_rect = Display_text.get_rect()
    Display_text_rect.centerx = x
    Display_text_rect.centery= y
    window.blit(Display_text, Display_text_rect)

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    pygame.quit()
                    sys.exit()
                return


def tileEntireBg(tilePath,screen,windowWidth = 1600,windowHeight = 900):
    #Fix Later, Make tiles load perfectly
    tile = pygame.image.load(tilePath)
    tile_rect = tile.get_rect()
    tileWidth  = tile.get_size()[0]
    tileHeight = tile.get_size()[1]
    xTiles = windowWidth / tileWidth
    yTiles = roundUp(windowHeight / tileHeight)
    xLoc = -tileWidth
    yLoc = 0
    for x in range( roundUp(xTiles * yTiles) + 100):
        print(x)
        if(xLoc >= windowWidth):
            xLoc = 0
            yLoc += tileHeight
        else:
            xLoc += tileWidth
        tile_rect.left = xLoc
        tile_rect.top = yLoc
        screen.blit(tile,tile_rect)


def speckleBackground(tilePath,screen,numTiles,windowWidth = 1600,windowHeight = 900):
    tile = pygame.image.load(tilePath)
    tile_rect = tile.get_rect()
    tileWidth = tile.get_size()[0]
    tileHeight = tile.get_size()[1]
    for x in range(numTiles):
        xpos = random.randint(0,windowWidth)
        xpos = xpos - (xpos % tileWidth)
        ypos = random.randint(0,windowHeight)
        ypos = ypos - (ypos % tileHeight)
        tile_rect.left = xpos
        tile_rect.top = ypos
        screen.blit(tile, tile_rect)


