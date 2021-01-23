list1 = [5, 91, 55, 20, 69, 19, 5, 20, 69, 78, 78]

y = []
x = []
z = []

for a in range(len(list1)):
    y.append(list1[a])
    if list1[a] in y[:-1] or list1[a] in x:
        y.remove(list1[a])
        x.append(list1[a])
for i in range(len(y)):
    z.append(max(y))
    y.remove(max(y))
print(z)