import Character, pygame, Camera, sys
from pygame.locals import *

WINDOWWIDTH = 1600
WINDOWHEIGHT = 900
# Credit to: https://nerdparadise.com/programming/pygame/part7

class Scene(object):
    def __init__(self):
        self.next = self

    # Put in event loop, process events since last frame
    def processEvents(self,events):
        pass

    #Game Logic
    def updateScene(self):
        pass

    # pass Pygame Surface to render onto in
    def renderScene(self,window):
        pass

    def changeScene(self,nextScene):
        self.next = nextScene

    def goToMenu(self,menuScene):
        # save current scene state
        self.changeScene(nextScene=menuScene)




class MenuScene(Scene):

    def __init__(self):
        Scene.__init__(self)

    def renderScene(self,window):
        print("Hello")
        menu = pygame.Rect(10,10,WINDOWHEIGHT-20,WINDOWWIDTH - 20)
        pygame.draw.rect(window,(100,100,100),menu)



class Scene_01(Scene):
    def __init__(self,background):
        Scene.__init__(self)
        self.next = self
        self.background = background
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

    def processEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == self.player.changeAnim):
                self.player.animationController()
            if event.type == KEYDOWN:
                if event.key == ord("e"):
                    print("yoYo")
                    self.goToMenu(MenuScene())

            self.player.movementController(event)

    def renderScene(self,window):
        # render background, player, enemies, npc's
        window.blit(self.background,self.camera.apply(self.background.get_rect()))
        for entity in self.entities:
            window.blit(entity.image,self.camera.apply(entity.rect))

