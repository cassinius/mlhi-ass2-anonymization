import catGenHierarchy as CGH

genh_dir = '../data/gen_hierarchies/'

class NodeCluster:

    def __init__(self):
        self._nodes = []
        self._neighborhoods = {}
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
        # Prepare categorical generalization hierarchies
        self.genh_workclass = CGH.CatGenHierarchy('workclass', genh_dir + 'WorkClassGH.json')
        self.genh_country = CGH.CatGenHierarchy('native-country', genh_dir + 'NativeCountryGH.json')
        self.genh_sex = CGH.CatGenHierarchy('sex', genh_dir + 'SexGH.json')
        self.genh_race = CGH.CatGenHierarchy('race', genh_dir + 'RaceGH.json')
        self.genh_marital = CGH.CatGenHierarchy('marital-status', genh_dir + 'MaritalStatusGH.json')


    def getNodes(self):
        return self._nodes


    def getNeighborhoods(self):
        return self._neighborhoods


    def addNode(self, node, adj_list):
        self._nodes.append(node)
        self._neighborhoods[node] = adj_list[node]


    def computeGIL(self, node, adults):
        costs = 0.0

        for genCatFeatureKey in self._genCatFeatures:
            costs += self.computeCategoricalCost(self._genCatFeatures[genCatFeatureKey])

        for genRangeFeatureKey in self._genRangeFeatures:
            costs += self.computeRangeCost(self._genRangeFeatures[genRangeFeatureKey])

        return costs / float(len(self._genCatFeatures) + len(self._genRangeFeatures))


    def computeCategoricalCost(self, gen_h, node):
        # TODO implement categorical cost function
        return 0


    def computeRangeCost(self, gen_h, node):
        # TODO implement categorical cost function
        return 0


    def computeSIL(self, node, adj_list):
        # TODO implement SIL function according to assignment
        return 0
