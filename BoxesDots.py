# Dots & Boxes
#
# Author: Luke Munro

import NN
import time
# -----------------------------------ADD MOVE DIAGRAM -----------------------

class Grid:
	def __init__(self, dim):
		""" Only square games allowed"""
		self.dim = dim 
		assert self.dim < 5, "Less than 5 please" # CHANGE COMMAND INPUT FOR BIGGER GAMES
		self.usedBoxes = 0
		self.moves = []
		for i in range(self.dim):
			self.moves.append([0]*dim)
			self.moves.append([0]*(dim+1))
		self.moves.append([0]*dim)

	def getDim(self):
		return self.dim

	def turn(self, row, index, player):
		if self.valid_move(row, index):
			self.move(row, index)
			self.update_scores(player)
		else:   
			# Recurse till valid move
			print "Invalid move"
			move = player.getMove()
			self.turn(move[0], move[1], player)



	def move(self, row, index):
		self.moves[row][index] = 1

#------------------------------ Checks ----------------------------------

# Figure out errors for this - works now but ehh
	def valid_move(self, row, index): 
		if (row%2 == 0 and index > self.dim-1) or\
		 (row%2 == 1 and index > self.dim) or (row > self.dim*2): 
			return False
		elif self.moves[row][index] == 1:
			return False
		return True

# ---------------------------- Scoring -----------------------------------

	def game_status(self):
		return (self.dim**2) != self.usedBoxes

	def update_scores(self, player): # THIS IS BUGGED sometimes need +2
		count = sum(self.check_boxes())
	#	print count
		if count != self.usedBoxes:
			diff = abs(self.usedBoxes-count)
			# self.display_game()
			# time.sleep(1)
			if diff == 1:
				player.plusOne()
			else:
				player.plusOne()
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
		moves = [i for x in self.moves for i in x]
		scores = [players[0].getScore(), players[1].getScore()]
		return str(moves + scores)

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
	train = int(input("How many games: "))
	for i in range(train):
		g = Grid(dim)
		player1 = Player("AI")
		name = raw_input("Player enter name: ")
		player2 = Player(name)
		players = [player1, player2]
		with open('data', 'w') as data:
			data.write(g.get_data(players))	
		aI = NN.Net(10, dim)
		val = input("1 for load weights 0 for no: ")
		if  val == 1:
			aI.loadWeights()
		print player1.getName() + " starts\n"
		g.display_game()
		turns = 0
		while g.game_status():
			cPlayer = players[turns%2]
			check = cPlayer.getScore()
			print cPlayer.getName() + " your move"
			if cPlayer.getName() == "AI":
				move = [int(x) for x in aI.getMove()] #change to fully internal no temp file
			else:
				move = cPlayer.getMove()
			print cPlayer.getName() + " move - " + str(move)
			g.turn(move[0], move[1], cPlayer)
			g.display_game()
			print cPlayer.getName() + " your score is " + str(cPlayer.getScore())
			if check == cPlayer.getScore():
				turns += 1
			with open('data', 'w') as data:
				data.write(g.get_data(players))

		print player1.getName() + " score is " + str(player1.getScore())
		print player2.getName() + " score is " + str(player2.getScore())
		if player1.getScore() == player2.getScore():
			print "Tie"
		elif player1.getScore() > player2.getScore():
			print "Winner is " + player1.getName()
		else:
			print "Winner is " + player2.getName()
		aI.writeWeights()





if __name__ == "__main__":
	main()
