import pygame
import random
import math
import os

pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
BLUE     = (   0,   0, 255)
RED      = ( 255,   0,   0)
YELLOW   = ( 255, 255,   0)
L_GREEN  = ( 181, 230,  29)
D_GREEN  = (   0, 183,   0)
N_BLUE   = (   0, 128, 255)


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

allSprites = pygame.sprite.Group()


 
# Set the width and height of the screen [width, height]
size = (700, 900)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("alpha")

#load backgroud

x_speed = 0
y_speed = 0

x_coord = 300
y_coord = 800

radius=100

x=random.randint(0,500)
y=random.randint(0,400)

myscore = 0

direct = 0
dodge = False
en_x_speed = 1
en_y_speed = 1
en_x_dir = 0
en_y_dir = 0
shoot = False
player_loc_x = 0
player_loc_y = 0
gameend = False
       
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        #self.image=pygame.Surface([width,height])
        #self.image.fill(color)
        self.image= pygame.image.load("001.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x =x_coord
        self.rect.y =y_coord
        self.x_speed = x_speed
        self.y_speed = y_speed
##      self.direct = direct
##      self.pos = (self.rect.centerx,self.rect.centery)
        self.score = 0
        self.live = 10000
        #pygame.draw.ellipse(self.image, WHITE, [-28,-33, 90, 90])
        #self.image.set_colorkey(WHITE)


    def move(self, x_speed,y_speed):
        if x_speed != 0:
            self.checkcollision(x_speed,0)
        if y_speed != 0:
            self.checkcollision(0,y_speed)

    def checkcollision(self,x_speed,y_speed):
        self.rect.x += x_speed
        self.rect.y += y_speed



    def update(self):
        self.pos = (self.rect.centerx,self.rect.centery)
        pressed = pygame.key.get_pressed()
        # Figure out if it was an arrow key. If so
        # adjust speed.
        if pressed[pygame.K_LEFT]:
            self.move(-2,0)
        if pressed[pygame.K_RIGHT]:
            self.move(2,0)
        if pressed[pygame.K_UP]:
            self.move(0,-2)
        if pressed[pygame.K_DOWN]:
            self.move(0,2)


        # User let up on a key
        if event.type == pygame.KEYUP:
        # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT:
                self.move(0,0)
            if event.key == pygame.K_RIGHT:
                self.move(0,0)
            if event.key == pygame.K_UP:
                self.move(0,0)
            if event.key == pygame.K_DOWN:
                self.move(0,0)


class hitbox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("hitbox.png").convert()
        self.image.set_colorkey(WHITE)
        pygame.draw.ellipse(self.image, YELLOW, [0,0, 7, 7])
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x = player.rect.x+26
        self.rect.y = player.rect.y+20

class Player_Bullet(pygame.sprite.Sprite):
    def __init__(self,color,width,height,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x -= 4

class attackrange(pygame.sprite.Sprite):
    def __init__(self,color,width,height,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        pygame.draw.ellipse(self.image, WHITE, [0,0, 240, 240])
        self.image.set_colorkey(WHITE)
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        self.rect.x = player.rect.x-103
        self.rect.y = player.rect.y - 108

player = Player()
player_list = pygame.sprite.Group()
player_list.add(player)
allSprites.add(player)
bullet_hit_list = pygame.sprite.Group()
hitbox_list=pygame.sprite.Group()
enemy_group=pygame.sprite.Group()
hitbox = hitbox()
hitbox_list.add(hitbox)
allSprites.add(hitbox)





class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        #self.image=pygame.Surface([width,height])
        #self.image.fill(color)
        self.image= pygame.image.load("001.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.x_offset=-1
        self.y_offset=-1
        self.direct = direct
        self.pos = (self.rect.centerx,self.rect.centery)
        self.score = 0
        self.live = 10000
        #pygame.draw.ellipse(self.image, WHITE, [-28,-33, 90, 90])
        #self.image.set_colorkey(WHITE)

##enemy go vertical up
    def update(self):
        self.rect.y+=self.y_offset

##enemy moving like "Z"
    def update_Z(self):
        if self.rect.x<1 or self.rect.x>620:
            self.x_offset=self.x_offset*-1
        self.rect.x+=self.x_offset
        self.rect.y+=self.y_offset
##enemy moving in circle
    def update_Circle(self):
        self.rect.x = radius*math.cos(counter/30)+radius+x
        self.rect.y = radius*math.sin(counter/30)+y
        
##enemy turns 180
    def update_Turn180(self):
        self.rect.y+=self.y_offset
        if self.rect.y < 150:
            self.rect.x = radius*math.cos(counter/30)+radius+x
            self.rect.y = radius*math.sin(counter/30)+y
            if self.rect.y ==150:
                self.rect.y-=self.y_offset
        
        
        
        

        
        




##for x in range(0,600,100):
##    enemy_object=Enemy()
##    enemy_object.rect.x=x
##    enemy_object.rect.y=random.randint(400,650)
##    allSprites.add(enemy_object)
##    enemy_group.add(enemy_object)
##




 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
counter=0
# -------- Main Program Loop -----------
end = False
while not done:
    
    pygame.display.flip()
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop



    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    if event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so
        # adjust speed.
        if event.key == pygame.K_LEFT:
            x_speed = -2
        if event.key == pygame.K_RIGHT:
            x_speed = 2
        if event.key == pygame.K_UP:
            y_speed = -2
        if event.key == pygame.K_DOWN:
            y_speed = 2  

    # User let up on a key
    if event.type == pygame.KEYUP:
        # If it is an arrow key, reset vector back to zero
        if event.key == pygame.K_LEFT:
            x_speed = 0
        if event.key == pygame.K_RIGHT:
            x_speed = 0
        if event.key == pygame.K_UP:
            y_speed = 0
        if event.key == pygame.K_DOWN:
            y_speed = 0

    

    x_coord += x_speed
    y_coord += y_speed

    if player.rect.x<1:
        player.rect.x=1
    elif player.rect.x>620:
        player.rect.x=620

    if player.rect.y<1:
        player.rect.y=1
    elif player.rect.y>845:
        player.rect.y=845

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
  

    counter+=1
    if counter%100==0:
        enemy_object=Enemy()
        enemy_object.rect.x=250
        enemy_object.rect.y=600
        allSprites.add(enemy_object)
        enemy_group.add(enemy_object)
    
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    allSprites.draw(screen)
    allSprites.update()
    for thing in enemy_group:
        thing.update_Turn180()
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
