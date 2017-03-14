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

# load background

x_speed = 0
y_speed = 0

x_coord = 350
y_coord = 800

myscore = 0

en_x_speed = 1
en_y_speed = 1
en_x_dir = 0
en_y_dir = 0
playerdead = False
bgtime = 0
time = 0
b1 = "background2.jpg"
game_start = False
game_end = False
enemy_pic = "a-01.png"

# --- background music
##pygame.mixer.music.load("level1.mp3")
##pygame.mixer.music.play(-1)


# --- background image
back = pygame.image.load(b1).convert()
back2 = pygame.image.load(b1).convert()


##class background(pygame.sprite.Sprite):
##    def __init__(self):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.image.load("background.png").convert()
##        self.rect = self.image.get_rect()
##
##    def update_Up(self):
##        self.rect.y+=1


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image=pygame.Surface([width,height])
        # self.image.fill(color)
        self.image = pygame.image.load("p02.png").convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.x_speed = x_speed
        self.y_speed = y_speed
        # self.direct = direct
        self.pos = (self.rect.centerx, self.rect.centery)
        self.score = 0
        self.hp = 100
        self.live = 3
        self.playershoot = False
        self.count = 100
        self.n = True
        # pygame.draw.ellipse(self.image, WHITE, [-28,-33, 90, 90])
        # self.image.set_colorkey(WHITE)

    def shoot(self):
        self.count += 1
        if self.playershoot == True and self.count >= 8:
            p_bullet = Bullet()
            if self.n == True:
                p_bullet.rect.x = player.rect.centerx + 6
                self.n = False
            else:
                p_bullet.rect.x = player.rect.centerx - 19
                self.n = True
            p_bullet.rect.y = player.rect.centery - 18
            p_bullet_group.add(p_bullet)
            allSprites.add(p_bullet)
            self.count = 0

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
        self.pos = (self.rect.centerx, self.rect.centery)
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


class hitbox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("hitbox.png").convert()
        self.image.set_colorkey(WHITE)
        ##        pygame.draw.ellipse(self.image, YELLOW, [0,0, 7, 7])
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x = player.rect.centerx-3
        self.rect.y = player.rect.centery-18


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pb.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.x_speed = 0
        self.y_speed = -12
        self.dmg = 1
        self.levelup = 0

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

    ##        if x_speed != 0:
    ##            self.checkcollision(x_speed,0)
    ##        if y_speed != 0:
    ##            self.checkcollision(0,y_speed)
    ##
    ##    def checkcollision(self,x_speed,y_speed):


##        self.levelup += 1

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image=pygame.Surface([width,height])
        # self.image.fill(color)
        self.image = pygame.image.load(enemy_pic).convert_alpha()
        self.image.set_colorkey(None)
        self.rect = self.image.get_rect()
        self.x_offset = -2
        self.y_offset = -2
        self.score = 10
        self.turn = 3.1415926535898 * 50
        self.radius = 100
        self.hp = 0
        self.crash_dmg = 20
        self.angle = self.get_angle(player.pos)
        self.count = 500
        # self.rotate = 0
        # pygame.draw.ellipse(self.image, WHITE, [-28,-33, 90, 90])
        # self.image.set_colorkey(WHITE)

    ##enemy bullet chase
    def get_angle(self, player):
        x = player[0] - self.rect.centerx
        y = player[1] - self.rect.centery - 20
        self.angle = 135 - math.degrees(math.atan2(y,x))
        return self.angle
    
    def shoot(self):
        self.count += 1
        if self.count >= 10:
            self.angle = self.get_angle(player.pos)
            en_bullet1 = en_Bullet(self.rect.centerx,self.rect.centery, self.angle)
            en_bullet1_group.add(en_bullet1)
            allSprites.add(en_bullet1)
            self.count = 0

    ##enemy go vertical up
    def update_Down(self):
        self.rect.y -= self.y_offset

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

    ##enemy moving 180 from right
    def update_180(self):
        if self.rect.y >= 150 and self.rect.x == 150:
            self.rect.y += self.y_offset
        elif self.rect.y < 150:
            self.turn += 1
            self.rect.x = self.radius * math.cos(self.turn / 50) + 250
            self.rect.y = self.radius * math.sin(self.turn / 50) + 150
        elif self.rect.y >= 150 and self.rect.x > 250:
            self.rect.y -= self.y_offset

            ##enemy moving 180 from left

    def update_180_2(self):
        if self.rect.y >= 150 and self.rect.x == 550:
            self.rect.y += self.y_offset
        elif self.rect.y < 150:
            # self.image = pygame.transform.rotate(pygame.image.load(enemy_pic).convert_alpha(), self.rotate)
            # self.rotate += 1.15
            self.turn += 1
            self.rect.x = self.radius * math.sin(self.turn / 50) + 450
            self.rect.y = self.radius * math.cos(self.turn / 50) + 150
        elif self.rect.y >= 150 and self.rect.x < 450:
            self.rect.y -= self.y_offset

            ##enemy suicide attack

    def update_S(self):
        if self.rect.x > player.rect.x:
            self.rect.x += self.x_offset
        elif self.rect.x < player.rect.x:
            self.rect.x -= self.x_offset
        if self.rect.y < player.rect.y:
            self.rect.y -= self.y_offset
        elif self.rect.y > player.rect.y:
            self.rect.y += self.y_offset

            ##enemy turrent

    def update_T(self):
        self.rect.y += 1

    ##enemy boss
    def update_boss(self):
        self.turn += 1
        self.rect.x = self.radius * math.cos(self.turn / 100) + 350
        self.rect.y = self.radius / 2 * math.sin(self.turn / 100) + 100
        self.shoot()


class en_Bullet(pygame.sprite.Sprite):
    def __init__(self, x,y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.angle = -math.radians(angle-135)
        self.image= pygame.Surface([5,5])
        self.image.fill(N_BLUE)
        self.rect = self.image.get_rect()
        self.move = [x, y]
        self.speed_magnitude = 5
        self.speed = (self.speed_magnitude*math.cos(self.angle),
                      self.speed_magnitude*math.sin(self.angle))
        self.done = False
        self.dmg = 5
    def update(self):
        self.move[0] += self.speed[0]
        self.move[1] += self.speed[1]
        self.rect.topleft = self.move

    def update_spin(self):
        self.move[0] 


player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)
allSprites.add(player)
bullet_hit_list = pygame.sprite.Group()
hitbox_group = pygame.sprite.Group()
enemy1_group = pygame.sprite.Group()
enemy2_group = pygame.sprite.Group()
enemy3_group = pygame.sprite.Group()
enemy4_group = pygame.sprite.Group()
boss_group = pygame.sprite.Group()
hitbox = hitbox()
hitbox_group.add(hitbox)
allSprites.add(hitbox)
p_bullet_group = pygame.sprite.Group()
en_bullet1_group = pygame.sprite.Group()
##background1 = background()
##backgroud_list = pygame.sprite.Group()
##allSprites.add(background1)


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


# --- Enemy generation type1
def enemytype1():
    if time % 40 == 0 and time % 4000 < 1000:
        enemy1 = Enemy()
        enemy1.hp = 3
        enemy1.angle = 3.1415926535898 * 25
        enemy1.rect.x = 550
        enemy1.rect.y = 900
        allSprites.add(enemy1)
        enemy1_group.add(enemy1)


def enemytype2():
    if time % 30 == 0 and time % 4000 > 1000 and time % 4000 < 2000:
        enemy2 = Enemy()
        enemy2.hp = 1
        enemy2.crash_dmg = 40
        enemy2.y_offset = -5
        enemy2.rect.x = random.randint(10, 690)
        enemy2.rect.y = 0
        allSprites.add(enemy2)
        enemy2_group.add(enemy2)


def enemytype3():
    if time % 40 == 0 and time % 4000 > 2000 and time % 4000 < 3000:
        enemy3 = Enemy()
        enemy3.hp = 2
        enemy3.rect.x = 0
        enemy3.rect.y = 900
        allSprites.add(enemy3)
        enemy3_group.add(enemy3)


def enemytype4():
    if time % 40 == 0 and time % 4000 > 3000 and time % 4000 < 4000:
        enemy4 = Enemy()
        enemy4.hp = 3
        enemy4.rect.x = 150
        enemy4.rect.y = 900
        allSprites.add(enemy4)
        enemy4_group.add(enemy4)


def enemytype5():
    if time % 100 == 0:
        enemy1 = Enemy()
        enemy1.hp = 3
        enemy1.turn = 3.1415926535898 * 25
        enemy1.rect.x = 550
        enemy1.rect.y = 900
        allSprites.add(enemy1)
        enemy1_group.add(enemy1)
    if (time + 50) % 100 == 0:
        enemy4 = Enemy()
        enemy4.hp = 3
        enemy4.rect.x = 150
        enemy4.rect.y = 900
        allSprites.add(enemy4)
        enemy4_group.add(enemy4)


def enemytype6():
    if time % 30 == 0 and time % 300 > 0 and time % 300 < 200:
        enemy2 = Enemy()
        enemy2.hp = 1
        enemy2.crash_dmg = 40
        enemy2.y_offset = -5
        enemy2.rect.x = random.randint(10, 690)
        enemy2.rect.y = 0
        allSprites.add(enemy2)
        enemy2_group.add(enemy2)


def enemyboss1():
    if time == 1:
        boss1 = Enemy()
        boss1.score = 1000
        boss1.hp = 1
        boss1.crash_dmg = 100
        boss1.rect.x = 350
        boss1.rect.y = 100
        boss1.image = pygame.image.load("boss.png").convert_alpha()
        allSprites.add(boss1)
        boss_group.add(boss1)


# -------- Main Program Loop ------------------- Main Program Loop ------------------- Main Program Loop ----------



while not done:

    while game_start == False:
        screen.fill(BLACK)
        myfont = pygame.font.SysFont('freesansbold.ttf', 80)
        instrucfont = pygame.font.SysFont('freesansbold.ttf', 50)
        nlabel = myfont.render('Press R to start', 2, L_GREEN)
        instruction_1 = instrucfont.render('Press arrow key to move', 1, WHITE)
        instruction_2 = instrucfont.render('Press Z to shoot', 1, WHITE)
        screen.blit(nlabel, (150, 230))
        screen.blit(instruction_1, (60, 700))
        screen.blit(instruction_2, (60, 750))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_start = True
                    game_end = False

    while game_end == True:
        screen.fill(WHITE)
        myfont = pygame.font.SysFont('freesansbold.ttf', 80)
        instrucfont = pygame.font.SysFont('freesansbold.ttf', 50)
        nlabel = myfont.render('Press R to start', 2, L_GREEN)
        instruction_1 = instrucfont.render('Press arrow key to move', 1, WHITE)
        instruction_2 = instrucfont.render('Press Z to shoot', 1, WHITE)
        screen.blit(nlabel, (150, 230))
        screen.blit(instruction_1, (60, 700))
        screen.blit(instruction_2, (60, 750))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    player.hp = 100
                    player.live = 3
                    game_end = False
                    game_start = False

    pygame.display.flip()
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # --- Game logic should go here
    time += 1
    bgtime += 1

    # --- background reset
    if bgtime == 900:
        bgtime = 0
        # --- Enemy generation code for testing
    ##    enemytype1()
    ##    enemytype2()
    ##    enemytype3()
    ##    enemytype4()
    enemytype5()

    # --- Enemy Update
    for enemy in enemy1_group:
        enemy.update_180_2()
    for enemy in enemy2_group:
        enemy.update_S()
    for enemy in enemy3_group:
        enemy.update_Z()
    for enemy in enemy4_group:
        enemy.update_180()
    for boss in boss_group:
        boss.update_boss()

    # --- Player control limit
    if player.rect.x < 1:
        player.rect.x = 1
    elif player.rect.x > 640:
        player.rect.x = 640

    if player.rect.y < 1:
        player.rect.y = 1
    elif player.rect.y > 830:
        player.rect.y = 830

    # --- Player bullet generation code
    player.shoot()
    p_bullet = Bullet()
    # if player.playershoot == True:
    #     p_bullet = Bullet()
    #     p_bullet.image = pygame.image.load("pb.png").convert_alpha()
    #     if time % p_bullet.gap == 0:
    #         p_bullet.rect.x = player.rect.centerx-3
    #         p_bullet.rect.y = player.rect.centery-18
    #         p_bullet_group.add(p_bullet)
    #         allSprites.add(p_bullet)
            ##                pygame.mixer.music.load("shoot.mp3")
            ##                pygame.mixer.music.play(-1)

            # --- Enemy bullet generation code
            ##    if enemy4.enemyshoot == True:
            ##        en_bullet=en_Bullet()
            ##        if time%en_bullet.gap == 0:
            ##            en_bullet.rect.x = enemy4.rect.x
            ##            en_bullet.rect.y = enemy4.rect.y

    # --- Remove bullet outside the screen
    for bullet in p_bullet_group:
        if bullet.rect.x > 725 or bullet.rect.x < -25 or bullet.rect.y < -25 or bullet.rect.y > 925:
            p_bullet_group.remove(bullet)
            allSprites.remove(bullet)

    for bullet in en_bullet1_group:
        if bullet.rect.x > 725 or bullet.rect.x < -25 or bullet.rect.y < -25 or bullet.rect.y > 925:
            en_bullet1_group.remove(bullet)
            allSprites.remove(bullet)
            ##        for enemy in enemy_group:
            ##            if enemy.rect.x > 725 or enemy.rect.x < -25 or enemy.rect.y < -25 or enemy.rect.y > 925:
            ##                enemy_group.remove(bullet)
            ##                allSprites.remove(bullet)
    
    # --- Player enemy collision
    enemy1_hit_player = pygame.sprite.groupcollide(hitbox_group, enemy1_group, False, True)
    enemy2_hit_player = pygame.sprite.groupcollide(hitbox_group, enemy2_group, False, True)
    enemy3_hit_player = pygame.sprite.groupcollide(hitbox_group, enemy3_group, False, True)
    enemy4_hit_player = pygame.sprite.groupcollide(hitbox_group, enemy4_group, False, True)
    boss_hit_player = pygame.sprite.groupcollide(hitbox_group, boss_group, False, False)

    for hitbox in enemy1_hit_player:
        player.hp -= enemy.crash_dmg

    for hitbox in enemy2_hit_player:
        player.hp -= enemy2.crash_dmg

    for hitbox in enemy3_hit_player:
        player.hp -= enemy.crash_dmg

    for hitbox in enemy4_hit_player:
        player.hp -= enemy.crash_dmg

    for hitbox in boss_hit_player:
        player.hp -= boss.crash_dmg

    # --- Player's bullet enemy collision
    bullet_hit_enemy1 = pygame.sprite.groupcollide(enemy1_group, p_bullet_group, False, True)
    bullet_hit_enemy2 = pygame.sprite.groupcollide(enemy2_group, p_bullet_group, False, True)
    bullet_hit_enemy3 = pygame.sprite.groupcollide(enemy3_group, p_bullet_group, False, True)
    bullet_hit_enemy4 = pygame.sprite.groupcollide(enemy4_group, p_bullet_group, False, True)
    bullet_hit_boss = pygame.sprite.groupcollide(boss_group, p_bullet_group, False, True)

    for enemy1 in bullet_hit_enemy1:
        enemy1.hp -= p_bullet.dmg
        if enemy1.hp <= 0:
            enemy1_group.remove(enemy1)
            allSprites.remove(enemy1)
            player.score += enemy1.score
        if enemy1.rect.x > 725 or enemy1.rect.x < -25 or enemy1.rect.y < -25 or enemy1.rect.y > 925:
            enemy1_group.remove(enemy1)
            allSprites.remove(enemy1)

    for enemy2 in bullet_hit_enemy2:
        enemy2.hp -= p_bullet.dmg
        if enemy2.hp <= 0:
            enemy2_group.remove(enemy2)
            allSprites.remove(enemy2)
            player.score += enemy2.score
        if enemy2.rect.x > 725 or enemy2.rect.x < -25 or enemy2.rect.y < -25 or enemy2.rect.y > 925:
            enemy2_group.remove(enemy2)
            allSprites.remove(enemy2)

    for enemy3 in bullet_hit_enemy3:
        enemy3.hp -= p_bullet.dmg
        if enemy3.hp <= 0:
            enemy3_group.remove(enemy3)
            allSprites.remove(enemy3)
            player.score += enemy3.score
        if enemy3.rect.x > 725 or enemy3.rect.x < -25 or enemy3.rect.y < -25 or enemy3.rect.y > 925:
            enemy3_group.remove(enemy3)
            allSprites.remove(enemy3)

    for enemy4 in bullet_hit_enemy4:
        enemy4.hp -= p_bullet.dmg
        if enemy4.hp <= 0:
            enemy4_group.remove(enemy4)
            allSprites.remove(enemy4)
            player.score += enemy4.score
        if enemy4.rect.x > 725 or enemy4.rect.x < -25 or enemy4.rect.y < -25 or enemy4.rect.y > 925:
            enemy4_group.remove(enemy4)
            allSprites.remove(enemy4)

    for boss in bullet_hit_boss:
        boss.hp -= p_bullet.dmg
        if boss.hp <= 0:
            boss_group.remove(boss)
            allSprites.remove(boss)
            player.score += boss.score

    # --- Enemy bullet and Player collision
    bullet_hit_player1 = pygame.sprite.groupcollide(hitbox_group, en_bullet1_group, False, True)

    for hitbox in bullet_hit_player1:
        player.hp -= 10
    
    # --- Player damage checking
    if player.hp <= 0:
        player.live -= 1
        player.hp = 100
        player.score -= 200
    ##        bullet.gap = 16

    if player.live <= 0:
        game_end = True

    ##    # --- Level up due to score
    ##    if player.score % 20 == 0 and player.score > 0:
    ##        for bullet in p_bullet_group:
    ##            bullet.levelup()
    ##            print(bullet.gap)

    # --- Blit screens
    p_score = instrucfont.render('Score:' + str(player.score), 1, N_BLUE)
    p_live = instrucfont.render('Live:' + str(player.live), 1, N_BLUE)
    p_hp = instrucfont.render('HP:' + str(player.hp) + '/100', 1, N_BLUE)

    # --- All debugging code
    ##    print(player.hp)
    ##    print(player.live)
    ##    print('end:'+str(game_end))
    ##    print('start:'+str(game_start))

    # --- Screen-clearing code goes here
    screen.fill(BLACK)
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    ##    bullet_collisions=pygame.sprite.groupcollide(enemy_group, p_bullet_list, False, True)
    ##    if len(bullet_collisions)>0:
    ##        score=score+10
    ##    for x in bullet_collisions:
    ##        x.hp-=p_bullet.damage
    ##        if x.hp==0:
    ##            enemy_group.remove(x)
    ##            allSprites.remove(x)
    # print(x.rect.x)
    # print(x.health)
    # score=len(bullet_collisions)*10
    # print(score)

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    ##    background.image = pygame.image.load("background.png").convert()

    # --- Drawing code should go here

    # --- Background scrolling
    screen.blit(back, (0, bgtime))
    screen.blit(back, (0, bgtime - 900))

    screen.blit(p_score, (15, 20))
    screen.blit(p_hp, (300, 20))
    screen.blit(p_live, (580, 20))

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
