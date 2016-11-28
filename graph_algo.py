# Graph Algorithms using Python Networkx library
# Application Structures, Assignment 1, Semester A
# Authors: Dudu Bistrov, Adiel Amshalom, Moshe Margaliot
# 21, November 2016

import networkx as nx
import time


class grpahAlgo:
    G = ''
    ec = None

    def __init__(self):
        self.G = nx.Graph()

    # read the file and initiales the Graph
    # the file format is givven as:
    # Nodes
    # Edges
    # source destination weight

    def init_graph_from_file(self,file):

        init_file_object = open(file, 'r')
        # TO DO: write validation test
        lines = init_file_object.readlines()

        number_of_nodes = lines[0]
        number_of_edges = lines[1]

        del lines[0:2]

        for line in lines:
            _node_i = int(line.split()[0])
            _node_j = int(line.split()[1])
            _weight = float(line.split()[2])
            self.G.add_weighted_edges_from([(_node_i, _node_j, _weight), ])

        init_file_object.close()

        return self.G



    # print all Outputs
    def test_graph(self,file,uw):

        start = time.clock()
        test_file_object = open(file, 'r')
        lines = test_file_object.readlines()

        if (uw == True):
            self.set_ec()

        del lines[0:1]

        for line in lines:
            line_args = line.split()
            if (str(line_args[0]).strip('\n') == "info"):
                print("Graph: |V|=" + str(self.get_num_of_nodes()) +
                       ", |E|=" + str(self.get_num_of_edges())     +
                       ", TIE=" + str(self.triangle_check())        +
                       ", Radius:" + str(self.get_rad2())            +
                       ", Diameter:" + str(self.get_diameter2())     +
                       ", Runtime:" + str(time.clock()-start))

            elif (int(line_args[2]) == 0):
                print ("%s %.2f" % (line.strip('\n'), self.get__length(line_args[0], line_args[1])))

            elif (int(line_args[2]) > 0):
                bl_list = line_args[3:]
                orig_list = []
                for item in bl_list:
                    n_list = nx.neighbors(self.G,int(item))
                    for n in n_list:
                        ed = str(self.G.get_edge_data(int(item), n))[11:-1]
                        t_list = [int(item), int(n), float(ed)]
                        orig_list.append(t_list)
                        self.G.add_weighted_edges_from([(int(item), int(n), float("inf")), ])

                print ("%s %.2f" % (line.strip('\n'), self.get_path_length(line_args[0], line_args[1])))

                for list in orig_list:
                    self.G.add_weighted_edges_from([(int(list[0]), int(list[1]), float(list[2])), ])

    # calculate the all pairs and put it at array
    def set_ec(self):
        start = time.clock()
        self.ec = nx.eccentricity(self.G, sp=nx.all_pairs_dijkstra_path_length(self.G))
        print str(time.clock()-start)

    # get minimal path
    def get_path_length(self,_source,_dest):
        return nx.dijkstra_path(self.G, source=int(_source), target=int(_dest), weight="weight")

    def get_path(self,_source,_dest):
        return nx.dijkstra_path(self.G, source=int(_source), target=int(_dest), weight="weight")

    def get_num_of_edges(self):
        return self.G.number_of_edges()

    def get_num_of_nodes(self):
        return self.G.number_of_nodes()

    def get_diameter2(self):
        if (self.ec == None):
            return nx.diameter(self.G)
        else:
            return nx.diameter(self.G,self.ec)

    def get_rad2(self):
        if (self.ec == None):
            return nx.radius(self.G)
        else:
            return nx.radius(self.G,self.ec)

    # Check if graph upholds the Triangle inequality condition
    # return True if all triangles upholds the Triangle inequality condition
    # otherwise return False

    def triangle_check(self):
        triangle = [circle for circle in nx.cycle_basis(self.G) if len(circle)==3]
        for item in triangle:
            a = float(str(self.G.get_edge_data(item[0],item[1]))[11:-1])
            b = float(str(self.G.get_edge_data(item[1],item[2]))[11:-1])
            c = float(str(self.G.get_edge_data(item[2],item[0]))[11:-1])

            if ((a>b+c) or (b>a+c) or (c>a+b)):
                return False
        return True


    def print_graph(self):
        for n, nbrs in self.G.adjacency_iter():
            for nbr, eattr in nbrs.items():
                data = eattr['weight']
                print('(%d, %d, %.2f)' % (n, nbr, data))
