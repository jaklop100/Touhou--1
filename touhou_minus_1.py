from cmu_graphics import *
import random
import math
#All sound effects are from this website: https://sfxr.me/
#All music tracks are from Mother 1 and are composed by Keiichi Suzuki and Hirokazu Tanaka.
#Tracks used: 
    #Roving Tank
    #Game Over
    #You Won
    
    
#constants
playerTime = 30
goodTime = 10
stageTime = 300
#Sounds
death = Sound("TouHou1_Music/09+-+MOTHER+-+Game+Over.mp3")
damage = Sound("TouHou1_Music/damage.wav")
hit = Sound("TouHou1_Music/hitHurt.wav")
backgroundMusic = Sound("TouHou1_Music/26+-+MOTHER+-+Roving+Tank.mp3") #"cmu://949828/44002809/03+-+MOTHER+-+Battle+with+a+Dangerous+Foe.mp3"
win = Sound("TouHou1_Music/08+-+MOTHER+-+You+Won.mp3")
backgroundMusic.play(loop = True)
app.musicCount = 1
#app stuff
app.winScreen = Label('You Win!', 200, 200, size = 40, fill = 'white')
app.loseScreen = Label('You died!', 200, 200, size = 40, fill = 'darkRed')
app.backdrop = Rect(0, 0, 400, 400, fill = 'black')
#boss
app.boss = Group(
    Circle(200, 100, 30, fill = gradient("black", "indigo", "black")),
    Circle(200, 100, 20, fill = gradient("white", "black")),
    Circle(200, 100, 9, fill = gradient("red", "darkRed")),
    Circle(200, 100, 4))

app.boss.location = 200
app.bossHP = Label(100, 50, 50, size = 30, fill = 'darkRed')
#bullets
app.bulletsD = Group()
app.bulletsD.speed = 7
app.bulletsD.time = 5
app.bulletsD.timer = app.bulletsD.time
app.bulletsC = Group()
app.bulletsC.speed = 5
app.bulletsC.time = 3
app.bulletsC.timer = app.bulletsC.time
app.bulletsS = Group()
app.bulletsS.speed = 5
app.bulletsS.time = 30
app.bulletsS.timer = 0
app.bulletsSb = Group()
app.bulletsSb.timer = 15
app.Scounter = 0
app.change = 0
#player
app.hitBox = Circle(200, 300, 4, fill = 'darkRed', opacity = 0)
app.player = Group(Star(200, 300, 15, 4, fill = gradient("lightBlue", "midnightBlue")), app.hitBox)
app.playerSpeed = 7
app.player.hp = [Circle(325, 375, 10, fill = gradient("lightBlue", "midnightBlue")), Circle(350, 375, 10, fill = gradient("lightBlue", "midnightBlue")), 
Circle(375, 375, 10, fill = gradient("lightBlue", "midnightBlue"))]
app.playerCooldown = playerTime
app.goodBullets = Group()
app.goodTimer = goodTime
#stages
app.stageTimer = stageTime
app.stage = 2


#onKeyHold function
def onKeyHold(keys):
    if 'right' in keys or 'd' in keys:
        app.player.centerX += app.playerSpeed
    if 'left' in keys or 'a' in keys:
        app.player.centerX -= app.playerSpeed
    if 'up' in keys or 'w' in keys:
        app.player.centerY -= app.playerSpeed
    if 'down' in keys or 's' in keys:
        app.player.centerY += app.playerSpeed
    if 'z' in keys or 'j' in keys:
        if app.goodTimer <= 0:
            createBullet(3) 
    if 'x' in keys or 'k' in keys:
        app.playerSpeed = 5
        app.hitBox.opacity = 100
    elif not 'x' in keys or not 'k' in keys:
        app.playerSpeed = 7
        app.hitBox.opacity = 0
    
#Boss functions
def createBullet(style):
    if style == 1:
        bulletC = Circle(app.boss.centerX, app.boss.centerY, 5, fill = gradient("white", "red"))
        bulletC.time = 60
        bulletC.rotateAngle = randrange(180, 360)
        app.bulletsC.add(bulletC)
    if style == 2:
        bulletD = Polygon(app.boss.centerX, app.boss.centerY - 10, app.boss.centerX + 5, app.boss.centerY, app.boss.centerX, app.boss.centerY + 10,
        app.boss.centerX - 5, app.boss.centerY, fill = gradient("white", "indigo"))
        bulletD.time = 60
        bulletD.rotateAngle = angleTo(bulletD.centerX, bulletD.centerY, app.player.centerX, app.player.centerY)
        app.bulletsD.add(bulletD)
    if  style == 3:
        bulletP = Star(app.player.centerX, app.player.centerY, 8, 30, fill = gradient("white", "aquamarine", "darkBlue"))
        #Polygon(app.player.centerX, app.player.centerY - 8, app.player.centerX + 4, app.player.centerY, app.player.centerX, app.player.centerY + 8, app.player.centerX - 4, app.player.centerY)
        app.goodBullets.add(bulletP)
    if style == 4:
        angleList = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
        bulletS = Circle(app.boss.centerX, app.boss.centerY, 5, fill = gradient("white", "darkRed"))
        bulletS.rotateAngle = angleList[app.Scounter - 1] + app.change
        app.Scounter += 1
        if app.Scounter > 11:
            app.Scounter = 0
        app.bulletsS.add(bulletS)
    if style == 5:
        angleList = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
        bulletSb = Circle(app.boss.centerX, app.boss.centerY, 5, fill = gradient("white", "red"))
        bulletSb.rotateAngle = angleList[app.Scounter - 1] + app.change
        app.Scounter += 1
        if app.Scounter > 11:
            app.Scounter = 0
        app.bulletsSb.add(bulletSb)
    #attacks
def bossAttack(stage):
    #bullets
    if stage == 1:
        #movement
        if app.bulletsD.timer <= 0 and app.bossHP.value > 0:
            createBullet(1)
            createBullet(1)
            createBullet(1)
            createBullet(1)
        if app.bulletsS.timer <= 0 and app.bossHP.value > 0:
            createBullet(4)
            createBullet(4)
            createBullet(4)
            createBullet(4)
            createBullet(4)
            createBullet(4)
            createBullet(4)
            createBullet(4)
            createBullet(4)
            createBullet(4)
            createBullet(4)
            createBullet(4)
            app.change = random.randint(0, 360)
        if app.bulletsSb.timer <= 0 and app.bossHP.value > 0:
            createBullet(5)
            createBullet(5)
            createBullet(5)
            createBullet(5)
            createBullet(5)
            createBullet(5)
            createBullet(5)
            createBullet(5)
            createBullet(5)
            createBullet(5)
            createBullet(5)
            createBullet(5)
            app.change = random.randint(0, 360)
    for bullet in app.bulletsD.children:
        bullet.centerX += app.bulletsD.speed * math.sin(bullet.rotateAngle * (math.pi/180))
        bullet.centerY -= app.bulletsD.speed * math.cos(bullet.rotateAngle * (math.pi/180))
    if stage == 2:
        if app.bulletsC.timer <= 0 and app.bossHP.value > 0:
            createBullet(1)
            createBullet(1)
            createBullet(1)
            createBullet(1)
    for bullet in app.bulletsC.children:
        bullet.centerX += app.bulletsC.speed * math.cos(bullet.rotateAngle)
        bullet.centerY += app.bulletsC.speed * math.sin(bullet.rotateAngle)
    if stage == 3:
        if app.bulletsD.timer <= 0 and app.bossHP.value > 0:
            createBullet(2)
            createBullet(1)
            createBullet(1)
            createBullet(1)
            createBullet(1)
    if stage == 4:
        if app.bulletsS.timer <= 0 and app.bossHP.value > 0:
            createBullet(4)
            createBullet(4)
            createBullet(4)
            createBullet(4)
            createBullet(4)
            createBullet(4)
            createBullet(4)
            createBullet(4)
            createBullet(4)
            createBullet(4)
            createBullet(4)
            createBullet(4)
            app.change = random.randint(0, 360)
        if app.bulletsSb.timer <= 0 and app.bossHP.value > 0:
            createBullet(5)
            createBullet(5)
            createBullet(5)
            createBullet(5)
            createBullet(5)
            createBullet(5)
            createBullet(5)
            createBullet(5)
            createBullet(5)
            createBullet(5)
            createBullet(5)
            createBullet(5)
            app.change = random.randint(0, 360)
    for bullet in app.bulletsS.children:
        bullet.centerX += app.bulletsS.speed * math.sin(bullet.rotateAngle * (math.pi/180))
        bullet.centerY -= app.bulletsS.speed * math.cos(bullet.rotateAngle * (math.pi/180))
        bullet.rotate(1, app.boss.centerX, app.boss.centerY)
    for bullet in app.bulletsSb.children:
        bullet.centerX += app.bulletsS.speed * math.sin(bullet.rotateAngle * (math.pi/180))
        bullet.centerY -= app.bulletsS.speed * math.cos(bullet.rotateAngle * (math.pi/180))
        bullet.rotate(-1, app.boss.centerX, app.boss.centerY)
        
#onstep function
def onStep():
    #timers
    app.playerCooldown -= 1
    app.bulletsD.timer -= 1
    app.bulletsC.timer -= 1
    app.bulletsS.timer -= 1
    app.bulletsSb.timer -= 1
    if app.bulletsD.timer < 0:
        app.bulletsD.timer = app.bulletsD.time
    if app.bulletsC.timer < 0:
        app.bulletsC.timer = app.bulletsC.time
    if app.bulletsS.timer < 0:
        app.bulletsS.timer = app.bulletsS.time
    if app.bulletsSb.timer < 0:
        app.bulletsSb.timer = app.bulletsS.time
    #player bullets
    app.goodTimer -= 1
    if app.goodTimer < 0:
        app.goodTimer = goodTime
    for bullet in app.goodBullets.children:
        bullet.centerY -= app.playerSpeed
        if bullet.hitsShape(app.boss):
            bullet.visible = False
            if len(app.player.hp) > 0:
                hit.play()
            app.bossHP.value -= 1
            if app.bossHP.value < 0:
                app.bossHP.value = 0
    #stages
    stageList = [1, 2, 4]
    app.stageTimer -= 1
    if app.stageTimer <= 0 and app.bossHP.value > 25:
        app.stage += 1
        if app.stage >= 5:
            app.stage = 1
        app.stageTimer = stageTime
    if app.bossHP.value < 25:
        app.stage = 3
    bossAttack(app.stage)
    #despawn bullets
    for bullet in app.goodBullets.children:
        if bullet.hitsShape(app.backdrop) == False:
            bullet.visible = False
    for bullet in app.bulletsD.children:
        if bullet.hitsShape(app.backdrop) == False:
            bullet.visible = False
        bullet.time -= 1
        if bullet.hitsShape(app.hitBox) == True and app.bossHP.value > 0:
            bullet.visible = False
            if app.playerCooldown < 0 and len(app.player.hp) > 0:
                    damage.play()
                    app.player.hp.pop().visible = False
                    app.player.centerX = 200
                    app.player.centerY = 300
                    app.playerCooldown = playerTime
    for bullet in app.bulletsC.children:
        if bullet.hitsShape(app.backdrop) == False:
            bullet.visible = False
        if bullet.hitsShape(app.hitBox) == True and app.bossHP.value > 0:
            bullet.visible = False
            if app.playerCooldown < 0 and len(app.player.hp) > 0:
                    damage.play()
                    app.player.hp.pop().visible = False
                    app.player.centerX = 200
                    app.player.centerY = 300
                    app.playerCooldown = playerTime
    for bullet in app.bulletsS.children:
        if bullet.hitsShape(app.backdrop) == False:
            bullet.visible = False
        if bullet.hitsShape(app.hitBox) == True and app.bossHP.value > 0:
            bullet.visible = False
            if app.playerCooldown < 0 and len(app.player.hp) > 0:
                    damage.play()
                    app.player.hp.pop().visible = False
                    app.player.centerX = 200
                    app.player.centerY = 300
                    app.playerCooldown = playerTime
    for bullet in app.bulletsSb.children:
        if bullet.hitsShape(app.backdrop) == False:
            bullet.visible = False
        if bullet.hitsShape(app.hitBox) == True and app.bossHP.value > 0:
            bullet.visible = False
            if app.playerCooldown < 0 and len(app.player.hp) > 0:
                    damage.play()
                    app.player.hp.pop().visible = False
                    app.player.centerX = 200
                    app.player.centerY = 300
                    app.playerCooldown = playerTime
    #death
    if len(app.player.hp) == 0:
        #music
        app.musicCount -= 1
        if app.musicCount == 0:
            backgroundMusic.pause()
            death.play()
        #other
        app.backdrop.fill = 'black'
        app.backdrop.toFront()
        app.boss.toFront()
        app.loseScreen.toFront()
    #win
    if app.bossHP.value <= 0:
        #music
        app.musicCount -= 1
        if app.musicCount == 0:
            backgroundMusic.pause()
            win.play()
        app.boss.centerY += 1
        if app.boss.opacity > 0:
            app.boss.opacity -= 2
        if len(app.bulletsC) > 0:
            if app.bulletsC.opacity > 0:
                app.bulletsC.opacity -= 2
        if len(app.bulletsD) > 0:
            if app.bulletsD.opacity > 0:
                app.bulletsD.opacity -= 2
        if len(app.bulletsS) > 0:
            if app.bulletsS.opacity > 0:
                app.bulletsS.opacity -= 2
        if len(app.bulletsSb) > 0:
            if app.bulletsSb.opacity > 0:
                app.bulletsSb.opacity -= 2
        if app.boss.opacity <= 1:
            app.winScreen.toFront()
cmu_graphics.run()
