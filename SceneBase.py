import Character, pygame, Camera, sys
import HelperFunctions as HF
from animation import Static_Animation as SA
from pygame.locals import *
pygame.init()

WINDOWWIDTH = 1600
WINDOWHEIGHT = 900
# Credit to: https://nerdparadise.com/programming/pygame/part7

class Scene(object):
    def __init__(self):
        self.next = self

    # Put in event loop, process events since last frame
    def processEvents(self,event):
        pass

    #Game Logic
    def updateScene(self):
        pass

    # pass Pygame Surface to render onto in
    def renderScene(self,window):
        print("renderScene base")


    def changeScene(self,nextScene):
        self.next = nextScene

    def goToMenu(self,menuScene):
        # save current scene state
        print("Hello World")
        self.changeScene(nextScene=menuScene)




class MenuScene(Scene):

    def __init__(self):
        Scene.__init__(self)
        self.entities = pygame.sprite.Group()
        self.nonAnimated = pygame.sprite.Group()
        fire_1 = SA(pygame.image.load("flames/tile001.png"),WINDOWWIDTH/2 -200,WINDOWHEIGHT/2 - 100)
        fire_1.loadAnimation("flames/tile00*.png")
        fire_2 = SA(pygame.image.load("flames/tile001.png"),WINDOWWIDTH/2 + 200,WINDOWHEIGHT/2 - 100)
        fire_2.loadAnimation("flames/tile0**.png")
        crest = SA(pygame.image.load("crest_nobg.png"),WINDOWWIDTH/2 ,WINDOWHEIGHT/2)
        self.entities.add(fire_1)
        self.entities.add(fire_2)
        self.nonAnimated.add(crest)
        self.changeAnim = pygame.USEREVENT + 2
        pygame.time.set_timer(self.changeAnim,175)
        self.setup = 0


    def __str__(self):
        return "Menu"

    def processEvents(self,event):
        print(event)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:

                pygame.quit()
                sys.exit()
            if event.key == K_SPACE:
                self.changeScene(Scene_01())
        if event.type == self.changeAnim:
            for entity in self.entities:
                entity.draw_animation()


    def renderScene(self,window):
        if self.setup == 0:
            HF.tileEntireBg("tiles/tile008.png",window)
            HF.speckleBackground("tiles/tile006.png",window, 200)
            self.setup = 1
        HF.draw_text('A  Simple  RPG',window,WINDOWWIDTH/2,WINDOWHEIGHT/5,font="Goth.ttf",size=72, color1=(114,60,12))
        HF.draw_text('Press Space To Begin',window,WINDOWWIDTH/2,WINDOWHEIGHT/1.33,font="Goth.ttf",size=60,color1=(114,60,12))
        HF.draw_text('Press Escape To exit',window,WINDOWWIDTH/2,WINDOWHEIGHT/1.33 + 80,font="Goth.ttf",size=60,color1=(114,60,12))

        for entity in self.entities:
            window.blit(entity.image,entity.rect)
        for sprite in self.nonAnimated:
            window.blit(sprite.image,sprite.rect)




    def updateScene(self):
        pass






class Scene_01(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.next = self
        self.background = pygame.image.load("earth.jpg")
        self.background_RECT = self.background.get_rect()
        self.background_RECT.centerx = WINDOWWIDTH/2
        self.background_RECT.centery = WINDOWHEIGHT/2
        self.camera = Camera.Camera()
        self.entities = pygame.sprite.Group()
        self.player = Character.Hero(pygame.image.load("chicken\chickenDown1.png"),
        "chicken/chickenLeft*.png",
        "chicken/chickenRight*.png",
        "chicken/chickenUp*.png",
        "chicken/chickenDown*.png")
        self.entities.add(self.player)

    def updateScene(self):
        self.player.draw_hero()
        self.camera.update(self.player)

    def processEvents(self,event):
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == self.player.changeAnim):
                self.player.animationController()
            if event.type == KEYDOWN:
                if event.key == ord("e"):
                    self.goToMenu(MenuScene())

            self.player.movementController(event)

    def renderScene(self,window):
        # render background, player, enemies, npc's
        window.blit(self.background,self.camera.apply(self.background_RECT))
        for entity in self.entities:
            window.blit(entity.image,self.camera.apply(entity.rect))

