from vpython import *
from random import randint
dt = 0.001

scene = canvas(width=800, height=450, center = vec(0,0,0))

def rand():
    if round(random()) == 1:
        return 1
    else:
        return -1

wall_1 = box (pos=vec(-400,0,0), length=5, height=450, width=5, color=color.blue)
wall_2 = box (pos=vec(400,0,0), length=5, height=450, width=5, color=color.blue)
wall_3 = box (pos=vec(0,225,0), length=800, height=5, width=5, color=color.blue)
wall_4 = box (pos=vec(0,-225,0), length=800, height=5, width=5, color=color.blue)

pos_random = vector(randint(-300, 300), randint(-175, 175), 0)
dvd = box(pos = pos_random, color=vector.random() ,
size = vector(200,100,1), v = vector(rand()*1000,rand()*1000,0))

def random_color():
    colorrrr = vector.random()
    if colorrrr == vector(0,0,0):
        return random_color()
    else:
        return vector(abs(colorrrr.x),abs(colorrrr.y), abs(colorrrr.z))
        
ct1 = 0
ct2 = 0
ct3 = 0
print(dvd.pos)
print(dvd.v)
while True:
    rate(500)
    dvd.pos = dvd.pos + dvd.v*dt
    if dvd.pos.x + 100 > 400 :
        dvd.v.x = -1*dvd.v.x
        dvd.color = random_color()
        ct1 += 1
    if dvd.pos.x - 100 < -400 :
        dvd.v.x = -1*dvd.v.x
        dvd.color = random_color()
        ct1 += 1
    if dvd.pos.y + 50 > 225 :
        dvd.v.y = -1*dvd.v.y
        dvd.color = random_color()
        ct1 += 1
    if dvd.pos.y - 50 < -225 :
        dvd.v.y = -1*dvd.v.y
        dvd.color = random_color()
        ct1 += 1
        
    if dvd.pos.x + 100 > 400 and dvd.pos.y + 50 > 225:
        ct2 += 1
        ct1 -= 1
        print(ct1 + "right up")
    if dvd.pos.x + 100 > 400 and dvd.pos.y - 50 < -225:
        ct2 += 1
        ct1 -= 1
        print(ct1 + "right down")
    if dvd.pos.x - 100 < -400 and dvd.pos.y + 50 > 225:
        ct2 += 1
        ct1 -= 1
        print(ct1 + "left up")
    if dvd.pos.x - 100 < -400 and dvd.pos.y - 50 < -225:
        ct2 += 1
        ct1 -= 1
        print(ct1 + "left down")
    if ct1 == 10000:
        break
