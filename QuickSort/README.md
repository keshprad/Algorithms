## QuickSort  
_**About**_  
This algorithms sorts elements in increasing order given a file of integers.  

---  

_**How it works**_  
1. The algorithm chooses a pivot element. Then, it sorts all elements simply to the left or right of the pivot based on whether it's less than or greater than the pivot.  

1. At this point, we know that the pivot must be in the correct spot since all smaller elements are on its left and all larger elements are on its right.  

1. From here, the algorithm recursively repeats on the group of elements on the left and right of the pivot.  
    1. Base case is that the list is one element, so it's already sorted.  

---  

_**Methods**_  
- reset  
- readFile(fileIn)  
- quicksort(l, r, pType)  
- partition(l, r)  
- choose3MedianPivot(l, r)  

---  

_**Input**_  
The input file describes an array of numbers. It uses the following format:  

\[num1\]  
\[num2\]  
\[num3\]  
...  

[Example Input File]( https://github.com/keshprad/Algorithms/blob/master/SelectIthOrderStatistic/testCases/1000Nums.txt )  

---  

_**Applications**_  
- [SelectIthOrderStatistic]( https://github.com/keshprad/Algorithms/tree/master/SelectIthOrderStatistic )  

---  

_**Credits**_  
Some test cases are used from [@beaunus]( https://github.com/beaunus )'s [stanford-algs]( https://github.com/beaunus/stanford-algs ) repository or provided by [Stanford's Algorithms Specialization]( https://www.coursera.org/specializations/algorithms ) taught by [Tim Roughgarden]( https://www.linkedin.com/in/tim-roughgarden-1a594855 ) on Coursera.  
