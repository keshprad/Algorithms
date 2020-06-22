## Karger's Min Cut  
_**About**_  
This randomized algorithm computes the minimum cut of a graph.  

---  

_**How it works**_  
1. The algorithm works by picking random edges( using [getRandomEdge(...)]( https://github.com/keshprad/Algorithms/blob/75535c5b925405c541b56a982f76981105489146/KargerMinCut/MinCuts.py#L21 ) ) and converging them.  

1. To maintain the graph we do some upkeeping in [restore(...)]( https://github.com/keshprad/Algorithms/blob/3be082a22ee6bed98555cbd57c8b728c2d7a671c/KargerMinCut/MinCuts.py#L26 ).  

1. We stop when we get down to 2 nodes. Our min-cut would be the partition of the graph such that the group of nodes we combined to get down to node 1 and node 2 have a minimum amount of crossing edges. This algorithm doesn't calculate this, but calculates the amount of edges in the min-cut.

---  

_**Methods**_  
- [readInput(filePath)]( https://github.com/keshprad/Algorithms/blob/75535c5b925405c541b56a982f76981105489146/KargerMinCut/MinCuts.py#L8 )  
    - Takes parameter _filePath_, a string representing the path to the input file.  
    - Reads the adjacency list input file and creates a dictionary with a list of adjacent vertices for each vertex.  
- [getRandomEdge(graph)]( https://github.com/keshprad/Algorithms/blob/75535c5b925405c541b56a982f76981105489146/KargerMinCut/MinCuts.py#L21 )  
    - Takes in the _graph_ as input.  
    - Returns a random edge by looking at a random node, then finding a second random node, this time from the first node's adjacency list.  
- [restore(graph, v1, v2)]( https://github.com/keshprad/Algorithms/blob/75535c5b925405c541b56a982f76981105489146/KargerMinCut/MinCuts.py#L26 )  
    - Takes in input edge represented by vertices _v1_ and _v2_
    - When we merge an edge, we notice a couple things that may cause problems.
    - Let's say we are merge an edge e(_v1_, _v2_)
        - All other nodes may have pointers to v2 in their adjacency list. The algorithm must go through all of the nodes sharing edges with _v2_ and reroute their pointers to _v1_.  
        - Next, to remove the self loops we look through _v1_'s adjacency list to find and remove any pointers to _v1_ or _v2_.  
        - It's okay and actually the algorithm relies on leaving the parallel edges in place.  
        - After the merge, there should be one common pointer either _v1_ or _v2_, so we can delete _v2_.  
- [KargerMinCut(graph)]( https://github.com/keshprad/Algorithms/blob/75535c5b925405c541b56a982f76981105489146/KargerMinCut/MinCuts.py#L41 )  
    - Takes in an input _graph_.  
    - Acts as the main method for the program.  
    - Essentially the idea is that we want to choose a random edges by invoking [getRandomEdge(...)]( https://github.com/keshprad/Algorithms/blob/75535c5b925405c541b56a982f76981105489146/KargerMinCut/MinCuts.py#L21 ). 
    - Then we want to converge the two nodes. This algorithm does this by joining the two vertices' adjacent edges.
    - Next, we need to take some steps to restore our graph. This is covered in a call to [restore(...)]( https://github.com/keshprad/Algorithms/blob/75535c5b925405c541b56a982f76981105489146/KargerMinCut/MinCuts.py#L26 ).
    - Returns the amount of edges going across those two nodes. The min-cut would be the nodes combined into each final node.  

---  

_**Input**_  
The input file describes an array of numbers. It uses the following format:  

\[num1\]  
\[num2\]  
\[num3\]  
...  

[Example Input File]( https://github.com/keshprad/Algorithms/blob/ae25d2ee685dbacb71566dac2db6f1a346456e3b/QuickSort/testCases/test5.txt )  

---    

_**Credits**_  
Some test cases are used from [@beaunus]( https://github.com/beaunus )'s [stanford-algs]( https://github.com/beaunus/stanford-algs ) repository or provided by [Stanford's Algorithms Specialization]( https://www.coursera.org/specializations/algorithms ) taught by [Tim Roughgarden]( https://www.linkedin.com/in/tim-roughgarden-1a594855 ) on Coursera.  
