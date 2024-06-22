from user import username, speed
import turtle
import random

window = turtle.Screen()
window.title("Avoid The Box")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Player
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("white")
player.penup()
player.goto(0, 0)

# Obstacle Boxes
boxRed = turtle.Turtle()
boxRed.speed(0)
boxRed.shape("square")
boxRed.shapesize(stretch_wid=2, stretch_len=2)
boxRed.color("red")
boxRed.penup()
boxRed.goto(-300, 0)
boxRed.dx = speed
boxRed.dy = speed

boxPurple = turtle.Turtle()
boxPurple.speed(0)
boxPurple.shape("square")
boxPurple.shapesize(stretch_wid=2, stretch_len=2)
boxPurple.color("purple")
boxPurple.penup()
boxPurple.goto(300, 0)
boxPurple.dx = speed
boxPurple.dy = speed

boxGreen = turtle.Turtle()
boxGreen.speed(0)
boxGreen.shape("square")
boxGreen.shapesize(stretch_wid=2, stretch_len=2)
boxGreen.color("green")
boxGreen.penup()
boxGreen.goto(0, -170)
boxGreen.dx = speed
boxGreen.dy = speed

# Scoring
score = 0

gold = turtle.Turtle()
gold.speed(0)
gold.shape("circle")
gold.color("yellow")
gold.penup()
gold.goto(random.uniform(-390, 390), random.uniform(-290, 290))

# Display user
user = turtle.Turtle()
user.speed(0)
user.color("white")
user.penup()
user.hideturtle()
user.goto(-390, 260)
user.write("Player: {}".format(username), align="left", font=('San Francisco', 24, "normal"))

# Display speed
userSpeed = turtle.Turtle()
userSpeed.speed(0)
userSpeed.color("white")
userSpeed.penup()
userSpeed.hideturtle()
userSpeed.goto(375, 263)
userSpeed.write("Speed: {}".format(speed), align="right", font=('San Francisco', 14, "normal"))

# Life
life = 3

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Life: 3      Score:", align="center", font=('San Francisco', 24, "normal"))


# Function
def player_up():
    y = player.ycor()
    y += 20
    player.sety(y)


def player_down():
    y = player.ycor()
    y -= 20
    player.sety(y)


def player_done():
    x = player.xcor()
    x += 20
    player.setx(x)


def player_left():
    x = player.xcor()
    x -= 20
    player.setx(x)


# Keyboard binding
window.listen()
window.onkeypress(player_up, 'Up')
window.onkeypress(player_down, 'Down')
window.onkeypress(player_done, 'Right')
window.onkeypress(player_left, 'Left')

collisionBoxRed = False
collisionBoxPurple = False
collisionBoxGreen = False
collisionGold = False

# Main game loop
while True:
    window.update()

    # Moving boxes
    boxRed.setx(boxRed.xcor() + boxRed.dx)
    boxRed.sety(boxRed.ycor() + boxRed.dy)

    boxPurple.setx(boxPurple.xcor() + boxPurple.dx)
    boxPurple.sety(boxPurple.ycor() + boxPurple.dy)

    boxGreen.setx(boxGreen.xcor() + boxGreen.dx)
    boxGreen.sety(boxGreen.ycor() + boxGreen.dy)

    # Border for red box
    if boxRed.ycor() > 290:
        boxRed.sety(290)
        boxRed.dy *= -1

    if boxRed.ycor() < -290:
        boxRed.sety(-290)
        boxRed.dy *= -1

    if boxRed.xcor() > 390:
        boxRed.setx(390)
        boxRed.dx *= -1

    if boxRed.xcor() < -390:
        boxRed.setx(-390)
        boxRed.dx *= -1

    # Border for purple box
    if boxPurple.ycor() > 290:
        boxPurple.sety(290)
        boxPurple.dy *= -1

    if boxPurple.ycor() < -290:
        boxPurple.sety(-290)
        boxPurple.dy *= -1

    if boxPurple.xcor() > 390:
        boxPurple.setx(390)
        boxPurple.dx *= -1

    if boxPurple.xcor() < -390:
        boxPurple.setx(-390)
        boxPurple.dx *= -1

    # Border for green box

    if boxGreen.ycor() > 290:
        boxGreen.sety(290)
        boxGreen.dy *= -1

    if boxGreen.ycor() < -290:
        boxGreen.sety(-290)
        boxGreen.dy *= -1

    if boxGreen.xcor() > 390:
        boxGreen.setx(390)
        boxGreen.dx *= -1

    if boxGreen.xcor() < -390:
        boxGreen.setx(-390)
        boxGreen.dx *= -1

    # Player collision with red box
    if abs(player.xcor() - boxRed.xcor()) < 20 and abs(
            player.ycor() - boxRed.ycor()) < 20 and not collisionBoxRed:
        print("Collision with Red Box!")
        collisionBoxRed = True
        life -= 1
        pen.clear()
        pen.write("Life: {} Score: {}".format(life, score), align="center", font=('San Francisco', 24, "normal"))

    # Player collision with purple box
    if abs(player.xcor() - boxPurple.xcor()) < 20 and abs(
            player.ycor() - boxPurple.ycor()) < 20 and not collisionBoxPurple:
        print("Collision with Purple Box!")
        collisionBoxPurple = True
        life -= 1
        pen.clear()
        pen.write("Life: {} Score: {}".format(life, score), align="center", font=('San Francisco', 24, "normal"))

    # Player collision with green box
    if abs(player.xcor() - boxGreen.xcor()) < 20 and abs(
            player.ycor() - boxGreen.ycor()) < 20 and not collisionBoxGreen:
        print("Collision with Green Box!")
        collisionBoxGreen = True
        life -= 1
        pen.clear()
        pen.write("Life: {} Score: {}".format(
            life, score), align="center", font=('San Francisco', 24, "normal"))

    # Player collision with gold
    if abs(player.xcor() - gold.xcor()) < 20 and abs(
            player.ycor() - gold.ycor()) < 20 and not collisionGold:
        print("+ 100 Score!")
        collisionGold = True
        score += 100
        gold.clear()
        gold.goto(random.uniform(-375, 375), random.uniform(-275, 275))
        pen.clear()
        pen.write("Life: {} Score: {}".format(life, score), align="center", font=('San Francisco', 24, "normal"))

    """
    if the Boxes is far enough it will reset itself for another collision to be recorded
    I did this instead because, without setting them as boolean True and false, whenever a collision happens
    it spams the record.
    """
    if (
            abs(player.xcor() - boxRed.xcor()) > 20 or abs(player.ycor() - boxRed.ycor()) > 20
    ) and collisionBoxRed:
        collisionBoxRed = False

    if (
            abs(player.xcor() - boxPurple.xcor()) > 20 or abs(player.ycor() - boxPurple.ycor()) > 20
    ) and collisionBoxPurple:
        collisionBoxPurple = False

    if (
            abs(player.xcor() - boxGreen.xcor()) > 20 or abs(player.ycor() - boxGreen.ycor()) > 20
    ) and collisionBoxGreen:
        collisionBoxGreen = False

    if (
            abs(player.xcor() - boxGreen.xcor()) > 20 or abs(player.ycor() - boxGreen.ycor()) > 20
    ) and collisionGold:
        collisionGold = False
    # Death messages
    if life == 0:
        penG = turtle.Turtle()
        penG.speed(0)
        penG.color("white")
        penG.penup()
        penG.hideturtle()
        penG.goto(0, 0)
        penG.write("Game Over", align="center", font=('San Francisco', 30, "bold"))

        penU = turtle.Turtle()
        penU.speed(0)
        penU.color("white")
        penU.penup()
        penU.hideturtle()
        penU.goto(0, -40)
        penU.write("Player: {}".format(username), align="center", font=('San Francisco', 24, "bold"))

        penScore = turtle.Turtle()
        penScore.speed(0)
        penScore.color("white")
        penScore.penup()
        penScore.hideturtle()
        penScore.goto(0, -75)
        penScore.write("Score: {}".format(score), align="center", font=('San Francisco', 24, "bold"))

        penSpeed = turtle.Turtle()
        penSpeed.speed(0)
        penSpeed.color("white")
        penSpeed.penup()
        penSpeed.hideturtle()
        penSpeed.goto(0, -105)
        penSpeed.write("Speed: {}".format(speed), align="center", font=('San Francisco', 17, "normal"))
