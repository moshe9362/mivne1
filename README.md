# Graph Algo 

* Authors: Dudu Bistrov, Moshe Margaliot, Adiel Amshalom
* Class: Appliction Structures 2016, Ariel 

### Dependencies

* [Python 2.7](https://www.python.org/download/releases/2.7/)
* Import [Networkx 1.1](https://networkx.github.io/) python lib

### Goal

Create a self containet pyhton class that will allow basic Undirrected Postitive Graph operations like: 

 * Intiialize a graph from input file
 * Compute shortest path from Node A to B
 * Compute shortest path with blacklisted Nodes
 * Compute diameter and radius
 * Check if graph upholds the Triangle inequality condition
 * and more

### Usage

clone/download latest master from github and use the *graph_algo_helper.py* to load and check your graph from a given input and test file:

```bash
# python graph_algo_helper.py --init-file <init_file_path> --test-file <test_file_path>

```

### Expected Output

```bash
# python graph_algo_helper.py --init-file init01.txt --test-file test01.txt

28,88,0 3890.69
19,50,0 2126.53
1,53,0 2509.00
21,64,1,22 2781.77
25,82,1,26 3733.01
10,69,1,11 3849.28
29,63,1,30 2436.08
35,74,1,36 2769.07
6,52,2,7,8 2575.17
22,91,2,23,24 4739.92
6,82,2,7,8 4463.69
3,81,2,4,5 4955.20
0,100,2,1,2 6335.37
11,88,2,12,13 4618.38
20,67,2,21,22 3065.49
3,72,2,4,5 4213.37
16,94,3,17,18,19 4847.45
18,69,3,19,20,21 3036.58
29,51,3,30,31,32 1655.69
34,76,3,35,36,37 2798.31
12,76,3,13,14,15 3974.99
19,59,3,20,21,22 3112.15
29,89,3,30,31,32 4244.71
23,89,2,24,25,26 4476.36

Graph: |V|=101, |E|=490, TIE=False, Radius:10, Diameter:20 Runtime:0.0635687810385

```

### Unit Tests

graph_algo_unittest.py is responsible for running short sanity to ensure basic graph functionality is in place. 
Currently there are 3 unit tests:
0. init graph with some values
1. test if number of nodes matches the correct value
2. test if number of edges matches the correct value
3. test if sortest path from node A to node B matches the correct value

#### usage:
```cmd
> python graph_algo_unittest.py -v
```

#### Expected UnitTest Output

```cmd
testEdges (__main__.GraphAlgoUnitTests) ... ok
testNodes (__main__.GraphAlgoUnitTests) ... ok
testPath (__main__.GraphAlgoUnitTests) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK
```

