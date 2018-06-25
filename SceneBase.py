import Character, pygame, Camera
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
        pass


    def changeScene(self,nextScene,player=None):
        self.next = nextScene

    def goToMenu(self):
        # save current scene state
        self.changeScene(nextScene=MenuScene())




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
        self.terrainimg = pygame.image.load("tiles/tile006.png")
        self.terrain = HF.speckleBackground("tiles/tile006.png", 100)
        self.cursor = pygame.image.load("null.png")
        self.cursor_Rect = self.cursor.get_rect()
        self.cursor_Rect.centery = WINDOWHEIGHT/1.33
        self.cursor_Rect.left = WINDOWWIDTH/3
        self.cursorLoc = 0

    def __str__(self):
        return "Menu"

    def processEvents(self,event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                HF.exitAction()
            if event.key == K_RETURN:
                if self.cursorLoc == 0:
                    self.changeScene(Scene_01())
                if self.cursorLoc == 1:
                    HF.exitAction()
            if event.key == ord("w"):
                if self.cursorLoc > 0:
                    self.cursor_Rect.top -= 80
                    self.cursorLoc -= 1
            if event.key == ord("s"):
                if self.cursorLoc < 2:
                    self.cursor_Rect.top += 80
                    self.cursorLoc += 1
        if event.type == self.changeAnim:
            for entity in self.entities:
                entity.draw_animation()



    def renderScene(self,window):
        HF.tileEntireBg("tiles/tile008.png",window)
        for tile in self.terrain:
            rect = pygame.Rect(tile,(32,32))
            window.blit(self.terrainimg, rect)
        HF.draw_text('A  Generic  RPG',window,WINDOWWIDTH/2,WINDOWHEIGHT/5,font="Goth.ttf",size=72, color1=(114,60,12))
        HF.draw_text('Press Space To Begin',window,WINDOWWIDTH/2,WINDOWHEIGHT/1.33,font="Goth.ttf",size=60,color1=(114,60,12))
        HF.draw_text('Press Escape To exit',window,WINDOWWIDTH/2,WINDOWHEIGHT/1.33 + 80,font="Goth.ttf",size=60,color1=(114,60,12))
        for entity in self.entities:
            window.blit(entity.image,entity.rect)
        for sprite in self.nonAnimated:
            window.blit(sprite.image,sprite.rect)
        window.blit(self.cursor,self.cursor_Rect)


    def updateScene(self):
        pass




class Scene_01(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.next = self
        self.camera = Camera.Camera()
        self.entities = pygame.sprite.Group()
        self.player = Character.Hero(pygame.image.load("hero/frontwalk/tile018.png"),
        "hero/rightWalk/tile0**.png",
        "hero/leftWalk/tile0**.png",
        "hero/backWalk/tile0**.png",
        "hero/frontwalk/tile0**.png")
        self.entities.add(self.player)
        self.terrainimg = pygame.image.load("tiles/tile061.png")
        self.terrain = HF.speckleBackground("tiles/tile061.png",100)
        self.walls = HF.generateWalls("basicWall.png")
        self.isMenuOpen = False
        self.BATTLE = pygame.USEREVENT + 3
        pygame.time.set_timer(self.BATTLE, 5000)
    def updateScene(self):
        self.player.draw_hero()
        self.camera.update(self.player)
        for wall in self.walls:
            wall.collisionAction(self.player)

    def processEvents(self,event):
        if not self.isMenuOpen:
                if event.type == QUIT:
                    HF.exitAction()
                if (event.type == self.player.changeAnim):
                    self.player.animationController()
                if event.type == KEYDOWN:
                    if event.key == ord("e"):
                        self.goToMenu()
                    if event.key == K_TAB:
                        self.isMenuOpen = True
                if event.type == self.BATTLE:
                    if HF.battleProbability():
                        self.changeScene(Battle([]),self.player)

                self.player.movementController(event)
        else:
            if event.type == QUIT:
                HF.exitAction()
            if event.type == KEYDOWN:
                self.player.menuController(event)
                if event.key == K_TAB:
                    self.isMenuOpen = False

    def renderScene(self,window):
        # render background, player, enemies, npc's
        window.fill((0,0,0))
        HF.tileEntireBg("tiles/tile056.png",window, self.camera)
        for tile in self.terrain:
            rect = pygame.Rect(tile,(32,32))
            window.blit(self.terrainimg,self.camera.apply(rect))
        for entity in self.entities:
            window.blit(entity.image,self.camera.apply(entity.rect))
        for wall in self.walls:
            window.blit(wall.img,self.camera.apply(wall.rect))

        if self.isMenuOpen:
            self.player.menu.renderChildren(window)
####################################################################



class Battle(Scene):
    #pass in array of enemies
    def __init__(self,enemies):
        Scene.__init__(self)
        self.enemies = enemies



    def processEvents(self,event):
        pass

    def updateScene(self):
        pass

    # pass Pygame Surface to render onto in
    def renderScene(self,window):
        pass


####################################################################