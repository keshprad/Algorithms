## Kruskal's Minimum Spanning Tree  
_**About**_  
Kruskal's is a greedy algorithm that finds the minimum spanning tree(the edges taken to reach all nodes while minimize the total weight), given a weighted undirected graph. It's different from Prim's Alg because it considers edges regardless of whether it has one node in the spanning tree.  

---  

_**How it works**_  
1. We look through each edge starting from lightest to heaviest.  

1. As long as the current edge doesn't cause a cycle, this is an optimal edge and can be added to the MST.  
    1. An edge causes a cycle when both it's nodes are in the same connected component. 
    1. Uses [Union Find]( https://github.com/keshprad/Algorithms/tree/master/UnionFind_DisjointSet ) to represent the connected components.  

---  

_**Methods**_  
- readFile(fileIn)  
    - Takes in parameter for _fileIn_, a path to an input file.  
    - Reads the file of edges.  
        - Adds each edge (represented with a tuple) to the array of edges.  
        - Adds all vertices to _c\_components_(later used as input for the Union Find data structure).  
    - Returns list of _edges_ and a Union Find data structure.  
- findMinSpanningTree()  
    - This method serves as the main method for this algorithm.  
    - Invokes sortCosts(...) to sort self.costs in increasing order by value.  
    - For every edge from lightest to heaviest...  
        - Invoke find\_ccomp\_headers(...) to find which components the 2 edges are in.  
        - If no cycles, we can add this to our MST and invoke the union(...) method from the Union Find _self.c\_components_ in order to merge connected components.  
- sortCosts(edges)  
    - Takes in as input an array of edges(represented as tuples).  
    - Returns the array of edges sorted by weight from lightest to heaviest.  
- find_ccomp_headers(edge)  
    - Takes in as input an edge.  
    - Uses the find(...) method from Union Find in order to find the component headers of the vertices.  
    - Returns these component headers in an array.  

---  

_**Input**_  
The input file describes an undirected graph of integers using the following format:  

\[number_of_nodes\] \[number_of_edges\]  
\[one_node_of_edge_1\] \[other_node_of_edge_1\] \[edge_1_cost\]  
\[one_node_of_edge_2\] \[other_node_of_edge_2\] \[edge_2_cost\]  
...  

[Example Input File]( https://github.com/keshprad/Algorithms/blob/master/PrimMinSpanningTree/testCases/test1.txt )  

---  

_**Credits**_  
Some test cases are used from [@beaunus]( https://github.com/beaunus )'s [stanford-algs]( https://github.com/beaunus/stanford-algs ) repository or provided by [Stanford's Algorithms Specialization]( https://www.coursera.org/specializations/algorithms ) taught by [Tim Roughgarden]( https://www.linkedin.com/in/tim-roughgarden-1a594855 ) on Coursera.  
