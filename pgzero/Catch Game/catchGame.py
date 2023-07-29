from pgzrun import go
from random import randint




#bad obstacles
#add sounds
#add fonts
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

#logic variables (global)
player_speed = 4
egg_speed = 3
score = 0 

#draw stuff
def draw():
  screen.fill('#D0F4F7')
  screen.draw.text(f"SCORE: {score}", (10,10), color='black', fontsize=30, fontname='vmsb')
  sky.draw()
  ground.draw()
  player.draw()
  egg.draw()
  
  
  
#this runs 60 times per second
def update():
  global score
  egg_speed = 3 + score / 5
  player_speed = 2 + score / 6
  egg.y += egg_speed
  
  #check if egg hits the ground
  if egg.bottom >= 500:
    print(egg_speed)
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