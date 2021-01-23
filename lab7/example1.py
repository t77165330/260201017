list1 = [("Jon",15), ("Ned",45), ("Arya",9), ("Catelyn",44), ("Bran",10)]
list1 = dict(list1)
list2 = list(list1.keys())
for a in list2:
    if list1[a] < 18:
        del(list1[a])
print(list1)