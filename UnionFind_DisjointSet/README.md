## Union Find or Disjoint Set  
_**About**_  
This data structure makes it easier to represent clustered data points. It has methods to find the cluster header, merge clusters, and optimize the cluster representation using path compression.  

---

_**Methods**_  
- [addVertex(vertex, parent)]( https://github.com/keshprad/Algorithms/blob/ae25d2ee685dbacb71566dac2db6f1a346456e3b/UnionFind_DisjointSet/UnionFind.py#L19 )  
	- Takes in parameters for vertex and parent nodes.  
	- Adds the given vertex to the graph with a pointer to its parent.  
- [find(vertex)]( https://github.com/keshprad/Algorithms/blob/ae25d2ee685dbacb71566dac2db6f1a346456e3b/UnionFind_DisjointSet/UnionFind.py#L22 )  
	- Takes in parameters for a single vertex.  
	- Finds and returns the oldest ancestor of this vertex.  
		- The oldest ancestor is also the head of the cluster the vertex belongs to.  
	- Calls pathCompression(...) on all visited nodes while finding the cluster head.  
- [union(vertex1, vertex2)]( https://github.com/keshprad/Algorithms/blob/ae25d2ee685dbacb71566dac2db6f1a346456e3b/UnionFind_DisjointSet/UnionFind.py#L34 )  
	- Takes in parameters for 2 vertices.  
	- Does nothing if vertex1 and vertex2 are members of the same cluster.  
		- Invokes find(...) to check cluster heads.  
	- Merges the two clusters in constant running time by updating the parent pointer of one of the cluster heads to the other cluster head.  
- [pathCompression(compress_list, parent)]( https://github.com/keshprad/Algorithms/blob/ae25d2ee685dbacb71566dac2db6f1a346456e3b/UnionFind_DisjointSet/UnionFind.py#L47 )  
	- Takes in parameters for a list of vertices and a parent.  
	- Updates the parent headers of all vertices in compress_list to point to the given parent.  
	- This helps improve the running time of the find(...) method. It reduces the amount of hops to get from a vertex in compress_list to the cluster header.  

---  

_**Input**_  
The class takes in as input a 2d-array that describes a list of clusters. The input should use the following format:  

\[  
&emsp;&emsp;\[cluster1_node1, cluster1_node2, ...\]  
&emsp;&emsp;\[cluster2_node1, cluster2_node2, ...\]      
&emsp;&emsp;\[cluster3_node1, cluster3_node2, ...\]  
&emsp;&emsp;...  
\]    

---  

_**Applications**_  
- [SimpleClustering]( https://github.com/keshprad/Algorithms/tree/master/SimpleClustering )  
