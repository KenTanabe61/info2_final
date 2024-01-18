import pyxel


class ship:
    def __init__(self, FW):
        self.field_width = FW
        self.field_length = self.field_width * 2

        self.slength = self.field_length / 20
        self.swidth = self.field_width / 5
        self.sx = self.field_width / 2
        self.sy = self.field_length - self.slength

    def smove(self):
        self.sx = pyxel.mouse_x

class enemy:
    def __init__(self, FW, x, y):
        self.field_width = FW
        self.field_length = self.field_width * 2

        self.ey = y
        self.ex = x
        self.lowx = x
        self.espeed = 4
        self.mxhp = 5
        self.esize = 20

    def emove(self):
        self.ex += self.espeed
        if self.lowx > self.ex or self.ex > self.lowx + self.field_width/2 :
            self.espeed *= -1

    def edraw(self):
        pyxel.rect(self.ex, self.ey, self.esize, self.esize, pyxel.COLOR_ORANGE)
    


"""class sheild:
    a"""

class mybullet:
    def __init__(self, FW):
        self.m_speed = 10
        self.field_width = FW
        self.field_length = self.field_width * 2
        self.restart()
        

    def restart(self):
        self.my = self.field_length - self.field_length / 20
        self.mx = pyxel.mouse_x - self.field_width / 20 - 1

    def mmove(self):
        self.my -= self.m_speed

    def mdraw(self):
        pyxel.rect(self.mx, self.my, 4, 6, pyxel.COLOR_RED)
        
        
"""class enebullet:
    a"""

class App:
    def __init__(self):
        self.field_width = 300
        self.field_length = self.field_width * 2
        pyxel.init(self.field_width, self.field_length)

        self.score = 0
        self.alive = True
        self.life = 3
        self.cooltime = 10
        self.previous_bullet_frame = 0
        self.ship = ship(self.field_width)
        self.mybullet = []
        self.enemy =[enemy(self.field_width, 0, 80),enemy(self.field_width, self.field_width/2, 80)]
        
        pyxel.run(self.update, self.draw)

    def bulletnum(self):
        if pyxel.btn(pyxel.KEY_SPACE) and pyxel.frame_count - self.previous_bullet_frame > self.cooltime:
            self.mybullet.append(mybullet(self.field_width))
            self.framecount = pyxel.frame_count
            self.previous_bullet_frame = pyxel.frame_count



    def myhit(self):
        for m in self.mybullet:
            for n in self.enemy:
                if n.ex <= m.mx and m.mx <= n.ex + n.esize and n.ey <= m.my and m.my <= n.ey + n.esize:
                    n.mxhp -= 1
                    print("a")
                    self.mybullet.remove(m)
                    if n.mxhp == 0:
                        self.enemy.remove(n)


    def update(self):
        self.myhit()
        self.bulletnum()
        for b in self.mybullet:
            b.mmove()
        if self.alive == True:
            self.ship.smove()
        for e in self.enemy:
            e.emove()

    def draw(self):
        pyxel.cls(7)
        for t in self.mybullet:
            t.mdraw()
        pyxel.rect(self.ship.sx - self.ship.swidth/2, self.ship.sy, self.ship.slength, self.ship.swidth, pyxel.COLOR_NAVY)
        for h in self.enemy:
                h.edraw()
                pyxel.rect(h.ex, h.ey,10, 10, pyxel.COLOR_ORANGE)
        

        

App()