## Continuous Streaming Medians Using Heaps  
_**About**_  
This algorithm utilizes two heaps to maintain a median as more and more numbers are streamed in.  

---  

_**How it works**_  
1. We will keep the largest half of elements in _self.min_heap_ and the smallest half in _self.max_heap_.
    1. This may seem counterintuitive, but it is necessary; we do this because when we need to balance the heaps and the median, we can easily pop off the top element to become the new median.  

1. We will use python's heapq module. Since this only expresses a min heap, any elements pushed to or popped from self.max_heap will be multiplied by -1.

1. We will have a separate variable holding the current median, so every time we insert an element, we have quick access to the current median and the element directly on its left and right.
    1. This means anytime our heaps are unbalanced, we only need to push the current median to the correct heap and pop off the new heap from the other heap.  

1. By repeating this for each line, we find the running median.

---  

_**Methods**_  
- findRunningMedians(filePath)  
    - Takes in parameter _filePath_, a string path to the input file.  
    - This method acts as the main method for the algorithm.  
    - Iterates through each line.  
        - First, inserting the integer into its respective heap by invoking insert(...).  
        - Next, we balance the heaps to ensure the size of heaps is close and to ensure the median is accurate.  
        - Our algorithm wants to maintain the median after inserting each element in order, so it'll append the current median to self.running_medians and move on to the next line.  
- insert(item, median)  
    - Takes in _item_(the number to be inserted to the heap) and _median_(the current median)
    - Inserts _item_ into _self.max_heap_ if it is lower than the current _median_. Inserts _item_ into _self.min_heap_ if it is greater than or equal to the current _median_.    
- balance(median)  
    - Takes a parameter _median_ which is the value of the current median.  
    - Balances out the work insert(...) does.  
    - If there are 2 more elements in _self.min_heap_(the larger half of the elements), we need to adjust the heaps to find the new median.  
    - If there is 1 more element in _self.max_heap_(the smaller half of the elements), we need to adjust the heaps to find the new median.  
    - Returns the new calculated median.  

---  

_**Input**_  
The input file describes an array of numbers. It uses the following format:  

\[num1\]  
\[num2\]  
\[num3\]  
...  

[Example Input File]( https://github.com/keshprad/Algorithms/blob/75535c5b925405c541b56a982f76981105489146/HeapMedians/testCases/test1.txt )  

---   

_**Credits**_  
Some test cases are used from [@beaunus]( https://github.com/beaunus )'s [stanford-algs]( https://github.com/beaunus/stanford-algs ) repository or provided by [Stanford's Algorithms Specialization]( https://www.coursera.org/specializations/algorithms ) taught by [Tim Roughgarden]( https://www.linkedin.com/in/tim-roughgarden-1a594855 ) on Coursera.  
