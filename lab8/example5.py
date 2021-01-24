def password(x):
  a = 0
  b = 0
  c = 0
  if len(x) <8 or " " in x:
    print("level 0")
  else:
    for i in range(len(x)):
      if x[i] >= "A" and x[i] <="z":
        a = 1
      elif x[i] >= "0" and x[i] <="9":
        b = 1
      else:
        if x[i] >= "!" and x[i] <="/":
          c = 1
    print("level", a + b +c)
  
x = input("Enter the password: ")
password(x)
      