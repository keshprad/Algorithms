## Selecting the Ith Order Statistic
_**About**_  
This algorithms finds the ith order statistic, the ith smallest number, in a given file of integers.

---  

_**How it works**_  
The algorithm "piggybacks" on the [QuickSort algorithm]( https://github.com/keshprad/Algorithms/tree/master/QuickSort ), but after each partition it throws away the half of the list that is known to not contain the ith order statistic.  

---  

_**Methods**_  
- findIthStatistic()  

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
