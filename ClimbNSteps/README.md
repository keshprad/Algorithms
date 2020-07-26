## Climb N Steps  
_**About**_  
Given n(the number of steps on the staircase) and x(an array of the different possible steps you can take at a time) this function outputs the number of combinations you can go up the stairs.  

---  

_**How it works**_  
1. Uses dynamic programming to keep track of the number of possible combinations at each step.  

---  

_**Methods**_  
- find_step_combinations(n, x)
    - Takes _n_(the number of steps on the staircase) and _x_(an array of the different possible steps you can take at a time) as input.  
    - Start by defining 1 way to get to the 0th step.  
    - For each step 1 to _n_ we can consider if there is a way to get to this step.
        - For each way to get to the step we add the combinations.  
            - eg: If we can get to step k from steps k-1, k-2, k-3 then we can add the combos at these three steps to find the combinations at step k.  

---  

_**Helpful Videos**_  
- [Recursive Staircase Problem]( https://www.youtube.com/watch?v=5o-kdjv7FD0 )  

---  

_**Input**_  
The input takes an integer _n_ (the number of steps of the staircase) and _x_(an array of different possible steps you can take at a time).  

