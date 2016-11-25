# Neural Network
#
# Author: Luke Munro
from Neuron1 import *
import numpy as np

"""Neural net class for systems with ONE hidden layer, 
				eventually will work generically for more. """
class Net:
	def __init__(self, nodes, sizeX, outputs):
# ------ One Hidden Layer ------
# Nodes = # nodes in layer | sizeX = # data points | ouptuts = # possible ouptuts
		self.Net = []
		self.nodes = nodes
		self.sizeX = sizeX+1 # For bias 
		self.outs = []
		self.data = []
		for i in range(nodes):
			self.Net.append(Neuron(1, i, self.sizeX, i))
		for i in range(outputs):
			self.outs.append(Neuron(2, i, self.nodes, i))


	def getNodes(self, layer):
# ------- will need to change for more layers ----------------------
		if layer == 1:
			return self.Net
		else: 
			return self.outs


def getData():
	with open('data', 'r') as d:
		data = d.read()
	data = [[int(data[x])] for x in range(len(data)) if x%3==1]
	data = np.array(data)
# ------------ Add bias ----------------- maybe?
	return addBias(data) 
		
def addBias(matrix):
# --------------- For hidden layer not a neuron just a 1 ----------------------------
	size = matrix.shape
	matrix = np.insert(matrix, 0, 1)
	return matrix


def forwardOne(Nodes, X):
	w = np.zeros(shape=(np.size(Nodes), np.size(X)))
	for i, node in enumerate(Nodes):
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

def formatMoves(legalOrderMoves): #passed in [[move indices], [order]]
	fmatMoves = []
	format = ["00", "01", 10, 11, 12, 20, 21, 30, 31, 32, 40, 41]
	format = [str(x) for x in format]
	moves = legalOrderMoves[0]
	order = legalOrderMoves[1]
	orderRef = list(order)
	for i, move in enumerate(moves):
		moves[i] = format[move]
	print moves
	for i, val in enumerate(orderRef):
		next = min(order)
		indexNext = order.index(next)
		nMove = moves[indexNext]
		print next, indexNext, nMove
		fmatMoves.append(nMove)
		order.remove(min(order))
		print order
	return fmatMoves

def justMoves(X):
	return X[1:13]

def onlyLegal(moves, data): # outputs 2D list of [[move indices], [order]]
	legalMoves = []
	for i in range(len(data)):
		if data[i] == 0:
			legalMoves.append(i)
	return [legalMoves, [moves[i] for i in legalMoves]]


	


# -------------------------- Cool Stuff -------------------------------


def main():
	a = []
	net = Net(100, 14, 12)
	a.append(getData())
	a.append(forwardOne(net.getNodes(1), a[0]))
	a.append(forwardOne(net.getNodes(2), a[1]))
	moves = findMoves(a[2])
	move = moves.index(min(moves))
	print moves
	print justMoves(a[0])
	print onlyLegal(moves, justMoves(a[0]))
	nextMoves = formatMoves(onlyLegal(moves, justMoves(a[0])))
	print nextMoves
	print nextMoves[0]
	with open('move', 'w') as f:
		f.write(nextMoves[0])

	# a.append(net.showData())
	# a.append(net.forwardOne())
	# a[1] = addBias(a[1])


	# X = np.array([[1, 1, 1]])
	# axion = Neuron(1, 1, 3)
	# print "Weights" 
	# print str(axion.getW())
	# print " ------------------ "
	# print "Z values - " + str(axion.getZ(X))
	# print "Prediction - " + str(axion.predict(X))

if __name__ == "__main__":
	main()