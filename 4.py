import pygame,sys
from pygame.locals import *
pygame.init()
window=pygame.display.set_mode((800,600))
pygame.display.set_caption('飞机大战')
window.fill((255,255,255))
img1=pygame.image.load('1.jpg')
window.blit(img1,(0,0))
w,h=img1.get_size()#获取图片高度宽度
#print(w,h)
window.blit(img1,(800-w,600-h))
img2=pygame.transform.scale(img1,(100,200))#压缩图片1
img3=pygame.transform.rotate(img1,180,0.5)#旋转缩放图片1

pygame.display.flip()
while True:
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()
   pygame.display.update()



