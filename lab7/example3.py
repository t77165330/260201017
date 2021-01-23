books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
values1 = []
values2 = []
x = []
values4 = []
for a in books:
  values1.append(len(a))
  y = 0
  for i in range(len(a)):
    if a[i] not in a[:i]: 
      y = y +1
  values2.append(y)
z = 0
for k in range(len(values1)):
  z = (values1[k] + values2[k])/2
  values4.append(z)
values3 = list(zip(values1, values2, values4))
books_dict = dict(zip(books, values3))
for k in range(len(books_dict)):
  print(books[k],"-> ", books_dict.get(books[k]))