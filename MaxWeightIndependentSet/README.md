## Max Weight Independent Set  
_**About**_  
Given a file of vertex weights, the algorithm will find the maximum weight independent set.  

---  

_**How it works**_  
1. The algorithm first goes through the vertices in order summing up to find the weight of the mwis of the currently visited nodes and appends this value to a list.  

1. Then, goes backward through the list, constructing a list of each vertex that is included in the mwis.  

---  

_**Methods**_  
- mwis()  
    - Serves as the main method of the algorithm.  
    - Runs the find_mwis(...) method.  
    - Uses the previous result to run the reconstruct_set() method.  
- find_mwis()  
    - Goes through each vertex in order.  
    - Decides whether the current vertex weight would produce a new maximum weight of the mwis.  
    - Appends the current summed weight to a list of continuous weight sums.
    - Returns this list
- reconstruct_set()  
    - Takes in a parameter _res_, a list produced by find_mwis(...).  
    - Goes through the list backwards, determining which of these vertices were in the mwis.  
        - Checks which is greater, _res\[z-1\]_ or if _res\[z-2\]_ + _self.weights(z-1)_.  
        - This determines whether the vertex is in the mwis.  
    - Appends the vertex number, not the vertex weight, to the list of vertices in mwis.  

---  

_**Input**_  
The input file describes an array of numbers. It uses the following format:  

\[number_of_vertices\]  
\[weight_of_first_vertex\]  
\[weight_of_second_vertex\]  
...  

[Example Input File]( https://github.com/keshprad/Algorithms/blob/master/MaxWeightIndependentSet/testCases/test1.txt )  

---  

_**Credits**_  
Some test cases are used from [@beaunus]( https://github.com/beaunus )'s [stanford-algs]( https://github.com/beaunus/stanford-algs ) repository or provided by [Stanford's Algorithms Specialization]( https://www.coursera.org/specializations/algorithms ) taught by [Tim Roughgarden]( https://www.linkedin.com/in/tim-roughgarden-1a594855 ) on Coursera.  
