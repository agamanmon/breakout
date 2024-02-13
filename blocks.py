from turtle import Turtle


class Blocks(Turtle):

	def __init__(self):
		super().__init__()
		self.spacing = 65
		self.row_spacing = 30
		self.hideturtle()
		self.x_rows = 9
		self.y_rows = 5
		self.start_x = -350
		self.start_y = 230
		self.shapesize(stretch_wid = 2.5, stretch_len = 4)
		self.block_size = 21
		self.bricks_list = self.layout()

	def stamp_brick(self, row, column):
		brick = Turtle(shape = 'square')
		brick.color('#C156FC')
		brick.shapesize(stretch_wid = 2.5, stretch_len = 4)
		brick.penup()
		new_x = self.start_x + row * (self.block_size + self.spacing)
		new_y = self.start_y - column * (self.block_size + self.spacing) + column * self.row_spacing
		brick.goto(new_x, new_y)
		brick.stamp()
		return brick

	def layout(self):
		bricks_list = []
		for row in range(self.x_rows):
			for column in range(self.y_rows):
				brick = self.stamp_brick(row, column)
				bricks_list.append(brick)
		return bricks_list

	def delete_brick(self, index):
		del self.bricks_list[index]
