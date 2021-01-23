number = int(input("Enter the number: "))
line = ""
for i in range(number):
    for a in range(number):
        if a == number - 1:
            if a == i:
                line = line + "1\n"
            else:
                line = line + "0\n"
        elif a == i and a != number - 1:
            line = line + "1 "
        else:
            if a != i and a != number - 1:
                line = line + "0 "
print(line)