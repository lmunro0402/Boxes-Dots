# Neural Network
#
# Author: Luke Munro
from Neuron1 import *
import numpy as np
from funcs import *

class Net:
#	def __init__(self, hiddenLayers, nPerLayer, X, outputs): ---- Eventually
	def __init__(self, nodes, sizeX, outputs):
# ------ One Hidden Layer ------
# Nodes = # nodes in layer | sizeX = # data points | ouptuts = # possible ouptuts
		self.Net = []
		self.nodes = nodes
		self.sizeX = sizeX
		self.outs = outputs
		self.data = []
		for i in range(nodes):
			self.Net.append(Neuron(1, i, self.sizeX, i))


	def getData(self):
		with open('data', 'r') as d:
			data = d.read()
		data = [[int(data[x])] for x in range(len(data)) if x%3==1]
		self.data = np.array(data)
# ------------ Add bias ----------------- maybe?
#		np.insert(self.data, 0, 1) 
#		print np.size(self.data)


	def activateHidden(self):
		w = np.zeros(shape=(self.nodes, self.sizeX))
		for i, node in enumerate(self.Net):
			w[i] = node.getW()
		print w.shape
		z = np.dot(w, self.data)
		return sigmoid(z)



def sigmoid(z):
	return 1/(1+np.exp(-z))

		# Neuron index instance variable not used

# -------------------------- Create Matrices -------------------------------


def main():
	net = Net(15, 14, 12)
	net.getData()
	print net.activateHidden()
	# X = np.array([[1, 1, 1]])
	# axion = Neuron(1, 1, 3)
	# print "Weights" 
	# print str(axion.getW())
	# print " ------------------ "
	# print "Z values - " + str(axion.getZ(X))
	# print "Prediction - " + str(axion.predict(X))

if __name__ == "__main__":
	main()