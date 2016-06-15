# Machine Learning for Health Informatics, Assignment 3:

# Social network anonymization with SaNGreeA

---

**Name change**: This is now officially assignment 3, as Marcus' last one was already assignment 2.

> Please read the original SaNGreeA paper contained in the 'paper' folder and / or watch the following YouTube movie before starting the assignment.

[K-Anonymity in Social Networks](https://www.youtube.com/watch?v=l2mU0xHMumo)

SaNGreeA is a Social Network Greedy Anonymization algorithm based on the concept of greedy clustering. Its input is given in the form of a graph structure; for this assignment, this graph is encoded as a list of feature vectors plus an adjacency list.

In order to compute its clusters, SaNGreeA takes into account two different distance measures (cost functions) from clusters to nodes / between 2 nodes:

1. The Generalization Information Loss (GIL), which measures the degree to which the features of a cluster would have to be generalized in order to incorporate a new node.
2. The Structural Information Loss representing the cost of edge generalization as the error probability in guessing the original network structure from the anonymized one.


### Input data

For this assignment we are using

* a subset of the [adult dataset](https://archive.ics.uci.edu/ml/datasets/Adult) as feature vector input for our GIL computations
	* please have a look at the respective [CSV file](https://github.com/cassinius/mlhi-ass2-anonymization/blob/master/data/input_sanitized.csv)
* a pre-generated random graph structure in the form of an adjacency list for our SIL computations.
	* please have a look at the respective [CSV file](https://github.com/cassinius/mlhi-ass2-anonymization/blob/master/data/adult_graph_adj_list.csv)
* generalization hierarchies in the form of json files
	* which can be  found in the gen hierarchy [folder](https://github.com/cassinius/mlhi-ass2-anonymization/tree/master/data/gen_hierarchies)


### Output data

The structure of a sample output file can be seen [here](https://github.com/cassinius/mlhi-ass2-anonymization/blob/master/data/sample_output/sample_output_different_weights.csv) and should be pretty intuitive - '*' stands for maximum generalization (and therefore loss), all other entries can be looked up in the respective generalization hierarchy json files.


### High-level algorithm walkthrough

The following steps would be taken given only the raw adults.csv input file (for this assignment, I have already prepared the first 4 steps in totality, only 3 functions have to be filled in, as we will see in the next section):

1. Read in the CSV, preprocessing / omitting erroneous entries
2. Generate a (random) graph structure for simulating a social network out of the resulting data
3. Instantiating generalization hierarchies for categorical values ('Italy' => 'Western Europe') as well as range values ([38-50] + 35 => [35-50])
4. Iterating over the dataset (1.), we execute the following steps:
    * Initialize a new cluster with the given node
    * While the cluster size is smaller k:
      * choose the node from the dataset with the best (lowest) total cost and add it to the cluster
5. If the last cluster is smaller in size than k, we disperse it's members amongst the previously computed clusters (this is not necessary for our example)


### Code structure

* data/ - input data as well as sample output data as described above
* output/ - folder to write results to
* paper/ - contains the original SaNGreeA paper
* src/
  * io/
    * csvInput.py - file to read .csv files into python dicts
    * jsonInput.py - file to read .json files into python dicts
    * output.py - file to write the resulting cluster structure to a .csv file
* catGenHierarchy.py - class to read .json based generalization hierarchy files and compute individual category generalization costs
* rangeGenHierarchy.py - class to compute individual range generalization costs
* globals.py - central settings file, giving the following options
  * K_FACTOR - the minimum cluster size
  * ALPHA - the weight applied to the GIL cost measure
  * BETA - the weight applied to the SIL cost measure
  * GEN_WEIGHT_VECTORS - 3 different pre-settings for feature weights
  * VECTOR - the one setting chosen for a given run
* SaNGreeA.py - the main file: prepares input structures, runs the main loop, prints results
* nodeCluster.py - Representing the anonymized clusters of size **k**, this class is responsible for computing the GIL / SIL cost functions in order to find the next best candidate node.

In order to run the code, simply execute the src/SaNGreeA.py file - if you need more orientation, there are still plenty of debug statements (sorry, I am not a python expert) currently commented out in the code...


### Known implementation deviations from the original algorithm
(should not have drastic consequences for the purpose of the demo / assignment)
* main loop starts with first node instead of node with max degree
* no dispersion of last cluster


### Your part

You work will consist of implementing 3 functions in the NodeCluster class:

1. computeRangeCost: Given this cluster and a candidate node, compute the cost for a potential expansion of the clusters current range (generalization, paper Definition 4, page 8)).
2. computeNewGeneralization: Given this cluster and a candidate node, compute the most specific possible generalization for the node to fit into the cluster (walk up the hierarchy, paper Definition 4, page 8):
  * cluster['sex'] = Male, candidate['sex'] = Female => result = 'all'
3. computeSIL: given the cluster and a candidate node, compute the structural neighborhood similarity using binary neighborhood vectors as given in the paper, Definition 11, page 12.

The difference between my reference implementation and the assignment version with method stubs is only a few dozen lines of code, so this should be fairly straightforward ;)

### Submission

Please just fork the github repository, add your code, and send me a pull request when you're done.


### Deadline

Friday, July 8th, 23:59 hours ;)


### Good luck!

[Bernd Malle, June 15th, 2016]
