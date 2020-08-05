## Levenshtein Distance  
_**About**_  
The Levenshtein Distance is a dynamic programming algorithm which represents the similarity between 2 strings as a numerical value.  

---  

_**How it works**_  
1. Assuming the strings are of length m and l, we create an m by l matrix.  

1. Uses a bottom-up dynamic programming structure to solve for the Levenshtein distance.  
    1. We iterate through this matrix, deciding at each step we look at the previous step and decide how to optimize the current step.  

1. By the time we are at the end of the matrix, we have exhausted all situations choosing the optimal one, and the last step holds the Levenshtein distance.

---  

_**Input**_  
The input takes two strings, a gap penalty, and a mismatch penalty. If the strings aren't given, the program takes user input from console. Both penalties default to 1.  
