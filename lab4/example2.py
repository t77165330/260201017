x = int(input("Enter the year please: "))
if x%100 == 0:
    if x%400 ==0:
        print("leap year")
    else:
        print("not leap year")
elif x%4 == 0:
    print("leap year")
else:
    print("not leap year")