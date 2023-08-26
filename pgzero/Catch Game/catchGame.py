from pgzrun import go
from random import randint

WIDTH = 800
HEIGHT = 600
MIDDLE = WIDTH / 2
BOTTOM = HEIGHT - 100


# Actors
rots = []
for i in range(5):
    r = Actor("monster")

    rots.append(r)
    r.x = randint(0, 800)
    r.y = 0
# hearts = []
# for i in range(5):
#     heart = Actor("heart")
#     hearts.append(heart)
#     heart.x = 550 + i * 50
#     heart.y = 550

player = Actor("bag")
player.midbottom = (MIDDLE, 500)
egg = Actor("egg")
egg.midtop = (MIDDLE, 0)
ground = Actor("ground")
ground.y = 570
sky = Actor("sky")
sky.bottomleft = (0, HEIGHT - 100)
rotton_egg = Actor("monster")

gold_egg = Actor("gold_egg")
gold_egg.x = -100

# usefull variables
lives = 5
player_speed = 3
egg_speed = 3
score = 0
gold_egg_speed = egg_speed * 1.25
drop_gold_egg = False
boost = 0
has_played = False
drop_eggs = False


def moveToTop(obs):
    obs.x = randint(50, WIDTH - 50)
    obs.bottom = 0


def isTouchingGround(obs):
    # this is either true or false depending on the location of the egg
    return obs.bottom >= 500


def isTouchPlayer(obs):
    global player
    if obs.colliderect(player):
        if obs.bottom >= player.y - 10:
            moveToTop(obs)
            return True
    else:
        return False


def game_over():
    if len(hearts) == 0:
        return True

    else:
        return False


# draw stuff
def draw():
    if game_over():
        screen.fill("black")
        screen.draw.text(
            "Game Over!",
            (MIDDLE, MIDDLE),
            color="red",
            fontsize=30,
            fontname="fancy_bold",
        )
    else:
        screen.fill("#D0F4F7")
        screen.draw.text(
            f"Score: {score}",
            (10, 10),
            color="black",
            fontsize=30,
            fontname="fancy_bold",
        )
        sky.draw()
        ground.draw()
        player.draw()
        egg.draw()
        rotton_egg.draw()
        gold_egg.draw()

        # for heart in hearts:
        #     heart.draw()

        for r in rots:
            r.draw()


# THIS RUNS 60 TIMES PER SECOND


def update():
    global score
    global drop_gold_egg
    global boost
    global has_played
    global drop_eggs

    if not has_played and game_over():
        sounds.lose1.play()
        has_played = True

    rand = randint(1, 1000)
    egg_speed = 2 + score / 5
    gold_egg_speed = egg_speed + 1
    player_speed = 2 + score / 6 + boost
    egg.y += egg_speed
    rotton_egg.y += egg_speed + 1
    for r in rots:
        if score % 5 == 0:
            drop_eggs = True
            if drop_eggs:
                r.y += 3
        if isTouchingGround(r):
            moveToTop(r)
            drop_eggs = False
    if rand < 10:
        drop_gold_egg = True

    if drop_gold_egg:
        gold_egg.y += gold_egg_speed

    if isTouchingGround(egg):
        moveToTop(egg)

    if isTouchingGround(rotton_egg):
        moveToTop(rotton_egg)

    if isTouchingGround(gold_egg):
        moveToTop(gold_egg)
        drop_gold_egg = False

    if isTouchPlayer(gold_egg):
        score += 3
        boost += 2
        drop_gold_egg = False

    if isTouchPlayer(egg):
        score += 1

    if isTouchPlayer(rotton_egg) and len(hearts) > 0:
        hearts.remove(hearts[0])
    # movement
    if keyboard.Left:
        player.x -= player_speed
    elif keyboard.Right:
        player.x += player_speed
    # bound to screen
    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH


go()  # has to be the last line
