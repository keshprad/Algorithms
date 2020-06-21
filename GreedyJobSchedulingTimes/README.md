## Minimum Completion Time (Weighted Job Scheduling)
_**About**_  
A greedy algorithm which figures the optimal order in which and the optimal total time a series of jobs takes based on their weight and length.  

---  

_**How it works**_  
1. First, we create a list of ratios(_weight_/_length_) sorted from greatest to least.  

1. The jobs will run in this order. 
    1. If there are multiple jobs with the same ratio, the order doesn't really matter. The completion time will be the same regardless of the order we handle ties.
    1. If we are running the algorithm of differences(_weight_-_length_), the order in which we handle ties matters. We will handle ties by taking the maximum weighted jobs first.
        1. The differences algorithm will not output an optimal solution. It's just there to show as example that it shouldn't work.

1. Next, we calculate the time the jobs will take. Each job takes (_weight_*_currLength_) time.  
    1. _currLength_ is the sum of lengths of all jobs that have previously executed and the length of the current job.

---  

_**Methods**_  
- [readFile(filePath)]( https://github.com/keshprad/Algorithms/blob/75535c5b925405c541b56a982f76981105489146/GreedyJobSchedulingTimes/Scheduling.py#L5 )  
    - Takes in _filePath_, a string representation of the path to the file.  
    - Iterates through each line, appending the weight and length of each job to it's correct array.  
- [findMinCompletionTimes()]( https://github.com/keshprad/Algorithms/blob/75535c5b925405c541b56a982f76981105489146/GreedyJobSchedulingTimes/Scheduling.py#L18 )  
    - Serves as the main method for this algorithm.  
    - The algorithm finds all ratios(_weight_ / _length_) with a call to [findRatios(...)]( https://github.com/keshprad/Algorithms/blob/75535c5b925405c541b56a982f76981105489146/GreedyJobSchedulingTimes/Scheduling.py#L27 ).  
    - Sorts the ratios in decreasing order.  
    - Then calculates the time if we were to do jobs in order of greatest ratio.
    - Does this same algorithm for differences(_weight_ - _length_). 
        - Although this is not the correct algorithm, it's used to show differences result in a slightly worse, nonoptimal job scheduling.  
- [findRatios()]( https://github.com/keshprad/Algorithms/blob/75535c5b925405c541b56a982f76981105489146/GreedyJobSchedulingTimes/Scheduling.py#L27 )  
    - Goes through each _weight_ & _length_ pair.  
    - Finds the ratio _weight_/_length_.  
    - Adds this to _ratios_.  
- [findDiffs()]( https://github.com/keshprad/Algorithms/blob/75535c5b925405c541b56a982f76981105489146/GreedyJobSchedulingTimes/Scheduling.py#L36 ) 
    - Again, using diffs will result in a nonoptimal solution and is only included to show this.  
    - Goes through each _weight_ & _length_ pair.  
    - Finds the difference weight-length.  
    - Adds this to _diffs_.  
- [findTime(unordered, ordered)]( https://github.com/keshprad/Algorithms/blob/75535c5b925405c541b56a982f76981105489146/GreedyJobSchedulingTimes/Scheduling.py#L45 )  
    - Takes two parameters: _unordered_, a dictionary with all ratios(or diffs) and the elements that have that ratio, and _ordered_, a list of all ratios(or diffs) sorted max to min.  
    - If there are multiple elements with the same ratio(or diff), we settle this by picking them in order of maximum weight.  
    - Finally, each job takes time _weight_*_currLength_.

---  

_**Input**_  
The input file describes an array of numbers. It uses the following format:  

\[num_jobs\]  
\[job1_weight\] \[job1_length\]  
\[job2_weight\] \[job2_length\]  
\[job3_weight\] \[job3_length\]  
...  

[Example Input File]( https://github.com/keshprad/Algorithms/blob/75535c5b925405c541b56a982f76981105489146/GreedyJobSchedulingTimes/testCases/test1.txt )  

---   

_**Credits**_  
Some test cases are used from [@beaunus]( https://github.com/beaunus )'s [stanford-algs]( https://github.com/beaunus/stanford-algs ) repository or provided by [Stanford's Algorithms Specialization]( https://www.coursera.org/specializations/algorithms ) taught by [Tim Roughgarden]( https://www.linkedin.com/in/tim-roughgarden-1a594855 ) on Coursera.  
