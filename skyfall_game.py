import turtle
import random
import time

score = 0
high_score = 0
lives = 5
# main window
window = turtle.Screen()
window.title("Skyfall game")
window.bgcolor("blue")
window.setup(height=600, width=600)
window.tracer(0)
# player setting
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("Yellow")
player.penup()
player.goto(0, -230)
player.direction = "stop"
# adding multiple good things
goods = []
# good things
for _ in range(20):
    good = turtle.Turtle()
    good.speed(0)
    good.shape("circle")
    good.color("green")
    good.penup()
    x = random.randint(-300, 300)
    y = random.randint(400, 500)
    good.goto(x, y)
    good.direction = "down"
    good.speed = random.randint(2, 5)
    goods.append(good)
# multiple bad things
bads = []
# bad things
for _ in range(20):
    bad = turtle.Turtle()
    bad.speed(0)
    bad.shape("circle")
    bad.color("red")
    bad.penup()
    x = random.randint(-300, 300)
    y = random.randint(300, 500)
    bad.goto(x, y)
    bad.direction = "down"
    bad.speed = random.randint(2, 5)
    bads.append(bad)

# score board
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High score : 0 Lives :5", align="center", font=("Courier", 20, "normal"))


# direction
def movement():
    if player.direction == "left":
        x = player.xcor()
        x -= 3
        player.setx(x)
    if player.direction == "right":
        x = player.xcor()
        x += 3
        player.setx(x)


# movement action
def go_right():
    player.direction = "right"


def go_left():
    player.direction = "left"


# key binding
window.listen()
window.onkeypress(go_right, "Right")
window.onkeypress(go_left, "Left")


# good guy movement
def good_guy():
    for good in goods:
        y = good.ycor()
        y -= good.speed
        good.sety(y)
        if y < -275:
            x = random.randint(-300, 300)
            y = random.randint(400, 500)
            good.goto(x, y)


# bad guy movement
def bad_guy():
    for bad in bads:
        y = bad.ycor()
        y -= bad.speed
        bad.sety(y)
        if y < -275:
            x = random.randint(-300, 300)
            y = random.randint(400, 500)
            bad.goto(x, y)


while True:
    window.update()
    movement()
    good_guy()
    bad_guy()
    # collision check
    for good in goods:
        if good.distance(player) < 20:
            x = random.randint(-300, 300)
            y = random.randint(300, 500)
            good.goto(x, y)
            # score
            score += 10
            if score > high_score:
                high_score = score
            pen.clear()
            pen.write("Score : {} High score : {} Lives :{}".format(score, high_score, lives), align="center",
                      font=("Courier", 20, "normal"))

    for bad in bads:
        if bad.distance(player) < 20:
            x = random.randint(-300, 300)
            y = random.randint(300, 500)
            bad.goto(x, y)
            score -= 10
            lives -= 1
            if lives <= 0:
                time.sleep(3)
                player.goto(0, -230)
                player.direction = "stop"
                score = 0
                lives = 5

            pen.clear()
            pen.write("Score : {} High score : {} Lives :{}".format(score, high_score, lives), align="center",
                      font=("Courier", 20, "normal"))

window.mainloop()
