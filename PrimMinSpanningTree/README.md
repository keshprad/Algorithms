## Prim's Minimum Spanning Tree  
_**About**_  
Given a representation of an undirected graph, this greedy algorithm finds the minimum spanning tree(the edges taken to reach all nodes while minimize the total cost).  

---  

_**How it works**_  
1. We look at the smallest cost unvisited edge that has one node in the current tree and one node not in the current tree.  

1. This is the most optimal next edge, so we add it to the spanning tree and add its cost to our overall cost.  

1. We repeat these steps until we have visited all nodes in the tree. 

---  

_**Methods**_   
- readFile(fileIn)  
    - Takes in parameter for _fileIn_, a path to an input file.  
    - Reads the file of edges and their cost and adds them to the appropriate dictionary.  
- findMinSpanningTree()  
    - This method serves as the main method for this algorithm.  
    - Invokes sortCosts(...) to sort self.costs in increasing order by value.  
    - Invokes findUnvisited(...) to find all the initially unvisited nodes.  
    - While there are unvisited nodes, the algorithm looks at the smallest cost unvisited edge that has one node in the current tree and one node not in the current tree.  
        - Adds it to our spanning tree and adds its cost to our overall cost.  
        - Updates the visited/unvisited lists to ensure the while loops exit condition
- sortCosts()  
    - Returns a dictionary sorted by its cost(value).  
- findUnvisited(visited)  
    - Takes in a parameter _visited_ which is a list of visited nodes.  
    - Iterates through all edges and makes a list of all nodes not in _visited_.
    - Returns a list of all unvisited nodes

---  

_**Input**_  
The input file describes an undirected graph of integers using the following format:  

\[number_of_nodes\] \[number_of_edges\]  
\[one_node_of_edge_1\] \[other_node_of_edge_1\] \[edge_1_cost\]  
\[one_node_of_edge_2\] \[other_node_of_edge_2\] \[edge_2_cost\]  
...  

[Example Input File]( https://github.com/keshprad/Algorithms/blob/7d9f160c63f6bbed509327dc18d49ff418017948/PrimMinSpanningTree/testCases/test1.txt )  

---    

_**Credits**_  
Some test cases are used from [@beaunus]( https://github.com/beaunus )'s [stanford-algs]( https://github.com/beaunus/stanford-algs ) repository or provided by [Stanford's Algorithms Specialization]( https://www.coursera.org/specializations/algorithms ) taught by [Tim Roughgarden]( https://www.linkedin.com/in/tim-roughgarden-1a594855 ) on Coursera.  
