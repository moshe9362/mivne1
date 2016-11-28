from graph_algo import grpahAlgo
import getopt
import sys
import os

def usage():
    print """Command line usage:

    -h, --help          This help screen
    -i, --init-file     Use CM (config management) default values
    -t, --test-file       Don't test after installation

    """

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

GG = grpahAlgo()
GG.init_graph_from_file(init_file_path)
GG.test_graph(test_file_path)
