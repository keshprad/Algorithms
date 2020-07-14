## Bellman-Ford Shortest Path  
_**About**_  
Given a file of edges(some of which may have negative edge weight) representing a directed graph, the Bellman Ford algorithm will find the shortest path from a source vertex to all other vertices in the graph.  

---  

_**How it works**_  
1. Go through all edges n-1 times, which should calculate the shortest path for each vertex as long as there are no negative weighted cycles.  

1. Look for any negative weighted cycles. If negative weighted cycles are found, we return as we cannot solve the problem.  

1. Computes and returns the results from the table.  

---  

_**Methods**_  
- read\_file(file\_path)
    - Takes in an input file _file\_path_.  
    - Reads each edge into _self.edges_ and reads the number of vertices into _self.numVertices_.  
- bf_path(source)
    - Takes in a _source_ vertex from which to find all distances from.  
    - First, we initialize a list of distances to infinity for vertices except the source, which is initialized to 0.  
    - Next, we go through all edge n-1 times. Here we are relaxing the values in _min\_dist_.  
    - Next we check for negative weighted cycles. If they exist, the Bellman Ford algorithm is incorrect and we can exit.  
    - If there are no negative weighted cycles, we go through _min\_dist_ printing out our result.
    
---  

_**Input**_  
The input file describes a weighted directed graph represented by edges. It uses the following format:  

\[num_vertices\]\[num_edges\]  
\[edge1_tail\]\[edge1_head\]\[edge1_weight\]  
\[edge2_tail\]\[edge2_head\]\[edge2_weight\]  
\[edge3_tail\]\[edge3_head\]\[edge3_weight\]  
...  

[Example Input File]( https://github.com/keshprad/Algorithms/blob/master/BellmanFord/testCases/test1.txt )  

---  

_**Credits**_  
Some test cases are used from [@beaunus]( https://github.com/beaunus )'s [stanford-algs]( https://github.com/beaunus/stanford-algs ) repository or provided by [Stanford's Algorithms Specialization]( https://www.coursera.org/specializations/algorithms ) taught by [Tim Roughgarden]( https://www.linkedin.com/in/tim-roughgarden-1a594855 ) on Coursera.  
