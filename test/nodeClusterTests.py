import unittest
import src.input.csvInput as csv
import src.nodeCluster as ncl

adults_file_csv = '../data/input_sanitized.csv'
adj_list_csv = '../data/adult_graph_adj_list.csv'
adults = csv.readAdults(adults_file_csv)
adj_list = csv.readAdjList(adj_list_csv)


#  test_ prefix for methods is needed in python unittest
class NodeClusterMethods(unittest.TestCase):

    def test_nodeClusterAddNode(self):
        cluster = ncl.NodeCluster()
        cluster.addNode(0, adj_list)
        self.assertEqual(cluster.getNodes(), [0])


    @unittest.skip("implement pertinent functionality first...")
    def test_nodeClusterComputeSIL(self):
        cluster = ncl.NodeCluster()
        cluster.addNode(0, adj_list)
        cluster.addNode(1, adj_list)
        self.assertEqual(cluster.getNodes(), [0, 1])
        self.assertEqual(round(cluster.computeSIL(2, adj_list), 4), 0.9983)


    @unittest.skip("implement pertinent functionality first...")
    def test_nodeClusterComputeSILIncludingIJNilCommon(self):
        adj_list_test = {
            0: [1, 2, 3, 4, 5],
            1: [6, 7, 0, 8, 9],
            2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8:[], 9:[]
        }
        self.assertEqual(len(adj_list_test), 10)
        cluster = ncl.NodeCluster()
        cluster.addNode(0, adj_list_test)
        self.assertEqual(round((cluster.computeSIL(1, adj_list_test)), 2), 1)


    @unittest.skip("implement pertinent functionality first...")
    def test_nodeClusterComputeSILIncludingIJOneCommon(self):
        adj_list_test = {
            0: [1, 2, 3, 4, 5],
            1: [6, 7, 0, 3, 8, 9],
            2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []
        }
        self.assertEqual(len(adj_list_test), 10)
        cluster = ncl.NodeCluster()
        cluster.addNode(0, adj_list_test)
        self.assertEqual(round((cluster.computeSIL(1, adj_list_test)), 2), 0.88)

if __name__ == '__main__':
    unittest.main()