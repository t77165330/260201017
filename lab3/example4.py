price = 3
age = float(input("Enter your age: "))
if age < 6 or age > 60:
 price = 0
 print(price)
elif 18 >= age >= 6:
 price = price/2
 print(price)
else:
  print(price)
