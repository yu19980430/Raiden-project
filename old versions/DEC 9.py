import pygame
import random
import math
import os

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
L_GREEN = (181, 230, 29)
D_GREEN = (0, 183, 0)
N_BLUE = (0, 128, 255)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

allSprites = pygame.sprite.Group()

# Set the width and height of the screen [width, height]
size = (700, 900)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("alpha")

# load backgroud

x_speed = 0
y_speed = 0

x_coord = 300
y_coord = 800

x = random.randint(0, 500)
y = random.randint(0, 400)

myscore = 0

en_x_speed = 1
en_y_speed = 1
en_x_dir = 0
en_y_dir = 0
playerdead = False
time = 0
b1 = "background.png"

##class background(pygame.sprite.Sprite):
##    def __init__(self):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.image.load("background.png").convert()
##        self.rect = self.image.get_rect()
##
##    def update_Up(self):
##        self.rect.y+=1
back = pygame.image.load(b1).convert()
back2 = pygame.image.load(b1).convert()


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5, 5])
        self.image.fill(L_GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.x_speed = 0
        self.y_speed = -7
        self.damage = 1
        self.gap = 20

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

    def move(self, x_speed, y_speed):
        if x_speed != 0:
            self.checkcollision(x_speed, 0)
        if y_speed != 0:
            self.checkcollision(0, y_speed)

    def checkcollision(self, x_speed, y_speed):
        self.rect.x += x_speed
        self.rect.y += y_speed

    ##        for bullet in en_bullet_list:
    ##            if self.rect.colliderect(bullet.rect):
    ##                self.hp -= bullet.damage
    ##                if self.hp <= 0 and self.live < 0:
    ##                    playdead = True
    ##                elif self.hp <= 0:
    ##                    self.live -= 1

    def levelup(self, gap):
        if self.gap > 4:
            gap -= 4


class en_Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.damage = 1
        pygame.draw.ellipse(self.image, RED, [-28, -33, 90, 90])
        self.image.set_colorkey(WHITE)
        self.angle = -math.radians(angle - 135)
        self.speed_magnitude = 1
        self.speed = (self.speed_magnitude * math.cos(self.angle),
                      self.speed_magnitude * math.sin(self.angle))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image=pygame.Surface([width,height])
        # self.image.fill(color)
        self.image = pygame.image.load("001.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.x_speed = x_speed
        self.y_speed = y_speed
        # self.direct = direct
        # self.pos = (self.rect.centerx,self.rect.centery)
        self.score = 0
        self.hp = 10000
        self.live = 3
        self.playershoot = False
        # pygame.draw.ellipse(self.image, WHITE, [-28,-33, 90, 90])
        # self.image.set_colorkey(WHITE)

    def moveX(self, x_speed):
        if x_speed != 0:
            self.checkcollision(x_speed, y_speed)

    def moveY(self, y_speed):
        if y_speed != 0:
            self.checkcollision(x_speed, y_speed)

    def checkcollision(self, x_speed, y_speed):
        self.rect.x += x_speed
        self.rect.y += y_speed

    ##        for bullet in en_bullet_list:
    ##            if self.rect.colliderect(bullet.rect):
    ##                self.hp -= bullet.damage
    ##                if self.hp <= 0 and self.live < 0:
    ##                    playdead = True
    ##                elif self.hp <= 0:
    ##                    self.live -= 1

    ##    def shoot(self,playershoot):
    ##        pressed = pygame.key.get_pressed()
    ##
    ##
    ##        if event.type == pygame.KEYUP:



    def update(self):
        # Figure out if it was an arrow key. If so
        # adjust speed.
        # old ver
        ##            if event.key == pygame.K_LEFT and event.key == pygame.K_UP:
        ##                self.move(-4,-4)
        ##            elif event.key == pygame.K_RIGHT and event.key == pygame.K_UP:
        ##                self.move(4,-4)
        ##            elif event.key == pygame.K_LEFT and event.key == pygame.K_DOWN:
        ##                self.move(-4,-4)
        ##            elif event.key == pygame.K_RIGHT and event.key == pygame.K_DOWN:
        ##                self.move(4,-4)
        ##            elif event.key == pygame.K_UP:
        ##                self.move(0,-4)
        ##            elif event.key == pygame.K_DOWN:
        ##                self.move(0,4)
        ##            elif event.key == pygame.K_LEFT:
        ##                self.move(-4,0)
        ##            elif event.key == pygame.K_RIGHT:
        ##                self.move(4,0)

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.moveY(-4)
        if pressed[pygame.K_DOWN]:
            self.moveY(4)
        if pressed[pygame.K_LEFT]:
            self.moveX(-4)
        if pressed[pygame.K_RIGHT]:
            self.moveX(4)

        if pressed[pygame.K_z]:
            self.playershoot = True

        # User let up on a key
        if event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            # Old ver for moving
            ##            if event.key == pygame.K_LEFT:
            ##                self.move(0,0)
            ##            elif event.key == pygame.K_RIGHT:
            ##                self.move(0,0)
            ##            if event.key == pygame.K_UP:
            ##                self.move(0,0)
            ##            elif event.key == pygame.K_DOWN:
            ##                self.move(0,0)
            ##            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            ##                self.moveY(0)
            ##            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            ##                self.moveX(0)
            if event.key == pygame.K_z:
                self.playershoot = False


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # self.image=pygame.Surface([width,height])
        # self.image.fill(color)
        self.image = pygame.image.load("Raiden fighter2.jpg").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.x_offset = -2
        self.y_offset = -2
        self.score = 0
        self.angle = 3.1415926535898 * 50
        self.radius = 100
        self.hp = 0
        # pygame.draw.ellipse(self.image, WHITE, [-28,-33, 90, 90])
        # self.image.set_colorkey(WHITE)

    ##enemy go vertical up
    def update_Up(self):
        self.rect.y += self.y_offset

    ##enemy move acorss screen
    def update_A(self):
        self.rect.y += self.y_offset * 2
        self.rect.x += self.x_offset

    ##enemy moving like "Z"
    def update_Z(self):
        if self.rect.x < 1 or self.rect.x > 620:
            self.x_offset = self.x_offset * -1
        self.rect.x += self.x_offset
        self.rect.y += self.y_offset

    ##enemy moving 180
    def update_180(self):
        if self.rect.y >= 150 and self.rect.x == 250:
            self.rect.y += self.y_offset
        elif self.rect.y < 150:
            self.angle += 1
            self.rect.x = self.radius * math.cos(self.angle / 50) + 350
            self.rect.y = self.radius * math.sin(self.angle / 50) + 150
        elif self.rect.y >= 150 and self.rect.x > 250:
            self.rect.y -= self.y_offset


class hitbox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("hitbox.png").convert()
        self.image.set_colorkey(WHITE)
        pygame.draw.ellipse(self.image, YELLOW, [0, 0, 7, 7])
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x = player.rect.x + 26
        self.rect.y = player.rect.y + 20


player = Player()
player_list = pygame.sprite.Group()
player_list.add(player)
allSprites.add(player)
bullet_hit_list = pygame.sprite.Group()
hitbox_list = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
hitbox = hitbox()
hitbox_list.add(hitbox)
allSprites.add(hitbox)
##background1 = background()
##backgroud_list = pygame.sprite.Group()
##allSprites.add(background1)

p_bullet_list = pygame.sprite.Group()

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
# -------- Main Program Loop -----------
end = False
while not done:

    pygame.display.flip()
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    time += 1
    if time % 40 == 0:
        enemy_object = Enemy()
        enemy_object.rect.x = 250
        enemy_object.rect.y = 600
        allSprites.add(enemy_object)
        enemy_group.add(enemy_object)
    # --- Enemy Update
    for enemy in enemy_group:
        enemy.update_180()

    x_coord += x_speed
    y_coord += y_speed

    if player.rect.x < 1:
        player.rect.x = 1
    elif player.rect.x > 640:
        player.rect.x = 640

    if player.rect.y < 1:
        player.rect.y = 1
    elif player.rect.y > 845:
        player.rect.y = 845

    ##    player.shoot(False)
    if player.playershoot == True:
        p_bullet = Bullet()
        if time % p_bullet.gap == 0:
            p_bullet.rect.x = player.rect.x + 27
            p_bullet.rect.y = player.rect.y
            p_bullet_list.add(p_bullet)
            allSprites.add(p_bullet)

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
    ##    background.image = pygame.image.load("background.png").convert()

    # --- Drawing code should go here
    screen.blit(back, (0, x))
    screen.blit(back, (0, x - 700))

    x += 2
    if x == 700:
        x = 0

    ##    for thing in enemy_group:
    ##        thing.update_Circle(angle)

    ##    background1=background()
    ##    background1.scroll(0,1)

    ##    background1.update_Up
    allSprites.update()
    allSprites.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
