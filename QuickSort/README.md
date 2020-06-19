## QuickSort  
_**About**_  
Given a file of integers, this algorithm sorts elements in increasing order in O(nlog(n)) running time.  

---  

_**How it works**_  
1. The algorithm chooses a pivot element. Then, it sorts all elements simply to the left or right of the pivot based on whether it's less than or greater than the pivot.  

1. At this point, we know that the pivot must be in the correct spot since all smaller elements are on its left and all larger elements are on its right.  

1. From here, the algorithm recursively repeats on the group of elements on the left and right of the pivot.  
    1. Base case is that the list is one element, so it's already sorted.  

---  

_**Methods**_  
- [reset()]( https://github.com/keshprad/Algorithms/blob/ae25d2ee685dbacb71566dac2db6f1a346456e3b/QuickSort/Comparisons.py#L7 )  
    - Resets the object in order to reuse the same object for another partition method.  
- [readFile(fileIn)]( https://github.com/keshprad/Algorithms/blob/ae25d2ee685dbacb71566dac2db6f1a346456e3b/QuickSort/Comparisons.py#L11 )
    - Takes in parameters for _fileIn_, a path to an input file.
    - Reads the file of integers and appends each integers to the self.input array.  
- [quicksort(l, r, pType)]( https://github.com/keshprad/Algorithms/blob/ae25d2ee685dbacb71566dac2db6f1a346456e3b/QuickSort/Comparisons.py#L21 )  
    - Takes in as parameters _l_, _r_, and _pType_
        - _l_ and _r_ define the range of indices we are currently looking at.  
        - _pType_ defines the type of pivot we will use.  
            - _pType_=1 for the leftmost element as pivot
            - _pType_=2 for the rightmost element as pivot
            - _pType_=3 to invoke the [choose3MedianPivot(...)]( https://github.com/keshprad/Algorithms/blob/ae25d2ee685dbacb71566dac2db6f1a346456e3b/QuickSort/Comparisons.py#L45 )
    - This method serves as the main method for this algorithm.  
    - Partitions about a pivot to sort the pivot to its correct location.  
    - Recursively partitions about the left and right sides of the pivot.  
- [partition(l, r)]( https://github.com/keshprad/Algorithms/blob/ae25d2ee685dbacb71566dac2db6f1a346456e3b/QuickSort/Comparisons.py#L35 )  
    - Takes in parameters for _l_ and _r_ that define the left and right bounds of the indices we are currently looking at.  
    - Assumes the [quicksort(...)]( https://github.com/keshprad/Algorithms/blob/ae25d2ee685dbacb71566dac2db6f1a346456e3b/QuickSort/Comparisons.py#L21 ) method has put the pivot at index _l_.  
    - Sorts elements to the left of a pointer if less than the pivot and to the right if greater.  
    - Swaps the pivot to the pointer position.  
    - Returns the new position of the pivot.  
- [choose3MedianPivot(l, r)]( https://github.com/keshprad/Algorithms/blob/ae25d2ee685dbacb71566dac2db6f1a346456e3b/QuickSort/Comparisons.py#L45 )  
    - Takes in parameters for _l_ and _r_ that define the left and right bounds of the indices we are currently looking at.  
    - Looks at the elements at indices _l_, _r_, and (_l_+_r_)//2.  
        - Determines the median of the elements at these indices, and returns its index.

---  

_**Input**_  
The input file describes an array of numbers. It uses the following format:  

\[num1\]  
\[num2\]  
\[num3\]  
...  

[Example Input File]( https://github.com/keshprad/Algorithms/blob/ae25d2ee685dbacb71566dac2db6f1a346456e3b/QuickSort/testCases/test5.txt )  

---  

_**Applications**_  
- [SelectIthOrderStatistic]( https://github.com/keshprad/Algorithms/tree/master/SelectIthOrderStatistic )  

---  

_**Credits**_  
Some test cases are used from [@beaunus]( https://github.com/beaunus )'s [stanford-algs]( https://github.com/beaunus/stanford-algs ) repository or provided by [Stanford's Algorithms Specialization]( https://www.coursera.org/specializations/algorithms ) taught by [Tim Roughgarden]( https://www.linkedin.com/in/tim-roughgarden-1a594855 ) on Coursera.  
