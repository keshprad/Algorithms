
def multiplyNumbers(n1, n2):
    s1 = str(n1)
    s2 = str(n2)

    if len(s1) == 1 or len(s2) == 1:
        return n1*n2

    while(len(s1) < len(s2) or len(s1)%2 == 1):
        s1 = "0" + s1
    while(len(s2) < len(s1) or len(s2)%2 == 1):
        s2 = "0" + s2

    mid1 = len(s1) // 2
    mid2 = len(s2) // 2

    a = int(s1[0: mid1])
    b = int(s1[mid1:])
    c = int(s2[0: mid2])
    d = int(s2[mid2:])

    ac = multiplyNumbers(a, c)
    bd = multiplyNumbers(b, d)
    prod = multiplyNumbers(a + b, c + d)
    diff = prod - bd - ac

    return (ac * (10 ** len(s1))) + bd + (diff * (10 ** (len(s1)//2)))