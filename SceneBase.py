import pygame, Camera,random, copy
import enemies as e
import HelperFunctions as HF
from animation import Static_Animation as SA
from pygame.locals import *
pygame.init()

WINDOWWIDTH = HF.WINDOWWIDTH
WINDOWHEIGHT = HF.WINDOWHEIGHT
# Credit to: https://nerdparadise.com/programming/pygame/part7

class Scene(object):
    def __init__(self):
        self.next = self
        self.background = []
        self.backgroundImage = 0

    # Put in event loop, process events since last frame
    def processEvents(self,event):
        pass

    #Game Logic
    def updateScene(self):
        pass

    # pass Pygame Surface to render onto in
    def renderScene(self,window):
        pass


    def changeScene(self,nextScene):
        self.next = nextScene

    def goToMenu(self):
        # save current scene state
        self.changeScene(nextScene=MenuScene())





#This will be the only menu, it is not necessary to prep it for inheritance
class MenuScene(Scene):

    def __init__(self,player=None):
        Scene.__init__(self)
        #Loads on data for all sprites and background Tiles
        self.player = player
        self.entities = pygame.sprite.Group()
        self.nonAnimated = pygame.sprite.Group()
        fire_1 = SA(pygame.image.load("flames/tile001.png"),WINDOWWIDTH/2 -200,WINDOWHEIGHT/2 - 100)
        fire_1.loadAnimation("flames/tile0**.png")
        fire_2 = SA(pygame.image.load("flames/tile001.png"),WINDOWWIDTH/2 + 200,WINDOWHEIGHT/2 - 100)
        fire_2.loadAnimation("flames/tile0**.png")
        crest = SA(pygame.image.load("crest_nobg.png"),WINDOWWIDTH/2 ,WINDOWHEIGHT/2)
        self.entities.add(fire_1)
        self.entities.add(fire_2)
        self.nonAnimated.add(crest)
        self.changeAnim = pygame.USEREVENT + 2
        pygame.time.set_timer(self.changeAnim,175)

        #Tiles bachground with Rects and loads images
        self.backgroundImage = pygame.image.load("tiles/tile008.png")
        #This must be an array of Rects
        self.background = HF.tileEntireBg("tiles/tile008.png")
        self.terrainimg = pygame.image.load("tiles/tile006.png")
        self.terrain = HF.speckleBackground("tiles/tile006.png", 100)

        #Places cursor in Scene
        self.cursor = pygame.image.load("null.png")
        self.cursor_Rect = self.cursor.get_rect()
        self.cursor_Rect.centery = WINDOWHEIGHT/1.33
        self.cursor_Rect.left = WINDOWWIDTH/2 - WINDOWWIDTH/8
        self.cursorLoc = 0

    def processEvents(self,event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                HF.exitAction()
            if event.key == K_RETURN:
                if self.cursorLoc == 0:
                    self.changeScene(Scene_01("tiles/tile056.png","tiles/tile061.png",self.player))
                if self.cursorLoc == 1:
                    HF.exitAction()
            if event.key == ord("w"):
                if self.cursorLoc > 0:
                    self.cursor_Rect.top -= 80
                    self.cursorLoc -= 1
            if event.key == ord("s"):
                if self.cursorLoc < 1:
                    self.cursor_Rect.top += 80
                    self.cursorLoc += 1
        if event.type == self.changeAnim:
            for entity in self.entities:
                entity.draw_animation()



    def renderScene(self,window):
        for tile in self.background:
            rect = pygame.Rect(tile,(32,32))
            window.blit(self.backgroundImage,rect)
        for tile in self.terrain:
            rect = pygame.Rect(tile,(32,32))
            window.blit(self.terrainimg, rect)
        HF.draw_text('A  Generic  RPG',window,WINDOWWIDTH/2,WINDOWHEIGHT/5,font="Goth.ttf",size=72, color1=(114,60,12))
        HF.draw_text('Begin Adventure',window,WINDOWWIDTH/2,WINDOWHEIGHT/1.33,font="Goth.ttf",size=60,color1=(114,60,12))
        HF.draw_text('Cower in Fear',window,WINDOWWIDTH/2,WINDOWHEIGHT/1.33 + 80,font="Goth.ttf",size=60,color1=(114,60,12))
        for entity in self.entities:
            window.blit(entity.image,entity.rect)
        for sprite in self.nonAnimated:
            window.blit(sprite.image,sprite.rect)
        window.blit(self.cursor,self.cursor_Rect)

class Scene_01(Scene):
    #Player will be passed from Scene to scene to save state
    def __init__(self,filepath1=None,filepath2=None,player=None,wallPath = "basicWall.png"):
        Scene.__init__(self)
        self.next = self
        self.camera = Camera.Camera()
        self.entities = pygame.sprite.Group()
        self.player = player
        self.entities.add(self.player)
        self.backgroundImage = pygame.image.load(filepath1)
        self.background = HF.tileEntireBg(filepath1,windowWidth=5120,windowHeight=2880)
        self.terrainimg = pygame.image.load(filepath2)
        self.terrain = HF.speckleBackground(filepath2,100)
        self.walls = HF.generateWalls(wallPath,windowWidth=5120,windowHeight=2880)
        self.isMenuOpen = False
        self.BATTLE = pygame.USEREVENT + 3
        pygame.time.set_timer(self.BATTLE, 1000)


    def updateScene(self):
        self.player.move_hero()
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
                        #Actually Fix
                if event.type == self.BATTLE:
                   #if HF.battleProbability():
                        self.player.image = self.player.animation.walkLeft[0]
                        self.changeScene(Battle("tiles/tile057.png","tiles/tile063.png",self.player,enemies=[e.spider]))

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
        #Fills background With black
        window.fill((0,0,0))
        #Draws Tiles
        for tile in self.background:
            rect = pygame.Rect(tile,(32,32))
            window.blit(self.backgroundImage,self.camera.apply(rect))

        #Draws Random Tiles To Give Game Random Feel
        for tile in self.terrain:
            rect = pygame.Rect(tile,(32,32))
            window.blit(self.terrainimg,self.camera.apply(rect))
        #Draws Entities (Players,NPC's,ENemies)
        for entity in self.entities:
            window.blit(entity.image,self.camera.apply(entity.rect))

        #Draws Walls
        for wall in self.walls:
            window.blit(wall.image,self.camera.apply(wall.rect))

        if self.isMenuOpen:
            self.player.menu.renderChildren(window)
####################################################################



class Battle(Scene_01):
    #pass in array of enemies
    def __init__(self,filepath1=None,filepath2=None,player=None,enemies=None):
        Scene_01.__init__(self,filepath1,filepath2,player,wallPath=None)
        self.enemies = []
        if enemies != None:
            for enemy in enemies:
                self.enemies.append(enemy)
        self.background = HF.tileEntireBg(filepath1,windowHeight=WINDOWHEIGHT,yLoc=WINDOWHEIGHT/1.7)
        self.terrain = HF.speckleBackground(filepath2,50,windowHeight=WINDOWHEIGHT,min_height=WINDOWHEIGHT*2/3)
        #Add to entities
        cloud = SA(pygame.image.load("cloud.png"))
        cloud.image = pygame.transform.scale(cloud.image,(int(WINDOWWIDTH/10),int(WINDOWHEIGHT/10)))
        cloud.rect = Rect((WINDOWWIDTH/2,WINDOWHEIGHT/10),(100,100))
        self.player.rect.centerx = WINDOWWIDTH*2/3
        self.player.rect.centery = WINDOWHEIGHT/1.35
        self.entities.add(self.player)
        self.isMenuOpen = True
        for x in range(random.randint(3,4)):
            tmp =copy.deepcopy(cloud)
            tmp.rect.centerx += random.randint(-WINDOWWIDTH,WINDOWWIDTH)
            tmp.rect.centery += random.randint(-WINDOWHEIGHT/10,WINDOWHEIGHT/10)
            self.entities.add(tmp)



    def processEvents(self,event):
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        HF.exitAction()
                    self.player.battleMenu.change_child(event,self.enemies)



    def updateScene(self):
        pass

    def renderScene(self,window):
        #Setup
        window.fill((117, 220, 255))
        for tile in self.background:
            rect = pygame.Rect(tile,(32,32))
            window.blit(self.backgroundImage,rect)
        for tile in self.terrain:
            rect = pygame.Rect(tile,(32,32))
            window.blit(self.terrainimg,rect)
        #end Setup
        for entity in self.entities:
            window.blit(entity.image,entity.rect)
        for enemy in self.enemies:
            window.blit(enemy.image,enemy.rect)
        self.player.battleMenu.renderChildren(window)





####################################################################