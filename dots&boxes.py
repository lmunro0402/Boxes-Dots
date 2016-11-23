# Dots & Boxes
#
# Author: Luke Munro

class Grid:
	def __init__(self, dim):
		""" Only square games allowed"""
		self.dim = dim 
		self.player = 0
		self.usedBoxes = 0
		self.moves = []
		for i in range(self.dim):
			self.moves.append([0]*dim)
			self.moves.append([0]*(dim+1))
		self.moves.append([0]*dim)

	def turn(self, row, index, player):
		self.move(row, index)
		self.update_scores(player)


	def move(self, row, index):
		self.moves[row][index] = 1
		self.player += 1

#	def validMove(self, row, index): #uneeded 

# ---------------------------- Scoring -----------------------------------

	def game_status(self):
		return (self.dim**2) != self.usedBoxes

	def update_scores(self, player):
		count = sum(self.check_boxs)
		if count != self.usedBoxes:
			player.plusOne()
			self.usedBoxes = count

	def check_boxs(self, player):
		boxes = []
		box_scores = []
		for i in range(0, self.dim*2, 2):
			# Go by rows
			for j in range(self.dim):
			# Each box
				boxes.append([self.moves[i][j], self.moves[i+1][j], \
				self.moves[i+1][j+1], self.moves[i+2][j]])
		box_scores = [sum(x)//4 for x in boxes]
		return box_scores

# ------------------------- Display methods --------------------------------

	def display_moves(self):
		return self.moves

	def display_game(self):
		buffer = [] #buffer? what is this
		hLine = "+---"
		hEmpty = "+   "
		vLine = "|   "
		vEmpty = "    "
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
	print g.game_status()
	while g.game_status():
		line = raw_input("Input 2 numbers: Row then Column (ex. first vertical line would be 10): ")
		line = [int(x) for x in line]
		
	g.move(0, 1)
	print g.display_moves()
	print g.display_game()
	print g.check_boxs("me")

if __name__ == "__main__":
	main()
