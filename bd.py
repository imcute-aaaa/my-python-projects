import pygame
from math import radians, sin, cos, atan2, degrees, sqrt
from pgzrun import *
import pgzrun
import rect
import random


pl=Actor('bird1')
yumdict={'birddead':1}
food=[]
debug=0
global sized,deltaa
sized=1
deltaa=0


class yummy(Actor):
    def upk(self,img):
        self.pid = len(food)
        self.image=img
        self.yumyum = yumdict[img]
        self.PLEASEUPDATEME = True
    def up(self,dela,sizd):
        #self.size = (1/sizd, 1/sizd)
        if self.PLEASEUPDATEME:
            if self.colliderect(pl):
                if sizd*sizd>=self.yumyum:
                    self.PLEASEUPDATEME=False
                    dela = sqrt(self.yumyum+dela**2)
                    if debug:
                        print('Oww!Player,don\'t eat me!')
                else:
                    if debug:
                        print('Haha,you can\'t eat me!')
            if debug:
                print('I\'m up to date!')
        else:
            if debug:
                print('...dead...')


def uk(dea, sied):
    dea = 0
    for il in food:
        il.up(dea, sied)
        sied += dea


def update():
    uk(deltaa,sized)


def draw():
    screen.blit('background', (0, 0))
    pl.draw()
    for ilj in food:
        if ilj.PLEASEUPDATEME:
            ilj.draw()


def on_mouse_move(pos,rel):
    pl.x = pos[0]
    pl.y = pos[1]
    if (rel[0]+rel[1])>=10:
        for igh in range(int((rel[0]+rel[1])/50)):
            a=yummy('birddead', (random.randint(0, 600), random.randint(0, 600)))
            a.upk('birddead')
            food.append(a)


pgzrun.go()
