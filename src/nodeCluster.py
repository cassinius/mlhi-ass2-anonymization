import globals as GLOB

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


    # TODO This should also update the feature levels and ranages
    def addNode(self, node):
        self._nodes.append(node)
        self._neighborhoods[node] = self._adjList[node]

        for genCatFeatureKey in self._genCatFeatures:
            self._genCatFeatures[genCatFeatureKey] = self.computeNewGeneralization(genCatFeatureKey, node)[1]
        # print self._genCatFeatures

        for genRangeFeatureKey in self._genRangeFeatures:
            range = self._genRangeFeatures[genRangeFeatureKey]
            self._genRangeFeatures[genRangeFeatureKey] = self.expandRange(range, self._dataset[node][genRangeFeatureKey])
        # print self._genRangeFeatures


    # TODO apply weight vector here (one centralized place...)
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
        # TODO implement categorical cost function
        # return 0

        cat_hierarchy = self._genHierarchies['categorical'][gen_h]
        cluster_level = self.computeNewGeneralization(gen_h, node)[0]
        return float((cat_hierarchy.nrLevels() - cluster_level) / cat_hierarchy.nrLevels())


    def computeNewGeneralization(self, gen_h, node):
        # TODO find the lowest common generalization level between
        # cluster and node and return level as well as the exact value
        # return [0, "generalized!"]

        cat_hierarchy = self._genHierarchies['categorical'][gen_h]
        cluster_feat = self._genCatFeatures[gen_h]
        cluster_level = cat_hierarchy.getLevelEntry(cluster_feat)
        node_feat = self._dataset[node][gen_h]
        # node_level = cat_hierarchy.getLevelEntry(node_feat)

        # print "Gen key: " + gen_h
        # print "Cluster feat: " + cluster_feat
        # print "Cluster level: " + str(cluster_level)
        # print "Node feat: " + node_feat
        # print "Node level: " + str(node_level)

        while cluster_feat != node_feat:
            node_feat = cat_hierarchy.getGeneralizationOf(node_feat)
            node_level = cat_hierarchy.getLevelEntry(node_feat)
            if cluster_level > node_level:
                cluster_feat = cat_hierarchy.getGeneralizationOf(cluster_feat)
                cluster_level = cat_hierarchy.getLevelEntry(cluster_feat)

        return [cluster_level, cluster_feat]


    def computeRangeCost(self, gen_h, node):
        # TODO implement range cost function
        # return 0

        range = self._genRangeFeatures[gen_h]
        # print range
        # print "New age info: " + str(self._dataset[node][gen_h])
        new_range = self.expandRange(range, self._dataset[node][gen_h])
        return self._genHierarchies['range'][gen_h].getCostOfRange(new_range[0], new_range[1])


    def expandRange(self, range, nr):
        min = nr if nr < range[0] else range[0]
        max = nr if nr > range[1] else range[1]
        return [min, max]


    def computeSIL(self, node):
        # TODO implement SIL function according to assignment
        # return 1

        population_size = len(self._adjList) - 2
        dists = []

        for cl_node in self._neighborhoods:
            dist = float(population_size)
            neighbors = self._neighborhoods[cl_node]
            for edge in neighbors:
                if edge != node and edge in self._adjList[node]:
                    dist -= 1
            dists.append(dist / population_size)
            # print dists

        return float(sum(dists)) / float(len(dists))


    def computeNodeCost(self, node):
        gil = self.computeGIL(node)
        # print "GIL: " + str(gil)
        sil = self.computeSIL(node)
        # print "SIL: " + str(sil)
        return GLOB.ALPHA*gil + GLOB.BETA*sil


    def toString(self):
        out_string = "blaa"

        return out_string