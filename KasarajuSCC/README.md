## Kasaraju's Strongly Connected Components  
_**About**_  
Given a directed graph representation, Kasaraju's Algorithm finds the strongly connected components of this graph.  

---  

_**How it works**_  
1. First, we reverse the edge directions and loop a Depth First Search for all unvisited vertices.  

1. Next, we replace the labels the vertexes by their finishing times.  
    1. The vertices in each SCC will have incrementing finishing times.  
    
1. From here, we loop a Depth Fisrt Search for all unvisited vertices. This time the edges will face the correct direction.  
    1. We will add these finishing times to a list of scc sizes because it represents the amount of nodes we passed, and it will only pass the nodes in the current SCC.

---  

_**Methods**_  
- [readFile(filePath)]( https://github.com/keshprad/Algorithms/blob/7d9f160c63f6bbed509327dc18d49ff418017948/KasarajuSCC/SCC.py#L10 )
    - Takes in a path to an input file _filePath_ containing edges to a directed graph.  
    - Returns a graph which has a dictionary for each vertex with all inward and outward edges represented and a boolean to indicate if a vertex had been visited.  
- [findSCC()]( https://github.com/keshprad/Algorithms/blob/7d9f160c63f6bbed509327dc18d49ff418017948/KasarajuSCC/SCC.py#L10 )
    - Serves as the main method for this algorithm.  
    - Invokes [DFS_Loop(...)]( https://github.com/keshprad/Algorithms/blob/7d9f160c63f6bbed509327dc18d49ff418017948/KasarajuSCC/SCC.py#L58 ) with reversed=True to find the finishing times of DFS for each node.  
    - Invokes [replaceFinishingTimes(...)]( https://github.com/keshprad/Algorithms/blob/7d9f160c63f6bbed509327dc18d49ff418017948/KasarajuSCC/SCC.py#L73 ) to replace node values with their finishing times from the previous call to [DFS_Loop(...)]( https://github.com/keshprad/Algorithms/blob/7d9f160c63f6bbed509327dc18d49ff418017948/KasarajuSCC/SCC.py#L58 ).  
    - Calls [DFS_Loop(...)]( https://github.com/keshprad/Algorithms/blob/7d9f160c63f6bbed509327dc18d49ff418017948/KasarajuSCC/SCC.py#L58 ), but this time with the edges directed in the correct ordering.  
- [DFS(i, order)]( https://github.com/keshprad/Algorithms/blob/7d9f160c63f6bbed509327dc18d49ff418017948/KasarajuSCC/SCC.py#L44 )  
    - Takes in as input _i_, a vertex, and _order_, which lets the code know whether to look at the inward edges or the outward edges.  
        - _order_ essentially allows us to reverse the order of the graph without actually iterating through every element.  
    - This method runs a depth first search on the given vertex.
    - It starts by marking the current vertex as explored.
    - Then it recursively calls [DFS(...)]( https://github.com/keshprad/Algorithms/blob/7d9f160c63f6bbed509327dc18d49ff418017948/KasarajuSCC/SCC.py#L44 ) on all the unexplored adjacent outward(or inward depending on _order_) vertices.  
    - Increments the global time by 1 after each node finished and adds this value of time to finishing_times if _order_='in'.
        - Again, when _order_='in' this essentially means we are looking at the graph with reversed edge directions.
- [DFS_Loop(reversed)]( https://github.com/keshprad/Algorithms/blob/7d9f160c63f6bbed509327dc18d49ff418017948/KasarajuSCC/SCC.py#L58 )  
    - Takes in as input _reversed_, a boolean indicating whether the direction of edges should be reversed
        - Having reversed edge directions allows us to find the finishing times or each node.
    - Iterates through each node and calls DFS on the unvisited nodes.
    - If reversed=False, meaning if we are already done with the finishing times, we will append the calculated time(in this case represents the size of the current SCC) to the list of self.scc_sizes.  
    - Finally, the method resets the time to 0.  
- [replaceFinishingTimes()]( https://github.com/keshprad/Algorithms/blob/7d9f160c63f6bbed509327dc18d49ff418017948/KasarajuSCC/SCC.py#L73 )  
    - Essentially, replaces the key for each vertex with its finishing time from the first call of [DFS_Loop(...)]( https://github.com/keshprad/Algorithms/blob/7d9f160c63f6bbed509327dc18d49ff418017948/KasarajuSCC/SCC.py#L58 ).  
- [find5MaxSizes()]( https://github.com/keshprad/Algorithms/blob/7d9f160c63f6bbed509327dc18d49ff418017948/KasarajuSCC/SCC.py#L85 )  
    - Finds and returns a list with up to 5 numbers representing the largest 5 SCC sizes in the list of self.scc_sizes.  

---  

_**Input**_  
The input file describes a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head. It uses the following format:  

\[edge1_tailVertex\] \[edge1_headVertex\]  
\[edge2_tailVertex\] \[edge2_headVertex\]  
\[edge3_tailVertex\] \[edge3_headVertex\]  
...  

[Example Input File]( https://github.com/keshprad/Algorithms/blob/7d9f160c63f6bbed509327dc18d49ff418017948/KasarajuSCC/testCases/test2.txt )  

---  

_**Credits**_  
Some test cases are used from [@beaunus]( https://github.com/beaunus )'s [stanford-algs]( https://github.com/beaunus/stanford-algs ) repository or provided by [Stanford's Algorithms Specialization]( https://www.coursera.org/specializations/algorithms ) taught by [Tim Roughgarden]( https://www.linkedin.com/in/tim-roughgarden-1a594855 ) on Coursera.  
