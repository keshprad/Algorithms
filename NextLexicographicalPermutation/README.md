## Next Lexicographical Permutation Algorithm
_**About**_  
Given a word, this algorithm finds the lowest lexicographical permutation that's greater than the input.  

---   

_**How it works**_  
1. Find the longest non-increasing suffix.  

1. Identify the pivot.  

1. Find the rightmost successor to the pivot in the suffix.  

1. Swap the rightmost successor with the pivot.  

1. Reverse the suffix.  

---  

_**Methods**_  
- findNextLexicographical(w)  
    - Takes in a word as a string parameter _w_.  
    - Acts as the main method for the function.  
    - Invokes findSuffix(w).  
    - Decides whether there is a next lexicographical permutation.  
        - If there isn't it returns "no answer".  
    - invokes swapPivot(w, l).  
    - returns the final word.  
- findSuffix(w)
    - Takes in a word as a string parameter _w_.  
    - Starts from the end of the list and iterates backwards with the goal of finding the non-decreasing suffix.  
    - This means we iterate from the back.  
        - When we see that the numbers start decreasing, we return the index.  
- swapPivot(w, l)
    - Takes in a word _w_ as a string parameter and an index.  
    - Finds the rightmost item just larger than the value of the item at the pivot.  
    - Swaps the pivot item with the rightmost item just found.  
    - Reverses that last section of the list to decrease the value as much as possible.  
    - Returns the final word.  
    
---  

_**Helpful Articles**_
- [Next Lexicographical Permutation Algorithm]( https://www.nayuki.io/page/next-lexicographical-permutation-algorithm )

---  

_**Input**_  
The input is a single word as a string.
