# Dots & Boxes
#
# Author: Luke Munro

import player

class Grid:
	def __init__(self, dim):
		""" Only square games allowed"""
		self.dim = dim 
		assert self.dim < 9, "Less than 10 please"
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

#------------------------------ Checks ----------------------------------

# Figure out errors for this 
	def valid_move(self, row, index): 
		if self.moves[row][index] == 1 or (row%2 == 0 and index > self.dim) or\
		 row%2 == 1 and index > self.dim+1 or row > self.dim*2+1: 
			return False
		return True

# ---------------------------- Scoring -----------------------------------

	def game_status(self):
		return (self.dim**2) != self.usedBoxes

	def update_scores(self, player):
		count = sum(self.check_boxes())
		if count != self.usedBoxes:
			player.plusOne()
			self.usedBoxes = count

	def get_boxes(self):
		boxes = []
		box_scores = []
		for i in range(0, self.dim*2, 2):
			# Go by rows
			for j in range(self.dim):
			# Each box
				boxes.append([self.moves[i][j], self.moves[i+1][j], \
				self.moves[i+1][j+1], self.moves[i+2][j]])
		return boxes

	def check_boxes(self):
		boxes = self.get_boxes()
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

		print "".join(buffer) 

# -------------------------- Data methods for AI ---------------------------
	
	def get_data(self, players):
		boxes = self.get_boxes()
# Experiement with what data to give the network
#		box_scores = self.check_boxes()
		scores = [players[0].getScore(), players[1].getScore()]
		return boxes + scores

# -------------------------- Player Class ----------------------------------
class Player:
	def __init__(self, name):
		self.name = name
		self.score = 0

	def getName(self):
		return self.name

	def getMove(self):
		move = raw_input("Input 2 numbers: Row then Column (ex. first vertical line would be 10): ")
		move = [int(x) for x in move]
		return move

	def plusOne(self):
		self.score += 1

	def getScore(self):
 		return self.score

def main():
	dim = int(input("Size of grid: "))
	g = Grid(dim)
	g.display_game()
	player1 = Player("Luke")
	player2 = Player("AI")
	players = [player1, player2]
	print player1.getName() + " starts\n"
	print "Game status - " + str(g.game_status()) + "\n"
	turns = 0
	while g.game_status():
		cPlayer = players[turns%2]
		check = cPlayer.getScore()
		print cPlayer.getName() + " your move"
		move = cPlayer.getMove()
		g.turn(move[0], move[1], cPlayer)
		g.display_game()
		print cPlayer.getName() + " your score is " + str(cPlayer.getScore())
		if check == cPlayer.getScore():
			turns += 1
	if player1.getScore() == player2.getScore():
		print "Tie"
	elif player1.getScore() > player2.getScore():
		print "Winner is " + player1.getName()
	else:
		print "Winner is " + player2.getName()



if __name__ == "__main__":
	main()
