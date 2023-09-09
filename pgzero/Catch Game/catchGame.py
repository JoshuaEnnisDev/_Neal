from pgzrun import go
from random import randint

WIDTH = 800
HEIGHT = 600
MIDDLE = WIDTH / 2
BOTTOM = HEIGHT - 100

rots = []
for _ in range(10):
    r = Actor("monster")
    r.drop = False
    r.speed = randint(3, 7)
    r.x = randint(0, 800)
    r.bottom = 0
    rots.append(r)

hearts = []
for i in range(1):
    heart = Actor("ommlete")
    hearts.append(heart)
    heart.x = 550 + i * 50
    heart.y = 550

# Actors
ground = Actor("ground")
ground.y = 570

sky = Actor("sky")
sky.bottomleft = (0, HEIGHT - 100)

player = Actor("bag")
player.midbottom = (MIDDLE, 500)
player.speed = 3
player.score = 0
player.boost = 0
player.last_multiple = player.score

egg = Actor("egg")
egg.midtop = (MIDDLE, 0)
egg.speed = 3

rotten_egg = Actor("monster")
rotten_egg.speed = egg.speed + 1

gold_egg = Actor("gold_egg")
gold_egg.x = -100
gold_egg.speed = 4
gold_egg.drop = False

# global variables
has_played = False


def handle_gold_egg():
    rand = randint(1, 1000)
    if rand < 10:
        gold_egg.drop = True

    gold_egg.speed = egg.speed + 1
    if gold_egg.drop:
        gold_egg.y += gold_egg.speed

    if isTouchingGround(gold_egg):
        moveToTop(gold_egg)
        gold_egg.drop = False

    if isTouchPlayer(gold_egg):
        player.score += 3
        player.boost += 2
        gold_egg.drop = False


def handle_egg():
    egg.speed = 2 + player.score / 5
    egg.y += egg.speed
    if isTouchingGround(egg):
        moveToTop(egg)
    if isTouchPlayer(egg):
        player.score += 1


def handle_rotten_egg():
    rotten_egg.y += egg.speed
    if isTouchPlayer(rotten_egg):
        lose_life()
    if isTouchingGround(rotten_egg):
        moveToTop(rotten_egg)


def lose_life():
    if len(hearts) > 0:
        hearts.remove(hearts[0])


def drop_eggs():
    for r in rots:
        r.drop = True


def handle_rotten_eggs():
    for r in rots:
        if r.drop:
            r.y += r.speed

        if isTouchingGround(r):
            moveToTop(r)
            r.drop = False

        if isTouchPlayer(r):
            lose_life()
            r.drop = False

    if player.last_multiple != player.score:
        if player.score % 5 == 0:
            player.last_multiple = player.score
            drop_eggs()


def draw_list(list):
    for item in list:
        item.draw()


def moveToTop(obs):
    obs.x = randint(50, WIDTH - 50)
    obs.bottom = 0


def isTouchingGround(obs):
    # this is either true or false depending on the location of the egg
    return obs.bottom >= 500


def isTouchPlayer(obs):
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


def move_player():
    player.speed = 2 + player.score / 6 + player.boost
    if keyboard.Left:
        player.x -= player.speed
    elif keyboard.Right:
        player.x += player.speed


def bound_player():
    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH


def play_lose_sound(has_played):
    if has_played:
        return
    elif game_over() and not has_played:
        sounds.lose1.play()
        has_played = True


def draw():
    if game_over():
        screen.fill("black")
        screen.draw.text(
            "Game Over!",
            (MIDDLE, MIDDLE),
            color="red",
            fontsize=30,
            fontname="vmsb",
        )
    else:
        screen.fill("#D0F4F7")

        sky.draw()
        ground.draw()
        player.draw()
        egg.draw()
        rotten_egg.draw()
        gold_egg.draw()
        screen.draw.text(
            f"Score: {player.score}",
            (25, 550),
            color="black",
            fontsize=30,
            fontname="vmsb",
        )

        draw_list(hearts)
        draw_list(rots)


def update():
    # play_lose_sound()
    game_over()
    move_player()
    bound_player()
    handle_gold_egg()
    handle_rotten_egg()
    handle_rotten_eggs()
    handle_egg()
    # play_lose_sound()


go()
