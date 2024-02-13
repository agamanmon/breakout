from turtle import Screen
from paddle import Paddle
from ball import Ball
from blocks import Blocks
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width = 800, height = 600)
screen.title('Breakout')
screen.tracer(0)

paddle = Paddle((0, -275))
ball = Ball()
blocks = Blocks()
bricks_list = blocks.bricks_list
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

game_is_on = True
touches = 0
ball.goto(0, -100)
while game_is_on:
	screen.update()
	ball.move()

	# Detect collision with wall
	if ball.ycor() > 280:
		ball.bounce_y()

	if ball.xcor() > 380 or ball.xcor() < -380:
		ball.bounce_x()

	# Detect collision with paddle
	if ball.distance(paddle) < 50 and ball.ycor() < -255:
		ball.bounce_y()

	# Detect paddle miss
	if ball.distance(paddle) > 50 and ball.ycor() < -270:
		ball.reset_position()
		scoreboard.death()

	# Detect collision with brick
	for brick in bricks_list:
		if (brick.ycor() + 45 > ball.ycor() > brick.ycor() - 45) and \
			(brick.xcor() + 50 > ball.xcor() > brick.xcor() - 50):
			blocks.delete_brick(bricks_list.index(brick))
			ball.bounce_y()
			brick.clear()
			brick.hideturtle()
			scoreboard.point()
			touches += 1
			screen.update()

	if touches == 4:
		ball.speed_up()
		print(f'current speed: {ball.move_speed}')
		touches = 0

	# Detect end game:
	if scoreboard.lives == 0 or len(bricks_list) == 0:
		ball.hideturtle()
		screen.update()
		scoreboard.final_score()
		game_is_on = False

screen.exitonclick()
