## The Greedy Knapsack Problem  
_**About**_  
Given a knapsack capacity and a list of items, each with a positive weight and a positive value, this greedy algorithm will maximize the value of items in the knapsack while keeping the total weight under the maximum capacity. The greedy solution assums items can be split into any percentage of the item. Weights or values are not necessarily unique to one item.  

---  

_**Applications**_  
- Need to maximize the value of something when there are limited resources. Useful when the items can be split, like a software download.  

---  

_**How it works**_  
1. The algorithm greedily sorts the items from greatest to least based on their ratio of value:weight.  

1. Using this order, we add the items to the knapsack one by one.  

1. If an item doesn't completely fit, we add the exact percentage of the item that can fit. This item will be the last item to go in the knapsack.  

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
    - Creates a list of the items based on their ratio of value:weight.  
        - Sorts this list from largest to smallest based on the ratio.  
    - This sorted list is the exact order we will add items to the knapsack.  
    - The last item to go in the knapsack may not completely fit.  
        - We can solve this by simply taking a fraction of the item.  
        - In fact we will take as much of the item as will fit in the knapsack.  
    - Returns the maximized value(_knap\_value_) of the knapsack and the items included in the knapsack.  

---  

_**Input**_  
The input file describes an array of items, each including a value and a weight. The first line of the file will include the capacity and the number of items. It uses the following format:  

\[knapsack_size\]\[number_of_items\]  
\[value_1\] \[weight_1\]  
\[value_2\] \[weight_2\]  
...  

[Example Input File]( https://github.com/keshprad/Algorithms/blob/master/GreedyKnapsack/testCases/test2.txt )  

---  

_**Credits**_  
Some test cases are used from [@beaunus]( https://github.com/beaunus )'s [stanford-algs]( https://github.com/beaunus/stanford-algs ) repository or provided by [Stanford's Algorithms Specialization]( https://www.coursera.org/specializations/algorithms ) taught by [Tim Roughgarden]( https://www.linkedin.com/in/tim-roughgarden-1a594855 ) on Coursera.  
