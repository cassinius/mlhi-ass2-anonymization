class NodeCluster:

    def __init__(self):
        self._nodes = []
        self._neighborhood = set()
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


    def addNode(self, node, adj_list):
        self._nodes.append(node)
        seen = self._neighborhood
        for edge in adj_list[node]:
            if edge not in seen:
                self._neighborhood.append(edge)
