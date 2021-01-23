a = int(input("How many students : "))
d = []
for i in range(a):
    print(i + 1, ". student")
    x = []
    b = input("Enter the grades by splitting with (,): ").split(",")
    for c in range(3):
        if c == 1:
            x.append(int(b[c]) *40/100)
        else:
            x.append(int(b[c]) *30/100)
    a = 0
    for k in x:
        a = a + k

    d.append(a)
    y = []
for i in range(len(d)):
    if d[i] > 90:
        y.append(d[i])
print(y)

