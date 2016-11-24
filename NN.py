# Neural Network
#
# Author: Luke Munro
from Neuron1 import *
import numpy as np

def main():
	X = np.array([[1, 1, 1]])
	axion = Neuron(1, 1, 3)
	print "Weights" 
	print str(axion.getW())
	print " ------------------ "
	print "Z values - " + str(axion.getZ(X))
	print "Prediction - " + str(axion.predict(X))

	with open('data', 'r') as d:
		data = d.read()
	data = np.array([data])

	print data

if __name__ == "__main__":
	main()