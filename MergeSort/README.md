## MergeSort  
_**About**_  
Given a file of integers, this algorithm sorts elements in increasing order in O(nlog(n)) running time.  

---  

_**How it works**_  
1. The algorithm recursively splits the list into two halves until it is of length 1 or less.  

1. After reaching the base case we merge the two halves in increasing order.  

1. We continue merging all halves retracing up the recursive stack until finishing the first call of [sortAndCount(...)]( https://github.com/keshprad/Algorithms/blob/7d9f160c63f6bbed509327dc18d49ff418017948/MergeSort/Inversions.py#L17 )  

---  

_**Methods**_  
- [readFile(f)]( https://github.com/keshprad/Algorithms/blob/7d9f160c63f6bbed509327dc18d49ff418017948/MergeSort/Inversions.py#L6 )  
    - Takes in a parameter for _f_, a path to an input file.  
    - Reads the file of integers and appends each integers to the self.res() array.  
- [sortAndCount(a)]( https://github.com/keshprad/Algorithms/blob/7d9f160c63f6bbed509327dc18d49ff418017948/MergeSort/Inversions.py#L17 )  
    - Takes _a_, a list of integers, as input  
    - Base Case: When array length is less than or equal to 1.  
        - Returns the list.  
    - Recursively calls [sortAndCount(...)]( https://github.com/keshprad/Algorithms/blob/7d9f160c63f6bbed509327dc18d49ff418017948/MergeSort/Inversions.py#L17 ) on the left and right half of the array.  
    - Merges the sorted right and left halves of the array by invoking [mergeAndCountSplits(...)]( https://github.com/keshprad/Algorithms/blob/7d9f160c63f6bbed509327dc18d49ff418017948/MergeSort/Inversions.py#L25 )  
- [mergeAndCountSplits(left, right)]( https://github.com/keshprad/Algorithms/blob/7d9f160c63f6bbed509327dc18d49ff418017948/MergeSort/Inversions.py#L25 )  
    - Takes in as input two sorted lists, _left_ and _right_, which are supposed to represent the left-half and right-half arrays.  
    - Since both lists are sorted, in order to merge we take the lowest unvisited element from each list.  
        - The program holds two pointers to the currently inspected elements in _left_ and _right_.  
        - Compares the element at each pointer and chooses the smaller element to append to the resulting 'out' array.  
        - Increments the pointer that pointed to the lower element.  

---  

_**Input**_  
The input file describes an array of numbers. It uses the following format:  

\[num1\]  
\[num2\]  
\[num3\]  
...  

[Example Input File]( https://github.com/keshprad/Algorithms/blob/7d9f160c63f6bbed509327dc18d49ff418017948/MergeSort/testCases/test5.txt )  

---    

_**Credits**_  
Some test cases are used from [@beaunus]( https://github.com/beaunus )'s [stanford-algs]( https://github.com/beaunus/stanford-algs ) repository or provided by [Stanford's Algorithms Specialization]( https://www.coursera.org/specializations/algorithms ) taught by [Tim Roughgarden]( https://www.linkedin.com/in/tim-roughgarden-1a594855 ) on Coursera.  
