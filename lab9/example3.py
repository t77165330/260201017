def get_evens(x):
  if len(x) >1:
    if x[0]%2 == 0:
      return get_evens(x[1:]) + 1
    else:
      return get_evens(x[1:])
  else:
    if x[0]%2 == 0:
      return 1
    else:
      return 0
x = [0, 1, 2, 3, 4, 5]
print(get_evens(x))
