# Graph Algorithms using Python Networkx
# Application Structures, Assignment 1, Semester A
# Authors: Dudu Bistrov, Adiel Amshalom, Moshe Margaliot
# 21, November 2016

import networkx as nx
import getopt
import sys
import os
import time

FG=nx.Graph()

def usage():
    print """Command line usage:

    -h, --help          This help screen
    -i, --init-file     Use CM (config management) default values
    -t, --test-file       Don't test after installation

    """

def init_graph_from_file(file):

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
        FG.add_weighted_edges_from([(_node_i, _node_j, _weight), ])

    init_file_object.close()
    return FG

def test_graph(G,file):

    start = time.clock()
    test_file_object = open(file, 'r')
    lines = test_file_object.readlines()

    del lines[0:1]

    for line in lines:
        line_args = line.split()
        if (str(line_args[0]) == "info"):
            print("Graph: |V|=" + str(G.number_of_nodes()) + ", "
                   "|E|=" + str(G.number_of_edges())  +
                    ", TIE=" + str(triangle_check(G)) +
                    ", Radius:" + str(get_rad(G))     +
                    ", Diameter:" + str(get_diamiter(G)) +
                    " Runtime:" + str(time.clock()-start))

        elif (int(line_args[2]) == 0):
            print ("%s %.2f" % (line.strip('\n'), get_path_length(G, line_args[0], line_args[1])))

        elif (int(line_args[2]) > 0):
            bl_list = line_args[3:]
            orig_list = []
            for item in bl_list:
                n_list = nx.neighbors(G,int(item))
                for n in n_list:
                    ed = str(G.get_edge_data(int(item), n))[11:-1]
                    t_list = [int(item), int(n), float(ed)]
                    orig_list.append(t_list)
                    G.add_weighted_edges_from([(int(item), int(n), float("inf")), ])

            print ("%s %.2f" % (line.strip('\n'), get_path_length(G, line_args[0], line_args[1])))

            for list in orig_list:
                G.add_weighted_edges_from([(int(list[0]), int(list[1]), float(list[2])), ])


def get_blacklist_graph(G,bl_list):
    bl_G=nx.Graph(G);

    for item in bl_list:
        bl_G.remove_node(int(item))

    return bl_G

def get_path_length(G,_source,_dest):
    return nx.dijkstra_path_length(G, source=int(_source), target=int(_dest), weight="weight")

def get_path(G,_source,_dest):
    return nx.dijkstra_path(G, source=int(_source), target=int(_dest), weight="weight")

def get_diamiter(G,):
    return nx.diameter(G)

def get_rad(G):
    return nx.radius(G)

def triangle_check(G):
    triangle = [circle for circle in nx.cycle_basis(G)]
    for item in triangle:
        a = float(str(G.get_edge_data(item[0],item[1]))[11:-1])
        b = float(str(G.get_edge_data(item[1],item[2]))[11:-1])
        c = float(str(G.get_edge_data(item[2],item[0]))[11:-1])

        if ((a>b+c) or (b>a+c) or (c>a+b)):
            return false

    return True

def print_graph(G):
    for n, nbrs in FG.adjacency_iter():
        for nbr, eattr in nbrs.items():
            data = eattr['weight']
            print('(%d, %d, %.2f)' % (n, nbr, data))

try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:t:", ["help", "init-file=", "test-file="])
except getopt.GetoptError as err:
    # print help information and exit:
    print str(err) # will print something like "option -a not recognized"
    usage()
    sys.exit(2)

init_file_path = ''
test_file_path = ''

for o, a in opts:
    if o in ("-h", "--help"):
        usage()
        sys.exit()
    elif o in ("-i", "--init-file"):
        if (os.path.isfile(a)):
            init_file_path = a
        else:
            print a + "input file not found"
            exit(1)
    elif o in ("-t", "--test-file"):
        if (os.path.isfile(a)):
            test_file_path = a
        else:
            print a + "test file not found"
            exit(1)
    else:
        assert False, "unhandled option"



GG=init_graph_from_file(init_file_path)
test_graph(GG,test_file_path)
