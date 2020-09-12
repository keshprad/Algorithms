# Algorithms
_**About**_  
This repository includes any algorithms I find interesting.  

---  

_**Algorithms**_  
- [Bellman-Ford Shortest Path]( https://github.com/keshprad/Algorithms/tree/master/BellmanFord )  
    - Given a file of edges(some of which may have negative edge weight) representing a directed graph, the Bellman Ford algorithm will find the shortest path from a source vertex to all other vertices in the graph.  
- [Climb N Steps]( https://github.com/keshprad/Algorithms/tree/master/ClimbNSteps )
    - Given n(the number of steps on the staircase) and x(an array of the different possible steps you can take at a time) this function outputs the number of combinations you can go up the stairs.  
- [Dijkstra's Shortest Path]( https://github.com/keshprad/Algorithms/tree/master/DijkstraShortestPath )  
    - This greedy algorithm computes the shortest path from a source vertex to every other vertex in the graph. Dijkstra's algorithm doesn't work as expected with negative edges lengths.  
- [Floyd-Warshall All Paths Shortest Path]( https://github.com/keshprad/Algorithms/tree/master/FloydWarshallShortestPath )  
    - Given a file of edges(some of which may have negative edge weight) representing a directed graph, the Floyd-Warshall algorithm will find the shortest path from a every vertex to every other vertex in the graph.  
- [Minimum Completion Time (Weighted Job Scheduling)]( https://github.com/keshprad/Algorithms/tree/master/GreedyJobSchedulingTimes )  
    - A greedy algorithm which figures the optimal order in which and the optimal total time a series of jobs takes based on their weight and length.  
- [The Greedy Knapsack Problem]( https://github.com/keshprad/Algorithms/tree/master/GreedyKnapsack )
    - Given a knapsack capacity and a list of items, each with a positive weight and a positive value, this greedy algorithm will maximize the value of items in the knapsack while keeping the total weight under the maximum capacity. The greedy solution assums items can be split into any percentage of the item. Weights or values are not necessarily unique to one item.  
- [Continuous Streaming Medians Using Heaps]( https://github.com/keshprad/Algorithms/tree/master/HeapMedians )  
    - This algorithm utilizes two heaps to maintain a median as more and more numbers are streamed in.  
- [Huffman Coding]( https://github.com/keshprad/Algorithms/tree/master/HuffmanCoding )
    - The algorithm assigns codes to the symbols in order to minimize the total bits. The more frequent a word is the smaller amount of bits in its huffman code.  
- [Karatsuba Multiplication]( https://github.com/keshprad/Algorithms/tree/master/KaratsubaMultiplication )  
    - This is a multiplication algorithm that is much quicker than the traditional grade school algorithm which works in quadratic running time.  
- [Karger's Min Cut]( https://github.com/keshprad/Algorithms/tree/master/KargerMinCut )  
    - This randomized algorithm computes the minimum cut of a graph.   
- [Kasaraju's Strongly Connected Components]( https://github.com/keshprad/Algorithms/tree/master/KasarajuSCC )  
    - Given a directed graph representation, Kasaraju's Algorithm finds the strongly connected components of this graph.  
- [The 0/1 Knapsack Problem]( https://github.com/keshprad/Algorithms/tree/master/Knapsack01 )
    - Given a knapsack capacity and a list of items, each with a positive weight and a positive value, this dynamic programming algorithm will maximize the value of items in the knapsack while keeping the total weight under the maximum capacity. Weights or values are not necessarily unique to one item.  
- [Kruskal's Minimum Spanning Tree]( https://github.com/keshprad/Algorithms/tree/master/KruskalMinSpanningTree )  
    - Kruskal's is a greedy algorithm that finds the minimum spanning tree(the edges taken to reach all nodes while minimize the total weight), given a weighted undirected graph. It's different from Prim's Alg because it considers edges regardless of whether it has one node in the spanning tree.  
- [Levenshtein Distance]( https://github.com/keshprad/Algorithms/tree/master/LevenshteinDistance )  
    - The Levenshtein Distance is a dynamic programming algorithm which represents the similarity between 2 strings as a numerical value.  
- [Max Weight Independent Set]( https://github.com/keshprad/Algorithms/tree/master/MaxWeightIndependentSet )  
    - Given a file of vertex weights, the algorithm will find the maximum weight independent set.  
- [MergeSort]( https://github.com/keshprad/Algorithms/tree/master/MergeSort )  
    - Given a file of integers, this algorithm sorts elements in increasing order in O(nlog(n)) running time.  
- [Next Lexicographical Permutation Algorithm]( https://github.com/keshprad/Algorithms/tree/master/NextLexicographicalPermutation )
    - Given a word, this algorithm finds the lowest lexicographical permutation that's greater than the input.  
- [Prim's Minimum Spanning Tree]( https://github.com/keshprad/Algorithms/tree/master/PrimMinSpanningTree )  
    - Given a representation of an undirected graph, this greedy algorithm finds the minimum spanning tree(the edges taken to reach all nodes while minimize the total cost).  
- [QuickSort]( https://github.com/keshprad/Algorithms/tree/master/QuickSort )  
    - Given a file of integers, this algorithm sorts elements in increasing order in O(nlog(n)) running time.  
- [Selecting the i-th Order Statistic]( https://github.com/keshprad/Algorithms/tree/master/SelectIthOrderStatistic )  
    - This algorithms finds the i-th order statistic, the i-th smallest number, in a given file of integers.  
- [Simple Clustering]( https://github.com/keshprad/Algorithms/tree/master/SimpleClustering )  
    - This is a greedy clustering algorithm that clusters graph data points into k clusters. The algorithm uses user input to determine k.  
- [Binary Tree Node]( https://github.com/keshprad/Algorithms/tree/master/TreeNode )
    - This data structure uses a series of nodes to represent a binary tree.  
- [Union Find or Disjoint Set]( https://github.com/keshprad/Algorithms/tree/master/UnionFind_DisjointSet )  
    - This data structure makes it easier to represent clustered data points. It has methods to find the cluster header, merge clusters, and optimize the cluster representation using path compression.  

---  

_**Credits**_  
Most files for test cases are used from [@beaunus]( https://github.com/beaunus )'s [stanford-algs]( https://github.com/beaunus/stanford-algs ) repository or provided by [Stanford's Algorithms Specialization]( https://www.coursera.org/specializations/algorithms ) taught by [Tim Roughgarden]( https://www.linkedin.com/in/tim-roughgarden-1a594855 ) on Coursera.  
