import pygame

class interactables(pygame.sprite.Sprite):

    def __init__(self,image=None):
        pygame.sprite.Sprite.__init__(self)
        if image != None:
            self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    def collisionAction(self,hero):
        print("Overwrite")

    def activateAction(self,hero,event):
        print("overwrite")


class walls(interactables):
    def __init__(self,image):
        interactables.__init__(self,image)

    def collisionAction(self,hero):
        if self.rect.colliderect(hero.rect):
            if(hero.moveLeft):
                hero.moveLeft = False
                hero.rect.left += 5
            if(hero.moveRight):
                hero.moveRight = False
                hero.rect.right -= 5
            if(hero.moveUp):
                hero.moveUp = False
                hero.rect.top += 5
            if(hero.moveDown):
                hero.moveDown = False
                hero.rect.bottom -= 5


class Weapons(interactables):
    def __init__(self,image,damage,ability = None):
        interactables.__init__(self,image)
        self.description = "It's very pointy..."
        self.damage = damage
        #Elemental Weapons?
        self.ability = ability



class Buildings(interactables):

    def __init__(self,x,y,img=None):
        interactables.__init__(self)
        self.rect.centerx = x
        self.rect.centery = y

    def collisionAction(self,hero):
        if self.rect.colliderect(hero.rect):
            #Enter Housr === ChangeScene
            pass
