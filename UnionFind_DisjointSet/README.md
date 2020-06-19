## Union Find or Disjoint Set  
_**About**_  
This data structure makes it easier to represent clustered data points. It has methods to find the cluster header, merge clusters, and optimize the cluster representation using path compression.  

---  

_**Methods**_  
- addVertex(vertex, parent)  
	- Takes in parameters for vertex and parent nodes.  
	- Adds the given vertex to the graph with a pointer to its parent.  
- find(vertex)  
	- Takes in parameters for a single vertex.  
	- Finds and returns the oldest ancestor of this vertex.  
		- The oldest ancestor is also the head of the cluster the vertex belongs to.  
	- Calls pathCompression(...) on all visited nodes while finding the cluster head.  
- union(vertex1, vertex2)  
	- Takes in parameters for 2 vertices.  
	- Does nothing if vertex1 and vertex2 are members of the same cluster.  
		- Invokes find(...) to check cluster heads.  
	- Merges the two clusters in constant running time by updating the parent pointer of one of the cluster heads to the other cluster head.  
- pathCompression(compress_list, parent)  
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

---

_**Credits**_  
Some test cases are used from [@beaunus]( https://github.com/beaunus )'s [stanford-algs]( https://github.com/beaunus/stanford-algs ) repository or provided by [Stanford's Algorithms Specialization]( https://www.coursera.org/specializations/algorithms ) taught by [Tim Roughgarden]( https://www.linkedin.com/in/tim-roughgarden-1a594855 ) on Coursera.  
