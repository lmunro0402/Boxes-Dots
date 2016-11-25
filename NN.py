# Neural Network
#
# Author: Luke Munro
from sigNeuron import *
import numpy as np

"""Neural net class for systems with ONE hidden layer, 
				eventually will work generically for more. """
class Net:
	def __init__(self, nodes, possibleMoves):
# ------ One Hidden Layer ------
# Nodes = # nodes in layer | sizeX = # data points | ouptuts = # possible ouptuts
		self.hidden = []
		self.nodes = nodes
		self.sizeX = possibleMoves + 3 # For bias and player scores 
		self.outs = []
		self.data = []
		for i in range(nodes):
			self.hidden.append(Neuron(1, i, self.sizeX, i))
		for i in range(possibleMoves): 
			self.outs.append(Neuron(2, i, self.nodes+1, i))  # +1 for bias


	def getNodes(self, layer):
# ------- will need to change for more layers ----------------------
		if layer == 1:
			return self.hidden
		elif layer == 2:
			return self.outs
		else:
			print "Fuck me if this gets printed"

	def getWeights(self, layer):
		layer1 = np.zeros(shape=(len(self.hidden), self.sizeX))
		layer2 = np.zeros(shape=(len(self.outs), len(self.hidden)+1)) # outs has weight for bias
		for i, node in enumerate(self.hidden):
			layer1[i] = node.getW()
		for i, node in enumerate(self.outs):
			layer2[i] = node.getW()
# ---------------------- Fix this when bored ------------------------------
		if layer == 1:
			return str(layer1.tolist())
		else:
			return str(layer2.tolist())




def getData():
	with open('data', 'r') as d:
		data = d.read()
	data = [[int(data[x])] for x in range(len(data)) if x%3==1]
	data = np.array(data)
# ------------ Add bias ----------------- maybe? yes
	return data 
		
def addBias(matrix):
# --------------- For hidden layer not a neuron just a 1 ----------------------------
	size = matrix.shape
	matrix = np.insert(matrix, 0, 1)
	return matrix


def forwardOne(Nodes, X):
	w = np.zeros(shape=(np.size(Nodes), np.size(X)))
#	print w.shape
	for i, node in enumerate(Nodes):
#		print node.getW()
		w[i] = node.getW()
	z = np.dot(w, X)
	return sigmoid(z)


def findMoves(probs): # Returns ranking of ALL moves
	moves = []
	probs = list(probs)
	tProbs = list(probs)
	for i in range(len(probs)):
		high = max(tProbs)
		index = probs.index(high)
		moves.append(index)
		tProbs.remove(high)
	return moves

def makeCommands(gridDim):
	l = []
	a = gridDim # easier
	for i in range(gridDim*2+1):
		if i%2==0:
			for x in range(gridDim):
				l.append(str(i)+str(x))
		else:
			for x in range(gridDim+1):
				l.append(str(i)+str(x))
	return l

def formatMoves(legalOrderMoves, commands): #passed in [[move indices], [order]]
	fmatMoves = []
	moves = legalOrderMoves[0]
	order = legalOrderMoves[1]
	orderRef = list(order)
	for i, move in enumerate(moves):
		moves[i] = commands[move]
#	print moves
	for i, val in enumerate(orderRef):
		next = min(order)
		indexNext = order.index(next)
		nMove = moves[indexNext]
#		print next, indexNext, nMove
		fmatMoves.append(nMove)
		order.remove(min(order))
#		print order
	return fmatMoves


def onlyLegal(moves, data): # outputs 2D list of [[move indices], [order]]
	legalMoves = []
	for i in range(len(data)):
		if data[i] == 0:
			legalMoves.append(i)
	return [legalMoves, [moves[i] for i in legalMoves]]


	


# -------------------------- Cool Stuff -------------------------------


def main(gridSize):
	data = getData()
	justMoves = list(data[:len(data)-2])
#	print len(justMoves), len(data)
	a = []
	a.append(addBias(data))
	net = Net(20, len(justMoves))
# ------------- Eventually condense this into just forwardPropagate ------------------
	a.append(forwardOne(net.getNodes(1), a[0]))
	a[1] = addBias(a[1])
	a.append(forwardOne(net.getNodes(2), a[1]))
	moves = findMoves(a[2])
	# move = moves.index(min(moves))
	# print [int(x) for x in justMoves]
	# print onlyLegal(moves, justMoves)
	# print makeCommands(gridSize)
	nextMoves = formatMoves(onlyLegal(moves, justMoves), makeCommands(gridSize))
	# print nextMoves
	print "Next Move - " + str(nextMoves[0])
	with open('move', 'w') as f:
		f.write(nextMoves[0])
	with open('weights1', 'w') as f:
		f.write(net.getWeights(1))
	with open('weights2', 'w') as f:
		f.write(net.getWeights(2))



if __name__ == "__main__":
	main(2)