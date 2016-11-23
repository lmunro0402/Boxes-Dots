# Dots & Boxes
#
# Author: Luke Munro

class Grid:
	def __init__(self, dim):
		""" Only square games allowed"""
		self.dim = dim 
		self.player = 0
		self.moves = []
		self.moves.append([0]*dim)
		self.moves.append([0]*(dim+1))
		self.moves = self.moves*dim
		self.moves.append([0]*dim)

	def move(self, row, index):
		self.moves[row][index] = 1

	def check_boxs(self, player):
		for i in range(dim):
			for j in range(dim):
				count = self.moves[i][j] + [i+1]

	def display_moves(self):
		return self.moves

	def display_game(self):
		buffer = [] #buffer? what is this
		hLine = "+---"
		hEmpty = "+   "
		vLine = "|  "
		vEmpty = "   "
		# Top row
		for i in range(self.dim):
			if self.moves[0][i] == 1:
				buffer.append(hLine)
			else: buffer.append(hEmpty)
		buffer.append("+\n")

		# Middle rows
		for i in range(1, self.dim*2, 2):
			# Make horizontal passes
			for j in range(self.dim+1):
				if self.moves[i][j] ==  1:
					buffer.append(vLine)
				else: buffer.append(vEmpty)
			buffer.append("\n")

			# Vertical passes
			for j in range(self.dim):
				if self.moves[i+1][j] == 1:
					buffer.append(hLine)
				else: buffer.append(hEmpty)
			buffer.append("+\n")
		return "".join(buffer)



def main():
	g = Grid(2)
	print g.display_moves()
	print g.display_game()

if __name__ == "__main__":
	main()
