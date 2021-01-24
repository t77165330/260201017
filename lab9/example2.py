def reverse(x):
  a = ""
  if len(x)>0:
    a += ","+str(x[-1])
    return a + reverse(x[:-1])
  else:
    return a
y = reverse([1,2,3,4,5])
print(y[1:].split(","))