import pygame, sys, random,interactables
from math import ceil as roundUp
from pygame.locals import *

def draw_text(text, window, x=0, y = 0, color1 = (255,255,255),color2 = None, font="Goth.ttf",size = 60):
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


def tileEntireBg(tilePath,screen, camera=None,windowWidth = 1600,windowHeight = 900):
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
        if(xLoc >= windowWidth):
            xLoc = 0
            yLoc += tileHeight
        else:
            xLoc += tileWidth
        tile_rect.left = xLoc
        tile_rect.top = yLoc
        if camera == None:
            screen.blit(tile,tile_rect)
        else:
            screen.blit(tile, camera.apply(tile_rect))


def speckleBackground(tilePath,numTiles,windowWidth = 1600,windowHeight = 900):
    tile = pygame.image.load(tilePath)
    tileWidth = tile.get_size()[0]
    tileHeight = tile.get_size()[1]
    tileLocs = []
    for x in range(numTiles):
        xpos = random.randint(0,windowWidth)
        xpos = xpos - (xpos % tileWidth)
        ypos = random.randint(0,windowHeight)
        ypos = ypos - (ypos % tileHeight)
        tileLocs.append((xpos,ypos))
    return tileLocs


def generateWalls(tilePath,windowWidth = 1600,windowHeight = 900):
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



def OpenInGameMenu(window):
    menu = pygame.image.load("menu.png")
    cursor = pygame.image.load("null.png")
    menu_Rect = menu.get_rect()
    cursor_Rect = cursor.get_rect()
    menu_Rect.top = 0
    menu_Rect.left = 0
    offset = menu_Rect.top + 130
    cursor_Rect.centery = offset
    cursor_Rect.left = menu_Rect.left - 20
    window.blit(menu,menu_Rect)
    window.blit(cursor,cursor_Rect)
    Categories = ["Inventory", "Spells","Abilities","Quests","Stats"]
    for item in Categories:
        draw_text(item, window, x=menu_Rect.left + 185, y=offset, size=40, font="Typewriter.ttf")
        offset += 60




























