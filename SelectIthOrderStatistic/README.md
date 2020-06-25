## Selecting the i-th Order Statistic
_**About**_  
This algorithms finds the i-th order statistic, the i-th smallest number, in a given file of integers.

---  

_**How it works**_  
1. The algorithm "piggybacks" on the [QuickSort algorithm]( https://github.com/keshprad/Algorithms/tree/master/QuickSort ) using it's partition(...) and choose3MedianPivot(...) methods.  
1. After each partition it throws away the portion of the list that is known to not contain the ith order statistic.  
1. Recursively continues with the portion of the list that's left.  

---  

_**Methods**_  
- findIthStatistic()  
    - Uses QuickSort's choose3MedianPivot(...) method to determine the pivot.  
    - Calls QuickSort's partition(...) method to partition around the pivot.  
        - This guarantees that the pivot will be in the sorted position since all elements on left are smaller and on right are greater. However, this doesn't mean the entire list is sorted.  
    - If the pivot is in the ith position, returns. Otherwise, the program throws away the portion of the list on the right or left of the pivot depending on which side the i-th statistic is know not to be in.  
    - Recursively computes with what is left.  

---  

_**Input**_  
The input file describes an array of numbers. It uses the following format:  

\[num1\]  
\[num2\]  
\[num3\]    
...  

[Example Input File]( https://github.com/keshprad/Algorithms/blob/master/SelectIthOrderStatistic/testCases/1000Nums.txt )  

---  

_**Credits**_  
Some test cases are used from [@beaunus]( https://github.com/beaunus )'s [stanford-algs]( https://github.com/beaunus/stanford-algs ) repository or provided by [Stanford's Algorithms Specialization]( https://www.coursera.org/specializations/algorithms ) taught by [Tim Roughgarden]( https://www.linkedin.com/in/tim-roughgarden-1a594855 ) on Coursera.  
