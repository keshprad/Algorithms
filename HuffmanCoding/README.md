## Huffman Coding  
_**About**_  
The algorithm assigns codes to the symbols in order to minimize the total bits. The more frequent a word is, the smaller amount of bits in its huffman code.

---  

_**How it works**_  
1. Works on a bottom-up approach. Starts with the least frequent words and merges them into a tree with a common parent.  

1. Uses the [Node]( https://github.com/keshprad/Algorithms/tree/master/TreeNode ) class to represent trees.

1. Loops through, combining the 2 least frequent nodes until 1 (the root) is left. 
    1. When 1 node left, this is the root of our final huffman coded tree.  

1. Next, we find the codes for each symbol. We can traverse the tree thinking of left as 0 and right as 1.  

---  

_**Methods**_  
- readFile(filePath)  
    - Takes in _filePath_, a string representing a path to the input file
    - Reads the input file. For each weight...  
        - If another node already had the same weight, we use linear probing to find a space for it.
        - Adds a Node to _nodes_  
            - The value of the node is a symbol(initially just a counter)  
        - Appends weight to weights  
- huffman()
    - Serves as the main method of the program.  
    - Runs tree(...) and codes(...) methods.  
    - Returns the tree's _root_ and the list _self.codes_.  
- tree(nodes, weights)  
    - Takes in a dictionary of _nodes_, and a list of _weights_.  
    - Picks the two least frequent/weight nodes and combines them by making them children of a parent node with a sum of the childrens' weights.  
    - Puts this back in _weights_ and _nodes_ using probing to solve weight ties.  
    - Returns the root node.  
- codes(root, path)
    - Takes in a _root_ pointing to the current node and _path_, the current path of the node.  
        - For path, 0 represents a left child and 1 represents a right child.  
    - If the current root is a leaf, we can set its huffman code to the path traversed to get here.  
    - Recursively traverses the list, adding a 0 to the left path and a 1 to the right path.  

---  

_**Input**_  
The input file describes an instance of the problem. It uses the following format:  

\[number_of_symbols\]  
\[weight of symbol #1\]  
\[weight of symbol #2\]  
...  

[Example Input File]( )  

---    

_**Credits**_  
Some test cases are used from [@beaunus]( https://github.com/beaunus )'s [stanford-algs]( https://github.com/beaunus/stanford-algs ) repository or provided by [Stanford's Algorithms Specialization]( https://www.coursera.org/specializations/algorithms ) taught by [Tim Roughgarden]( https://www.linkedin.com/in/tim-roughgarden-1a594855 ) on Coursera.  
