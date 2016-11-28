import unittest
from graph_algo import grpahAlgo
import networkx as nx

G_test = grpahAlgo()


def initGrpah():

    G_test.G.add_weighted_edges_from([(0, 3, 4.1), ])
    G_test.G.add_weighted_edges_from([(0, 4, 1.1), ])
    G_test.G.add_weighted_edges_from([(0, 5, 3), ])
    G_test.G.add_weighted_edges_from([(1, 2, 3), ])
    G_test.G.add_weighted_edges_from([(1, 4, 4.2), ])
    G_test.G.add_weighted_edges_from([(2, 3, 5.6), ])
    G_test.G.add_weighted_edges_from([(2, 3, 5.6), ])
    G_test.G.add_weighted_edges_from([(2, 4, 2.2), ])
    G_test.G.add_weighted_edges_from([(3, 5, 3), ])
    G_test.G.add_weighted_edges_from([(4, 5, 2.2), ])

def checkNumberOfEdges():
    return G_test.G.number_of_edges() == 9

def checkNumberOfNodes():
    return G_test.G.number_of_nodes() == 6

def checkShortestPath():
    return G_test.get_path_length(2,3) == 5.6

# Here's our "unit tests".
class GraphAlgoUnitTests(unittest.TestCase):

    initGrpah()

    def testEdges(self):
        self.failUnless(checkNumberOfEdges())

    def testNodes(self):
        self.failUnless(checkNumberOfNodes())

    def testPath(self):
        self.failUnless(checkShortestPath())

def main():
    unittest.main()

if __name__ == '__main__':
    main()