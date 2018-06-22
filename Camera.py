import pygame
from pygame import *


def simple_camera(camera, target_rect,HALF_WWIDTH,HALF_WHEIGHT):
    #Find out what this does
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l+HALF_WWIDTH, -t+HALF_WHEIGHT, HALF_WWIDTH*2, HALF_WHEIGHT*2)

class Camera(object):
    def __init__(self, camera_func = simple_camera, width = 5120, height = 2880):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.move(self.state.topleft)

    def update(self, target,width= 800,height = 450):
        self.state = self.camera_func(self.state, target.rect,width,height)

