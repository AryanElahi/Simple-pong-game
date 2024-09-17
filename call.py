import turtle
import time

# Create screen
sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("black")
sc.setup(width=1000, height=600)

# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("red")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(20)
right_pad.shape("square")
right_pad.color("aqua")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

# Ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(1000)  # تنظیم سرعت برگشت توپ 
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# Initialize the score
left_player = 0
right_player = 0

# Displays the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("aqua")
sketch.penup()
sketch.hideturtle()
sketch.goto(200, 260)
sketch.write( "Left_player: 0",
             align="left", font=("Courier", -24, "normal"))

# Displays the score
sketche = turtle.Turtle()
sketche.speed(0)
sketche.color("red")
sketche.penup()
sketche.hideturtle()
sketche.goto(-200, 260)
sketche.write( "Right_player: 0",
             align="right", font=("Courier", 24, "normal"))

# Functions to move paddles


def paddleaup():
    y = left_pad.ycor()
    if y < 250:  # Limit paddle movement
        y += 20
        left_pad.sety(y)


def paddleadown():
    y = left_pad.ycor()
    if y > -240:  # Limit paddle movement
        y -= 20
        left_pad.sety(y)


def paddlebup():
    y = right_pad.ycor()
    if y < 250:  # Limit paddle movement
        y += 20
        right_pad.sety(y)


def paddlebdown():
    y = right_pad.ycor()
    if y > -240:  # Limit paddle movement
        y -= 20
        right_pad.sety(y)


# Keyboard bindings
sc.listen()
sc.onkeypress(paddleaup, "w")  # Changed to 'w'
sc.onkeypress(paddleadown, "s")  # Changed to 's'
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")

# Main game loop
while True:
    sc.update()
    time.sleep(0.00000000000000001)  # Add delay to make game smoother

    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # Checking borders
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1

    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        sketche.clear()
        sketche.write("left_player : {}".format(
            left_player), align="left",
            font=("Courier", 24, "normal"))
        sketche.clear()
        sketche.write("right_player : {}".format(
            right_player), align="Right",
            font=("Courier", 24, "normal"))
    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("right_player : {}".format(
            right_player), align="Right",
            font=("Courier", 24, "normal"))
        sketch.clear()
        sketch.write("left_player : {}".format(
            left_player), align="left",
            font=("Courier", 24, "normal"))

    # Paddle ball collision
    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and \
            (hit_ball.ycor() < right_pad.ycor() + 50 and hit_ball.ycor() > right_pad.ycor() - 50):
        hit_ball.setx(360)
        hit_ball.dx *= -1

    if (hit_ball.xcor() < -360 and hit_ball.xcor() > -370) and \
            (hit_ball.ycor() < left_pad.ycor() + 50 and hit_ball.ycor() > left_pad.ycor() - 50):
        hit_ball.setx(-360)
        hit_ball.dx *= -1