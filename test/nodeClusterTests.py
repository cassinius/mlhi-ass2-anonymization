import unittest
import src.input.csvInput as csv
import src.nodeCluster as ncl

#  test_ prefix for methods is needed in python unittest
class NodeClusterMethods(unittest.TestCase):

    adults_file_csv = '../data/input_sanitized.csv'
    adj_list_csv = '../data/adult_graph_adj_list.csv'
    adults = csv.readAdults(adults_file_csv)
    adj_list = csv.readAdjList(adj_list_csv)

    def test_catGenSexLevels(self):
        cluster = ncl.NodeCluster()
        cluster.addNode(0)
        self.assertEqual(cluster.getNodes(), [0])
