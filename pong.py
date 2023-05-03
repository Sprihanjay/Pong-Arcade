import turtle

# Set up the game window
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=600, height=400)

# Create the game paddles
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-250, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(250, 0)

# Create the game ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = -3

# Create the score displays
score_a = 0
score_b = 0

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 170)
score_display.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 16, "normal"))

# Define the game functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Bind the game functions to the keyboard keys
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for top and bottom borders
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.dy *= -1

    # Check for left and right borders
    if ball.xcor() > 290:
        score_a += 1
        score_display.clear()
        score_display.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 16, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
    elif ball.xcor() < -290:
        score_b += 1
        score_display.clear()
        score_display.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 16, "normal"))
        ball.goto(0, 0)
        ball.dx = 1

    # Check for collision with paddles
    if (ball.dx > 0) and (250 < ball.xcor() + 10 < 260) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.dx *= -1
    elif (ball.dx < 0) and (-260 < ball.xcor() - 10 < -250) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.dx *= -1

    # Determine the winner
    winner = ""
    if score_a == 2:
        winner = "blue"
    elif score_b == 2:
        winner = "red"

    # Check if there is a winner
    if winner:
        print("{} wins!".format(winner))
        answer = input("Press 'c' to continue or any other key to terminate: ")
        if answer.lower() == "c":
            # Reset the game
            score_a = 0
            score_b = 0
            ball.goto(0, 0)
            paddle_a.goto(-250, 0)
            paddle_b.goto(250, 0)
            score_display.clear()
            score_display.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 16, "normal"))
        else:
            break

    # Update the game window
    wn.update()

# Exit the game window when clicked
wn.exitonclick()

