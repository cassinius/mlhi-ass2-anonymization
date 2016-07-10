import globals as GLOB
import random

class NodeCluster:

    # Allow initialization of a new cluster only with a node given
    def __init__(self, node, dataset=None, adj_list=None, gen_hierarchies=None):
        self._nodes = [node]
        self._dataset = dataset
        self._adjList = adj_list
        self._neighborhoods = {
            node: self._adjList[node]
        }
        self._genHierarchies = gen_hierarchies
        self._genCatFeatures = {
            'workclass': self._dataset[node]['workclass'],
            'native-country': self._dataset[node]['native-country'],
            'sex': self._dataset[node]['sex'],
            'race': self._dataset[node]['race'],
            'marital-status': self._dataset[node]['marital-status']
        }
        self._genRangeFeatures = {
            'age': [self._dataset[node]['age'], self._dataset[node]['age']]
        }


    def getNodes(self):
        return self._nodes


    def getNeighborhoods(self):
        return self._neighborhoods


    def addNode(self, node):
        self._nodes.append(node)
        self._neighborhoods[node] = self._adjList[node]

        # Updating feature levels and ranges

        for genCatFeatureKey in self._genCatFeatures:
            self._genCatFeatures[genCatFeatureKey] = self.computeNewGeneralization(genCatFeatureKey, node)[1]
        # print self._genCatFeatures

        for genRangeFeatureKey in self._genRangeFeatures:
            range = self._genRangeFeatures[genRangeFeatureKey]
            self._genRangeFeatures[genRangeFeatureKey] = self.expandRange(range, self._dataset[node][genRangeFeatureKey])
        # print self._genRangeFeatures


    def computeGIL(self, node):
        costs = 0.0
        weight_vector = GLOB.GEN_WEIGHT_VECTORS[GLOB.VECTOR]
        # print weight_vector

        for genCatFeatureKey in self._genCatFeatures:
            weight = weight_vector['categorical'][genCatFeatureKey]
            costs += weight * self.computeCategoricalCost(genCatFeatureKey, node)

        for genRangeFeatureKey in self._genRangeFeatures:
            weight = weight_vector['range'][genRangeFeatureKey]
            costs += weight * self.computeRangeCost(genRangeFeatureKey, node)

        return costs # / float(len(self._genCatFeatures) + len(self._genRangeFeatures))


    def computeCategoricalCost(self, gen_h, node):
        cat_hierarchy = self._genHierarchies['categorical'][gen_h]
        cluster_level = self.computeNewGeneralization(gen_h, node)[0]
        return float((cat_hierarchy.nrLevels() - cluster_level) / cat_hierarchy.nrLevels())


    def computeRangeCost(self, gen_h, node):
        feat = self._genRangeFeatures[gen_h]
        range_h = self._genHierarchies['range'][gen_h]
        costs = range_h.getCostOfRange(min(feat), max(feat))
        #print node_value, feat, costs
        return costs
        # Fake...
        #return random.randint(0, 1)


    def computeNewGeneralization(self, gen_h, node):
        """ find the lowest common generalization level between cluster
        and node and return level as well as the exact (string) value
        """

        c_hierarchy = self._genHierarchies['categorical'][gen_h]
        n_value = self._dataset[node][gen_h]
        n_level = c_hierarchy.getLevelEntry(n_value)
        c_value = self._genCatFeatures[gen_h]
        c_level = c_hierarchy.getLevelEntry(c_value)

        while n_value != c_value:
            old_n_level = n_level

            if c_level <= n_level:
                n_value = c_hierarchy.getGeneralizationOf(n_value)
                n_level -= 1

            # if node and cluster are at the same level, go cluster up too
            if old_n_level <= c_level:
                c_value = c_hierarchy.getGeneralizationOf(c_value)
                c_level -= 1


        return [c_level, c_value]


    def computeSIL(self, node):
        # TODO implement SIL function with binary neighborhood vectors

        # Fake...
        return random.randint(0, 1)


    def expandRange(self, range, nr):
        min = nr if nr < range[0] else range[0]
        max = nr if nr > range[1] else range[1]
        return [min, max]


    def computeNodeCost(self, node):
        gil = self.computeGIL(node)
        # print "GIL: " + str(gil)
        sil = self.computeSIL(node)
        # print "SIL: " + str(sil)
        return GLOB.ALPHA*gil + GLOB.BETA*sil


    def toString(self):
        out_string = ""

        for count in range(0, len(self._nodes)):

            # Non-automatic, but therefore in the right order...

            age = self._genRangeFeatures['age']
            if age[0] == age[1]:
                out_string += str(age[0]) + ", "
            else:
                out_string += "[" + str(age[0]) + " - " + str(age[1]) + "], "

            out_string += self._genCatFeatures['workclass'] + ", "
            out_string += self._genCatFeatures['native-country'] + ", "
            out_string += self._genCatFeatures['sex'] + ", "
            out_string += self._genCatFeatures['race'] + ", "
            out_string += self._genCatFeatures['marital-status'] + "\n"

        out_string = out_string.replace("all", "*")
        return out_string
