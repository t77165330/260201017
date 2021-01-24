def calculate(a_list):
  a = 0
  for i in a_list:
    a += i
  return a**2
a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]
print(calculate(a_list))