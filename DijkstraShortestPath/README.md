## Dijkstra's Shortest Path  
_**About**_  
This greedy algorithm computes the shortest path from a source vertex to every other vertex in the graph. Dijkstra's algorithm doesn't work as expected with negative edges lengths.  

---  

_**How it works**_  
1. The algorithm starts at a source vertex and greedily chooses the adjacent vertex with the shortest edge.  

1. Completes all necessary calculations.  
    1. Setting the new minimum distance and path

1. Then it recursively moves to this adjacent vertex with the shortest edge and repeats.  

---  

_**Methods**_  
- [readFile(filePath)]( https://github.com/keshprad/Algorithms/blob/3be082a22ee6bed98555cbd57c8b728c2d7a671c/DijkstraShortestPath/DijkstraAlg.py#L5 )  
    - Takes the parameter _filePath_, a string representing the path to the input file.  
    - Iterates through each line, initially setting the distance to infinity, the path to '', and setting the graph in the following format:
        - vertex:\[ \[adjVert1, cost1\], \[adjVert2, cost2\], ... \]
- [findShortestPath(source)]( https://github.com/keshprad/Algorithms/blob/3be082a22ee6bed98555cbd57c8b728c2d7a671c/DijkstraShortestPath/DijkstraAlg.py#L24 )  
    - Takes in a _source_ vertex.  
    - Serves as the main method for this algorithm.
    - Sets initial conditions for the source vertex and adds all vertices to the unvisited list.   
    - Invokes [useDijkstra(source, vertex)]( https://github.com/keshprad/Algorithms/blob/3be082a22ee6bed98555cbd57c8b728c2d7a671c/DijkstraShortestPath/DijkstraAlg.py#L31 ).  
- [useDijkstra(vertex, unvisited)]( https://github.com/keshprad/Algorithms/blob/3be082a22ee6bed98555cbd57c8b728c2d7a671c/DijkstraShortestPath/DijkstraAlg.py#L31 )  
    - Takes input _vertex_, the current vertex looked at, and _unvisited_, a list of all so far unvisited nodes.
    - Goes through all unvisited vertices adjacent to _vertex_.  
        - If the distance along this path is shorter than the current minimum, we update the _adj\_vert_'s _self.minimum_ and _self.path_.  
    - Removes the node from unvisited.
    - Finds the next vertex to visit by invoking [nextVertex(...)]( https://github.com/keshprad/Algorithms/blob/3be082a22ee6bed98555cbd57c8b728c2d7a671c/DijkstraShortestPath/DijkstraAlg.py#L50 ).  
    - Recursively calls [useDijkstra(...)]( https://github.com/keshprad/Algorithms/blob/3be082a22ee6bed98555cbd57c8b728c2d7a671c/DijkstraShortestPath/DijkstraAlg.py#L31 ).  
- [nextVertex(unvisited)]( https://github.com/keshprad/Algorithms/blob/3be082a22ee6bed98555cbd57c8b728c2d7a671c/DijkstraShortestPath/DijkstraAlg.py#L50 )  
    - Takes as input a list of unvisited nodes.  
    - Objective is to calculate the next vertex.  
    - Does this by looking at all unvisited vertices and selecting the one with the shortest distance.

---  

_**Input**_  
The input file describes a graph with varying edge lengths. It uses the following format:  

\[vert1\] \[adjVert1,cost1\] \[adjVert2,cost2\] \[adjVert3,cost3\] ...  
\[vert2\] \[adjVert1,cost1\] \[adjVert2,cost2\] \[adjVert3,cost3\] ...  
\[vert3\] \[adjVert1,cost1\] \[adjVert2,cost2\] \[adjVert3,cost3\] ...  
...  

[Example Input File]( https://github.com/keshprad/Algorithms/blob/3be082a22ee6bed98555cbd57c8b728c2d7a671c/DijkstraShortestPath/testCases/test1.txt )  

---  

_**Credits**_  
Some test cases are used from [@beaunus]( https://github.com/beaunus )'s [stanford-algs]( https://github.com/beaunus/stanford-algs ) repository or provided by [Stanford's Algorithms Specialization]( https://www.coursera.org/specializations/algorithms ) taught by [Tim Roughgarden]( https://www.linkedin.com/in/tim-roughgarden-1a594855 ) on Coursera.  
