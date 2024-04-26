import sys
import pygame
import time
import random
from pygame.locals import *

class zidan(object):#玩家子弹类
    def __init__(self,windows,x,y):
        self.window=windows
        self.x=x+100
        self.y=y+50


    def zidan(self):#渲染子弹
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        pygame.draw.circle(self.window,(r,g,b),(self.x,self.y),20)


    def zidanmove(self):#子弹移动
        self.x+=20
    def judge(self):#判断子弹越界
         if self.x>1400:
             return True
         else:
             return False
class paodan(object):#怪物炮弹类
    def __init__(self,windows,x,y):
        self.window=windows
        self.x=x-30
        self.y=y+130
        self.h=30
        self.w=70

    def paodan(self):#渲染怪物弹图片

        pygame.draw.rect(self.window,(255,255,255),(self.x,self.y,self.w,self.h))

    def paodanmove(self):#怪物炮弹弹移动
        self.x-=50
    def judge(self):#判断炮弹是否越界
         if self.x<30:
             return True
         else:
             return False
class player(object):#创建玩家类
    def __init__(self,windows):#构造玩家,定义玩家初始属性
        self.zidan_list=[]

        self.window=windows
        self.x=0
        self.y=400
        self.img3 = pygame.image.load('1.png')#创建玩家图片
        self.img4 = pygame.transform.scale(self.img3, (100, 100))#拉伸玩家图片

    def player(self):

        self.window.blit(self.img4, (self.x, self.y))  # 渲染玩家图片
        for zidan in self.zidan_list:#遍历子弹
            zidan.zidan()#调用子弹渲染
            zidan.zidanmove()#调用子弹移动
            if zidan.judge():#调用子弹越界判定
                self.zidan_list.remove(zidan)

    def playermovel(self):#玩家左移
        self.x -= 20
    def playermoveu(self):#玩家上移
        self.y-=10
    def playermoved(self):#玩家下移
        self.y+=10
    def playmover(self):#玩家右移

        self.x+=20

    def fire(self):  # 定义玩家开火函数

        self.zidan_list.append(zidan(self.window, self.x, self. y))
def key(player):#创建键盘点击事件
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_a:
                player.playermovel()
            if event.key==K_d:
                player.playmover()
            if event.key==K_j:
                player.fire()
            if event.key==K_w:
                player.playermoveu()
            if event.key==K_s:
                player.playermoved()
class guai(object):#定义怪物类
    def __init__(self,windows):
        self.hit=1
        self.x=1400
        self.y=320
        self.paodan_list = []
        self.window=windows
        self.img=pygame.image.load('3.png')
        self.img2=pygame.transform.scale(self.img,(250,250))
        self.img3=pygame.image.load('4.png')
    def blast(self,x1):#判断是否爆炸

        if x1>=self.x:#判断子弹是否碰撞

            self.hit+=1#累加碰撞次数

    def guai(self):#渲染怪物或爆炸图片

        if self.hit>=300:#如果碰撞大于三百次

            self.window.blit(self.img3,(self.x,self.y-100))#渲染爆炸图片
            font = pygame.font.Font('FZQTFW.TTF', 200)#结算文本
            txt = font.render('你赢了!', True, (0, 0, 255))
            self.window.blit(txt, (510, 170))
        else:
            self.window.blit(self.img2,(self.x,self.y))
            for paodan in self.paodan_list:
                paodan.paodan()
                paodan.paodanmove()
                if paodan.judge():
                    self.paodan_list.remove(paodan)
    def move(self):#定义怪物移动和怪物子弹发射函数
        if self.hit>=300:#如果碰撞大于三百次

            pass#停止移动
        else:
          self.x-=1#怪物移动
          if self.x % 30 ==0:#控制怪物子弹发射频率
             self.paodan_list.append(paodan(self.window, self.x, self.y))#怪物子弹发射
    def bleed(self):#定义玩家血量函数
        font = pygame.font.Font('FZQTFW.TTF', 20)#血条前面文本
        txt = font.render('玩家血量', True, (0, 0, 0))
        self.window.blit(txt, (100, 20))
        if self.x>=1200:#根据怪物移动距离扣除玩家血量
            pygame.draw.rect(self.window, (0, 0, 0), (200, 20, 600, 30), 2)
            pygame.draw.rect(self.window, (255, 0, 0), (200, 20, 600, 30))
        elif self.x>=1000:
            pygame.draw.rect(self.window, (0, 0, 0), (200, 20, 600, 30), 2)
            pygame.draw.rect(self.window, (255, 0, 0), (200, 20, 500, 30))
        elif self.x>=800:
            pygame.draw.rect(self.window, (0, 0, 0), (200, 20, 600, 30), 2)
            pygame.draw.rect(self.window, (255, 0, 0), (200,20, 400, 30))
        elif self.x>=600:
            pygame.draw.rect(self.window, (0, 0, 0), (200, 20, 600, 30), 2)
            pygame.draw.rect(self.window, (255, 0, 0), (200, 20, 300, 30))
        elif self.x>=400:
            pygame.draw.rect(self.window, (0, 0, 0), (200, 20, 600, 30), 2)
            pygame.draw.rect(self.window, (255, 0, 0), (200, 20, 200, 30))
        elif self.x>=200:
            pygame.draw.rect(self.window, (0, 0, 0), (200, 20, 600, 30), 2)
            pygame.draw.rect(self.window, (255, 0, 0), (200, 20, 100, 30))

        elif self.x>=100:
            pygame.draw.rect(self.window, (0, 0, 0), (200, 20, 600, 30), 2)
            pygame.draw.rect(self.window, (255, 0, 0), (200, 20, 1, 30))
            font = pygame.font.Font('FZQTFW.TTF', 200)#玩家死亡文本
            txt = font.render('你已死亡!', True, (0, 0, 255))
            self.window.blit(txt, (410, 170))

def main():#定义主体函数
    pygame.init()
    window = pygame.display.set_mode((1500, 500))
    img1 = pygame.image.load('1.jpg')  # 创建背景图片
    img2 = pygame.transform.scale(img1, (1500, 500))  # 拉伸图片1

    pygame.display.set_caption('射击小游戏')
    pygame.mixer.music.load('bgm.mp3')#背景音乐
    pygame.mixer.music.play(-1,0.0)
    player_1 = player(window)#创建玩家对象
    guai_1=guai(window)#创建怪物对象
    while True:#开始循环
        window.blit(img2, (0, 0))  # 渲染图片
        player_1.player()
        for zidan in player_1.zidan_list:#遍历玩家子弹并取出子弹x坐标
            x1=zidan.x
            guai_1.blast(x1)
        guai_1.guai()
        guai_1.move()
        guai_1.bleed()
        key(player_1)

        pygame.display.update()
        time.sleep(0.02)

main()










