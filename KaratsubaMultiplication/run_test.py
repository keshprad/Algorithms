from KaratsubaMultiplication import Karatsuba

while True:
    try:
        n1 = int(input("Type the first number(Type: int)"))
        break
    except:
        print("This function expects an integer value")
while True:
    try:
        n2 = int(input("Type the second number(Type: int)"))
        break
    except:
        print("This function expects an integer value")
print(Karatsuba.multiplyNumbers(n1, n2))




