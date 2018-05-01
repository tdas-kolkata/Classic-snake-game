import pygame
import time
import random

pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,155,0)

display_width=800
display_height=600
block_size=20
fps=8
c=0
gdisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('snake')

eat_sound=pygame.mixer.Sound('Beep_Short.wav')
img6=pygame.image.load('head.png')
img2=pygame.image.load('apple.png')
img3=pygame.image.load('tail1.png')
img4=pygame.image.load('body3.png')
img5=pygame.image.load('body4.png')
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,25)
direction='right'

    
def message_to_screen(msg,color):
    screen_text=font.render(msg,True,color)
    gdisplay.blit(screen_text,[display_width/2-4*len(msg),display_height/2])

def Score(s):
    text=font.render('Score:%s'%str(s),True,black)
    gdisplay.blit(text,[0,0])


def snake(block_size,snakelist,imgb1,imgb2):
    i=0
    if len(snakelist)>1:
        if snakelist[1][0]>snakelist[0][0]:
            tail=pygame.transform.rotate(img3,0)
            gdisplay.blit(tail,[snakelist[0][0],snakelist[0][1]])    #rotate tail
        if snakelist[1][0]<snakelist[0][0]:
            tail=pygame.transform.rotate(img3,180)
            gdisplay.blit(tail,[snakelist[0][0],snakelist[0][1]])
        if snakelist[1][1]>snakelist[0][1]:
            tail=pygame.transform.rotate(img3,270)
            gdisplay.blit(tail,[snakelist[0][0],snakelist[0][1]])
        if snakelist[1][1]<snakelist[0][1]:
            tail=pygame.transform.rotate(img3,90)
        gdisplay.blit(tail,[snakelist[0][0],snakelist[0][1]])
    for i in range(1,len(snakelist)-1):
        if len(snakelist)>2:
            if snakelist[i][0]==snakelist[i+1][0]:
                if c%2==1:
                    body=pygame.transform.rotate(imgb1,0)
                else:
                    body=pygame.transform.rotate(imgb2,0)      #body
            if snakelist[i][1]==snakelist[i+1][1]:
                if c%2==1:
                    body=pygame.transform.rotate(imgb1,90)
                else:
                    body=pygame.transform.rotate(imgb2,90)
            gdisplay.blit(body,[snakelist[i][0],snakelist[i][1]])

    if direction=='right':
        head=pygame.transform.rotate(img6,270)
    if direction=='left':
            head=pygame.transform.rotate(img6,90)               #rotate the head
    if direction=='up':
            head=pygame.transform.rotate(img6,0)
    if direction=='down':
        head=pygame.transform.rotate(img6,180)
    gdisplay.blit(head,[snakelist[len(snakelist)-1][0],snakelist[len(snakelist)-1][1]])
            
def gameloop():
    global direction
    global c
    score=0
    lead_x=display_width/2
    lead_y=display_height/2
    lead_x_delta=0
    lead_y_delta=0
    snakelen=1
    snakelist=[]
    ranapplex=random.randrange(0,display_width-2*block_size)
    ranapplex=round(ranapplex/block_size)*block_size
    ranappley=random.randrange(0,display_height-2*block_size)
    ranappley=round(ranappley/block_size)*block_size
    gameexit=False
    gameover=False
    while gameexit==False:
        while gameover==True:
            gdisplay.fill(white)
            message_to_screen("game over press c to continue and q to quit ,your score is %s" %str(snakelen-1),red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameexit=True
                        gameover=False
                    if event.key==pygame.K_c:
                        gameloop()
                
            
    
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                gameexit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    direction='left'
                    lead_x_delta= -block_size
                    lead_y_delta=0
                elif event.key==pygame.K_RIGHT:
                    direction='right'
                    lead_x_delta= block_size
                    lead_y_delta=0
                elif event.key==pygame.K_UP:
                    direction='up'
                    lead_y_delta= -block_size
                    lead_x_delta=0
                elif event.key==pygame.K_DOWN:
                    direction='down'
                    lead_y_delta= block_size
                    lead_x_delta=0
            if lead_x>display_width-block_size/2 or lead_x<block_size/2 or lead_y>display_height-block_size/2 or lead_y<block_size/2:#boundary
                gameover=True
        lead_x +=lead_x_delta
        lead_y +=lead_y_delta
        gdisplay.fill(white)
        gdisplay.blit(img2,[ranapplex,ranappley])
        
        snakehead=[]#head is at the last of the list
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        if len(snakelist)>snakelen:
            del snakelist[0]

        for segment in snakelist[:-1]:#self bite
            if segment==snakehead:
                gameover=True
        if c%2==0:
            snake(block_size,snakelist,img4,img5)
        else:
            snake(block_size,snakelist,img5,img4)

        Score(snakelen-1)
        pygame.display.update()
        #eating
        if lead_x==ranapplex and lead_y==ranappley:
            pygame.mixer.Sound.play(eat_sound)
            ranapplex=random.randrange(0,display_width-2*block_size)
            ranapplex=round(ranapplex/block_size)*block_size
            ranappley=random.randrange(0,display_height-2*block_size)
            ranappley=round(ranappley/block_size)*block_size
    
            snakelen=snakelen+1
        c=c+1
        if c>20:
            c=0
        clock.tick(fps)
    pygame.quit()
    quit()


gameloop()


