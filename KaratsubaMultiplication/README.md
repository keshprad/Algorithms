## Karatsuba Multiplication  
_**About**_  
This is a multiplication algorithm that is much quicker than the traditional grade school algorithm which works in quadratic running time.  

---  

_**How it works**_  
1. Takes in two numbers, _n1_ and _n2_, which will be multiplied to each other.  

1. Follows Karatsuba's formula for multiplication.  

1. Recursively calls itself to compute shorter and shorter products.  

---  

_**Methods**_  
- multiplyNumbers(n1, n2)  
    - Takes in two numbers, _n1_ and _n2_, which will be multiplied to each other.  
    - Follows Karatsuba's formula for multiplication.  
        - _a_ is the first half of integers in _n1_, _b_ is the second half of integers in _n1_, _c_ is the first half of integers in _n2_, _d_ is the second half of integers in _n2_.  
        - We want to make some calculations: _ac_=_a_\*_c_; _bd_=_b_\*_d_; _prod_=(_a_+_b_)(_c_+_d_); and _diff_=_prod_-_bd_-_ac_;  
            - We can recursively call on multiplyNumbers to solve these.  
            - Our base condition would be having 1 digit numbers.  
        - After all the recursive calls, we can calculate the following, giving us our answer.  
            - _ac_\*(10^s1) + _bd_ + (_diff_\*(10^(s1//2)))  
                - For this, let's assume that _s1_ is the number of digits in _n1_.  

---  

_**Input**_  
The method takes 2 integer parameters _n1_, _n2_. I've made it such that the run_test.py file takes user input before running Karatsuba's Algorithm.  
