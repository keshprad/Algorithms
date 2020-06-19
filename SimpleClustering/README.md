## Simple Clustering  
_**About**_  
This is a greedy clustering algorithm that clusters graph data points into k clusters. The algorithm uses user input to determine k.  

---  

_**Methods**_  
- readFile(fileName)  
- findClusters()  
- findSpacing()  

---  

_**How it works**_  
The algorithm greedily chooses the unvisited edge with the lowest cost and combines its 2 vertices into a cluster. If the vertices are already in clusters, it merges the two clusters; however, if they are in the same cluster, the algorithms skips over the edge.  

The algorithm uses the [Union Find (Disjoint Set)]( https://github.com/keshprad/Algorithms/tree/master/UnionFind_DisjointSet ) to find the cluster's parent, determine if vertices are in the same cluster, and merge clusters.  

---  

_**Input**_  
The input file describes a complete graph with edge costs. It uses the following format:  

\[number of nodes\]  
\[edge1_node1\] \[edge1_node2\] \[edge1_cost\]    
\[edge2_node1\] \[edge2_node2\] \[edge2_cost\]  
...  

[Example Input File]( https://github.com/keshprad/Algorithms/blob/master/SimpleClustering/testCases/test1.txt )  

---  

_**Credits**_  
Some test cases are used from [@beaunus]( https://github.com/beaunus )'s [stanford-algs]( https://github.com/beaunus/stanford-algs ) repository or provided by [Stanford's Algorithms Specialization]( https://www.coursera.org/specializations/algorithms ) taught by [Tim Roughgarden]( https://www.linkedin.com/in/tim-roughgarden-1a594855 ) on Coursera.  
