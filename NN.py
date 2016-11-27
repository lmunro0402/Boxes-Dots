# Neural Network
#
# Author: Luke Munro
from sigNeuron import *
import numpy as np


"""Neural net class for systems with ONE hidden layer, 
				eventually will work generically for more. """
class Net:
	def __init__(self, nodes, gridSize):
# ------ One Hidden Layer ------
# Nodes = # nodes in layer | sizeX = # data points | ouptuts = # possible ouptuts
# ----------- All sizes do NOT CONTAIN BIAS UNITS -----------
		self.gridSize = gridSize
		self.sizeX = 2*(gridSize*(gridSize+1))+2 
# ------ Hidden layer variables -------------------
		self.hidden = []
		self.sizeH = nodes
#-------- Output variables ----------
		self.outs = []
		self.sizeO = self.sizeX-2# For player scores
		for i in range(nodes):
			self.hidden.append(Neuron(1, i, self.sizeX+1, i))
		for i in range(self.sizeO): 
			self.outs.append(Neuron(2, i, self.sizeH+1, i))  # +1 for bias
		self.layers = [self.hidden, self.outs]


	def getWeights(self): 
		layer1 = np.zeros(shape=(self.sizeH, self.sizeX+1))
		layer2 = np.zeros(shape=(self.sizeO, self.sizeH+1))
		for i, node in enumerate(self.hidden):
			layer1[i] = node.getW()
		for i, node in enumerate(self.outs):
			layer2[i] = node.getW()
		layers = [layer1, layer2]
		return layers

	def writeWeights(self):
		layerWeights = self.getWeights()
		layerWeights[0].tofile('weights1')
		layerWeights[1].tofile('weights2')


	def loadWeights(self):
		weights1 = np.fromfile('weights1').reshape(self.sizeH, self.sizeX+1)
		weights2 = np.fromfile('weights2').reshape(self.sizeO, self.sizeH+1)
		for i, weight in enumerate(weights1):
			self.hidden[i].assignW(weight)
		for i, weight in enumerate(weights2):
			self.outs[i].assignW(weight)

	def getMove(self):
		a = []
		a0 = getData()
		justMoves = list(a0[:len(a0)-2])
		a0 = addBias(a0)
		a.append(a0)
		a1 = forwardOne(self.layers[0], a[0])
		a1 = addBias(a1)
		a.append(a1)
		a2 = forwardOne(self.layers[1], a[1])
		a.append(a2)
		moves = findMoves(a[2])
		legalMoves = onlyLegal(moves, justMoves)
		nextMoves = formatMoves(legalMoves, makeCommands(self.gridSize)))
		return nextMoves[0]





# -------------------------- Computations -------------------------------

def sigmoid(z):
    return 1/(1+np.exp(-z))

def forwardOne(Nodes, X):
	w = np.zeros(shape=(np.size(Nodes), np.size(X)))
	for i, node in enumerate(Nodes):
		w[i] = node.getW()
	z = np.dot(w, X).reshape(np.size(Nodes), 1)
	return sigmoid(z)


# ---------------------------- Utility ----------------------------------

def getData():
	with open('data', 'r') as d:
		data = d.read()
	data = [[int(data[x])] for x in range(len(data)) if x%3==1]
	data = np.array(data)
	return data 
		
def addBias(matrix):
	size = matrix.shape
	matrix = np.insert(matrix, 0, 1, axis=0)
	return matrix



# ------------------ Translating to BoxesDotes ----------------------


def findMoves(probs): # CONDENSE fix for same prob
	moves = []
	probs = probs.tolist()
	tProbs = list(probs)
	for i in range(len(probs)):
		high = max(tProbs)
		index = probs.index(high)
		probs[index] = -1 # working fix for same probs bug
		moves.append(index)
		tProbs.remove(high)
	return moves

def makeCommands(gridDim):
	moveCommands = []
	for i in range(gridDim*2+1):
		if i%2==0:
			for x in range(gridDim):
				moveCommands.append(str(i)+str(x))
		else:
			for x in range(gridDim+1):
				moveCommands.append(str(i)+str(x))
	return moveCommands

def formatMoves(moveOrder, commands): # CONDENSE
	fmatMoves = []
	for i, move in enumerate(moveOrder):
		fmatMoves.append(commands[move])
	return fmatMoves


def onlyLegal(moves, justMoves): # CONDENSE
	legalMoves = []
	for i in range(len(justMoves)):
		if justMoves[i] == 0:
			legalMoves.append(i)
	moveOrder = filter(lambda x: x in legalMoves, moves)
	return moveOrder


	
