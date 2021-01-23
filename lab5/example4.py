password = "abc123"
a = 1
while a ==1:
  psw = str(input("enter password: "))
  if psw == password:
    print("Welcome")
    a = 0
  elif psw == "help":
    print(password[0])
  else:
    print("Wrong")
