import globals as GLOB
import random
import rangeGenHierarchy as RGH

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
        # TODO implement range cost function
        range_hierarchy = self._genHierarchies['range'][gen_h]
        
        range_features = self._genRangeFeatures[gen_h]
        if range_features[1] < range_features[0]:
            range_value = range_hierarchy.getCostOfRange(range_features[1], range_features[0])
        else: 
            range_value = range_hierarchy.getCostOfRange(range_features[0], range_features[1])
        #print range_value
        # Fake...
        return range_value
        #return random.randint(0, 1)


    def computeNewGeneralization(self, gen_h, node):
        # TODO find the lowest common generalization level between cluster
        # and node and return level as well as the exact (string) value
        cat_hierarchy = self._genHierarchies['categorical'][gen_h]

        cluster_value = self._genCatFeatures[gen_h]
        node_value = self._dataset[node][gen_h]
        cluster_level = cat_hierarchy.getLevelEntry(cluster_value)
        node_level = cat_hierarchy.getLevelEntry(node_value)
        if cluster_value != node_value:
            if node_level < cluster_level:
                result_level = node_level
                result_value = at_hierarchy.getGeneralizationOf(node_value)
            else:
                result_level = cluster_level
                result_value = cat_hierarchy.getGeneralizationOf(cluster_value)
        else:
            result_level = node_level
            result_value = cluster_value
        #print cat_hierarchy.getEntries()
        #print cluster_level
        #print node_level
        #print result_level
        #print result_value
        #print self._genCatFeatures[gen_h]
        #print self._dataset[node][gen_h]
        # Fake...
        return [result_level, result_value]
        #return [0, "generalized!"]

    def computeSIL(self, node):
        # TODO implement SIL function with binary neighborhood vectors
        #print self.getNodes()
        current_neighbourhood = self.getNeighborhoods()
        boolean_vector = {}
        #print node
        #print "adj list: "
        #print self._adjList[node]
        #print "neighborhood:"
        #print current_neighbourhood
        temp_cost = 0.0       

        for node_root in current_neighbourhood:
            temp_compare = {}
            temp_compare[node] = []
            temp_compare[node_root] = [] 
            for node_in_all in self._dataset:     
                value_node = 0
                value_node_root = 0  
                if node_in_all != node_root and node_in_all != node:
                    if str(node_in_all) in self._adjList[node]:
                        value_node = 1
                    
                    temp_compare[node].append(value_node)

                    if str(node_in_all) in self._adjList[node_root]:
                        value_node_root = 1
                    temp_compare[node_root].append(value_node_root)
            #symmetric binary dissimilarity from reference 8 (page 70/71) of the paper         
            q = 0.0
            r = 0.0
            s = 0.0
            t = 0.0
            for i in range(0, len(temp_compare[node])):
                if temp_compare[node][i] == 1 and temp_compare[node_root][i] == 1:
                    q += 1
                elif temp_compare[node][i] == 0 and temp_compare[node_root][i] == 1:
                    r += 1
                elif temp_compare[node][i] == 1 and temp_compare[node_root][i] == 0:
                    s += 1
                elif temp_compare[node][i] == 0 and temp_compare[node_root][i] == 0:
                    t += 1
            temp_cost += (q+s)/(q+r+s+t)

            #print q
            #print r
            #print s
            #print t
            #temp_vector = {}
            #for node_neighbour in current_neighbourhood[node_root]:
            #    
            #    if node_neighbour == node:
            #        print node_neighbour == node 
            #        temp_vector[node_neighbour] = 1
            #    else:
            #        temp_vector[node_neighbour] = 0
            #    boolean_vector[node_root] = temp_vector
            #for node_adj in self_adjList[node]:
        cost = temp_cost/(len(current_neighbourhood))
        
        #print boolean_vector
        #print self.getNeighborhoods()


        
        return cost
        # Fake...
        #return random.randint(0, 1)


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