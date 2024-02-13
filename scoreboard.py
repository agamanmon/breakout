from turtle import Turtle


class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.penup()
		self.hideturtle()
		self.score = 0
		self.lives = 5
		self.color('white')
		self.update_scoreboard()

	def update_scoreboard(self):
		self.clear()
		self.goto(-250, 255)
		self.write(f'Score: {self.score}', align = 'center', font=("Courier", 40, "normal"))
		self.goto(200, 255)
		self.write(f'Lives: {self.lives}', align = 'center', font = ("Courier", 40, "normal"))

	def point(self):
		self.score += 1
		self.update_scoreboard()

	def death(self):
		self.lives -= 1
		self.update_scoreboard()

	def final_score(self):
		self.goto(0, 0)
		self.write(f'Your final score is: {self.score}', align='center', font=('Courier', 35, 'normal'))
