## The 0/1 Knapsack Problem  
_**About**_  
Given a knapsack capacity and a list of items, each with a positive weight and a positive value, this dynamic programming algorithm will maximize the value of items in the knapsack while keeping the total weight under the maximum capacity. Weights or values are not necessarily unique to one item.  

---  

_**How it works**_  
1. The algorithm splits the problem into subproblems going through each item.  

1. At each item, it maximizes the value of the items visited thus far.  
    1. In order to do this, it starts with a maximum capacity of 0 and makes its way to the knapsack capacity, keeping track of the calculated total values in a 2d-array.  

---  

_**Methods**_  
- read_file(path)  
    - Takes as input the path to an input file.  
    - Goes through the file...  
        - Stores the maximum capacity as _capacity_.  
        - Stores the value of each item in the _values_ array.  
        - Stores the weight of each item in the _weights_ array.  
- maximize_value()  
    - This is the driving method of the algorithm.  
    - Creates a 2d array in which each array represents an item, and the values in each array represent the maximized value at the current weight.  
        - eg: if the maximum capacity is 100  
            - For the first item we have a list of the maximized value of the first item at weight 0, 1, ... 99, 100.  
            - For the second item we have a list of the maximized value of both the first and second item at weights, 0, 1, ... 99, 100.  
            - Continues for all items.  
    - How do we do this?  
        - We go through each weight for each item and decide if it would can include the item or not, based on the current maximum weight.  
            - If it is possible to include the item, we check whether including the item will give us a larger or smaller value and pick the situation that gives us the larger.  

---  

_**Input**_  
The input file describes an array of items, each including a value and a weight. The first line of the file will include the capacity and the number of items. It uses the following format:  

\[knapsack_size\]\[number_of_items\]  
\[value_1\] \[weight_1\]  
\[value_2\] \[weight_2\]  
...  

[Example Input File]( https://github.com/keshprad/Algorithms/blob/master/Knapsack01/testCases/test2.txt )  

---  

_**Helpful Videos**_  
- [0/1 Knapsack Problem Dynamic Programming]( https://www.youtube.com/watch?v=8LusJS5-AGo&t=29s )  

---  

_**Credits**_  
Some test cases are used from [@beaunus]( https://github.com/beaunus )'s [stanford-algs]( https://github.com/beaunus/stanford-algs ) repository or provided by [Stanford's Algorithms Specialization]( https://www.coursera.org/specializations/algorithms ) taught by [Tim Roughgarden]( https://www.linkedin.com/in/tim-roughgarden-1a594855 ) on Coursera.  
