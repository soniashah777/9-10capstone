import pygame
pygame.init()

window= pygame.display.set_mode((500,500))
clock=pygame.time.Clock()
x=250
y=0
v=1
d="down"
red=(255,0,0)
green=(0,255,0)
black = (0,0,0)
color=red

while (True):
   
    if y<480 and d=="down" :
        
         y+=v
         if (y==479):
             d="up"
         
    if y>0 and d=="up" :
    
        y-=v
        if (y==2):
            d="down"
        
        
    window.fill(black)
    pygame.draw.circle(window,color,(x,y),20)
    clock.tick(150)
    pygame.display.update()
    for event in pygame.event.get():
         if event.type== pygame.QUIT:
             pygame.quit()
