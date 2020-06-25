from HuffmanCoding import Huffman


def runHuffman(filePath):
    print(filePath + ":")

    filePath = "testCases/" + filePath
    huff = Huffman.Huffman(filePath)

    root, huff_codes = huff.huffman()
    maxLength, minLength = huff.find_MinMax_length()

    print("\tMaximum codeword length: " + str(maxLength))
    print("\tMinimum codeword length: " + str(minLength))


#######################
runHuffman("test1.txt")
runHuffman("test2.txt")
runHuffman("test3.txt")
runHuffman("test4.txt")
runHuffman("test5.txt")
runHuffman("huffman.txt")
