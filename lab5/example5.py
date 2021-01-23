nmb = int(input("How many numbers? "))
a = 1
x = [1]
if nmb == 1:
  print(x)
else:
 while nmb >1:
   x.append(a)
   a = a+x[-2]
   nmb  = nmb-1
print(x)
  