N = int(input("How many numbers? "))
y =[]
while N >0:
  N = N-1
  x = int(input("Enter an integer: "))
  y.append(x)
z = 0
for i in y:
  if i%2 == 0:
    z = z+1
print(z/len(y)*100,"%")


