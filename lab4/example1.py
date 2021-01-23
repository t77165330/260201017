x = int(input("enter the integer: "))
if (x/10) < 1:
    print(x)
else:
    x = x%100
    print(x%10+x//10)