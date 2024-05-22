from tkinter import *
import math
import time
from random import choice
import random
from random import randint

p=0
def scetch():
    global p
    p+=1
root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
class ball():
    def __init__(self,  x, y):
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        if p % 2 == 1:
            self.id  = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
        else:
            self.id = canv.create_rectangle(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
        self.live = 30
    def set_coords(self):
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
    def move(self):
        if self.y <= 500:
            self.vy -= 1.2
            self.y -= self.vy
            self.x += self.vx
            self.vx *= 0.99
            self.set_coords()
        else:
            if self.vx ** 2 + self.vy ** 2 > 10:
                self.vy = -self.vy / 2
                self.vx = self.vx / 2
                self.y = 499
            if self.live < 0:
                balls.pop(balls.index(self))
                canv.delete(self.id)
            else:
                self.live -= 1
        if self.x > 780:
            self.vx = -self.vx / 2
            self.x = 779
    def hittest(self, ob):
        if abs(ob.x - self.x) <= (self.r + ob.r) and abs(ob.y - self.y) <= (self.r + ob.r):
            return True
        else:
            return False
class gun():
    def __init__(self,x,y):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.x=x
        self.y=y
        self.r=10
        self.id = canv.create_line(self.x, self.y, self.x+30, self.y-30, width=7)
    def fire2_start(self,event):
        self.f2_on = 1
    def fire2_end(self,event):
        global balls, bullet
        bullet += 1
        new_ball = ball(self.x,self.y)
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = -self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10
    def targetting(self, event=0):
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.x, self.y, self.x + max(self.f2_power, self.x) * math.cos(self.an),
                    self.y+ max(self.f2_power, self.x) * math.sin(self.an))
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

    def move1(self):
        self.y -= 5
    def move2(self):
        self.y += 5
class target():
    def __init__(self):
        self.points = 0
        self.id = canv.create_oval(0, 0, 0, 0)

        self.live = 1
        self.vx = randint(-10, 10)
        self.vy = randint(-10, 10)
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.r = randint(2, 50)
    def new_target(self,color):
        self.x = randint(600, 780)
        self.y = randint(100, 400)
        self.r = randint(2, 50)
        canv.itemconfig(self.id, fill=color)
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
    def hit(self, points=1):
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
    def move(self,t):
        if t==1:
            if self.y <= 500:
               self.vy -= 1.2
               self.y -= self.vy
               self.x += self.vx
               self.vx *= randint(-5,5)/2
            else:
                if self.vx ** 2 + self.vy ** 2 > 10:
                   self.vy = -self.vy
                   self.vx = self.vx / 2
                   self.y -= self.vy
        else:
            self.vx=0.4
            self.vy=0.3
            if self.y >= 0:
               self.vy = -self.vy
            if self.y >= 500:
               self.vy=-self.vy
            if self.x>=600:
               self.vx = -self.vx
            if self.x<= 300:
               self.vx =-self.vx
            else:
                self.y+=self.vy
                self.x += self.vx
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
t1=target()
t2=target()
bomb=target()
class Enemy(gun):
    def __init__(self):
        self.x=600
        self.f2_power = 40
        self.f2_on = 0
        self.an = 1
        self.y = random.randint(100,500)
        self.id = canv.create_line(self.x, self.y, self.x-30, self.y, width=7)
        canv.itemconfig(self.id, fill='purple')
        self.vy=5
    def scope(self):
         canv.coords(self.id,self.x, self.y, self.x-30, self.y)
    def move(self):
        self.y+=self.vy
        self.scope()
        if self.y>=490 or self.y<=0:
            self.vy=-self.vy
    def fire(self,event):
        global balls
        new_ball = ball(self.x-30,self.y)
        new_ball.r += 5
        new_ball.vx = -self.f2_power
        new_ball.vy = -self.f2_power
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 80
    def fire2_start(self, event):
        self.f2_on = 1

    def targetting(self, event=0):
        if self.f2_on:
            canv.itemconfig(self.id, fill='green')
        else:
            canv.itemconfig(self.id, fill='purple')
        canv.coords(self.id, self.x, self.y, self.x + max(self.f2_power, self.x),
                    self.y + max(self.f2_power, self.x))

t1.id_points = canv.create_text(30, 30, text=t1.points, font='28')
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun(10,200)
bullet = 0
balls = []
enem =Enemy()

def new_game(event=''):
    global gun, t1, screen1, balls, bullet,t2,bomb , enem_bullet , enem_balls
    t1.new_target("red")
    t2.new_target("red")
    bomb.new_target("black")
    bullet = 0
    balls = []
    root.bind('<space>', lambda event:scetch())
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Button-3>', enem.fire)
    canv.bind('<Motion>', g1.targetting)
    root.bind('<Up>',lambda event:g1.move1())
    root.bind('<Down>',lambda event:g1.move2())
    g1.live=1
    t2.live = 1
    t1.live = 1
    bomb.live = 1
    t = choice([1, 2])
    m = choice([1, 2])
    while t1.live or balls or t2.live :
        enem.move()
        if bomb.live :
            bomb.move(choice([t,m]))
            if t1.live :
                t1.move(t)
            if t2.live :
                t2.move(m)
            for b in balls:
                b.move()
                if b.hittest(g1) and g1.live:
                    exit()
                if b.hittest(t1) and t1.live:
                     t1.live = 0
                     t1.hit()
                     canv.itemconfig(t1.id_points, text=t2.points + t1.points)
                if b.hittest(bomb) and bomb.live:
                     bomb.live = 0
                if b.hittest(t2) and t2.live:
                     t2.live = 0
                     t2.hit()
                     canv.itemconfig(t1.id_points, text=t2.points+t1.points)
                if t2.live==0 and t1.live==0:
                     canv.bind('<Button-1>', '')
                     canv.bind('<ButtonRelease-1>', '')
                     canv.itemconfig(screen1, text='' + str(bullet) + '')
        else:
            canv.bind('<Button-1>', '')
            canv.bind('<ButtonRelease-1>', '')
            canv.itemconfig(screen1, text='Проигрыш')
            canv.update()
            time.sleep(5)
            exit()
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)
new_game()
mainloop()