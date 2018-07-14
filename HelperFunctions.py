import pygame, sys, random,interactables
from math import ceil as roundUp
from pygame.locals import *

WINDOWWIDTH = 1920
WINDOWHEIGHT = 1080
ICONSIZE =(32,32)

def draw_text(text, window, x=0, y = 0, color1 = (255,255,255),color2 = None, font="Goth.ttf",size = 60):
    Font = pygame.font.Font(font, size)
    Display_text = Font.render(text, True, color1)
    Display_text_rect = Display_text.get_rect()
    Display_text_rect.centerx = x
    Display_text_rect.centery= y
    window.blit(Display_text, Display_text_rect)




def tileEntireBg(tilePath,windowWidth = WINDOWWIDTH,windowHeight = WINDOWHEIGHT,yLoc=0):
    tile = pygame.image.load(tilePath)
    tileWidth  = tile.get_size()[0]
    tileHeight = tile.get_size()[1]
    xTiles = roundUp( windowWidth / tileWidth)
    yTiles = roundUp(windowHeight / tileHeight)
    xLoc = -tileWidth
    tiles = []
    for y in range(yTiles):
        for x in range(xTiles+40):
            if(xLoc >= windowWidth):
                xLoc = 0
                yLoc += tileHeight
            else:
                xLoc += tileWidth
            tiles.append((xLoc,yLoc))
    return tiles



def speckleBackground(tilePath,numTiles,windowWidth = WINDOWWIDTH,windowHeight = WINDOWHEIGHT,min_height=0):
    tile = pygame.image.load(tilePath)
    tileWidth = tile.get_size()[0]
    tileHeight = tile.get_size()[1]
    tileLocs = []
    for x in range(numTiles):
        xpos = random.randint(0,windowWidth)
        xpos = xpos - (xpos % tileWidth)
        ypos = random.randint(min_height,windowHeight)
        ypos = ypos - (ypos % tileHeight)
        tileLocs.append((xpos,ypos))
    return tileLocs


def generateWalls(tilePath,windowWidth = WINDOWWIDTH,windowHeight = WINDOWHEIGHT):
    if tilePath == None:
        return None
    tile = pygame.image.load(tilePath)
    width = roundUp(tile.get_size()[0])
    height = roundUp(tile.get_size()[1])
    tileLocs = []
    for x in range(roundUp(windowWidth/width)):
        wallTop = interactables.walls(tilePath)
        wallBottom = interactables.walls(tilePath)
        wallTop.rect.left = x*width
        wallBottom.rect.left = x*width
        wallTop.rect.top = 0
        wallBottom.rect.top = windowHeight
        tileLocs.append(wallTop)
        tileLocs.append(wallBottom)
    for y in range(roundUp(windowHeight/height)):
        wallRight = interactables.walls(tilePath)
        wallLeft = interactables.walls(tilePath)
        wallLeft.rect.left = 0
        wallRight.rect.left = windowWidth
        wallLeft.rect.top = y*height
        wallRight.rect.top = y*height
        tileLocs.append(wallLeft)
        tileLocs.append(wallRight)
    return tileLocs



def battleProbability():
    # A pseudorandom Algorithm that will be called every 5 seconds to
    #determine if you enter a battle
    var1 = random.randint(0,100)
    var2 = random.randint(0,100)
    for x in range(var2 - 7,var2 +7):
        if var1 == x:
            return True
    return False


def selectTextSize():
    textSize = 0
    if WINDOWWIDTH >= 3440:
        textSize = 24
    if WINDOWWIDTH >= 2560:
        textSize = 20
    if WINDOWWIDTH >= 1600:
        textSize = 18
    else:
        textSize = 14
    return textSize

def selectScale():
    scale = 0
    if WINDOWWIDTH >= 3440:
        scale = 1
    if WINDOWWIDTH >= 2560:
        scale = 0.8
    if WINDOWWIDTH >= 1600:
        scale = 0.6
    else:
        scale = 0.5
    return scale


def exitAction(*args):
        pygame.quit()
        sys.exit(0)



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
























