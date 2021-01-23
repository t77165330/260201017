nmb1 = int(input("enter the number1: "))
nmb2 = int(input("enter the number2: "))
count = 0
x = str(nmb1)
y = str(nmb2)
a = min(len(x),len(y))
while a >0:
  if nmb1 % 10 == nmb2 % 10:
    count = count + 1
  nmb1_1 = nmb1%10
  nmb2_1 = nmb2%10
  nmb1 = (nmb1-nmb1_1)/10
  nmb2 = (nmb2-nmb2_1)/10
  a = a-1
print(count)
