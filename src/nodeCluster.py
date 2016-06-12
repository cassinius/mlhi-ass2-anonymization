class NodeCluster:

    def __init__(self):
        self._nodes = []
        self._neighborhood = []
        self._genCatFeatures = {
            'workclass': '',
            'native-country': '',
            'sex': '',
            'race': '',
            'marital-status': ''
        }
        self._genRangeFeatures = {
            'age': [-float('inf'), float('inf')]
        }


    def getNodes(self):
        return self._nodes


    def getNeighborhood(self):
        return self._neighborhood


    def addNode(self, node, adj_list):
        self._nodes.append(node)
        new_neighbor = self._neighborhood.append([adj_list[node]])


    def computeGIL(self, node, adults):
        # TODO implement GIL function according to assignment
        return 1


    def computeSIL(self, node, adj_list):
        # TODO implement SIL function according to assignment
        return 1
        
