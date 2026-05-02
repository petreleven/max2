import pygame
width=800
heigh=400
gamescreen=pygame.display.set_mode((width,heigh))
player=pygame.Rect(100,100,50,50)
pltform=pygame.Rect(100,340,50,20)
px=0
py=350
jumptime=0
isjump=False
isfalling = True
gravity = 0.8
#player speed
playerspeedx=0

#forevor blocf
while True :
    player.x=px
    
    gamescreen.fill('black')
    pygame.draw.rect(gamescreen,'red',player)
    pygame.draw.rect(gamescreen,'blue',pltform)
    pygame.display.flip()
    buttons=pygame.event.get()
    for button in buttons:
        if button.type==pygame.QUIT:
            exit()
   
    button=pygame.key.get_pressed()
    if button[pygame.K_LEFT]:
        playerspeedx = -1
        print('left button pressed')
    if button[pygame.K_RIGHT]:
        playerspeedx = 1

    px+=playerspeedx
    playerspeedx =0
    if button[pygame.K_UP]:
        #jump 
        isjump=True
    if isjump==True:
        jumptime+=0.1
        print(jumptime)
    if jumptime>15:
        jumptime=0
        isjump=False
    if isjump==True:
        speed=3*(1-(jumptime/15))
        player.y-=speed
    #falling down
    if isjump==False and player.y<350 and isfalling == True:
        fallspeed = gravity * 0.8
        player.y+=fallspeed
    #check if we the pltform
    if player.colliderect(pltform):
        print('pltform')
        #isjump=False
        isfalling=False
    else:
        isfalling = True
