import pygame, sys
from pygame.locals import *

def draw_text(text, window, x=0, y = 0, color1 = (255,255,255),color2 = (0,0,0)):
    basicFont = pygame.font.SysFont(None, 32)
    basicFont2 = pygame.font.SysFont(None, 60, False, True)
    text2 = basicFont2.render(text, True, color1, color2)
    textRect2 = text2.get_rect()
    textRect2.right = x
    textRect2.top = y
    window.blit(text2, textRect2)

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
