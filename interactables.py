import pygame

class interactables(pygame.sprite.Sprite):

    def __init__(self,img=None):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(img)
        self.rect = self.img.get_rect()

    def collisionAction(self,hero):
        print("Overwrite")

    def activateAction(self,hero):
        print("overwrite")


class walls(interactables):
    def __init__(self,img):
        interactables.__init__(self,img)

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
    def __init__(self,img,damage,ability = None):
        interactables.__init__(self,img)
        self.description = "It's very pointy..."
        self.damage = damage
        #Elemental Weapons?
        self.ability = ability