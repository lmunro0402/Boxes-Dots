#Setup for individual neuron
#
#Author: Patrick Kerrigan

class Neuron:
    """this is an individual neuron. It carries a personal id, weights, input ids, and values.
    It outputs a single value as some combination of weights and vals."""
    def __init__(self, id):
        self.id = id
        self.weights = []
        self.idIn = []
        self.vals = []
        self.out = 0

    def setOut(self):
        i = 0
        tot = 0
        for val in self.vals:
            tot += val*self.weights[i]
            i += 1
        self.out = tot/i

    def addCon(self, id, weight):
        self.idIn.append(id)
        self.weights.append(weight)
