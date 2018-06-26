import pygame
from HelperFunctions import WINDOWWIDTH, WINDOWHEIGHT
from pygame import *


def simple_camera(target_rect):
    l, t, _, _ = target_rect
    return Rect(-l+WINDOWWIDTH/2, -t+WINDOWHEIGHT/2, WINDOWWIDTH*2, WINDOWHEIGHT*2)

class Camera(object):
    #total level width, height
    def __init__(self, camera_func = simple_camera, width = 1280, height = 720):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(target.rect)

