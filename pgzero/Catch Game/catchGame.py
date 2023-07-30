from pgzrun import go
from random import randint

#bad obstacles
#add sounds
#game over screen

#screen
WIDTH = 800
HEIGHT = 600
MIDDLE = WIDTH / 2
BOTTOM = HEIGHT - 50

#player
player = Actor('bag')
player.midbottom = (MIDDLE, 515)

#ground
ground = Actor('ground')
ground.topleft = (0, 500) 

#sky
sky = Actor('sky')
sky.bottomleft = (0, HEIGHT - 100)

#obstacles
egg = Actor('egg')
egg.midtop = (MIDDLE, 0)

gold_egg = Actor('gold_egg')
gold_egg.x = -100

#logic variables (global)
score = 0 
drop_gold_egg = False
boost = 0

#draw stuff
def draw():
  screen.fill('#D0F4F7')
  screen.draw.text(f"SCORE: {score}", (10,10), color='black', fontsize=30, fontname='vmsb')
  sky.draw()
  ground.draw()
  player.draw()
  egg.draw()
  gold_egg.draw()
  
  
  
#this runs 60 times per second
def update():
  global score
  global drop_gold_egg
  global boost
  
  egg_speed = 3 + score / 5
  gold_egg_speed = egg_speed + 1
  player_speed = 2 + score / 6 + boost
  egg.y += egg_speed
  
  #gold egg
  if gold_egg.bottom >= 500:
    gold_egg.x = randint(50, WIDTH - 50)
    gold_egg.bottom = 0
    drop_gold_egg = False
    
  if score % 3 == 0:
    drop_gold_egg = True
  
  if drop_gold_egg:
    gold_egg.y += gold_egg_speed
  
  if gold_egg.colliderect(player):
    if gold_egg.bottom >= player.y - 10:
      score += 3
      gold_egg.bottom = 0
      gold_egg.x = randint(50, WIDTH - 50)
      boost += 1
      drop_gold_egg = False
    
  #check if egg hits the ground
  if egg.bottom >= 500:
    egg.bottom = 0
    egg.x = randint(50, WIDTH - 50)
  
  #check collision with the bag
  if egg.colliderect(player):
    #comparing y values
    if egg.bottom >= player.y - 10:
      score += 1
      egg.bottom = 0
      egg.x = randint(50, WIDTH - 50)
    # print(score)
  
  #movement
  if keyboard.a:
    player.x -= player_speed
  elif keyboard.d:
    player.x += player_speed
    
  #bound to edge of sceen
  if player.left < 0:
    player.left = 0
  if player.right > WIDTH:
    player.right = WIDTH
  
  


go() # has to be the last line