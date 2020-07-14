## Floyd-Warshall All Paths Shortest Path  
_**About**_  
Given a file of edges(some of which may have negative edge weight) representing a directed graph, the Floyd-Warshall algorithm will find the shortest path from a every vertex to every other vertex in the graph.  

---  

_**How it works**_  
1. Fill an initial matrix with it's respective direct distance of each edge.  
    1. eg: A<sup>0</sup>\[1,3\]  will hold the direct distance of an edge with it's tail at 1 and head at 3.  

1. Next create A<sup>1</sup>, A<sup>2</sup>, ... A<sup>n</sup>
    1. Where in each case our new element at A<sup>k</sup>\[a, b\] = min(A<sup>k-1</sup>\[a, b\], A<sup>k-1</sup>\[a, k\] + A<sup>k-1</sup>\[k, b\]).  
    1. Essentially, each time we are trying to take a new intermediary vertex to determine if that vertex decreases the distance between a and b.  

1. As long as there were no negative cycles, A<sup>n</sup> will be our final matrix, holding the shortest distance between all pairs.  

---  

_**Methods**_  
- read\_file(file\_path)
    - Takes in an input file _file\_path_.  
    - Reads each edge weight into _self.pair\_dists_ with its position within the matrix determined by the tail and head pointer.  
    - Reads the number of vertices into _self.num\_vertices_.  
- floyd\_warshall()  
    - Acts as the main driving method for the algorithm.  
    - The following is repeated n times
        - First creates a new matrix, based on the previous matrix.  
        - A<sup>k</sup>\[a, b\] = min(A<sup>k-1</sup>\[a, b\], A<sup>k-1</sup>\[a, k\] + A<sup>k-1</sup>\[k, b\])  
    - Then sets _self.pair\_dists_ to the new matrix. This is because we only need to remember the current one and the previous one.  
    - Looks for negative cycles.  
        - This is done by checking if the pairs of A<sup>n</sup>\[a, a\] < 0.  
        - If this is less than zero, there must be some negative cycle which reduces the length of a path from a node starting and ending on itself.  
        - If there are negative cycles, the data will be inaccurate so we can just return false.  
- print\_results()  
    - Just creates a resultant string with the final distances from _self.pair_dists_.  
        
---  

_**Input**_  
The input file describes a weighted directed graph represented by edges. It uses the following format:  

\[num_vertices\]\[num_edges\]  
\[edge1_tail\]\[edge1_head\]\[edge1_weight\]  
\[edge2_tail\]\[edge2_head\]\[edge2_weight\]  
\[edge3_tail\]\[edge3_head\]\[edge3_weight\]  
...  

[Example Input File]( https://github.com/keshprad/Algorithms/blob/master/FloydWarshallShortestPath/testCases/test1.txt )  

---  

_**Helpful Videos**_
- [4.2 All Pairs Shortest Path (Floyd-Warshall) - Dynamic Programming]( https://www.youtube.com/watch?v=oNI0rf2P9gE )

---  

_**Credits**_  
Some test cases are used from [@beaunus]( https://github.com/beaunus )'s [stanford-algs]( https://github.com/beaunus/stanford-algs ) repository or provided by [Stanford's Algorithms Specialization]( https://www.coursera.org/specializations/algorithms ) taught by [Tim Roughgarden]( https://www.linkedin.com/in/tim-roughgarden-1a594855 ) on Coursera.  
