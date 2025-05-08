import random
import pygame
pygame.init()
screen = pygame.display.set_mode((900, 640))
done = False
clock = pygame.time.Clock()
white=(255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
bg = (0,0,0)
screen.fill(bg) 
mov=0
rns=0
rwe=0
hp = 100
d = 5
csh = 0
cho=0
md = 1
man = 0
dist = 128
x1=286
y1=286
z1=68
a1=68
list1=[]
inputs=[]
attacks=[]
font = pygame.font.SysFont("Ancient Modern Tales", 100)
text = ""
input_active = True

run = True
while run == True:
    txtsurf = font.render("Input your name:", True, white)
    screen.blit(txtsurf,(300 - txtsurf.get_width() // 2, 80 - txtsurf.get_height() // 2))
    pygame.display.flip()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_active = True
            text = ""
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                input_active = False
                name = text
                run = False
                break
            elif event.key == pygame.K_BACKSPACE:
                text =  text[:-1]
            else:
                text += event.unicode
        screen.fill(0)
        txtsurf = font.render(text, True, white)
        screen.blit(txtsurf, txtsurf.get_rect(center = screen.get_rect().center))
        pygame.display.flip()
def refresh():
    screen.fill(bg) 
    drawGrid()
    outofbounds()
    specialsq()
    pygame.draw.rect(screen, blue, pygame.Rect(x1, y1, z1, a1))
    pygame.display.flip()
def refresh2():
    screen.fill(bg) 
    drawGrid()
    outofbounds2()
    specialsq2()
    pygame.draw.rect(screen, blue, pygame.Rect(x1, y1, z1, a1))
    pygame.display.flip()
def refresh3():
    screen.fill(bg) 
    drawGrid()
    outofbounds3()
    specialsq3()
    pygame.draw.rect(screen, blue, pygame.Rect(x1, y1, z1, a1))
    pygame.display.flip()
def enemy1():
    global hp
    global d
    global csh
    font = pygame.font.SysFont("Ancient Modern Tales", 36)
    ehp=random.randint(1,10)
    c=random.randint(1,3)
    ed=random.randint(1,4)
    if random.randint(1,5) == 3:
        txtsurf = font.render("Tier1 enemy appears...", True, red)
        screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
        txtsurf = font.render("Enemy Hp: " + str(ehp), True, white)
        screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436 - txtsurf.get_height() // 2))
        txtsurf = font.render("Enemy Attack: " + str(ed), True, white)
        screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 472 - txtsurf.get_height() // 2))
        pygame.display.flip()
        while ehp>0 and hp>0:
            yd=random.randint(0,d)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                        ehp-=yd
                        if ehp<1:
                            txtsurf = font.render("Dealt " + str(yd) + " damage", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                            txtsurf = font.render("Enemy defeated", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436 - txtsurf.get_height() // 2))
                            pygame.display.flip()
                            screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                            csh+=c
                        else:
                            txtsurf = font.render("Dealt " + str(yd) + " damage", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                            txtsurf = font.render("Enemy hp: " + str(ehp) , True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436- txtsurf.get_height() // 2))
                            txtsurf = font.render("Enemy deals " + str(ed) + " damage" , True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 472- txtsurf.get_height() // 2))
                            hp-=ed
                            txtsurf = font.render("You have " + str(hp) + " hp left", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 508 - txtsurf.get_height() // 2))
                            pygame.display.flip()
                            screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                            if hp<1:
                                txtsurf = font.render("You died", True, red)
                                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                                pygame.display.flip()
def enemy11():
    global hp
    global d
    global csh
    global md
    global man
    ehp=random.randint(20,80)
    c=random.randint(10,25)
    ed=random.randint(10,20)
    if random.randint(1,6) == 3:
        print("You hear a City Tier 1 enemy...")
        print("Enemy HP =" , ehp , "Enemy Attack =" , ed )
        while ehp>0 and hp>0:
            yd=random.randint(0,d)
            mrd=random.randint(0,md)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        ehp-=yd
                        if ehp<1:
                            print("You dealt", yd ,"damage")
                            print("Enemy defeated")
                            csh+=c
                        else:
                            print("You dealt" ,yd, "damage")
                            print("Enemy has" ,ehp, "health")
                            print("Enemy attacks!")
                            hp-=ed
                            print("You are down to" ,hp, "health")
                            if hp<1:
                                print("You died")
                    if event.key == pygame.K_m and man>5:
                        man-=5
                        ehp-=mrd
                        if ehp<1:
                            print("You dealt", mrd ,"damage")
                            print("Enemy defeated")
                            csh+=c
                        else:
                            print("You dealt" ,mrd, "damage")
                            print("Enemy has" ,ehp, "health")
                            print("Enemy attacks!")
                            hp-=ed
                            print("You are down to" ,hp, "health")
                            if hp<1:
                                print("You died")
def enemy12m():
    global hp
    global d
    global csh
    global md
    global man
    ehp=random.randint(40,110)
    c=random.randint(35,60)
    ed=random.randint(25,40)
    if random.randint(1,7) == 3:
        print("You hear a City Tier 2m Aggravated enemy...")
        print("Enemy HP =" , ehp , "Enemy Attack =" , ed )
        while ehp>0 and hp>0:
            yd=random.randint(0,d)
            mrd=random.randint(0,md)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        ehp-=(yd//2)
                        if ehp<1:
                            print("Its not very effective...")
                            print("You dealt", yd//2 ,"damage")
                            print("Enemy defeated")
                            csh+=c
                            md+=5
                        else:
                            print("Its not very effective...")
                            print("You dealt" ,yd//2, "damage")
                            print("Enemy has" ,ehp, "health")
                            print("Enemy attacks!")
                            hp-=ed
                            print("You are down to" ,hp, "health")
                            if hp<1:
                                print("You died")
                    if event.key == pygame.K_m and man>5:
                        man-=5
                        ehp-=(mrd*2)
                        if ehp<1:
                            print("Its super effective!")
                            print("You dealt", mrd*2 ,"damage")
                            print("Enemy defeated")
                            csh+=c
                        else:
                            print("Its super effective!")
                            print("You dealt" ,mrd*2, "damage")
                            print("Enemy has" ,ehp, "health")
                            print("Enemy attacks!")
                            hp-=ed
                            print("You are down to" ,hp, "health")
                            if hp<1:
                                print("You died")
def enemy12():
    global hp
    global d
    global csh
    global md
    global man
    ehp=random.randint(40,110)
    c=random.randint(35,60)
    ed=random.randint(25,40)
    if random.randint(1,7) == 3:
        print("You hear a City Tier 2 Aggravated enemy...")
        print("Enemy HP =" , ehp , "Enemy Attack =" , ed )
        while ehp>0 and hp>0:
            yd=random.randint(0,d)
            mrd=random.randint(0,md)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        ehp-=yd
                        if ehp<1:
                            print("You dealt", yd ,"damage")
                            print("Enemy defeated")
                            csh+=c
                        else:
                            print("You dealt" ,yd, "damage")
                            print("Enemy has" ,ehp, "health")
                            print("Enemy attacks!")
                            hp-=ed
                            print("You are down to" ,hp, "health")
                            if hp<1:
                                print("You died")
                    if event.key == pygame.K_a and man>5:
                        man-=5
                        ehp-=mrd
                        if ehp<1:
                            print("You dealt", mrd ,"damage")
                            print("Enemy defeated")
                            csh+=c
                        else:
                            print("You dealt" ,mrd, "damage")
                            print("Enemy has" ,ehp, "health")
                            print("Enemy attacks!")
                            hp-=ed
                            print("You are down to" ,hp, "health")
                            if hp<1:
                                print("You died")
def enemy13m():
    global hp
    global d
    global csh
    global md
    global man
    ehp=random.randint(100,175)
    c=random.randint(125,160)
    ed=random.randint(50,80)
    if random.randint(1,8) == 3:
        print("You hear a City Tier 3m Deadly enemy...")
        print("Enemy HP =" , ehp , "Enemy Attack =" , ed )
        while ehp>0 and hp>0:
            yd=random.randint(0,d)
            mrd=random.randint(0,md)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        ehp-=(yd//2)
                        if ehp<1:
                            print("Its not very effective...")
                            print("You dealt", yd//2 ,"damage")
                            print("Enemy defeated")
                            csh+=c
                            md+=5
                        else:
                            print("Its not very effective...")
                            print("You dealt" ,yd//2, "damage")
                            print("Enemy has" ,ehp, "health")
                            print("Enemy attacks!")
                            hp-=ed
                            print("You are down to" ,hp, "health")
                            if hp<1:
                                print("You died")
                    if event.key == pygame.K_m and man>5:
                        man-=5
                        ehp-=(mrd*2)
                        if ehp<1:
                            print("Its super effective!")
                            print("You dealt", mrd*2 ,"damage")
                            print("Enemy defeated")
                            csh+=c
                        else:
                            print("Its super effective!")
                            print("You dealt" ,mrd*2, "damage")
                            print("Enemy has" ,ehp, "health")
                            print("Enemy attacks!")
                            hp-=ed
                            print("You are down to" ,hp, "health")
                            if hp<1:
                                print("You died")
                    if event.key == pygame.K_s and list1.count(2)>0:
                        ehp-=(yd*3)
                        list1.remove(2)
                        if ehp<1:
                            print("You dealt", yd*3 ,"damage")
                            print("Enemy defeated")
                            csh+=c
                        else:
                            print("You dealt" ,yd*3, "damage")
                            print("Enemy has" ,ehp, "health")
                            print("Enemy attacks!")
                            hp-=ed
                            print("You are down to" ,hp, "health")
                            if hp<1:
                                print("You died")
def enemy13():
    global hp
    global d
    global csh
    global md
    global man
    ehp=random.randint(100,175)
    c=random.randint(125,160)
    ed=random.randint(50,80)
    if random.randint(1,8) == 3:
        print("You hear a City Tier 3 Deadly enemy...")
        print("Enemy HP =" , ehp , "Enemy Attack =" , ed )
        while ehp>0 and hp>0:
            yd=random.randint(0,d)
            mrd=random.randint(0,md)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        ehp-=yd
                        if ehp<1:
                            print("You dealt", yd ,"damage")
                            print("Enemy defeated")
                            csh+=c
                        else:
                            print("You dealt" ,yd, "damage")
                            print("Enemy has" ,ehp, "health")
                            print("Enemy attacks!")
                            hp-=ed
                            print("You are down to" ,hp, "health")
                            if hp<1:
                                print("You died")
                    if event.key == pygame.K_m and man>5:
                        man-=5
                        ehp-=mrd
                        if ehp<1:
                            print("You dealt", mrd ,"damage")
                            print("Enemy defeated")
                            csh+=c
                        else:
                            print("You dealt" ,mrd, "damage")
                            print("Enemy has" ,ehp, "health")
                            print("Enemy attacks!")
                            hp-=ed
                            print("You are down to" ,hp, "health")
                            if hp<1:
                                print("You died")
                    if event.key == pygame.K_a and list1.count(2)>0:
                        ehp-=(yd*3)
                        list1.remove(2)
                        if ehp<1:
                            print("You dealt", yd*3 ,"damage")
                            print("Enemy defeated")
                            csh+=c
                        else:
                            print("You dealt" ,yd*3, "damage")
                            print("Enemy has" ,ehp, "health")
                            print("Enemy attacks!")
                            hp-=ed
                            print("You are down to" ,hp, "health")
                            if hp<1:
                                print("You died")
def enemy14():
    global hp
    global d
    global csh
    global md
    global man
    ehp=random.randint(150,225)
    c=random.randint(280,315)
    ed=random.randint(70,115)
    if random.randint(1,9) == 3:
        print("You hear a City Tier 4 Unforgiving enemy...")
        print("Enemy HP =" , ehp , "Enemy Attack =" , ed )
        while ehp>0 and hp>0:
            yd=random.randint(0,d)
            mrd=random.randint(0,md)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        ehp-=yd
                        if ehp<1:
                            print("You dealt", yd ,"damage")
                            print("Enemy defeated")
                            csh+=c
                        else:
                            print("You dealt" ,yd, "damage")
                            print("Enemy has" ,ehp, "health")
                            print("Enemy attacks!")
                            hp-=ed
                            print("You are down to" ,hp, "health")
                            if hp<1:
                                print("You died")
                    if event.key == pygame.K_m and man>5:
                        man-=5
                        ehp-=mrd
                        if ehp<1:
                            print("You dealt", mrd ,"damage")
                            print("Enemy defeated")
                            csh+=c
                        else:
                            print("You dealt" ,mrd, "damage")
                            print("Enemy has" ,ehp, "health")
                            print("Enemy attacks!")
                            hp-=ed
                            print("You are down to" ,hp, "health")
                            if hp<1:
                                print("You died")
                    if event.key == pygame.K_s and list1.count(2)>0:
                        ehp-=(yd*3)
                        list1.remove(2)
                        if ehp<1:
                            print("You dealt", yd*3 ,"damage")
                            print("Enemy defeated")
                            csh+=c
                        else:
                            print("You dealt" ,yd*3, "damage")
                            print("Enemy has" ,ehp, "health")
                            print("Enemy attacks!")
                            hp-=ed
                            print("You are down to" ,hp, "health")
                            if hp<1:
                                print("You died")
def npc1():
    global d
    global csh
    if random.randint(1,12) == 3:
        if csh>30:
            print("A very sluggish man approaches you")
            print("He offers you 15 damage for all of your money, press N to decline or Y to accept")
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        print("Pleasure doing Business")
                        csh=0
                        d+=15
                    if event.key == pygame.K_n:
                        print("If you say so...")
                        pass
def npc2():
    global d
    global csh
    global mov
    if random.randint(1,8) == 2:
        if mov<200:
            print("A wise old man approaches you")
            print("Dont dwell - he says.")
def npc3():
    if random.randint(1,10) == 2:
        print("Welcome to the Tourist centre")
        print("Enemies with a m in their tier number take double the damage from magic attacks and twice less damage from normal attacks")
def enemy2():
    global hp
    global d
    global csh
    ehp=random.randint(1,25)
    c=random.randint(2,5)
    ed=random.randint(1,7)
    if random.randint(1,8) == 3:
        txtsurf = font.render("Tier2 enemy appears...", True, red)
        screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
        txtsurf = font.render("Enemy Hp: " + str(ehp), True, white)
        screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436 - txtsurf.get_height() // 2))
        txtsurf = font.render("Enemy Attack: " + str(ed), True, white)
        screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 472 - txtsurf.get_height() // 2))
        pygame.display.flip()
        while ehp>0 and hp>0:
            yd=random.randint(1,d)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                        ehp-=yd
                        if ehp<1:
                            txtsurf = font.render("Dealt " + str(yd) + " damage", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                            txtsurf = font.render("Enemy defeated", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436 - txtsurf.get_height() // 2))
                            pygame.display.flip()
                            screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                            drawGrid()
                            csh+=c
                        else:
                            txtsurf = font.render("Dealt " + str(yd) + " damage", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                            txtsurf = font.render("Enemy hp: " + str(ehp) , True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436- txtsurf.get_height() // 2))
                            txtsurf = font.render("Enemy deals " + str(ed) + " damage" , True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 472- txtsurf.get_height() // 2))
                            hp-=ed
                            txtsurf = font.render("You have " + str(hp) + " hp left", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 508 - txtsurf.get_height() // 2))
                            pygame.display.flip()
                            screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                            if hp<1:
                                txtsurf = font.render("You died", True, red)
                                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                                pygame.display.flip()
def enemysalt():
    global hp
    global d
    global csh
    ehp=75
    ed=10
    dr=random.randint(1,3)
    c=37
    if random.randint(1,3) == 2:
        txtsurf = font.render("Tier4 enemy appears...", True, red)
        screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
        txtsurf = font.render("Enemy Hp: " + str(ehp), True, white)
        screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436 - txtsurf.get_height() // 2))
        txtsurf = font.render("Enemy Attack: " + str(ed), True, white)
        screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 472 - txtsurf.get_height() // 2))
        pygame.display.flip()
        while ehp>0 and hp>0:
            yd=random.randint(1,d)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        ehp-=yd
                        screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                        if ehp<1:
                            txtsurf = font.render("Dealt " + str(yd) + " damage", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                            txtsurf = font.render("Enemy defeated", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436 - txtsurf.get_height() // 2))
                            pygame.display.flip()
                            screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                            drawGrid()
                            csh+=c
                            if dr == 2:
                                txtsurf = font.render("+ Salt Enhancement", True, white)
                                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 472 - txtsurf.get_height() // 2))
                                pygame.display.flip()
                                screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                                d+=5
                        else:
                            txtsurf = font.render("Dealt " + str(yd) + " damage", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                            txtsurf = font.render("Enemy hp: " + str(ehp) , True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436- txtsurf.get_height() // 2))
                            txtsurf = font.render("Enemy deals " + str(ed) + " damage" , True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 472- txtsurf.get_height() // 2))
                            hp-=ed
                            txtsurf = font.render("You have " + str(hp) + " hp left", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 508 - txtsurf.get_height() // 2))
                            pygame.display.flip()
                            screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                            if hp<1:
                                txtsurf = font.render("You died", True, red)
                                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                                pygame.display.flip()
                    if event.key == pygame.K_s and list1.count(2)>0:
                        ehp-=(yd*3)
                        screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                        list1.remove(2)
                        if ehp<1:
                            txtsurf = font.render("Dealt " + str(yd*3) + " damage", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                            txtsurf = font.render("Enemy defeated", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436 - txtsurf.get_height() // 2))
                            pygame.display.flip()
                            screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                            drawGrid()
                            csh+=c
                            if dr == 2:
                                txtsurf = font.render("+ Salt Enhancement", True, white)
                                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 472 - txtsurf.get_height() // 2))
                                pygame.display.flip()
                                screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                                d+=5
                        else:
                            txtsurf = font.render("Dealt " + str(yd*3) + " damage", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                            txtsurf = font.render("Enemy hp: " + str(ehp) , True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436- txtsurf.get_height() // 2))
                            txtsurf = font.render("Enemy deals " + str(ed) + " damage" , True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 472- txtsurf.get_height() // 2))
                            hp-=ed
                            txtsurf = font.render("You have " + str(hp) + " hp left", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 508 - txtsurf.get_height() // 2))
                            pygame.display.flip()
                            screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                            if hp<1:
                                txtsurf = font.render("You died", True, red)
                                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                                pygame.display.flip()
def enemy3():
    global hp
    global d
    global csh
    ehp=random.randint(12,50)
    c=random.randint(14,38)
    ed=random.randint(5,17)
    if random.randint(1,10) == 3 and rns>0 and rwe>=0:
        txtsurf = font.render("Tier3 enemy appears...", True, red)
        screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
        txtsurf = font.render("Enemy Hp: " + str(ehp), True, white)
        screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436 - txtsurf.get_height() // 2))
        txtsurf = font.render("Enemy Attack: " + str(ed), True, white)
        screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 472 - txtsurf.get_height() // 2))
        pygame.display.flip()
        while ehp>0 and hp>0:
            yd=random.randint(1,d)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                        ehp-=yd
                        if ehp<1:
                            txtsurf = font.render("Dealt " + str(yd) + " damage", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                            txtsurf = font.render("Enemy defeated", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436 - txtsurf.get_height() // 2))
                            pygame.display.flip()
                            screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                            drawGrid()
                            csh+=c
                        else:
                            txtsurf = font.render("Dealt " + str(yd) + " damage", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                            txtsurf = font.render("Enemy hp: " + str(ehp) , True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436- txtsurf.get_height() // 2))
                            txtsurf = font.render("Enemy deals " + str(ed) + " damage" , True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 472- txtsurf.get_height() // 2))
                            hp-=ed
                            txtsurf = font.render("You have " + str(hp) + " hp left", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 508 - txtsurf.get_height() // 2))
                            pygame.display.flip()
                            screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                            if hp<1:
                                txtsurf = font.render("You died", True, red)
                                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                                pygame.display.flip()
                    if event.key == pygame.K_s and list1.count(2)>0:
                        ehp-=(yd*3)
                        screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                        list1.remove(2)
                        if ehp<1:
                            txtsurf = font.render("Dealt " + str(yd*3) + " damage", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                            txtsurf = font.render("Enemy defeated", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436 - txtsurf.get_height() // 2))
                            pygame.display.flip()
                            screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                            drawGrid()
                            csh+=c
                        else:
                            txtsurf = font.render("Dealt " + str(yd*3) + " damage", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                            txtsurf = font.render("Enemy hp: " + str(ehp) , True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436- txtsurf.get_height() // 2))
                            txtsurf = font.render("Enemy deals " + str(ed) + " damage" , True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 472- txtsurf.get_height() // 2))
                            hp-=ed
                            txtsurf = font.render("You have " + str(hp) + " hp left", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 508 - txtsurf.get_height() // 2))
                            pygame.display.flip()
                            screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                            if hp<1:
                                txtsurf = font.render("You died", True, red)
                                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                                pygame.display.flip()
def shop1(csh, hp, d, list1, md, man):
    font = pygame.font.SysFont("Ancient Modern Tales", 36)
    txtsurf = font.render("1.Healing potion, 10$", True, white)
    screen.blit(txtsurf, (755 - txtsurf.get_width() // 2, 30 - txtsurf.get_height() // 2))
    txtsurf = font.render("2.Strength potion, 10$", True, white)
    screen.blit(txtsurf, (770 - txtsurf.get_width() // 2, 66 - txtsurf.get_height() // 2))
    txtsurf = font.render("3.Super attack, 50$", True, white)
    screen.blit(txtsurf, (755 - txtsurf.get_width() // 2, 102 - txtsurf.get_height() // 2))
    txtsurf = font.render("4.Magic Kit, 200$", True, white)
    screen.blit(txtsurf, (745 - txtsurf.get_width() // 2, 138 - txtsurf.get_height() // 2))
    pygame.display.flip()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1] and csh >= 10:
        csh -= 10
        if 6 in list1:
            hp = 250
        elif 5 in list1:
            hp = 150
        elif 4 in list1:
            hp = 125
        else:
            hp = 100
    elif keys[pygame.K_2] and csh >= 10:
        d += 5
        csh -= 10
    elif keys[pygame.K_3] and csh >= 50:
        csh -= 50
        list1.append(2)
    elif keys[pygame.K_4] and csh >= 200:
        csh -= 200
        md += 25
        man += 100
    return csh, hp, d, list1, md, man
def chest1():
    global csh
    global d
    global man
    ree=random.randint(1,20)
    font = pygame.font.SysFont("Ancient Modern Tales", 36)
    if rns == -1 and rwe == 0 and csh>=5:
        txtsurf = font.render("Opened chest", True, white)
        screen.blit(txtsurf,(765 - txtsurf.get_width() // 2, 30 - txtsurf.get_height() // 2))
        if ree == 1 or ree == 2 or ree == 5 or ree == 6 or ree == 7 or ree == 9 or ree == 14:
            d+=1
            csh-=5
            txtsurf = font.render("+ Damage attribute", True, white)
            screen.blit(txtsurf,(765 - txtsurf.get_width() // 2, 66 - txtsurf.get_height() // 2))
            pygame.display.flip
        elif ree == 3:
            txtsurf = font.render("+ Sword Improvement", True, white)
            screen.blit(txtsurf,(765 - txtsurf.get_width() // 2, 210 - txtsurf.get_height() // 2))
            pygame.display.flip
            d+=7
            csh-=5
        elif ree == 8:
            list1.append(1)
            csh-=5
            txtsurf = font.render("+ Overground key", True, white)
            screen.blit(txtsurf,(755 - txtsurf.get_width() // 2, 138 - txtsurf.get_height() // 2))
            pygame.display.flip
        elif ree == 11:
            csh-=5
            man+=5
            txtsurf = font.render("+ Essence of Mana", True, white)
            screen.blit(txtsurf,(755 - txtsurf.get_width() // 2, 174 - txtsurf.get_height() // 2))
            pygame.display.flip
        else:
            csh-=5
            csh+=7
            txtsurf = font.render("+ Pouch of Money", True, white)
            screen.blit(txtsurf,(755 - txtsurf.get_width() // 2, 102 - txtsurf.get_height() // 2))
            pygame.display.flip
def chest2():
    global csh
    global d
    global md
    global man
    global hp
    ree=random.randint(1,20)
    if rns == 12 and rwe == 13 and csh>=25:
        print("You have opened the City chest")
        if ree == 1 or ree == 2 or ree == 5 or ree == 6 or ree == 7 or ree == 9 or ree == 14:
            hp+=15
            csh-=25
            print("You received a Small Additive Healing Potion")
        elif ree == 3:
            print("You received a Wand improvement")
            md+=17
            csh-=25
        elif ree == 11:
            csh-=25
            man+=15
            print("You received an Essence of Mana")
        elif ree == 13 or ree == 18:
            csh-=25
            d+=15
            print("You received a Sword enhancement")
        else:
            csh-=25
            csh+=20
            print("You received a Pouch of Money")
def boss1():
    global hp
    global d
    global csh
    global md
    ehp=100
    ed=20
    dr=random.randint(1,3)
    c=100
    txtsurf = font.render("Boss appears...", True, red)
    screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
    txtsurf = font.render("He is Top 50 Yassou", True, red)
    screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
    txtsurf = font.render("in Lithuania...", True, red)
    screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
    txtsurf = font.render("Boss Hp: " + str(ehp), True, white)
    screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436 - txtsurf.get_height() // 2))
    txtsurf = font.render("Boss Attack: " + str(ed), True, white)
    screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 472 - txtsurf.get_height() // 2))
    pygame.display.flip()
    while ehp>0 and hp>0:
        yd=random.randint(1,d)
        if mov<250:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        ehp-=yd
                        screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                        if ehp<1:
                            txtsurf = font.render("Dealt " + str(yd) + " damage", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                            txtsurf = font.render("Boss defeated", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436 - txtsurf.get_height() // 2))
                            pygame.display.flip()
                            screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                            drawGrid()
                            csh+=c
                            if dr == 2:
                                txtsurf = font.render("+ Magic Wand", True, white)
                                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 472 - txtsurf.get_height() // 2))
                                md+=10
                            else:
                                txtsurf = font.render("+ Boss Armor", True, white)
                                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 472 - txtsurf.get_height() // 2))
                                list1.append(5)
                        else:
                            txtsurf = font.render("Dealt " + str(yd) + " damage", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                            txtsurf = font.render("Boss hp: " + str(ehp) , True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436- txtsurf.get_height() // 2))
                            txtsurf = font.render("Boss deals " + str(ed) + " damage" , True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 472- txtsurf.get_height() // 2))
                            hp-=ed
                            txtsurf = font.render("You have " + str(hp) + " hp left", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 508 - txtsurf.get_height() // 2))
                            pygame.display.flip()
                            screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                            if hp<1:
                                txtsurf = font.render("You died", True, red)
                                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                                pygame.display.flip()
                    if event.key == pygame.K_s and list1.count(2)>0:
                        ehp-=(yd*3)
                        screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                        list1.remove(2)
                        if ehp<1:
                            txtsurf = font.render("Dealt " + str(yd*3) + " damage", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                            txtsurf = font.render("Boss defeated", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436 - txtsurf.get_height() // 2))
                            txtsurf = font.render("Ceiling starts to crack...", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 472 - txtsurf.get_height() // 2))
                            pygame.display.flip()
                            screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                            drawGrid()
                            csh+=c
                            if dr == 2:
                                txtsurf = font.render("+ Magic Wand", True, white)
                                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 508 - txtsurf.get_height() // 2))
                                md+=10
                            else:
                                txtsurf = font.render("+ Broken Boss Armor", True, white)
                                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 508 - txtsurf.get_height() // 2))
                                list1.append(4)
                        else:
                            txtsurf = font.render("Dealt " + str(yd*3) + " damage", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                            txtsurf = font.render("Boss hp: " + str(ehp) , True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436- txtsurf.get_height() // 2))
                            txtsurf = font.render("Boss deals " + str(ed) + " damage" , True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 472- txtsurf.get_height() // 2))
                            hp-=ed
                            txtsurf = font.render("You have " + str(hp) + " hp left", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 508 - txtsurf.get_height() // 2))
                            pygame.display.flip()
                            screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                            if hp<1:
                                txtsurf = font.render("You died", True, red)
                                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                                pygame.display.flip()
        else:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                        ehp-=yd
                        if ehp<1:
                            txtsurf = font.render("Dealt " + str(yd) + " damage", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                            txtsurf = font.render("Boss defeated", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436 - txtsurf.get_height() // 2))
                            pygame.display.flip()
                            screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                            drawGrid()
                            csh+=c
                            if dr == 2:
                                txtsurf = font.render("+ Improved Magic Wand", True, white)
                                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 508 - txtsurf.get_height() // 2))
                                md+=20
                            else:
                                txtsurf = font.render("+ Boss Armor", True, white)
                                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 508 - txtsurf.get_height() // 2))
                                list1.append(5)
                        else:
                            txtsurf = font.render("Dealt " + str(yd) + " damage", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                            txtsurf = font.render("Boss hp: " + str(ehp) , True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436- txtsurf.get_height() // 2))
                            txtsurf = font.render("Boss deals " + str(ed*2) + " damage" , True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 472- txtsurf.get_height() // 2))
                            hp-=(ed*2)
                            txtsurf = font.render("You have " + str(hp) + " hp left", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 508 - txtsurf.get_height() // 2))
                            pygame.display.flip()
                            screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                            if hp<1:
                                txtsurf = font.render("You died", True, red)
                                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                                pygame.display.flip()
                    if event.key == pygame.K_s and list1.count(2)>0:
                        ehp-=(yd*3)
                        screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                        list1.remove(2)
                        if ehp<1:
                            txtsurf = font.render("Dealt " + str(yd*3) + " damage", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                            txtsurf = font.render("Boss defeated", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436 - txtsurf.get_height() // 2))
                            txtsurf = font.render("Ceiling starts to crack...", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 472 - txtsurf.get_height() // 2))
                            pygame.display.flip()
                            screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                            drawGrid()
                            csh+=c
                            if dr == 2:
                                txtsurf = font.render("+ Magic Wand", True, white)
                                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 508 - txtsurf.get_height() // 2))
                                md+=10
                            else:
                                txtsurf = font.render("+ Broken Boss Armor", True, white)
                                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 508 - txtsurf.get_height() // 2))
                                list1.append(4)
                        else:
                            txtsurf = font.render("Dealt " + str(yd*3) + " damage", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                            txtsurf = font.render("Boss hp: " + str(ehp) , True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436- txtsurf.get_height() // 2))
                            txtsurf = font.render("Boss deals " + str(ed*2) + " damage" , True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 472- txtsurf.get_height() // 2))
                            hp-=(ed*2)
                            txtsurf = font.render("You have " + str(hp) + " hp left", True, white)
                            screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 508 - txtsurf.get_height() // 2))
                            pygame.display.flip()
                            screen.fill(pygame.Color("black"), (640, 0, 640, 640))
                            if hp<1:
                                txtsurf = font.render("You died", True, red)
                                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                                pygame.display.flip()
def boss2():
    global hp
    global d
    global csh
    global man 
    global md
    ehp=350
    ed=125
    dr=random.randint(1,3)
    c=1000
    print("The Boss steals your PC...")
    print("Boss HP =" , ehp , "Boss Attack =" , ed )
    while ehp>0 and hp>0:
        yd=random.randint(1,d)
        mrd=random.randint(1,md)
        rr=random.randint(1,2)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if ehp<1:
                        print("You dealt", yd ,"damage")
                        print("The Boss has been defeated")
                        csh+=c
                        if dr == 2:
                            print("The boss dropped a Magic Rune")
                            md+=25
                            man+=50
                        else:
                            print("The boss dropped his Intricate armor")
                            list1.append(6)
                    else:
                        print("You dealt" ,yd, "damage")
                        print("Boss has" ,ehp, "health")
                        print("Boss attacks!")
                        hp-=ed
                        print("You are down to" ,hp, "health")
                        if hp<1:
                            print("You died")
                if event.key == pygame.K_s and list1.count(2)>0:
                    ehp-=(yd*3)
                    list1.remove(2)
                    if ehp<1:
                        print("You dealt", yd*3 ,"damage")
                        print("You hear the Boss screaming in agony")
                        csh+=c
                        if dr == 2:
                            print("The boss dropped his Intricate armor")
                            list1.append(6)
                        else:
                            print("The boss dropped his Raging Sword")
                            d+=100
                    else:
                        print("You dealt" ,yd*3, "damage")
                        print("Enemy has" ,ehp, "health")
                        print("Enemy attacks!")
                        hp-=ed
                        print("You are down to" ,hp, "health")
                        if hp<1:
                            print("You died")
                if event.key == pygame.K_m and man>5:
                    man-=5
                    if list1.count(10)>0 and rr==1:
                        ehp-=(mrd*2)      
                    else:
                        ehp-=mrd
                    if ehp<1:
                        print("You dealt", mrd ,"damage")
                        if list1.count(10)>0 and rr==1:
                            print("Double Damage!")
                        print("You hear the Boss screaming in agony")
                        csh+=c
                        if dr == 2:
                            print("The boss dropped his Raging Sword")
                            d+=100
                        else:
                            print("The boss dropped his Magical Magic Wand")
                            md+=75
                    else:
                        print("You dealt" ,mrd, "damage")
                        if list1.count(10)>0 and rr==1:
                            print("Double Damage!")
                        print("Enemy has" ,ehp, "health")
                        print("Enemy attacks!")
                        hp-=ed
                        print("You are down to" ,hp, "health")
                        if hp<1:
                            print("You died")
def case1():
    global csh
    if rns == 8 and rwe == 12:
        x=(random.randint(1,782))
        y=(random.randint(1,10))
        csh-=3
        if x==782 or x==1:
            print("Exceedingly Rare")
            csh+=250
            if y==10:
                csh+=100
                print("STATRAK")
        elif x>=777 and x<=781:
            print("Covert")
            csh+=100
            if y==10:
                csh+=100
                print("STATRAK")
        elif x>=752 and x<=776:
            print("Classified")
            csh+=10
            if y==10:
                csh+=10
                print("STATRAK")
        elif x>=627 and x<=751:
            print("Restricted")
            csh+=3
            if y==10:
                csh+=3
                print("STATRAK")
        else:
            print("Mil-Spec Grade")
            if y==10:
                csh+=1
                print("STATRAK")  
def mboss1():
    global hp
    global d
    global csh
    global md
    global man
    ehp=random.randint(250,325)
    c=random.randint(380,500)
    ed=random.randint(90,165)
    if random.randint(1,2) == 2:
        print("You hear a Fishing Boat behind you...")
        print("You continue walking forwards, and get punched hard in the back (you lose 25% of your hp)...")
        hp-=(hp//4)
        print("Enemy HP =" , ehp , "Enemy Attack =" , ed )
        while ehp>0 and hp>0:
            yd=random.randint(2,d)
            mrd=random.randint(2,md)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        ehp-=yd
                        if ehp<1:
                            print("You dealt", yd ,"damage")
                            print("Enemy defeated")
                            csh+=c
                        else:
                            print("You dealt" ,yd, "damage")
                            print("Enemy has" ,ehp, "health")
                            print("Enemy attacks!")
                            hp-=ed
                            print("You are down to" ,hp, "health")
                            if hp<1:
                                print("You died")
                    if event.key == pygame.K_m and man>5:
                        man-=5
                        ehp-=mrd
                        if ehp<1:
                            print("You dealt", mrd ,"damage")
                            print("Enemy defeated")
                            csh+=c
                        else:
                            print("You dealt" ,mrd, "damage")
                            print("Enemy has" ,ehp, "health")
                            print("Enemy attacks!")
                            hp-=ed
                            print("You are down to" ,hp, "health")
                            if hp<1:
                                print("You died")
                    if event.key == pygame.K_s and list1.count(2)>0:
                        ehp-=(yd*3)
                        list1.remove(2)
                        if ehp<1:
                            print("You dealt", yd*3 ,"damage")
                            print("Enemy defeated")
                            csh+=c
                        else:
                            print("You dealt" ,yd*3, "damage")
                            print("Enemy has" ,ehp, "health")
                            print("Gabris Gabris attacks!")
                            hp-=ed
                            print("You are down to" ,hp, "health")
                            if hp<1:
                                print("You died")
def shop2():
    global hp
    global csh
    global d
    global list1
    global md
    global man
    if rns == 12 and rwe == 18:
        print("5 Items available:")
        print("1.Healing potion, say Heal to buy for 100 money") 
        print("2.Magic potion, say Magic to buy for 75 money")
        print("3.Scroll to use Super attack (Only effective to enemies above tier 2, Triple damage once), say Scroll to buy for 100 money")
        print("4.Giant-Slayer Spell (Only effects bosses from the City tier and above, 50% to do double damage from magic attacks (permanent usage)), say GSpell to buy for 300 money")
        print("5.Life-Long(Trademark) Public Transport Ticket, say PTTicket, to buy for 250 money, (lets you ride the bus and train without extra fees)")
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_5 and csh>250:
                    csh-=250
                    list1.count(11)
                if event.key == pygame.K_1 and csh>100:
                    csh-=100
                    if list1.count(13):
                        hp=500
                    elif list1.count(6):
                        hp=250
                    elif list1.count(5):
                        hp=150
                    elif list1.count(4):
                        hp=125
                    else:
                        hp=100
                if event.key == pygame.K_3 and csh>100:
                    csh-=100
                    list1.append(2)
                if event.key == pygame.K_4 and csh>300:
                    csh-=300
                    list1.append(10)
                if event.key == pygame.K_2 and csh>75:
                    csh-=75
                    md+=15
                    man+=50
                else:
                    pass
def boss3():
    global hp
    global d
    global csh
    global man 
    global md
    ehp=600
    ed=175
    dr=random.randint(1,3)
    c=1555
    print("Out of Nowhere a Boss appears...")
    print("It looks like he expected you...")
    print("Boss HP =" , ehp , "Boss Attack =" , ed )
    while ehp>0 and hp>0:
        yd=random.randint(1,d)
        mrd=random.randint(1,md)
        rr=random.randint(1,2)
        dc=random.randint(1,3)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if dc==2:
                        print("The boss Dodged your attack!")
                        print("Boss attacks!")
                        hp-=ed
                        print("You are down to" ,hp, "health")
                        if hp<1:
                            print("You died")
                    elif ehp<1:
                        print("You dealt", yd ,"damage")
                        print("The Boss has been defeated?")
                        csh+=c
                        if dr == 2:
                            print("The boss dropped a Magic Infused Armor")
                            md+=20
                            man+=75
                            list1.append(13)
                        else:
                            print("The boss dropped his Damage Ring")
                            d+=50
                            md+=150
                    else:
                        print("You dealt" ,yd, "damage")
                        print("Boss has" ,ehp, "health")
                        print("Boss attacks!")
                        hp-=ed
                        print("You are down to" ,hp, "health")
                        if hp<1:
                            print("You died")
                if event.key == pygame.K_s and list1.count(2)>0:
                    if dc==2:
                        print("The boss Dodged your attack!")
                        print("Boss attacks!")
                        hp-=ed
                        print("You are down to" ,hp, "health")
                        if hp<1:
                            print("You died")
                    ehp-=(yd*3)
                    list1.remove(2)
                    if ehp<1:
                        print("You dealt", yd*3 ,"damage")
                        print("You hear the Boss screaming in agony")
                        csh+=c
                        if dr == 2:
                            print("The boss dropped his Damage Ring")
                            d+=50
                            md+=150
                        else:
                            print("The boss dropped his Slaying Sword")
                            d+=150
                    else:
                        print("You dealt" ,yd*3, "damage")
                        print("Enemy has" ,ehp, "health")
                        print("Enemy attacks!")
                        hp-=ed
                        print("You are down to" ,hp, "health")
                        if hp<1:
                            print("You died")
                if event.key == pygame.K_m and man>5:
                    man-=5
                    if dc==2:
                        print("The boss Dodged your attack!")
                        print("Boss attacks!")
                        hp-=ed
                        print("You are down to" ,hp, "health")
                        if hp<1:
                            print("You died")
                    if list1.count(10)>0 and rr==1:
                        ehp-=(mrd*2)      
                    else:
                        ehp-=mrd
                    if ehp<1:
                        print("You dealt", mrd ,"damage")
                        if list1.count(10)>0 and rr==1:
                            print("Double Damage!")
                        print("You hear the Boss screaming in agony")
                        csh+=c
                        if dr == 2:
                            print("The boss dropped his Slaying Sword")
                            d+=150
                        else:
                            print("The boss dropped his Magic Hat")
                            md+=100
                            man+=1000
                    else:
                        print("You dealt" ,mrd, "damage")
                        if list1.count(10)>0 and rr==1:
                            print("Double Damage!")
                        print("Enemy has" ,ehp, "health")
                        print("Enemy attacks!")
                        hp-=ed
                        print("You are down to" ,hp, "health")
                        if hp<1:
                            print("You died")
def train():
    pass
def npc4():
    if random.randint(1,11) == 2 and list1.count(21)<1:
        print("Yo, could you help me?")
        print("Bring this parcel to my Friend which lives in the Village")
        print("I will compensate you accordingly")
        list1.append(21)
    elif random.randint(1,11) == 2 and list1.count(21)<1 and list1.count(22)>0:
        print("Bro thank you so much!")
        print("Those are my whole life savings, just for you!")
        c+=2500
def drawGrid():
    blockSize = 128
    for x in range(0, 640, blockSize):
        for y in range(0, 900, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, white, rect, 1)
def outofbounds():
    pygame.draw.rect(screen, red, pygame.Rect(30, 30, 68, 68))
    pygame.draw.rect(screen, red, pygame.Rect(30, 158, 68, 68))
    pygame.draw.rect(screen, red, pygame.Rect(30, 414, 68, 68))
    pygame.draw.rect(screen, red, pygame.Rect(158, 158, 68, 68))
    pygame.draw.rect(screen, red, pygame.Rect(414, 30, 68, 68))
    pygame.draw.rect(screen, red, pygame.Rect(542, 30, 68, 68))
    pygame.draw.rect(screen, red, pygame.Rect(414, 542, 68, 68))
    pygame.draw.rect(screen, red, pygame.Rect(542, 542, 68, 68))
    pygame.draw.rect(screen, red, pygame.Rect(542, 414, 68, 68))
    pygame.draw.rect(screen, red, pygame.Rect(542, 286, 68, 68))
def outofbounds2():
    pygame.draw.rect(screen, red, pygame.Rect(30, 158, 68, 68))
    pygame.draw.rect(screen, red, pygame.Rect(542, 30, 68, 68))
    pygame.draw.rect(screen, red, pygame.Rect(542, 158, 68, 68))
    pygame.draw.rect(screen, red, pygame.Rect(286, 30, 68, 68))
    pygame.draw.rect(screen, red, pygame.Rect(158, 414, 68, 68))
    pygame.draw.rect(screen, red, pygame.Rect(158, 542, 68, 68))
def outofbounds3():
    pygame.draw.rect(screen, red, pygame.Rect(30, 158, 68, 68))
    pygame.draw.rect(screen, red, pygame.Rect(30, 286, 68, 68))
    pygame.draw.rect(screen, red, pygame.Rect(30, 414, 68, 68))
    pygame.draw.rect(screen, red, pygame.Rect(30, 542, 68, 68))
    pygame.draw.rect(screen, red, pygame.Rect(158, 158, 68, 68))
    pygame.draw.rect(screen, red, pygame.Rect(286, 414, 68, 68))
    pygame.draw.rect(screen, red, pygame.Rect(542, 286, 68, 68))
    pygame.draw.rect(screen, red, pygame.Rect(542, 542, 68, 68))


    font = pygame.font.SysFont("Ancient Modern Tales", 68)
    txtsurf = font.render("B", True, white)
    screen.blit(txtsurf,(60 - txtsurf.get_width() // 2, 585 - txtsurf.get_height() // 2))
    txtsurf = font.render("C", True, white)
    screen.blit(txtsurf,(321 - txtsurf.get_width() // 2, 455 - txtsurf.get_height() // 2))
    txtsurf = font.render("S", True, white)
    screen.blit(txtsurf,(450 - txtsurf.get_width() // 2, 200 - txtsurf.get_height() // 2))
    txtsurf = font.render("O", True, white)
    screen.blit(txtsurf,(195 - txtsurf.get_width() // 2, 70 - txtsurf.get_height() // 2))
def specialsq():
    font = pygame.font.SysFont("Ancient Modern Tales", 68)
    txtsurf = font.render("B", True, white)
    screen.blit(txtsurf,(60 - txtsurf.get_width() // 2, 585 - txtsurf.get_height() // 2))
    txtsurf = font.render("C", True, white)
    screen.blit(txtsurf,(321 - txtsurf.get_width() // 2, 455 - txtsurf.get_height() // 2))
    txtsurf = font.render("S", True, white)
    screen.blit(txtsurf,(450 - txtsurf.get_width() // 2, 200 - txtsurf.get_height() // 2))
    txtsurf = font.render("O", True, white)
    screen.blit(txtsurf,(195 - txtsurf.get_width() // 2, 70 - txtsurf.get_height() // 2))
def specialsq2():
    font = pygame.font.SysFont("Ancient Modern Tales", 68)
    txtsurf = font.render("B", True, white)
    screen.blit(txtsurf,(580 - txtsurf.get_width() // 2, 330 - txtsurf.get_height() // 2))
    txtsurf = font.render("C", True, white)
    screen.blit(txtsurf,(450 - txtsurf.get_width() // 2, 70 - txtsurf.get_height() // 2))
    txtsurf = font.render("S", True, white)
    screen.blit(txtsurf,(320 - txtsurf.get_width() // 2, 330 - txtsurf.get_height() // 2))
    txtsurf = font.render("O", True, white)
    screen.blit(txtsurf,(60 - txtsurf.get_width() // 2, 330 - txtsurf.get_height() // 2))
    txtsurf = font.render("G", True, white)
    screen.blit(txtsurf,(320 - txtsurf.get_width() // 2, 590 - txtsurf.get_height() // 2))
def specialsq3():
    font = pygame.font.SysFont("Ancient Modern Tales", 68)
    txtsurf = font.render("B", True, white)
    screen.blit(txtsurf,(60 - txtsurf.get_width() // 2, 70 - txtsurf.get_height() // 2))
    txtsurf = font.render("S", True, white)
    screen.blit(txtsurf,(450 - txtsurf.get_width() // 2, 70 - txtsurf.get_height() // 2))
    txtsurf = font.render("S", True, white)
    screen.blit(txtsurf,(320 - txtsurf.get_width() // 2, 330 - txtsurf.get_height() // 2))
    txtsurf = font.render("B", True, white)
    screen.blit(txtsurf,(580 - txtsurf.get_width() // 2, 460 - txtsurf.get_height() // 2))
    txtsurf = font.render("T", True, white)
    screen.blit(txtsurf,(320 - txtsurf.get_width() // 2, 590 - txtsurf.get_height() // 2))

screen.fill(pygame.Color("black"))
txtsurf = font.render("Welcome to Python RPG", True, red)
screen.blit(txtsurf, txtsurf.get_rect(center = screen.get_rect().center))
pygame.display.update()
pygame.time.delay(500)
screen.fill(pygame.Color("black"))
pygame.display.update()
pygame.time.delay(250)
txtsurf = font.render("Welcome to Python RPG", True, red)
screen.blit(txtsurf, txtsurf.get_rect(center = screen.get_rect().center))
pygame.display.update()
pygame.time.delay(750)
refresh()
while hp>0:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            mov+=1
            rect=pygame.Rect(x1, y1, z1, a1)
            if event.key == pygame.K_LEFT:
                rwe -= 1
                x1-=dist
                refresh()
            elif event.key == pygame.K_RIGHT:
                rwe += 1
                x1+=dist
                refresh()
            elif event.key == pygame.K_UP:
                rns+=1
                y1-=dist
                refresh()
            elif event.key == pygame.K_DOWN:
                rns-=1
                y1+=dist
                refresh()
            elif event.key == pygame.K_o:
                chest1()
                chest2()
                case1()
                cho+=1
                pass
            elif event.key == pygame.K_RETURN:
                if rns == 2 and rwe == -1 and list1.count(1)>0:
                    print("You have reached the Overground")
                    print("Beware, enemies here are WAY harder to defeat")
                    rns +=8
                    rwe +=11
                elif rns == 10 and rwe == 10 and len(inputs)<500:
                    print("You have returned to the Underground")
                    print("Beware, the ceiling seems to be unstable")
                    rns -=8
                    rwe -=11
                elif rns == 2 and rwe == -1 and list1.count(1)==0:
                    print("You are missing the Overground key, which is required to unlock this door")
                elif rns == 10 and rwe == 10 and len(inputs)>500:
                    print("Rubble is blocking the entrance")
                elif rns == 10 and rwe == 12 and (csh>25 or list1.count(11)>0):
                    if list1.count(11)==0:
                        csh-=25
                        rwe+=5
                elif rns == 10 and rwe == 17 and (csh>25 or list1.count(11)>0):
                    if list1.count(11)==0:
                        csh-=25
                        rwe-=5
                else:
                    pass
            elif event.key == pygame.K_i:
                mov-=1
                txtsurf = font.render("Magic Damage: " + str(md), True, white)
                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
                txtsurf = font.render("Attack Damage: " + str(d) , True, white)
                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 436- txtsurf.get_height() // 2))
                txtsurf = font.render("Lootboxes opened: " + str(cho) , True, white)
                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 472- txtsurf.get_height() // 2))
                txtsurf = font.render("Moves Done: " + str(mov), True, white)
                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 508 - txtsurf.get_height() // 2))
                txtsurf = font.render("Items: " + str(list1), True, white)
                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 544 - txtsurf.get_height() // 2))
                txtsurf = font.render("Mana: " + str(man) , True, white)
                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 580- txtsurf.get_height() // 2))
                txtsurf = font.render("HP: " + str(hp) , True, white)
                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 364- txtsurf.get_height() // 2))
                txtsurf = font.render("Money: " + str(csh), True, white)
                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 328 - txtsurf.get_height() // 2))
                pygame.display.flip()
                continue
            if mov==450 and rns<5:
                print("You hear a loud cracking noise")
            if mov==500 and rns<5:
                print("The ceiling cracks and falls on you")
                print("You died")
                break
            if rns == -1 and rwe == 0:
                font = pygame.font.SysFont("Ancient Modern Tales", 36)
                txtsurf = font.render("Chest Room", True, white)
                screen.blit(txtsurf,(770 - txtsurf.get_width() // 2, 625 - txtsurf.get_height() // 2))
                pygame.display.flip()
                #these 3 things could be optimised (list)
            if rns == 1 and rwe == 0:
                font = pygame.font.SysFont("Ancient Modern Tales", 36)
                txtsurf = font.render("Main Hall", True, white)
                screen.blit(txtsurf,(760 - txtsurf.get_width() // 2, 620 - txtsurf.get_height() // 2))
                pygame.display.flip()
                enemy1()
            if rns == 2 and rwe == 0:
                txtsurf = font.render("Caverns", True, white)
                screen.blit(txtsurf,(760 - txtsurf.get_width() // 2, 620 - txtsurf.get_height() // 2))
                pygame.display.flip()
                enemy1()
                enemy2()
            if rns == 0 and rwe == 0:
                font = pygame.font.SysFont("Ancient Modern Tales", 36)
                txtsurf = font.render("Lobby", True, white)
                screen.blit(txtsurf,(760 - txtsurf.get_width() // 2, 620 - txtsurf.get_height() // 2))
                pygame.display.flip()
            if rns == -2 and rwe == 0:
                txtsurf = font.render("Ruin Entrance", True, white)
                screen.blit(txtsurf,(760 - txtsurf.get_width() // 2, 620 - txtsurf.get_height() // 2))
                pygame.display.flip()
                enemy2()
            if rns == -2 and rwe == -1:
                txtsurf = font.render("Ruins", True, white)
                screen.blit(txtsurf,(760 - txtsurf.get_width() // 2, 620 - txtsurf.get_height() // 2))
                pygame.display.flip()
                enemy2()
                npc2()
            if rns == -2 and rwe == -2:
                txtsurf = font.render("Boss room", True, white)
                screen.blit(txtsurf,(760 - txtsurf.get_width() // 2, 620 - txtsurf.get_height() // 2))
                pygame.display.flip()
                boss1()
            if rns == 0 and rwe == 1:
                font = pygame.font.SysFont("Ancient Modern Tales", 36)
                txtsurf = font.render("Cliffside", True, white)
                screen.blit(txtsurf,(760 - txtsurf.get_width() // 2, 620 - txtsurf.get_height() // 2))
                pygame.display.flip()
                enemy1()
            if rns == 2 and rwe == -1:
                txtsurf = font.render("Overground Door", True, white)
                screen.blit(txtsurf,(760 - txtsurf.get_width() // 2, 620 - txtsurf.get_height() // 2))
                pygame.display.flip()
            if rns == -1 and rwe == -1:
                txtsurf = font.render("Winding Caves", True, white)
                screen.blit(txtsurf,(760 - txtsurf.get_width() // 2, 620 - txtsurf.get_height() // 2))
                pygame.display.flip()
                enemy2()
            if rns == 0 and rwe == -1:
                font = pygame.font.SysFont("Ancient Modern Tales", 36)
                txtsurf = font.render("Salt Cave", True, white)
                screen.blit(txtsurf,(760 - txtsurf.get_width() // 2, 620 - txtsurf.get_height() // 2))
                pygame.display.flip()
                enemy3()
            if rns == 0 and rwe == -2:
                txtsurf = font.render("Salt Castle", True, white)
                screen.blit(txtsurf,(760 - txtsurf.get_width() // 2, 620 - txtsurf.get_height() // 2))
                pygame.display.flip()
                enemysalt()
                csh+=5
            if rns == -1 and rwe == 1:
                txtsurf = font.render("Abandoned mine", True, white)
                screen.blit(txtsurf,(760 - txtsurf.get_width() // 2, 620 - txtsurf.get_height() // 2))
                pygame.display.flip()
                enemy1()
                npc1()
            if rns == 1 and rwe == 2:
                txtsurf = font.render("Shop Backdoor", True, white)
                screen.blit(txtsurf,(760 - txtsurf.get_width() // 2, 620 - txtsurf.get_height() // 2))
                pygame.display.flip()
                enemy3()
            if rns == 1 and rwe == 1:
                txtsurf = font.render("Shop", True, white)
                screen.blit(txtsurf,(760 - txtsurf.get_width() // 2, 620 - txtsurf.get_height() // 2))
                shop1(csh, hp, d, list1, md, man)
                csh, hp, d, list1, md, man = shop1(csh, hp, d, list1, md, man)
                pygame.display.flip()
            if rns == 10 and rwe == 10:
                print("Entering the Overground Door")
            if rns == 8 and rwe == 10:
                print("Entering the Slums")
                enemy13m()
            if rns == 9 and rwe == 10:
                print("Entering the Industry centre")
                enemy11()
            if rns == 12 and rwe == 10:
                print("Entering the Highway underpass")
                enemy14()
            if rns == 10 and rwe == 11:
                print("Entering the Main Avenue")
                enemy11()
            if rns == 10 and rwe == 12:
                print("Entering the Main Avenue Bus Stop")
            if rns == 11 and rwe == 11:
                print("Entering the Concert place")
                enemy12()
            if rns == 12 and rwe == 11:
                print("Entering the Confusing Roundabout")
                enemy11()
            if rns == 11 and rwe == 12:
                print("Entering the Apartments")
                enemy12()
            if rns == 9 and rwe == 12:
                print("Entering the Rich Estates")
                enemy13()
            if rns == 8 and rwe == 12:
                print("Entering the Casino")
            if rns == 8 and rwe == 13:
                print("Entering the Tourist Centre")
                enemy11()
                npc3()
            if rns == 9 and rwe == 13:
                print("Entering the Old town")
                enemy12()
            if rns == 10 and rwe == 13:
                print("Entering the Church of Saint Anne")
                enemy12m()
            if rns == 11 and rwe == 13:
                print("Entering the Fountain Square")
                enemy12()
            if rns == 12 and rwe == 13:
                print("Entering the Chest Estate")
            if rns == 10 and rwe == 14:
                print("Entering the Second Boss Room")
                boss2()
            if rns == 9 and rwe == 14:
                print("Entering the Sports Arena")
                enemy13()
            if rns == 8 and rwe == 14:
                print("Entering the Gym")
                enemy13()
            if rns == 10 and rwe == 17:
                print("Entering the Train Station Bus Stop")
            if rns == 12 and rwe == 15:
                print("Entering the Fishing Docks")
                mboss1()
            if rns == 12 and rwe == 16:
                print("Entering the Cargo Port")
                enemy13()
            if rns == 12 and rwe == 17:
                print("Entering the Harbor")
                enemy12m()
            if rns == 12 and rwe == 18:
                print("Entering the Shopping Mall")
                shop2()
            if rns == 11 and rwe == 19:
                print("Entering the Construction area")
                enemy13()
            if rns == 11 and rwe == 18:
                print("Entering the Workers Plaza")
                enemy12m()
            if rns == 11 and rwe == 17:
                print("Entering the Opera House")
                enemy11()
            if rns == 10 and rwe == 18:
                print("Entering the Suspiciously Dark set of Apartments")
                enemy13()
                npc4()
            if rns == 10 and rwe == 16:
                print("Entering the IT Cluster")
                enemy12m()
            if rns == 9 and rwe == 18:
                print("Entering the Suburbs")
                enemy11()
            if rns == 9 and rwe == 16:
                print("Entering the Unnecessarily large road")
                enemy12m()
            if rns == 9 and rwe == 19:
                print("Entering the Abandoned Estate")
                boss3()
            if rns == 8 and rwe == 16:
                print("Entering the Kebab Kiosk")
                enemy14()
            if rns == 8 and rwe == 17:
                print("Entering the Train Station")
                train()
            if rns == 8 and rwe == 18:
                print("Entering the Overly Confusing Junction")
                enemy13m()
            if rns==3 or rwe==3 or rwe==-3 or rns==-3 or (rns==-2 and rwe==1) or (rns!=1 and rwe==2) or (rns==1 and rwe==-1) or (rns==2 and rwe==1) or ((rns==-1 or rns==1 or rns==2)and rwe==-2) or rns == 13 or rns == 7 or rwe == 9 or rwe == 20 or (rns == 11 and rwe == 10) or ((rns == 9 or rns == 8) and rwe == 11) or (rns == 12 and rwe == 12) or ((rns == 11 or rns == 12) and rwe == 14) or (rwe == 15 and rns!=12) or (rwe == 16 and rns == 11) or (rns == 9 and rwe == 17) or ((rns == 10 or rns == 8) and rwe == 19):
                print("Out of bounds")
                hp-=1
                rect=pygame.Rect(x1, y1, z1, a1)
                if event.key == pygame.K_LEFT:
                    rwe += 1
                    x1+=dist
                    refresh()
                elif event.key == pygame.K_RIGHT:
                    rwe -= 1
                    x1-=dist
                    refresh()
                elif event.key == pygame.K_UP:
                    rns-=1
                    y1+=dist
                    refresh()
                elif event.key == pygame.K_DOWN:
                    rns+=1
                    y1-=dist
                    refresh()
                    specialsq()
                    pygame.draw.rect(screen, blue, pygame.Rect(x1, y1, z1, a1))
                    pygame.display.flip()
