import pgzrun
import random

HEIGHT = 800
WIDTH = 1200
white = (255,255,255)
blue =  (10,10,255)

ship = Actor("images/galaga")
ship.pos = (WIDTH//2,HEIGHT-60)
 
alien = Actor("images/bug")
 
speed=5
bullets = []
enemies=[]
for x in range(8):
    for y in range(4):
        alien = Actor("images/bug")
        enemies.append(alien)
        


def draw():


















pgzrun.go()